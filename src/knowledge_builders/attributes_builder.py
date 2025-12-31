from typing import Any, Dict, List, Optional, Set
import re
from src.knowledge_builders.utils import require_bs4, clean_ws

try:
    from bs4 import BeautifulSoup  # type: ignore
except ImportError:
    BeautifulSoup = None

UGC_ATTRIBUTES_URL = "https://ugc.aoe2.rocks/general/attributes/attributes/"


def build_attributes_knowledge(html: str, keep_ids: Optional[Set[int]] = None) -> Dict[int, Dict[str, Any]]:
    """
    Extracts attributes by ID from the UGC attributes page.
    If keep_ids is provided, only those IDs are kept.
    """
    require_bs4()
    soup = BeautifulSoup(html, "html.parser")

    # UGC attributes are h2 headings like: "42. Train Location"
    attrs: Dict[int, Dict[str, Any]] = {}
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

        attrs[attr_id] = {
            "id": attr_id,
            "name": attr_name,
            "description": " ".join(desc_lines),
            "source": UGC_ATTRIBUTES_URL,
        }

    return attrs
