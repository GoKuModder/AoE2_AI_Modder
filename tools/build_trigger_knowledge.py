from __future__ import annotations

import inspect
import os
import re
import sys
import textwrap
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional

# If you prefer zero deps, keep urllib. If you can install deps, requests is nicer.
try:
    import requests  # type: ignore
except Exception:  # pragma: no cover
    requests = None  # type: ignore

try:
    from bs4 import BeautifulSoup  # type: ignore
except Exception:  # pragma: no cover
    BeautifulSoup = None  # type: ignore


UGC_EFFECTS_URL = "https://ugc.aoe2.rocks/scenarios/triggers/effects/effects/"
UGC_ATTRIBUTES_URL = "https://ugc.aoe2.rocks/general/attributes/attributes/"

OUT_DIR = Path("docs/trigger_knowledge")
CACHE_DIR = OUT_DIR / "_cache"

# Heuristic mapping from UGC editor field names -> AoE2ScenarioParser parameter names
UGC_TO_AOE2SP_FIELD_MAP = {
    "Unit List 1": "object_list_unit_id",
    "Unit List 2": "object_list_unit_id_2",
    "Selected Objects": "object_list_unit_id",
    "Source Player": "source_player",
    "Enabled": "enabled",
    "Technology": "technology",
    "Button Location": "button_location",
    "Button": "button_location",
    "Operation": "operation",
    "Attribute List": "object_attributes",
    "Quantity": "quantity",
    "Message": "message",
    "Area": "area_x1_y1_x2_y2 (varies; see library effect)",
}

# Fix title-casing mismatches (AI -> AI, etc.)
METHOD_TITLE_OVERRIDES = {
    "acknowledge_ai_signal": "Acknowledge AI Signal",
    "acknowledge_multiplayer_ai_signal": "Acknowledge Multiplayer AI Signal",
}


@dataclass
class Aoe2SpMethod:
    name: str
    signature: str
    params: List[str]


@dataclass
class UgcEffect:
    name: str
    url: str
    config_fields: List[str]
    notes: str


def _http_get(url: str, cache_path: Path) -> str:
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    if cache_path.exists():
        return cache_path.read_text(encoding="utf-8", errors="ignore")

    if requests is None:
        raise RuntimeError(
            "Missing dependency 'requests'. Install it (PyCharm Interpreter Packages) or adapt to urllib."
        )

    resp = requests.get(url, timeout=30, headers={"User-Agent": "ChainBoundTriggerKnowledge/1.0"})
    resp.raise_for_status()
    cache_path.write_text(resp.text, encoding="utf-8")
    return resp.text


def _require_bs4() -> None:
    if BeautifulSoup is None:
        raise RuntimeError(
            "Missing dependency 'beautifulsoup4'. Install it (PyCharm Interpreter Packages)."
        )


def _clean_ws(s: str) -> str:
    s = s.replace("¶", "")
    return re.sub(r"\s+", " ", s).strip()



def parse_ugc_effects(html: str) -> Dict[str, UgcEffect]:
    """
    Parses the UGC effects page into {effect_name: UgcEffect}.
    We key by effect display name (e.g. 'Enable Disable Object').
    """
    _require_bs4()
    soup = BeautifulSoup(html, "html.parser")

    effects: Dict[str, UgcEffect] = {}

    # UGC uses h3 headings like: "3.44. Enable Disable Object"
    h3_list = soup.find_all("h3")
    for h3 in h3_list:
        heading = _clean_ws(h3.get_text(" ", strip=True))
        m = re.match(r"^\d+\.\d+\.\s+(.*)$", heading)
        if not m:
            continue

        effect_name = m.group(1).strip()

        # Pull content until next h3
        notes_chunks: List[str] = []
        config_fields: List[str] = []

        saw_config_intro = False
        for sib in h3.next_siblings:
            if getattr(sib, "name", None) == "h3":
                break
            if not getattr(sib, "get_text", None):
                continue

            text = _clean_ws(sib.get_text(" ", strip=True))
            if not text:
                continue

            # Detect config intro line
            if "The configurations for this effect are as follows" in text:
                saw_config_intro = True
                continue

            # If next element is a list after config intro, extract fields
            if saw_config_intro and getattr(sib, "name", None) in {"ol", "ul"}:
                for li in sib.find_all("li"):
                    item = _clean_ws(li.get_text(" ", strip=True))
                    # strip "1. " if present in text
                    item = re.sub(r"^\d+\.\s*", "", item).strip()
                    if item:
                        config_fields.append(item)
                saw_config_intro = False
                continue

            # Keep short notes (avoid page bloat)
            if len(text) <= 240:
                notes_chunks.append(text)

        # Build a stable URL: point to the page; agents can search within
        effects[effect_name] = UgcEffect(
            name=effect_name,
            url=UGC_EFFECTS_URL,
            config_fields=config_fields,
            notes="\n".join(notes_chunks[:8]),
        )

    return effects


