from __future__ import annotations

import re
from pathlib import Path
from typing import Any


COMMAND_RE = re.compile(r"\(([a-z][a-z0-9-]*)")


def _strip_quoted_strings(text: str) -> str:
    # Avoid false command matches from text like "(choice ..." inside chat strings.
    return re.sub(r'"[^"\\]*(?:\\.[^"\\]*)*"', '""', text)


def _strip_per_comments(text: str) -> str:
    # In .per files, ';' starts a comment to end-of-line.
    return re.sub(r";.*$", "", text, flags=re.MULTILINE)


def _extract_commands(script_text: str) -> list[str]:
    normalized = _strip_quoted_strings(script_text)
    normalized = _strip_per_comments(normalized)
    return COMMAND_RE.findall(normalized)


def validate_ai_script(script_text: str, metadata_index: dict[str, Any]) -> dict[str, Any]:
    """Validate generated .per script against allowlist constraints.

    This is intentionally strict because the project goal is no-error AI script output.
    """
    rows = metadata_index.get("commands", [])
    status_by_cmd = {r["command"]: r["status"] for r in rows if "command" in r}

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

    # Domain-specific quality checks.
    if "taunt-detected" in commands and "acknowledge-taunt" not in commands:
        warnings.append("taunt-detected used without acknowledge-taunt")

    if "attack-now" in commands:
        gating_tokens = {
            "goal",
            "timer-triggered",
            "game-time",
            "defend-soldier-count",
            "attack-soldier-count",
        }
        if not any(tok in commands for tok in gating_tokens):
            warnings.append("attack-now appears without obvious state/timer/army gate")

    ok = not blocked and not unknown

    return {
        "ok": ok,
        "commands_found": sorted(set(commands)),
        "blocked_commands": sorted(blocked),
        "unknown_commands": sorted(unknown),
        "warnings": warnings,
    }


def load_and_validate(script_path: Path, metadata_path: Path) -> dict[str, Any]:
    import json

    script_text = script_path.read_text(encoding="utf-8", errors="replace")
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    return validate_ai_script(script_text, metadata)
