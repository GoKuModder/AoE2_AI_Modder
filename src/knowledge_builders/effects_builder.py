from typing import Any, Dict, List, Optional
import re
from dataclasses import dataclass
from src.knowledge_builders.utils import require_bs4, clean_ws

try:
    from bs4 import BeautifulSoup  # type: ignore
except ImportError:
    BeautifulSoup = None

UGC_EFFECTS_URL = "https://ugc.aoe2.rocks/scenarios/triggers/effects/effects/"

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

METHOD_TITLE_OVERRIDES = {
    "acknowledge_ai_signal": "Acknowledge AI Signal",
    "acknowledge_multiplayer_ai_signal": "Acknowledge Multiplayer AI Signal",
}


@dataclass
class UgcEffect:
    name: str
    url: str
    config_fields: List[str]
    notes: str


def _method_to_ugc_title(method_name: str) -> str:
    if method_name in METHOD_TITLE_OVERRIDES:
        return METHOD_TITLE_OVERRIDES[method_name]
    return method_name.replace("_", " ").title()


def _parse_ugc_effects(html: str) -> Dict[str, UgcEffect]:
    """
    Parses the UGC effects page into {effect_name: UgcEffect}.
    """
    require_bs4()
    soup = BeautifulSoup(html, "html.parser")

    effects: Dict[str, UgcEffect] = {}

    # UGC uses h3 headings like: "3.44. Enable Disable Object"
    h3_list = soup.find_all("h3")
    for h3 in h3_list:
        heading = clean_ws(h3.get_text(" ", strip=True))
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

            text = clean_ws(sib.get_text(" ", strip=True))
            if not text:
                continue

            # Detect config intro line
            if "The configurations for this effect are as follows" in text:
                saw_config_intro = True
                continue

            # If next element is a list after config intro, extract fields
            if saw_config_intro and getattr(sib, "name", None) in {"ol", "ul"}:
                for li in sib.find_all("li"):
                    item = clean_ws(li.get_text(" ", strip=True))
                    # strip "1. " if present in text
                    item = re.sub(r"^\d+\.\s*", "", item).strip()
                    if item:
                        config_fields.append(item)
                saw_config_intro = False
                continue

            # Keep short notes (avoid page bloat)
            if len(text) <= 240:
                notes_chunks.append(text)

        effects[effect_name] = UgcEffect(
            name=effect_name,
            url=UGC_EFFECTS_URL,
            config_fields=config_fields,
            notes="\n".join(notes_chunks[:8]),
        )

    return effects


def build_effects_knowledge(html: str, aoe2sp_methods: Dict[str, Any]) -> Dict[str, Any]:
    """
    Merges UGC effect data with AoE2SP method introspection data.
    """
    ugc_effects = _parse_ugc_effects(html)
    
    merged_dict: Dict[str, Any] = {}

    for method_name, method in sorted(aoe2sp_methods.items()):
        ugc_title = _method_to_ugc_title(method_name)
        ugc = ugc_effects.get(ugc_title)

        # Assuming method object has .signature and .params
        # If it's a dict, use .get or ['key']. 
        # The prompt implies "input: normalized inputs". 
        # The Orchestrator will likely pass the objects created by introspection.
        
        # Safe access helper
        signature = getattr(method, "signature", None) or method.get("signature")
        params = getattr(method, "params", None) or method.get("params")

        row = {
            "method": method_name,
            "signature": signature,
            "params": params,
            "ugc_name": ugc.name if ugc else None,
            "ugc_url": ugc.url if ugc else None,
            "ugc_config_fields": ugc.config_fields if ugc else [],
            "ugc_notes": ugc.notes if ugc else "",
            "ugc_to_aoe2sp_field_map": {
                field: UGC_TO_AOE2SP_FIELD_MAP.get(field)
                for field in (ugc.config_fields if ugc else [])
            },
        }
        merged_dict[method_name] = row

    return merged_dict