def parse_ugc_attributes(html: str, keep_ids: Optional[set[int]] = None) -> Dict[int, Dict[str, Any]]:
    """
    Extracts attributes by ID from the UGC attributes page.
    If keep_ids is provided, only those IDs are kept.
    """
    _require_bs4()
    soup = BeautifulSoup(html, "html.parser")

    # UGC attributes are h2 headings like: "42. Train Location"
    attrs: Dict[int, Dict[str, Any]] = {}
    for h2 in soup.find_all("h2"):
        heading = _clean_ws(h2.get_text(" ", strip=True))
        m = re.match(r"^(\d+)\.\s+(.*)$", heading)
        if not m:
            continue

        attr_id = int(m.group(1))
        attr_name = m.group(2).strip()
        if keep_ids is not None and attr_id not in keep_ids:
            continue

        desc_lines: List[str] = []
        for sib in h2.next_siblings:
            if getattr(sib, "name", None) == "h2":
                break
            if not getattr(sib, "get_text", None):
                continue
            text = _clean_ws(sib.get_text(" ", strip=True))
            if text:
                desc_lines.append(text)
            if len(desc_lines) >= 6:
                break

        attrs[attr_id] = {
            "id": attr_id,
            "name": attr_name,
            "description": " ".join(desc_lines),
            "source": UGC_ATTRIBUTES_URL,
        }

    return attrs


def introspect_aoe2sp_effects() -> Dict[str, Aoe2SpMethod]:
    """
    Introspects AoE2ScenarioParser NewEffectSupport to obtain methods + signatures.
    """
    try:
        from AoE2ScenarioParser.objects.support.new_effect import NewEffectSupport  # type: ignore
    except Exception as e:
        raise RuntimeError(
            "Could not import AoE2ScenarioParser. Ensure your venv/interpreter is set correctly."
        ) from e

    methods: Dict[str, Aoe2SpMethod] = {}
    for name, fn in inspect.getmembers(NewEffectSupport, predicate=inspect.isfunction):
        if name.startswith("_"):
            continue
        sig = str(inspect.signature(fn))
        params = [p.name for p in inspect.signature(fn).parameters.values() if p.name != "self"]
        methods[name] = Aoe2SpMethod(name=name, signature=f"{name}{sig}", params=params)
    return methods


def method_to_ugc_title(method_name: str) -> str:
    if method_name in METHOD_TITLE_OVERRIDES:
        return METHOD_TITLE_OVERRIDES[method_name]
    return method_name.replace("_", " ").title()


def write_python_module(path: Path, var_name: str, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    content = f"{var_name} = {repr(payload)}\n"
    path.write_text(content, encoding="utf-8")


def write_markdown_effects(path: Path, merged: List[Dict[str, Any]]) -> None:
    lines: List[str] = []
    lines.append("# Trigger Knowledge: Effects\n")
    lines.append("Generated file. Do not hand-edit; run tools/build_trigger_knowledge.py.\n")
    lines.append("| AoE2SP Method | Signature | UGC Name | UGC Fields | |\n")
    lines.append("|---|---|---|---|---|\n")

    for row in merged:
        fields = ", ".join(row.get("ugc_config_fields") or [])
        lines.append(
            f"| `{row['method']}` | `{row['signature']}` | {row.get('ugc_name','')} | {fields} | {row.get('ugc_url','')} |\n"
        )

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(lines), encoding="utf-8")


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    CACHE_DIR.mkdir(parents=True, exist_ok=True)

    ugc_effects_html = _http_get(UGC_EFFECTS_URL, CACHE_DIR / "ugc_effects.html")
    ugc_attrs_html = _http_get(UGC_ATTRIBUTES_URL, CACHE_DIR / "ugc_attributes.html")

    ugc_effects = parse_ugc_effects(ugc_effects_html)
    # Keep the attributes you already rely on for training/enable logic.
    # Train Location (42), Train Button (43), Available Unit Flag (126), Disabled Unit Flag (127)
    ugc_attrs = parse_ugc_attributes(ugc_attrs_html)

    aoe2sp_methods = introspect_aoe2sp_effects()

    merged_rows: List[Dict[str, Any]] = []
    merged_dict: Dict[str, Any] = {}

    for method_name, method in sorted(aoe2sp_methods.items()):
        ugc_title = method_to_ugc_title(method_name)
        ugc = ugc_effects.get(ugc_title)

        row = {
            "method": method_name,
            "signature": method.signature,
            "params": method.params,
            "ugc_name": ugc.name if ugc else None,
            "ugc_url": ugc.url if ugc else None,
            "ugc_config_fields": ugc.config_fields if ugc else [],
            "ugc_notes": ugc.notes if ugc else "",
            "ugc_to_aoe2sp_field_map": {
                field: UGC_TO_AOE2SP_FIELD_MAP.get(field)
                for field in (ugc.config_fields if ugc else [])
            },
        }
        merged_rows.append(row)
        merged_dict[method_name] = row

    write_python_module(OUT_DIR / "effects_knowledge.py", "EFFECTS", merged_dict)
    write_markdown_effects(OUT_DIR / "effects_knowledge.md", merged_rows)

    write_python_module(OUT_DIR / "attributes_knowledge.py", "ATTRIBUTES", ugc_attrs)
    (OUT_DIR / "attributes_knowledge.md").write_text(
        "# Trigger Knowledge: Attributes (subset)\n\n"
        "Generated file. Do not hand-edit; run tools/build_trigger_knowledge.py.\n\n"
        + "\n".join(
            f"- **{a['id']} {a['name']}**: {a['description']} (Source: {a['source']})"
            for a in ugc_attrs.values()
        )
        + "\n",
        encoding="utf-8",
    )

    print(f"Wrote:\n- {OUT_DIR / 'effects_knowledge.py'}\n- {OUT_DIR / 'effects_knowledge.md'}\n"
          f"- {OUT_DIR / 'attributes_knowledge.py'}\n- {OUT_DIR / 'attributes_knowledge.md'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
