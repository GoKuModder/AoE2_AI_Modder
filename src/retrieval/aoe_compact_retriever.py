from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any


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


@dataclass
class CompactRetrievalResult:
    dataset_id: str
    entry_id: str
    title: str
    score: float
    summary: str
    payload: dict[str, Any]


class AoECompactKnowledgeRetriever:
    """Fast retrieval over compact AoE recipe datasets.

    This retriever is designed for low-token routing over the smallest
    implementation-oriented datasets in the repo.
    """

    def __init__(self, repo_root: Path | None = None):
        self.repo_root = repo_root or Path(__file__).resolve().parents[2]
        self.routing_rules = self._load_query_router()
        self.dataset_specs = self._load_dataset_specs()
        self.datasets = {
            spec["intent"]: self._load_dataset(spec["dataset_path"])
            for spec in self.dataset_specs
        }

    def _load_query_router(self) -> list[dict[str, Any]]:
        path = self.repo_root / "docs" / "agent" / "routing" / "query_router.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        return [rule for rule in data.get("rules", []) if isinstance(rule, dict)]

    def _load_dataset_specs(self) -> list[dict[str, Any]]:
        path = self.repo_root / "docs" / "agent" / "routing" / "agent_query_map.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        specs: list[dict[str, Any]] = []
        for entry in data.get("intents", []):
            if not isinstance(entry, dict):
                continue
            dataset_path = str(entry.get("dataset_path", ""))
            if "/recipes/" not in dataset_path.replace("\\", "/"):
                continue
            specs.append(entry)
        return specs

    def _load_dataset(self, relpath: str) -> list[dict[str, Any]]:
        path = self.repo_root / relpath
        data = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(data, list):
            return [row for row in data if isinstance(row, dict)]
        return []

    @staticmethod
    def _tokenize(value: str) -> set[str]:
        tokens = {token for token in TOKEN_RE.findall(value.lower()) if token not in STOPWORDS}
        return tokens or set(TOKEN_RE.findall(value.lower()))

    @staticmethod
    def _normalize(value: str) -> str:
        return NORMALIZE_RE.sub("", value.strip().lower())

    def detect_domains(self, query: str) -> list[str]:
        query_tokens = self._tokenize(query)
        matches: dict[str, int] = {}
        for rule in self.routing_rules:
            rule_tokens = self._tokenize(str(rule.get("query_term", "")))
            if not rule_tokens:
                continue
            if not (query_tokens & rule_tokens):
                continue
            priority = int(rule.get("priority", 0))
            for domain in rule.get("target_domains", []):
                matches[domain] = max(matches.get(domain, 0), priority)
        return [
            domain
            for domain, _score in sorted(
                matches.items(), key=lambda item: item[1], reverse=True
            )
        ]

    def _score_entry(
        self,
        query_tokens: set[str],
        query: str,
        entry: dict[str, Any],
        lookup_keys: list[str],
        detected_domains: set[str],
    ) -> float:
        text_parts: list[str] = []
        important_parts: list[str] = []
        for key in lookup_keys:
            value = entry.get(key)
            if isinstance(value, str):
                text_parts.append(value)
            elif isinstance(value, list):
                text_parts.extend(str(item) for item in value)
        for key in ("id", "title", "query_terms"):
            value = entry.get(key)
            if isinstance(value, str):
                important_parts.append(value)
            elif isinstance(value, list):
                important_parts.extend(str(item) for item in value)
        haystack_tokens = self._tokenize(" ".join(text_parts))
        if not haystack_tokens:
            return 0.0
        overlap = query_tokens & haystack_tokens
        if not overlap:
            return 0.0
        score = len(overlap) / max(1, len(query_tokens))
        important_tokens = self._tokenize(" ".join(important_parts))
        if important_tokens:
            important_overlap = query_tokens & important_tokens
            score += 0.6 * (len(important_overlap) / max(1, len(query_tokens)))
        phrase_bonus = 0.0
        for part in important_parts:
            part_tokens = self._tokenize(part)
            if len(part_tokens) >= 3 and part_tokens and part_tokens <= query_tokens:
                phrase_bonus = max(phrase_bonus, 0.6 + (0.1 * len(part_tokens)))
        score += phrase_bonus
        normalized_query = self._normalize(query)
        for part in important_parts + text_parts:
            normalized_part = self._normalize(part)
            if len(normalized_part) < 5:
                continue
            if normalized_part in normalized_query or normalized_query in normalized_part:
                score += 0.75
                break
        entry_domains = set(entry.get("primary_domains", []))
        if detected_domains and entry_domains & detected_domains:
            score += 0.35
        return score

    def search(self, query: str, *, limit: int = 8) -> list[CompactRetrievalResult]:
        query_tokens = self._tokenize(query)
        detected_domains = set(self.detect_domains(query))
        ranked: list[CompactRetrievalResult] = []

        for spec in self.dataset_specs:
            intent = str(spec.get("intent", ""))
            dataset_path = str(spec.get("dataset_path", ""))
            dataset_id = Path(dataset_path).name
            lookup_keys = [str(key) for key in spec.get("lookup_keys", [])]
            for entry in self.datasets.get(intent, []):
                score = self._score_entry(
                    query_tokens, query, entry, lookup_keys, detected_domains
                )
                if score <= 0:
                    continue
                ranked.append(
                    CompactRetrievalResult(
                        dataset_id=dataset_id,
                        entry_id=str(entry.get("id", "")),
                        title=str(entry.get("title", entry.get("id", ""))),
                        score=score,
                        summary=str(entry.get("summary", "")),
                        payload=entry,
                    )
                )

        ranked.sort(key=lambda item: item.score, reverse=True)
        deduped: list[CompactRetrievalResult] = []
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
        results = self.search(query, limit=limit)
        return {
            "query": query,
            "domains_detected": self.detect_domains(query),
            "retrieved": [
                {
                    "dataset_id": result.dataset_id,
                    "entry_id": result.entry_id,
                    "title": result.title,
                    "score": round(result.score, 4),
                    "summary": result.summary,
                    "steps": result.payload.get("steps", []),
                    "best_files": result.payload.get("best_files", []),
                    "pitfalls": result.payload.get("pitfalls", []),
                }
                for result in results
            ],
        }
