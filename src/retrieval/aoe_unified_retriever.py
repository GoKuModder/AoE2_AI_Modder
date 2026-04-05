from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from src.retrieval.aoe_compact_retriever import AoECompactKnowledgeRetriever


TOKEN_RE = re.compile(r"[a-z0-9_]+")
NORMALIZE_RE = re.compile(r"[^a-z0-9]")
STOPWORDS = {
    "a",
    "an",
    "and",
    "about",
    "do",
    "does",
    "for",
    "how",
    "i",
    "in",
    "is",
    "me",
    "of",
    "tell",
    "the",
    "to",
    "use",
    "what",
}
FEATURE_HINTS = {
    "build",
    "clear",
    "change",
    "checkpoint",
    "create",
    "fail",
    "gate",
    "implement",
    "link",
    "make",
    "payout",
    "recipe",
    "resolve",
    "reset",
    "reward",
    "scale",
    "setup",
    "store",
    "structure",
    "system",
    "unlock",
}
BUNDLE_HINTS = {
    "bundle",
    "campaign",
    "design",
    "dungeon",
    "full",
    "idea",
    "loop",
    "map",
    "needs",
    "scenario",
    "together",
}


@dataclass
class UnifiedRetrievalResult:
    dataset_id: str
    entry_id: str
    title: str
    score: float
    domain: str
    source_kind: str
    summary: str
    payload: dict[str, Any]


