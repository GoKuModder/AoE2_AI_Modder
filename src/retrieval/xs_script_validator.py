from __future__ import annotations

import re
import math
import json
from functools import lru_cache
from importlib import resources
from pathlib import Path
from typing import Any


# Match function calls in XS: functionName(
XS_COMMAND_RE = re.compile(r"\b([a-zA-Z_][a-zA-Z0-9_]*)\s*\(")

# XS single-line comment: //
XS_COMMENT_RE = re.compile(r"//.*$", re.MULTILINE)

# XS multi-line comment: /* ... */
XS_MULTILINE_COMMENT_RE = re.compile(r"/\*.*?\*/", re.DOTALL)


def _strip_comments(text: str) -> str:
    """Strip comments from XS script to avoid false positives."""
    text = XS_MULTILINE_COMMENT_RE.sub("", text)
    text = XS_COMMENT_RE.sub("", text)
    return text


def _extract_commands(script_text: str) -> list[str]:
    """Extract function/command names from XS script."""
    normalized = _strip_comments(script_text)
    return XS_COMMAND_RE.findall(normalized)


@lru_cache(maxsize=1)
def _packaged_xs_function_names() -> frozenset[str]:
    """Load builtin function names from the packaged XS symbol catalog."""
    try:
        text = resources.files("src.data.xs").joinpath(
            "agent_database/xs_functions_catalog.json"
        ).read_text(encoding="utf-8")
        rows = json.loads(text)
    except (FileNotFoundError, ModuleNotFoundError, OSError, TypeError, json.JSONDecodeError):
        return frozenset()
    if not isinstance(rows, list):
        return frozenset()
    return frozenset(
        row["name"]
        for row in rows
        if isinstance(row, dict) and isinstance(row.get("name"), str) and row["name"]
    )


def validate_xs_script(script_text: str, metadata_index: dict[str, Any]) -> dict[str, Any]:
    """Validate generated .xs script against allowlist constraints.

    Explicit command statuses in metadata_index take precedence. Builtin XS functions
    from the packaged function catalog are added as allowed entries when they are not
    listed there, so newly cataloged engine functions are recognized by validation.

    API parity with validate_ai_script for consistent validation interface.
    """
    rows = metadata_index.get("commands", [])
    if not isinstance(rows, list):
        rows = []
    status_by_cmd = {
        row["name"]: "allowed" for row in _packaged_xs_function_names()
    }
    for row in rows:
        if isinstance(row, dict) and isinstance(row.get("command"), str):
            status_by_cmd[row["command"]] = row.get("status", "allowed")

    commands = _extract_commands(script_text)

    unknown: set[str] = set()
    blocked: set[str] = set()
    warnings: list[str] = []

    for cmd in commands:
        if cmd not in status_by_cmd:
            unknown.add(cmd)
            continue
        if status_by_cmd[cmd] == "blocked":
            blocked.add(cmd)

    # Domain-specific quality checks for XS.
    # XS-specific: warn about potential infinite loops without sleep/delay.
    if "while" in commands and "xsSleep" not in commands and "xsDisableSelf" not in commands:
        warnings.append("while loop without xsSleep may cause infinite loop")

    # XS-specific: warn about rule without condition when likely needed.
    if "rule" in commands and "condition" not in commands:
        warnings.append("rule defined without explicit condition may run every tick")

    ok = not blocked and not unknown

    return {
        "ok": ok,
        "commands_found": sorted(set(commands)),
        "blocked_commands": sorted(blocked),
        "unknown_commands": sorted(unknown),
        "warnings": warnings,
    }


def _context_error(error_code: str, error_path: str, message: str) -> dict[str, Any]:
    return {
        "ok": False,
        "error_code": error_code,
        "error_path": error_path,
        "message": message,
    }


def validate_xs_retrieval_context(payload: Any) -> dict[str, Any]:
    """Validate XS retrieval context payload with deterministic error output."""
    if not isinstance(payload, dict):
        return _context_error(
            "XS_CONTEXT_INVALID_TYPE",
            "",
            "context payload must be an object",
        )

    for key in ("query", "commands_detected", "retrieved"):
        if key not in payload:
            return _context_error(
                "XS_CONTEXT_MISSING_KEY",
                key,
                f"missing required key: {key}",
            )

    query = payload["query"]
    if not isinstance(query, str):
        return _context_error(
            "XS_CONTEXT_INVALID_TYPE",
            "query",
            "query must be a string",
        )

    commands_detected = payload["commands_detected"]
    if not isinstance(commands_detected, list):
        return _context_error(
            "XS_CONTEXT_INVALID_TYPE",
            "commands_detected",
            "commands_detected must be a list",
        )

    for index, value in enumerate(commands_detected):
        if not isinstance(value, str):
            return _context_error(
                "XS_CONTEXT_INVALID_TYPE",
                f"commands_detected[{index}]",
                "commands_detected items must be strings",
            )

    retrieved = payload["retrieved"]
    if not isinstance(retrieved, list):
        return _context_error(
            "XS_CONTEXT_INVALID_TYPE",
            "retrieved",
            "retrieved must be a list",
        )

    required_item_keys = ("source", "title", "score", "text")
    for index, item in enumerate(retrieved):
        item_path = f"retrieved[{index}]"
        if not isinstance(item, dict):
            return _context_error(
                "XS_CONTEXT_INVALID_TYPE",
                item_path,
                "retrieved items must be objects",
            )

        for key in required_item_keys:
            if key not in item:
                return _context_error(
                    "XS_CONTEXT_MISSING_KEY",
                    f"{item_path}.{key}",
                    f"missing required key: {key}",
                )

        if not isinstance(item["source"], str):
            return _context_error(
                "XS_CONTEXT_INVALID_TYPE",
                f"{item_path}.source",
                "source must be a string",
            )
        if not isinstance(item["title"], str):
            return _context_error(
                "XS_CONTEXT_INVALID_TYPE",
                f"{item_path}.title",
                "title must be a string",
            )

        score = item["score"]
        if not isinstance(score, (int, float)) or isinstance(score, bool):
            return _context_error(
                "XS_CONTEXT_INVALID_TYPE",
                f"{item_path}.score",
                "score must be a number",
            )
        if not math.isfinite(float(score)):
            return _context_error(
                "XS_CONTEXT_INVALID_VALUE",
                f"{item_path}.score",
                "score must be finite",
            )

        if not isinstance(item["text"], str):
            return _context_error(
                "XS_CONTEXT_INVALID_TYPE",
                f"{item_path}.text",
                "text must be a string",
            )

    return {
        "ok": True,
        "error_code": "OK",
        "error_path": "",
        "message": "",
    }


def load_and_validate(script_path: Path, metadata_path: Path) -> dict[str, Any]:
    """Load XS script and metadata, then validate."""
    import json

    script_text = script_path.read_text(encoding="utf-8", errors="replace")
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    return validate_xs_script(script_text, metadata)
