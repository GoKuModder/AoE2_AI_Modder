from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from src.retrieval import AoEUnifiedKnowledgeRetriever


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_GOLDEN_PATH = (
    REPO_ROOT
    / "docs"
    / "agent"
    / "references"
    / "recipes"
    / "unified_retrieval_eval.json"
)


def _load_golden(path: Path | None) -> dict[str, Any]:
    golden_path = path or DEFAULT_GOLDEN_PATH
    payload = json.loads(golden_path.read_text(encoding="utf-8"))
    cases = payload.get("cases")
    if not isinstance(cases, list):
        raise ValueError("golden file must contain a 'cases' list")
    defaults = payload.get("defaults", {})
    if defaults is None:
        defaults = {}
    if not isinstance(defaults, dict):
        raise ValueError("golden file defaults must be an object")
    return {"golden_path": golden_path, "defaults": defaults, "cases": cases}


def _candidate_texts(hit: dict[str, Any]) -> list[str]:
    values = [
        str(hit.get("entry_id", "")),
        str(hit.get("title", "")),
        str(hit.get("dataset_id", "")),
        str(hit.get("domain", "")),
    ]
    values.extend(str(symbol) for symbol in hit.get("exact_symbols", []))
    return [value.lower() for value in values if value]


def _first_match_rank(results: list[dict[str, Any]], expected_any: list[str]) -> int | None:
    expected = [token.lower() for token in expected_any]
    for idx, hit in enumerate(results, start=1):
        candidates = _candidate_texts(hit)
        for token in expected:
            if any(token == candidate or token in candidate for candidate in candidates):
                return idx
    return None


def _match_ranks(results: list[dict[str, Any]], expected_tokens: list[str]) -> dict[str, int]:
    matched: dict[str, int] = {}
    expected = [token.lower() for token in expected_tokens]
    for idx, hit in enumerate(results, start=1):
        candidates = _candidate_texts(hit)
        for token in expected:
            if token in matched:
                continue
            if any(token == candidate or token in candidate for candidate in candidates):
                matched[token] = idx
    return matched


def _context_budget_status(
    context: dict[str, Any],
    *,
    max_context_chars: int,
    max_retrieved: int,
    max_steps_per_result: int,
    max_best_files_per_result: int,
) -> dict[str, Any]:
    context_chars = len(json.dumps(context, sort_keys=True))
    retrieved = context.get("retrieved", [])
    retrieved_count = len(retrieved) if isinstance(retrieved, list) else 0
    max_steps_seen = 0
    max_best_files_seen = 0
    for row in retrieved if isinstance(retrieved, list) else []:
        if not isinstance(row, dict):
            continue
        steps = row.get("steps", [])
        best_files = row.get("best_files", [])
        if isinstance(steps, list):
            max_steps_seen = max(max_steps_seen, len(steps))
        if isinstance(best_files, list):
            max_best_files_seen = max(max_best_files_seen, len(best_files))

    passed = (
        context_chars <= max_context_chars
        and retrieved_count <= max_retrieved
        and max_steps_seen <= max_steps_per_result
        and max_best_files_seen <= max_best_files_per_result
    )
    return {
        "pass": passed,
        "context_chars": context_chars,
        "retrieved_count": retrieved_count,
        "max_steps_seen": max_steps_seen,
        "max_best_files_seen": max_best_files_seen,
    }


