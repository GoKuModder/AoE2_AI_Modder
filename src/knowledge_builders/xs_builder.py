from __future__ import annotations

import hashlib
import re
from pathlib import Path
from typing import Any


SOURCE_LINE_RE = re.compile(r"-\s+`([^`]+)`\s+<-\s+(\S+)")


def _normalize_rel_path(path: str) -> str:
    return path.strip().replace("\\", "/")


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def _sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def parse_source_page_index(path: Path) -> list[dict[str, str]]:
    entries: list[dict[str, str]] = []
    for raw_line in _read_text(path).splitlines():
        match = SOURCE_LINE_RE.search(raw_line)
        if not match:
            continue
        rel_path = _normalize_rel_path(match.group(1))
        source_url = match.group(2)
        entries.append({"relative_path": rel_path, "source_url": source_url})

    deduped: dict[str, dict[str, str]] = {}
    for row in entries:
        deduped[row["relative_path"]] = row

    return [deduped[key] for key in sorted(deduped)]


def collect_source_documents(
    source_root: Path,
    index_entries: list[dict[str, str]],
) -> list[dict[str, Any]]:
    docs: list[dict[str, Any]] = []
    for row in index_entries:
        rel = row["relative_path"]
        full_path = source_root / rel
        if not full_path.exists() or not full_path.is_file() or full_path.suffix.lower() != ".md":
            continue
        text = _read_text(full_path)
        docs.append(
            {
                "relative_path": rel,
                "source_url": row["source_url"],
                "sha256": _sha256_text(text),
                "text": text,
            }
        )

    return sorted(docs, key=lambda item: item["relative_path"])


def build_metadata_index(documents: list[dict[str, Any]]) -> dict[str, Any]:
    rows = [
        {
            "id": f"doc::{doc['relative_path']}",
            "relative_path": doc["relative_path"],
            "source_url": doc["source_url"],
            "sha256": doc["sha256"],
            "kind": "markdown",
        }
        for doc in documents
    ]
    return {
        "schema_version": 1,
        "dataset": "xs_knowledge",
        "counts": {
            "source_documents": len(rows),
        },
        "documents": rows,
    }


def build_chunk_store(documents: list[dict[str, Any]]) -> list[dict[str, Any]]:
    chunks: list[dict[str, Any]] = []
    for doc in documents:
        chunks.extend(_chunk_markdown(doc))
    return chunks


def _chunk_markdown(document: dict[str, Any]) -> list[dict[str, Any]]:
    source_file = document["relative_path"]
    text = document["text"]
    lines = text.splitlines()
    chunks: list[dict[str, Any]] = []
    current_title = "document"
    buffer: list[str] = []
    chunk_index = 0

    def flush() -> None:
        nonlocal chunk_index
        payload = "\n".join(buffer).strip()
        if not payload:
            return
        chunks.append(
            {
                "id": f"{source_file}::h{chunk_index}",
                "source_file": source_file,
                "source_url": document["source_url"],
                "source_sha256": document["sha256"],
                "kind": "markdown",
                "title": current_title,
                "text": payload,
            }
        )
        chunk_index += 1

    for line in lines:
        if line.startswith("#"):
            flush()
            buffer = [line]
            current_title = line.lstrip("#").strip() or "section"
            continue
        buffer.append(line)

    flush()
    return chunks
