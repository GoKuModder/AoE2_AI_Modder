from __future__ import annotations

import argparse
import importlib.resources as resources
import json
from pathlib import Path
from typing import Any

from src.retrieval.xs_script_retriever import XSScriptKnowledgeRetriever


# Package identifier for bundled XS data
_XS_DATA_PACKAGE = "src.data.xs"

# Default to None (use packaged resources)
DEFAULT_DATASET_DIR: Path | None = None
DEFAULT_GOLDEN_PATH: Path | None = None


def _get_default_golden_path() -> Path | None:
    """Get path to the default golden evaluation file from packaged resources.

    Returns:
        Path to the golden file, or None if not available
    """
    try:
        # Try to verify the packaged golden file exists
        ref = resources.files(_XS_DATA_PACKAGE).joinpath("agent_database/xs_eval.json")
        ref.read_text()
        # Return a special marker - we'll handle it in the code
        return Path("__packaged__:agent_database/xs_eval.json")
    except (ModuleNotFoundError, FileNotFoundError, TypeError):
        return None


# Initialize default golden path at module load time
_default_golden = _get_default_golden_path()


def _load_golden(path: Path | None) -> list[dict[str, Any]]:
    """Load golden evaluation cases.

    Args:
        path: Path to golden JSON file, or None for default packaged

    Returns:
        List of golden test cases
    """
    if path is None:
        # Use packaged default
        if _default_golden is None:
            raise ValueError(
                "No golden path provided and default packaged golden data not available"
            )
        # Load from package
        text = resources.files(_XS_DATA_PACKAGE).joinpath(
            "agent_database/xs_eval.json"
        ).read_text(encoding="utf-8")
    else:
        text = path.read_text(encoding="utf-8")

    payload = json.loads(text)
    cases = payload.get("cases")
    if not isinstance(cases, list):
        raise ValueError("golden file must contain a 'cases' list")
    return cases


def _extract_candidates(hit: Any) -> tuple[str, str]:
    return (hit.title.lower(), hit.source_file.lower())


def _first_match_rank(
    results: list[Any], expected_any: list[str], *, substring_match: bool
) -> int | None:
    expected = [token.lower() for token in expected_any]
    for idx, hit in enumerate(results, start=1):
        title, source_file = _extract_candidates(hit)
        for token in expected:
            if substring_match:
                if token in title or token in source_file:
                    return idx
            elif token == title or token == source_file:
                return idx
    return None


def evaluate_golden(
    *,
    dataset_dir: Path | None,
    golden_path: Path | None,
    k: int,
    min_recall: float,
    min_mrr: float,
) -> dict[str, Any]:
    # Use None to trigger default (packaged resources)
    retriever = XSScriptKnowledgeRetriever(dataset_dir)
    cases = _load_golden(golden_path)

    answerable = 0
    hits = 0
    reciprocal_rank_total = 0.0
    miss_total = 0
    miss_pass = 0
    per_case: list[dict[str, Any]] = []

    for case in cases:
        case_id = str(case.get("id", ""))
        query = str(case.get("query", "")).strip()
        kind = str(case.get("kind", "answerable")).strip().lower()

        if not query:
            raise ValueError(f"case '{case_id}' is missing query")

        results = retriever.search(query, limit=k)
        top_items = [
            {"title": row.title, "source_file": row.source_file, "score": round(row.score, 6)}
            for row in results
        ]

        if kind == "miss":
            miss_total += 1
            passed = len(results) == 0
            if passed:
                miss_pass += 1
            per_case.append(
                {
                    "id": case_id,
                    "query": query,
                    "kind": kind,
                    "pass": passed,
                    "top_k": top_items,
                }
            )
            continue

        expected_any = case.get("expected_any")
        if not isinstance(expected_any, list) or not expected_any:
            raise ValueError(f"answerable case '{case_id}' requires non-empty expected_any")

        answerable += 1
        rank = _first_match_rank(results, expected_any, substring_match=True)
        hit = rank is not None
        if hit:
            hits += 1
            reciprocal_rank_total += 1.0 / float(rank)

        per_case.append(
            {
                "id": case_id,
                "query": query,
                "kind": kind,
                "expected_any": expected_any,
                "hit": hit,
                "rank": rank,
                "top_k": top_items,
            }
        )

    recall_at_k = (hits / answerable) if answerable else 0.0
    mrr = (reciprocal_rank_total / answerable) if answerable else 0.0
    miss_pass_rate = (miss_pass / miss_total) if miss_total else 1.0

    thresholds_passed = recall_at_k >= min_recall and mrr >= min_mrr

    # Format dataset_dir for output
    dataset_dir_str = "packaged" if dataset_dir is None else str(dataset_dir)
    golden_str = "packaged" if golden_path is None else str(golden_path)

    return {
        "dataset_dir": dataset_dir_str,
        "golden": golden_str,
        "k": k,
        "metrics": {
            "answerable_cases": answerable,
            "miss_cases": miss_total,
            "hits": hits,
            "miss_pass": miss_pass,
            "recall_at_k": round(recall_at_k, 6),
            "mrr": round(mrr, 6),
            "miss_pass_rate": round(miss_pass_rate, 6),
        },
        "thresholds": {
            "min_recall": min_recall,
            "min_mrr": min_mrr,
        },
        "thresholds_passed": thresholds_passed,
        "cases": per_case,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Evaluate XS retrieval against a golden dataset")
    parser.add_argument("--dataset-dir", default=None)
    parser.add_argument("--golden", default=None)
    parser.add_argument("--k", type=int, default=5)
    parser.add_argument("--min-recall", type=float, default=0.0)
    parser.add_argument("--min-mrr", type=float, default=0.0)
    args = parser.parse_args(argv)

    # Convert None string back to None
    dataset_dir = Path(args.dataset_dir) if args.dataset_dir else None
    golden_path = Path(args.golden) if args.golden else None

    result = evaluate_golden(
        dataset_dir=dataset_dir,
        golden_path=golden_path,
        k=args.k,
        min_recall=args.min_recall,
        min_mrr=args.min_mrr,
    )
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["thresholds_passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
