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
class GenieDatRetrievalResult:
    entry_id: str
    title: str
    score: float
    summary: str
    payload: dict[str, Any]


class GenieDatKnowledgeRetriever:
    """Fast retriever for compact .dat/genie concept knowledge."""

    def __init__(self, repo_root: Path | None = None):
        self.repo_root = repo_root or Path(__file__).resolve().parents[2]
        self.dataset_path = (
            self.repo_root / "docs" / "agent_database" / "genie_dat_concepts.json"
        )
        self.entries = self._load_dataset()

    def _load_dataset(self) -> list[dict[str, Any]]:
        data = json.loads(self.dataset_path.read_text(encoding="utf-8"))
        if isinstance(data, list):
            return [entry for entry in data if isinstance(entry, dict)]
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
        if isinstance(value, list):
            return " ".join(str(item) for item in value)
        return ""

    def _score_entry(self, query: str, query_tokens: set[str], entry: dict[str, Any]) -> float:
        fields = (
            "name",
            "display_name",
            "category",
            "summary",
            "why_it_matters",
            "owners",
            "exact_terms",
            "aliases",
            "related_fields",
            "how_it_works",
            "project_evidence",
            "query_terms",
            "pitfalls",
        )
        haystack = " ".join(self._stringify(entry.get(field)) for field in fields)
        haystack_tokens = self._tokenize(haystack)
        if not haystack_tokens:
            return 0.0

        overlap = query_tokens & haystack_tokens
        if not overlap:
            return 0.0

        score = len(overlap) / max(1, len(query_tokens))
        normalized_query = self._normalize(query)

        important_terms: list[str] = []
        for key in ("name", "display_name"):
            value = entry.get(key)
            if isinstance(value, str):
                important_terms.append(value)
        for key in ("exact_terms", "aliases"):
            value = entry.get(key)
            if isinstance(value, list):
                important_terms.extend(str(item) for item in value)

        important_tokens = self._tokenize(" ".join(important_terms))
        if important_tokens:
            score += 0.5 * (len(query_tokens & important_tokens) / max(1, len(query_tokens)))

        for term in important_terms:
            normalized_term = self._normalize(term)
            if len(normalized_term) < 5:
                continue
            if normalized_term == normalized_query:
                score += 1.25
                break
            if normalized_term in normalized_query or normalized_query in normalized_term:
                score += 0.8
                break

        return score

    def search(self, query: str, *, limit: int = 6) -> list[GenieDatRetrievalResult]:
        query_tokens = self._tokenize(query)
        ranked: list[GenieDatRetrievalResult] = []
        for entry in self.entries:
            score = self._score_entry(query, query_tokens, entry)
            if score <= 0:
                continue
            ranked.append(
                GenieDatRetrievalResult(
                    entry_id=str(entry.get("id", "")),
                    title=str(entry.get("display_name", entry.get("name", entry.get("id", "")))),
                    score=score,
                    summary=str(entry.get("summary", "")),
                    payload=entry,
                )
            )

        ranked.sort(key=lambda item: item.score, reverse=True)
        return ranked[:limit]

    def build_context(self, query: str, *, limit: int = 4) -> dict[str, Any]:
        results = self.search(query, limit=limit)
        return {
            "query": query,
            "retrieved": [
                {
                    "entry_id": result.entry_id,
                    "title": result.title,
                    "score": round(result.score, 4),
                    "category": result.payload.get("category", ""),
                    "owners": result.payload.get("owners", [])[:4],
                    "exact_terms": result.payload.get("exact_terms", [])[:6],
                    "related_fields": result.payload.get("related_fields", [])[:5],
                    "summary": result.summary,
                    "how_it_works": str(result.payload.get("how_it_works", "")),
                    "best_files": result.payload.get("best_files", [])[:3],
                    "pitfalls": result.payload.get("pitfalls", [])[:3],
                }
                for result in results
            ],
        }