class AoEUnifiedKnowledgeRetriever:
    """Low-token retrieval across compact recipes and exact AoE knowledge datasets."""

    def __init__(self, repo_root: Path | None = None):
        self.repo_root = repo_root or Path(__file__).resolve().parents[2]
        self.compact_retriever = AoECompactKnowledgeRetriever(self.repo_root)
        self.dataset_specs = self._load_dataset_specs()
        self.datasets = {
            spec["intent"]: self._load_dataset(spec["dataset_path"])
            for spec in self.dataset_specs
        }

    def _load_dataset_specs(self) -> list[dict[str, Any]]:
        path = self.repo_root / "docs" / "agent" / "routing" / "agent_query_map.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        specs: list[dict[str, Any]] = []
        for entry in data.get("intents", []):
            if not isinstance(entry, dict):
                continue
            dataset_path = str(entry.get("dataset_path", ""))
            normalized = dataset_path.replace("\\", "/")
            if "/recipes/" in normalized:
                continue
            specs.append(entry)
        return specs

    def _load_dataset(self, relpath: str) -> list[dict[str, Any]]:
        path = self.repo_root / relpath
        data = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(data, list):
            return [row for row in data if isinstance(row, dict)]
        if isinstance(data, dict):
            commands = data.get("commands")
            if isinstance(commands, list):
                return [row for row in commands if isinstance(row, dict)]
        return []

    @staticmethod
    def _tokenize(value: str) -> set[str]:
        tokens = {token for token in TOKEN_RE.findall(value.lower()) if token not in STOPWORDS}
        return tokens or set(TOKEN_RE.findall(value.lower()))

    @staticmethod
    def _normalize(value: str) -> str:
        return NORMALIZE_RE.sub("", value.strip().lower())

    @staticmethod
    def _stringify(value: Any) -> str:
        if isinstance(value, str):
            return value
        if isinstance(value, (int, float)):
            return str(value)
        if isinstance(value, list):
            return " ".join(AoEUnifiedKnowledgeRetriever._stringify(item) for item in value)
        if isinstance(value, dict):
            return " ".join(
                f"{key} {AoEUnifiedKnowledgeRetriever._stringify(val)}"
                for key, val in value.items()
            )
        return ""

    def detect_domains(self, query: str) -> list[str]:
        return self.compact_retriever.detect_domains(query)

    @staticmethod
    def _entry_id(entry: dict[str, Any]) -> str:
        for key in (
            "id",
            "name",
            "command",
            "internal_name",
            "display_name",
            "parser_enum_name",
            "ugc_name",
            "effect_id",
            "condition_id",
            "genie_id",
        ):
            value = entry.get(key)
            if value not in (None, ""):
                return str(value)
        return ""

    @staticmethod
    def _entry_title(entry: dict[str, Any]) -> str:
        for key in ("title", "display_name", "name", "command", "internal_name", "id"):
            value = entry.get(key)
            if value:
                return str(value)
        return ""

    @staticmethod
    def _entry_summary(entry: dict[str, Any]) -> str:
        for key in (
            "summary",
            "desc",
            "description",
            "primary_role",
            "how_it_is_used",
            "notes",
        ):
            value = entry.get(key)
            if isinstance(value, str) and value.strip():
                return value.strip()
            if isinstance(value, list) and value:
                return " ".join(str(item) for item in value[:2]).strip()
        return ""

    @staticmethod
    def _entry_symbols(entry: dict[str, Any]) -> list[str]:
        symbols: list[str] = []
        for key in (
            "name",
            "command",
            "internal_name",
            "display_name",
            "parser_enum_name",
            "ugc_name",
            "source_internal_name",
            "aliases",
            "exact_terms",
        ):
            value = entry.get(key)
            if isinstance(value, str) and value and value not in symbols:
                symbols.append(value)
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, str) and item and item not in symbols:
                        symbols.append(item)
        return symbols

    @staticmethod
    def _entry_signature(entry: dict[str, Any]) -> str:
        signature = entry.get("signature")
        if isinstance(signature, str) and signature.strip():
            return signature.strip()

        name = entry.get("name")
        params = entry.get("params")
        return_type = entry.get("return_type")
        if isinstance(name, str) and isinstance(params, list) and isinstance(return_type, str):
            parts: list[str] = []
            for param in params:
                if not isinstance(param, dict):
                    continue
                param_type = str(param.get("type", "any"))
                param_name = str(param.get("name", "arg"))
                parts.append(f"{param_type} {param_name}")
            return f"{return_type} {name}({', '.join(parts)})"
        return ""

    @staticmethod
    def _entry_steps(entry: dict[str, Any]) -> list[str]:
        for key in ("steps", "implementation_steps", "agent_instructions", "operations"):
            value = entry.get(key)
            if isinstance(value, list):
                return [str(item) for item in value[:6]]
        return []

    @staticmethod
    def _entry_best_files(entry: dict[str, Any]) -> list[str]:
        value = entry.get("best_files")
        if isinstance(value, list):
            return [str(item) for item in value[:5]]
        return []

    @staticmethod
    def _entry_pitfalls(entry: dict[str, Any]) -> list[str]:
        for key in ("pitfalls", "common_pitfalls"):
            value = entry.get(key)
            if isinstance(value, list):
                return [str(item) for item in value[:5]]
        notes = entry.get("notes")
        if isinstance(notes, list):
            return [str(item) for item in notes[:3]]
        return []

    @staticmethod
    def _compress_text(value: str, *, max_chars: int = 220) -> str:
        text = " ".join(value.split())
        if len(text) <= max_chars:
            return text
        return text[: max_chars - 3].rstrip() + "..."

    @staticmethod
    def _truncate_list(values: list[str], *, max_items: int) -> list[str]:
        return [str(item) for item in values[:max_items]]

    def _select_context_results(
        self, query_tokens: set[str], results: list[UnifiedRetrievalResult], limit: int
    ) -> list[UnifiedRetrievalResult]:
        if not results:
            return []

        exactish_kinds = {"exact_lookup", "reference", "usage", "playbook"}
        if len(query_tokens) <= 2:
            exactish = [item for item in results if item.source_kind in exactish_kinds]
            if exactish:
                first_exact = exactish[0]
                same_title = [
                    item
                    for item in exactish
                    if item.title.lower() == first_exact.title.lower()
                    and item.domain == first_exact.domain
                ]
                return (same_title or exactish)[:limit]

        feature_query = self._is_feature_query(query_tokens)
        bundle_query = self._is_bundle_query(query_tokens)
        if feature_query or bundle_query:
            compact = [item for item in results if item.source_kind == "compact_recipe"]
            if compact:
                primary_domain = compact[0].domain
                same_domain = [item for item in compact if item.domain == primary_domain]
                narrowed = same_domain or compact
                compact_limit = 4 if bundle_query else 2
                return narrowed[: min(limit, compact_limit)]

        first = results[0]
        if first.source_kind in exactish_kinds:
            same_title = [
                item
                for item in results
                if item.title.lower() == first.title.lower() and item.domain == first.domain
            ]
            if same_title:
                return same_title[:limit]

        return results[:limit]

    @staticmethod
    def _source_kind_for_path(dataset_path: str) -> str:
        normalized = dataset_path.replace("\\", "/")
        if "/patterns/" in normalized:
            return "pattern"
        if "playbook" in normalized:
            return "playbook"
        if "usage" in normalized:
            return "usage"
        if "catalog" in normalized or "metadata" in normalized or "registry" in normalized:
            return "exact_lookup"
        if "knowledge" in normalized or "attributes" in normalized:
            return "reference"
        return "reference"

    @staticmethod
    def _domains_for_path(dataset_path: str) -> list[str]:
        normalized = dataset_path.replace("\\", "/").lower()
        if "xs_" in normalized or "/agent_database/xs_" in normalized:
            return ["xs"]
        if "ai_scripting_knowledge" in normalized:
            return ["ai_scripts"]
        if "genie_registry" in normalized:
            return ["dat_genie_tooling"]
        if "genie_dat_concepts" in normalized:
            return ["dat_genie_tooling"]
        if "genie_workflow" in normalized:
            return ["dat_genie_tooling"]
        if "trigger_xs_patterns" in normalized:
            return ["scenario_triggers", "xs"]
        if "trigger_knowledge" in normalized:
            return ["scenario_triggers"]
        return []

    def _score_entry(
        self,
        query: str,
        query_tokens: set[str],
        entry: dict[str, Any],
        lookup_keys: list[str],
        dataset_domains: set[str],
        detected_domains: set[str],
    ) -> float:
        text_parts: list[str] = []
        for key in lookup_keys:
            text_parts.append(self._stringify(entry.get(key)))
        exact_symbols = self._entry_symbols(entry)
        text_parts.extend(exact_symbols)
        haystack_tokens = self._tokenize(" ".join(text_parts))
        if not haystack_tokens:
            return 0.0

        overlap = query_tokens & haystack_tokens
        score = len(overlap) / max(1, len(query_tokens))
        if score <= 0:
            return 0.0

        normalized_query = self._normalize(query)
        normalized_symbols = {self._normalize(symbol) for symbol in exact_symbols if symbol}
        if normalized_query in normalized_symbols:
            score += 1.2
        elif any(symbol and symbol in normalized_query for symbol in normalized_symbols):
            score += 0.8

        if detected_domains and dataset_domains & detected_domains:
            score += 0.25
        return score

    @staticmethod
    def _is_feature_query(query_tokens: set[str]) -> bool:
        return bool(query_tokens & FEATURE_HINTS)

    @staticmethod
    def _is_bundle_query(query_tokens: set[str]) -> bool:
        bundle_matches = query_tokens & BUNDLE_HINTS
        return "design" in query_tokens or len(bundle_matches) >= 2

    def _convert_compact_result(self, result: Any) -> UnifiedRetrievalResult:
        payload = dict(result.payload)
        primary_domains = payload.get("primary_domains", [])
        domain = str(primary_domains[0]) if primary_domains else "unknown"
        return UnifiedRetrievalResult(
            dataset_id=result.dataset_id,
            entry_id=result.entry_id,
            title=result.title,
            score=result.score,
            domain=domain,
            source_kind="compact_recipe",
            summary=result.summary,
            payload=payload,
        )

    def search(self, query: str, *, limit: int = 8) -> list[UnifiedRetrievalResult]:
        query_tokens = self._tokenize(query)
        detected_domains = set(self.detect_domains(query))
        is_feature_query = self._is_feature_query(query_tokens)
        is_bundle_query = self._is_bundle_query(query_tokens)
        ranked: list[UnifiedRetrievalResult] = []

        for result in self.compact_retriever.search(query, limit=max(6, limit)):
            compact_result = self._convert_compact_result(result)
            if is_feature_query or is_bundle_query:
                compact_result.score += 0.45
            ranked.append(compact_result)

        for spec in self.dataset_specs:
            dataset_path = str(spec.get("dataset_path", ""))
            dataset_domains = set(self._domains_for_path(dataset_path))
            lookup_keys = [str(key) for key in spec.get("lookup_keys", [])]
            dataset_id = Path(dataset_path).name
            source_kind = self._source_kind_for_path(dataset_path)
            for entry in self.datasets.get(str(spec.get("intent", "")), []):
                score = self._score_entry(
                    query, query_tokens, entry, lookup_keys, dataset_domains, detected_domains
                )
                if score <= 0:
                    continue
                domain = next(iter(dataset_domains), "unknown")
                ranked.append(
                    UnifiedRetrievalResult(
                        dataset_id=dataset_id,
                        entry_id=self._entry_id(entry),
                        title=self._entry_title(entry),
                        score=score,
                        domain=domain,
                        source_kind=source_kind,
                        summary=self._entry_summary(entry),
                        payload=entry,
                    )
                )

        ranked.sort(key=lambda item: item.score, reverse=True)
        deduped: list[UnifiedRetrievalResult] = []
        seen: set[tuple[str, str]] = set()
        for item in ranked:
            key = (item.dataset_id, item.entry_id)
            if key in seen:
                continue
            seen.add(key)
            deduped.append(item)
            if len(deduped) >= limit:
                break
        return deduped

    def build_context(self, query: str, *, limit: int = 6) -> dict[str, Any]:
        query_tokens = self._tokenize(query)
        bundle_query = self._is_bundle_query(query_tokens)
        raw_results = self.search(query, limit=max(limit * 2, 8))
        results = self._select_context_results(query_tokens, raw_results, limit)
        return {
            "query": query,
            "domains_detected": self.detect_domains(query),
            "retrieved": [
                {
                    "dataset_id": result.dataset_id,
                    "entry_id": result.entry_id,
                    "title": result.title,
                    "score": round(result.score, 4),
                    "domain": result.domain,
                    "source_kind": result.source_kind,
                    "summary": self._compress_text(
                        result.summary,
                        max_chars=120 if bundle_query and result.source_kind == "compact_recipe" else 220,
                    ),
                    "exact_symbols": self._truncate_list(
                        self._entry_symbols(result.payload),
                        max_items=0 if result.source_kind == "compact_recipe" else 4,
                    ),
                    "signature": ""
                    if result.source_kind == "compact_recipe"
                    else self._compress_text(self._entry_signature(result.payload), max_chars=160),
                    "best_files": self._truncate_list(
                        self._entry_best_files(result.payload),
                        max_items=1 if bundle_query and result.source_kind == "compact_recipe" else 2,
                    ),
                    "steps": self._truncate_list(
                        self._entry_steps(result.payload),
                        max_items=2 if bundle_query and result.source_kind == "compact_recipe" else 4,
                    ),
                    "pitfalls": self._truncate_list(
                        self._entry_pitfalls(result.payload),
                        max_items=1 if bundle_query and result.source_kind == "compact_recipe" else 3,
                    ),
                }
                for result in results
            ],
        }
