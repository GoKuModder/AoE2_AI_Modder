import ast
import inspect
from typing import Any, Dict, List, Optional


def _sanitize_text(text: str) -> str:
    return (
        text.replace("\u2764", "<3")
        .replace("\u201c", '"')
        .replace("\u201d", '"')
        .replace("\u2018", "'")
        .replace("\u2019", "'")
    )


def _humanize_name(name: str) -> str:
    humanized = name.rstrip("_").replace("_", " ").title()
    return humanized.replace("Ai ", "AI ").replace(" Hp", " HP")


def _method_name_for_enum(enum_name: str) -> str:
    lowered = enum_name.lower()
    if lowered == "and":
        return "and_"
    if lowered == "or":
        return "or_"
    return lowered


def _parse_condition_doc(doc: str) -> Dict[str, Any]:
    cleaned = _sanitize_text(inspect.cleandoc(doc) if doc else "")
    lines = [line.strip() for line in cleaned.splitlines()]

    source_internal_name: Optional[str] = None
    doc_parameters: List[str] = []
    notes: List[str] = []

    for line in lines:
        if not line:
            continue
        if line.startswith("Attributes for the **") and "**" in line:
            parts = line.split("**")
            if len(parts) >= 3:
                source_internal_name = parts[1]
            continue
        if line.startswith("- "):
            doc_parameters.append(line[2:].strip())
            continue
        notes.append(line)

    description = " ".join(notes)
    return {
        "source_internal_name": source_internal_name,
        "doc_parameters": doc_parameters,
        "notes": notes,
        "description": description,
    }


def build_conditions_knowledge(
    source_text: str,
    aoe2_methods: Dict[str, Any],
) -> List[Dict[str, Any]]:
    """
    Builds the canonical condition knowledge list from AoE2ScenarioParser source text
    plus method signatures from NewConditionSupport.
    """
    module = ast.parse(source_text)
    condition_class = None
    for node in module.body:
        if isinstance(node, ast.ClassDef) and node.name == "ConditionId":
            condition_class = node
            break
    if condition_class is None:
        raise ValueError("Could not find ConditionId in conditions source.")

    entries: List[Dict[str, Any]] = []
    body = condition_class.body

    for index, node in enumerate(body):
        if not isinstance(node, ast.Assign):
            continue
        if len(node.targets) != 1 or not isinstance(node.targets[0], ast.Name):
            continue
        if not isinstance(node.value, ast.Constant) or not isinstance(node.value.value, int):
            continue

        enum_name = node.targets[0].id
        condition_id = node.value.value
        method_name = _method_name_for_enum(enum_name)
        method_info = aoe2_methods.get(method_name)

        doc = ""
        if index + 1 < len(body):
            next_node = body[index + 1]
            if (
                isinstance(next_node, ast.Expr)
                and isinstance(next_node.value, ast.Constant)
                and isinstance(next_node.value.value, str)
            ):
                doc = next_node.value.value

        parsed_doc = _parse_condition_doc(doc)

        parameters: List[Dict[str, Any]] = []
        method_params = method_info.get("params", []) if method_info else []
        doc_param_map = {name: "" for name in parsed_doc["doc_parameters"]}

        for param in method_params:
            parameters.append(
                {
                    "name": param["name"],
                    "type": param["type"],
                    "default": param["default"],
                    "description": doc_param_map.get(param["name"], ""),
                }
            )

        method_param_names = {param["name"] for param in method_params}
        for doc_param in parsed_doc["doc_parameters"]:
            if doc_param not in method_param_names:
                parameters.append(
                    {
                        "name": doc_param,
                        "type": "",
                        "default": None,
                        "description": "",
                    }
                )

        display_name = _humanize_name(method_name)
        description = parsed_doc["description"] or f"Parser condition for {display_name}."

        entries.append(
            {
                "condition_id": condition_id,
                "internal_name": method_name,
                "source_internal_name": parsed_doc["source_internal_name"] or method_name,
                "display_name": display_name,
                "description": description,
                "signature": method_info["signature"] if method_info else method_name,
                "parameters": parameters,
                "notes": parsed_doc["notes"],
            }
        )

    entries.sort(key=lambda entry: entry["condition_id"])
    return entries
