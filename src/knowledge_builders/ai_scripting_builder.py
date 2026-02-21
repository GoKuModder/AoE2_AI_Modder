from __future__ import annotations

import re
from pathlib import Path
from typing import Any


COMMAND_RE = re.compile(r"\(([a-z][a-z0-9-]*)")


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def _extract_commands_from_per(text: str) -> list[str]:
    """Extract command tokens from .per scripts.

    We intentionally keep this parser simple and resilient.
    """
    commands = []
    for match in COMMAND_RE.finditer(text):
        token = match.group(1)
        if token in {"defrule", "defconst", "and", "or", "not", "true", "false"}:
            continue
        commands.append(token)
    return sorted(set(commands))


def parse_allowlist_markdown(path: Path) -> dict[str, Any]:
    """Parse allowlist markdown into structured command sets.

    Expected source: AoE2_AI_Scripting_Guide/06_LLM_COMMAND_ALLOWLIST.md
    """
    text = _read_text(path)
    allowed: dict[str, dict[str, Any]] = {}
    blocked: dict[str, dict[str, Any]] = {}

    section = ""
    parse_mode = ""
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if line.startswith("### A"):
            section = line.replace("### ", "")
            parse_mode = "allowed"
            continue
        if line.startswith("## B)"):
            section = "blocked"
            parse_mode = "blocked"
            continue
        if line.startswith("## C)") or line.startswith("## D)"):
            section = ""
            parse_mode = ""
            continue
        if not line.startswith("- `"):
            continue
        if not parse_mode:
            continue

        # Handles "- `cmd` - desc" and grouped forms like "- `a` / `b` - desc"
        backtick_tokens = re.findall(r"`([^`]+)`", line)
        if not backtick_tokens:
            continue

        description = ""
        if " - " in line:
            description = line.split(" - ", 1)[1].strip()

        for token in backtick_tokens:
            if " " in token:
                # Skip non-command literals like snippets in prose.
                continue
            if not re.match(r"^[a-z][a-z0-9-]*$", token):
                continue
            if parse_mode == "blocked":
                blocked[token] = {
                    "command": token,
                    "status": "blocked",
                    "section": "B",
                    "description": description,
                    "source_file": str(path).replace("\\", "/"),
                }
            else:
                allowed[token] = {
                    "command": token,
                    "status": "allowed",
                    "section": section or "A",
                    "description": description,
                    "source_file": str(path).replace("\\", "/"),
                }

    return {
        "allowed": allowed,
        "blocked": blocked,
    }


def build_metadata_index(
    allowlist_path: Path,
    template_paths: list[Path],
) -> dict[str, Any]:
    """Build metadata index for deterministic retrieval and validation."""
    parsed = parse_allowlist_markdown(allowlist_path)

    allowed = parsed["allowed"]
    blocked = parsed["blocked"]

    # Attach usage examples from template scripts.
    template_examples: dict[str, list[dict[str, Any]]] = {}
    for tpath in template_paths:
        text = _read_text(tpath)
        commands = _extract_commands_from_per(text)
        for cmd in commands:
            template_examples.setdefault(cmd, []).append(
                {
                    "template": str(tpath).replace("\\", "/"),
                    "snippet": _extract_first_snippet_for_command(text, cmd),
                }
            )

    entries: list[dict[str, Any]] = []
    for cmd, row in sorted(allowed.items()):
        enriched = dict(row)
        enriched["examples"] = template_examples.get(cmd, [])
        entries.append(enriched)

    for cmd, row in sorted(blocked.items()):
        enriched = dict(row)
        enriched["examples"] = template_examples.get(cmd, [])
        entries.append(enriched)

    return {
        "schema_version": 1,
        "source": str(allowlist_path).replace("\\", "/"),
        "counts": {
            "allowed": len(allowed),
            "blocked": len(blocked),
            "total": len(entries),
        },
        "commands": entries,
    }


def _extract_first_snippet_for_command(text: str, cmd: str) -> str:
    for line in text.splitlines():
        if f"({cmd}" in line:
            return line.strip()
    return ""


def build_document_store(doc_paths: list[Path]) -> list[dict[str, Any]]:
    """Build chunked document store from markdown/per guides.

    Chunking approach:
    - Markdown: split by heading blocks for high-signal retrieval chunks.
    - .per files: keep full file as one chunk (small templates).
    """
    chunks: list[dict[str, Any]] = []

    for path in doc_paths:
        rel = str(path).replace("\\", "/")
        text = _read_text(path)
        suffix = path.suffix.lower()

        if suffix == ".md":
            chunks.extend(_chunk_markdown(rel, text))
        else:
            chunks.append(
                {
                    "id": f"{rel}::full",
                    "source_file": rel,
                    "kind": "template" if suffix == ".per" else "text",
                    "title": path.name,
                    "text": text.strip(),
                }
            )

    return chunks


def _chunk_markdown(source_file: str, text: str) -> list[dict[str, Any]]:
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