def evaluate_golden(
    *,
    golden_path: Path | None = None,
    k: int | None = None,
    min_recall: float | None = None,
    min_mrr: float | None = None,
    min_budget_pass_rate: float | None = None,
) -> dict[str, Any]:
    golden_payload = _load_golden(golden_path)
    defaults = golden_payload["defaults"]
    cases = golden_payload["cases"]
    retriever = AoEUnifiedKnowledgeRetriever()

    limit_default = int(defaults.get("k", 4))
    max_context_chars_default = int(defaults.get("max_context_chars", 2600))
    max_retrieved_default = int(defaults.get("max_retrieved", limit_default))
    max_steps_default = int(defaults.get("max_steps_per_result", 6))
    max_best_files_default = int(defaults.get("max_best_files_per_result", 5))

    effective_k = k if k is not None else limit_default
    effective_min_recall = (
        min_recall if min_recall is not None else float(defaults.get("min_recall", 0.0))
    )
    effective_min_mrr = (
        min_mrr if min_mrr is not None else float(defaults.get("min_mrr", 0.0))
    )
    effective_budget_pass_rate = (
        min_budget_pass_rate
        if min_budget_pass_rate is not None
        else float(defaults.get("min_budget_pass_rate", 0.0))
    )

    answerable = 0
    hits = 0
    reciprocal_rank_total = 0.0
    miss_total = 0
    miss_pass = 0
    budget_total = 0
    budget_pass = 0
    context_chars_total = 0
    retrieved_total = 0
    max_context_chars_seen = 0
    per_case: list[dict[str, Any]] = []

    for case in cases:
        case_id = str(case.get("id", ""))
        query = str(case.get("query", "")).strip()
        kind = str(case.get("kind", "answerable")).strip().lower()
        if not query:
            raise ValueError(f"case '{case_id}' is missing query")

        case_limit = int(case.get("limit", effective_k))
        context = retriever.build_context(query, limit=case_limit)
        results = context.get("retrieved", [])
        budget = _context_budget_status(
            context,
            max_context_chars=int(case.get("max_context_chars", max_context_chars_default)),
            max_retrieved=int(case.get("max_retrieved", max_retrieved_default)),
            max_steps_per_result=int(case.get("max_steps_per_result", max_steps_default)),
            max_best_files_per_result=int(
                case.get("max_best_files_per_result", max_best_files_default)
            ),
        )
        budget_total += 1
        context_chars_total += budget["context_chars"]
        retrieved_total += budget["retrieved_count"]
        max_context_chars_seen = max(max_context_chars_seen, budget["context_chars"])
        if budget["pass"]:
            budget_pass += 1

        top_items = [
            {
                "dataset_id": row.get("dataset_id", ""),
                "entry_id": row.get("entry_id", ""),
                "title": row.get("title", ""),
                "domain": row.get("domain", ""),
                "source_kind": row.get("source_kind", ""),
                "score": row.get("score", 0),
            }
            for row in results
            if isinstance(row, dict)
        ]

        if kind == "miss":
            miss_total += 1
            passed = len(top_items) == 0
            if passed:
                miss_pass += 1
            per_case.append(
                {
                    "id": case_id,
                    "query": query,
                    "kind": kind,
                    "pass": passed,
                    "budget": budget,
                    "top_k": top_items,
                }
            )
            continue

        expected_any = case.get("expected_any")
        expected_all = case.get("expected_all")
        if expected_all is not None:
            if not isinstance(expected_all, list) or not expected_all:
                raise ValueError(f"answerable case '{case_id}' expected_all must be non-empty")
            matched = _match_ranks(top_items, expected_all)
            hit = len(matched) == len(expected_all)
            rank = max(matched.values()) if hit else None
            expected_payload = {"expected_all": expected_all, "matched": matched}
        else:
            if not isinstance(expected_any, list) or not expected_any:
                raise ValueError(f"answerable case '{case_id}' requires non-empty expected_any")
            rank = _first_match_rank(top_items, expected_any)
            hit = rank is not None
            expected_payload = {"expected_any": expected_any}

        answerable += 1
        if hit:
            hits += 1
            reciprocal_rank_total += 1.0 / float(rank)

        per_case.append(
            {
                "id": case_id,
                "query": query,
                "kind": kind,
                "hit": hit,
                "rank": rank,
                "budget": budget,
                "top_k": top_items,
                **expected_payload,
            }
        )

    recall_at_k = (hits / answerable) if answerable else 0.0
    mrr = (reciprocal_rank_total / answerable) if answerable else 0.0
    miss_pass_rate = (miss_pass / miss_total) if miss_total else 1.0
    budget_pass_rate = (budget_pass / budget_total) if budget_total else 1.0
    avg_context_chars = (context_chars_total / budget_total) if budget_total else 0.0
    avg_retrieved = (retrieved_total / budget_total) if budget_total else 0.0

    thresholds_passed = (
        recall_at_k >= effective_min_recall
        and mrr >= effective_min_mrr
        and budget_pass_rate >= effective_budget_pass_rate
    )

    return {
        "golden": str(golden_payload["golden_path"]),
        "k": effective_k,
        "metrics": {
            "answerable_cases": answerable,
            "miss_cases": miss_total,
            "hits": hits,
            "miss_pass": miss_pass,
            "budget_cases": budget_total,
            "budget_pass": budget_pass,
            "recall_at_k": round(recall_at_k, 6),
            "mrr": round(mrr, 6),
            "miss_pass_rate": round(miss_pass_rate, 6),
            "budget_pass_rate": round(budget_pass_rate, 6),
            "avg_context_chars": round(avg_context_chars, 2),
            "max_context_chars": max_context_chars_seen,
            "avg_retrieved_count": round(avg_retrieved, 2),
        },
        "thresholds": {
            "min_recall": effective_min_recall,
            "min_mrr": effective_min_mrr,
            "min_budget_pass_rate": effective_budget_pass_rate,
        },
        "thresholds_passed": thresholds_passed,
        "cases": per_case,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Evaluate unified AoE retrieval quality and compactness budgets"
    )
    parser.add_argument("--golden", default=None)
    parser.add_argument("--k", type=int, default=None)
    parser.add_argument("--min-recall", type=float, default=None)
    parser.add_argument("--min-mrr", type=float, default=None)
    parser.add_argument("--min-budget-pass-rate", type=float, default=None)
    args = parser.parse_args(argv)

    result = evaluate_golden(
        golden_path=Path(args.golden) if args.golden else None,
        k=args.k,
        min_recall=args.min_recall,
        min_mrr=args.min_mrr,
        min_budget_pass_rate=args.min_budget_pass_rate,
    )
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["thresholds_passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
