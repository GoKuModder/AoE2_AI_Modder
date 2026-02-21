from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any


TOKEN_RE = re.compile(r"[a-z0-9-]+")


@dataclass
class RetrievalResult:
    source_file: str
    title: str
    score: float
    text: str


class AIScriptKnowledgeRetriever:
    """Hybrid retrieval utility for local AI scripting knowledge.

    This intentionally stays lightweight:
    - deterministic command lookup from metadata index
    - token-overlap relevance over chunked document store
    - simple context builder for LLM prompt injection

    Semantic embeddings can be added later without changing callers.
    """

    def __init__(self, dataset_dir: Path):
        self.dataset_dir = dataset_dir
        self.metadata = self._load_json(dataset_dir / "metadata_index.json")
        self.chunks = self._load_jsonl(dataset_dir / "document_store.jsonl")

        self._commands_by_name = {
            row["command"]: row for row in self.metadata.get("commands", [])
        }

    @staticmethod
    def _load_json(path: Path) -> dict[str, Any]:
        return json.loads(path.read_text(encoding="utf-8"))

    @staticmethod
    def _load_jsonl(path: Path) -> list[dict[str, Any]]:
        rows = []
        for line in path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            rows.append(json.loads(line))
        return rows

    def lookup_command(self, command: str) -> dict[str, Any] | None:
        return self._commands_by_name.get(command)

    def search(self, query: str, *, limit: int = 8) -> list[RetrievalResult]:
        """Route query and return ranked chunks.

        Routing strategy:
        - if query contains exact command token, prioritize command-linked snippets
        - else, do token-overlap retrieval over markdown/per chunks
        """
        tokens = set(TOKEN_RE.findall(query.lower()))

        # 1) Structured hit path: known commands in query.
        command_hits = [c for c in tokens if c in self._commands_by_name]
        ranked: list[RetrievalResult] = []

        if command_hits:
            for cmd in command_hits:
                row = self._commands_by_name[cmd]
                examples = row.get("examples", [])
                for ex in examples:
                    ranked.append(
                        RetrievalResult(
                            source_file=ex.get("template", row.get("source_file", "")),
                            title=f"command:{cmd}",
                            score=1.0,
                            text=ex.get("snippet", "") or row.get("description", ""),
                        )
                    )

        # 2) Token-overlap retrieval against chunk store.
        for chunk in self.chunks:
            text = chunk.get("text", "")
            if not text:
                continue
            chunk_tokens = set(TOKEN_RE.findall(text.lower()))
            if not chunk_tokens:
                continue
            overlap = tokens & chunk_tokens
            if not overlap:
                continue
            score = len(overlap) / max(1, len(tokens))
            ranked.append(
                RetrievalResult(
                    source_file=chunk.get("source_file", ""),
                    title=chunk.get("title", "section"),
                    score=score,
                    text=text,
                )
            )

        ranked.sort(key=lambda r: r.score, reverse=True)

        # Deduplicate by (source,title,text-prefix) to keep context compact.
        seen = set()
        deduped: list[RetrievalResult] = []
        for item in ranked:
            key = (item.source_file, item.title, item.text[:120])
            if key in seen:
                continue
            seen.add(key)
            deduped.append(item)
            if len(deduped) >= limit:
                break

        return deduped

    def build_context(self, query: str, *, limit: int = 8) -> dict[str, Any]:
        results = self.search(query, limit=limit)
        commands = sorted(
            {
                token
                for token in TOKEN_RE.findall(query.lower())
                if token in self._commands_by_name
            }
        )

        return {
            "query": query,
            "commands_detected": commands,
            "retrieved": [
                {
                    "source_file": r.source_file,
                    "title": r.title,
                    "score": round(r.score, 4),
                    "text": r.text,
                }
                for r in results
            ],
        }
