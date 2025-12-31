from typing import Any, Dict, List, Optional, Set
import re
from src.knowledge_builders.utils import require_bs4, clean_ws

try:
    from bs4 import BeautifulSoup  # type: ignore
except ImportError:
    BeautifulSoup = None

UGC_ATTRIBUTES_URL = "https://ugc.aoe2.rocks/general/attributes/attributes/"
DOCS_BASE_URL = "https://ksneijders.github.io/AoE2ScenarioParser/api_docs/datasets/trigger_lists/object_attribute/#AoE2ScenarioParser.datasets.trigger_lists.object_attribute.ObjectAttribute"


def build_attributes_knowledge(
    html: str, 
    parser_enums: Dict[int, str], 
    keep_ids: Optional[Set[int]] = None
) -> Dict[int, Dict[str, Any]]:
    """
    Extracts attributes by ID from the UGC attributes page and merges with Parser Enums.
    
    Args:
        html: HTML content of the UGC page.
        parser_enums: Dict mapping int ID -> Enum Name (str).
        keep_ids: Optional set of IDs to keep.
        
    Returns:
        Dict[int, Record] where Record has UGC + Parser fields.
    """
    require_bs4()
    soup = BeautifulSoup(html, "html.parser")

    # 1. Parse UGC
    # UGC attributes are h2 headings like: "42. Train Location"
    ugc_attrs: Dict[int, Dict[str, Any]] = {}
    for h2 in soup.find_all("h2"):
        heading = clean_ws(h2.get_text(" ", strip=True))
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
            text = clean_ws(sib.get_text(" ", strip=True))
            if text:
                desc_lines.append(text)
            if len(desc_lines) >= 6:
                break

        ugc_attrs[attr_id] = {
            "id": attr_id,
            "ugc_name": attr_name,
            "description": " ".join(desc_lines),
            "source_url": UGC_ATTRIBUTES_URL,
        }

    # 2. Merge with Parser Enums (Primary Key: ID)
    # We want a unified record for every ID found in (UGC U Parser)
    all_ids = set(ugc_attrs.keys()) | set(parser_enums.keys())
    
    unified: Dict[int, Dict[str, Any]] = {}
    
    for aid in sorted(all_ids):
        if keep_ids is not None and aid not in keep_ids:
            continue
            
        ugc_rec = ugc_attrs.get(aid)
        enum_name = parser_enums.get(aid)
        
        # Base record
        record: Dict[str, Any] = {
            "id": aid,
            "ugc_name": ugc_rec["ugc_name"] if ugc_rec else None,
            "description": ugc_rec["description"] if ugc_rec else None,
            "source_url": ugc_rec["source_url"] if ugc_rec else None,
            "parser_enum_name": enum_name,
            "parser_enum_value": aid if enum_name else None,
            "parser_doc_url": f"{DOCS_BASE_URL}.{enum_name}" if enum_name else None,
            "usage_hint": (
                f"Use with Modify Attribute effect; object_attributes=ObjectAttribute.{enum_name}" 
                if enum_name else None
            ),
        }
        
        unified[aid] = record

    return unified
