import ast
import json
import warnings
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple


IGNORED_PATH_PARTS = {".venv", "__pycache__"}


def _path_has_ignored_part(path: Path, extra_ignored_parts: Iterable[str]) -> bool:
    parts = set(path.parts)
    if parts & IGNORED_PATH_PARTS:
        return True
    return any(part in parts for part in extra_ignored_parts)


def _load_reference_projects(reference_projects_path: Path) -> List[Dict[str, Any]]:
    payload = json.loads(reference_projects_path.read_text(encoding="utf-8"))
    return payload["projects"]


def _call_chain(node: ast.AST) -> List[str]:
    parts: List[str] = []
    current = node
    while isinstance(current, ast.Attribute):
        parts.append(current.attr)
        current = current.value
    if isinstance(current, ast.Name):
        parts.append(current.id)
    return list(reversed(parts))


def _scan_project_calls(
    project: Dict[str, Any],
    extra_ignored_parts: Iterable[str],
) -> List[Dict[str, Any]]:
    root = Path(project["path"])
    observations: List[Dict[str, Any]] = []

    for path in root.rglob("*.py"):
        if _path_has_ignored_part(path, extra_ignored_parts):
            continue

        text = path.read_text(encoding="utf-8", errors="ignore")
        try:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore", SyntaxWarning)
                tree = ast.parse(text)
        except SyntaxError:
            continue

        lines = text.splitlines()
        relative_path = str(path.relative_to(root))

        for node in ast.walk(tree):
            if not isinstance(node, ast.Call) or not isinstance(node.func, ast.Attribute):
                continue
            chain = _call_chain(node.func)
            if len(chain) < 2 or chain[-2] not in {"new_condition", "new_effect"}:
                continue

            kind = "condition" if chain[-2] == "new_condition" else "effect"
            line_number = getattr(node, "lineno", 1)
            code = lines[line_number - 1].strip() if 0 < line_number <= len(lines) else ""

            observations.append(
                {
                    "kind": kind,
                    "internal_name": chain[-1],
                    "project_id": project["id"],
                    "project_title": project["title"],
                    "project_priority": project["priority"],
                    "path": relative_path.replace("/", "\\"),
                    "line_number": line_number,
                    "code": code,
                }
            )

    return observations


def _sort_examples(examples: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    return sorted(
        examples,
        key=lambda item: (
            item["project_priority"],
            item["project_id"],
            item["path"].lower(),
            item["line_number"],
        ),
    )


def _build_usage_entries(
    knowledge_entries: List[Dict[str, Any]],
    observations: List[Dict[str, Any]],
    id_key: str,
) -> List[Dict[str, Any]]:
    grouped: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    for observation in observations:
        grouped[observation["internal_name"]].append(observation)

    usage_entries: List[Dict[str, Any]] = []
    for entry in knowledge_entries:
        item_observations = _sort_examples(grouped.get(entry["internal_name"], []))
        project_groups: Dict[Tuple[str, str, int], List[Dict[str, Any]]] = defaultdict(list)
        for observation in item_observations:
            key = (
                observation["project_id"],
                observation["project_title"],
                observation["project_priority"],
            )
            project_groups[key].append(observation)

        project_summaries = []
        for (project_id, project_title, project_priority), project_examples in sorted(
            project_groups.items(),
            key=lambda item: (item[0][2], item[0][0]),
        ):
            representative_paths = []
            for example in project_examples:
                if example["path"] not in representative_paths:
                    representative_paths.append(example["path"])
                if len(representative_paths) >= 3:
                    break
            project_summaries.append(
                {
                    "project_id": project_id,
                    "project_title": project_title,
                    "project_priority": project_priority,
                    "usage_count": len(project_examples),
                    "representative_paths": representative_paths,
                }
            )

        usage_entries.append(
            {
                id_key: entry[id_key],
                "internal_name": entry["internal_name"],
                "display_name": entry["display_name"],
                "usage_status": (
                    "used_in_reference_projects"
                    if item_observations
                    else "not_observed_in_reference_projects"
                ),
                "usage_count": len(item_observations),
                "used_in_projects": [summary["project_id"] for summary in project_summaries],
                "project_summaries": project_summaries,
                "examples": [
                    {
                        "project_id": observation["project_id"],
                        "project_title": observation["project_title"],
                        "path": observation["path"],
                        "line_number": observation["line_number"],
                        "code": observation["code"],
                    }
                    for observation in item_observations[:8]
                ],
            }
        )

    return usage_entries


def build_trigger_project_usage(
    condition_entries: List[Dict[str, Any]],
    effect_entries: List[Dict[str, Any]],
    reference_projects_path: Path,
) -> Dict[str, List[Dict[str, Any]]]:
    reference_projects = _load_reference_projects(reference_projects_path)

    project_filters = {
        "goku_rpg_project": {"Difficulty"},
        "goku_rpg_genie_code": set(),
        "lords_of_diplomacy_easy_mode": set(),
        "hide_and_seek": set(),
    }

    trigger_projects = [
        project
        for project in reference_projects
        if project["id"]
        in {
            "lords_of_diplomacy_easy_mode",
            "goku_rpg_project",
            "hide_and_seek",
        }
    ]

    observations: List[Dict[str, Any]] = []
    for project in trigger_projects:
        observations.extend(
            _scan_project_calls(project, project_filters.get(project["id"], set()))
        )

    condition_observations = [
        observation for observation in observations if observation["kind"] == "condition"
    ]
    effect_observations = [
        observation for observation in observations if observation["kind"] == "effect"
    ]

    return {
        "conditions": _build_usage_entries(
            condition_entries,
            condition_observations,
            "condition_id",
        ),
        "effects": _build_usage_entries(
            effect_entries,
            effect_observations,
            "effect_id",
        ),
    }
