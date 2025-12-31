from typing import List, Iterable

def generate_table(headers: List[str], rows: Iterable[List[str]]) -> str:
    """
    Generates a Markdown table.
    """
    lines = []
    # Header
    lines.append("| " + " | ".join(headers) + " |")
    # Separator
    lines.append("| " + " | ".join(["---"] * len(headers)) + " |")
    
    for row in rows:
        # Ensure row has same length as headers? 
        # Or just join. 
        # We assume caller handles data cleanliness (strings).
        lines.append("| " + " | ".join(row) + " |")
    
    return "\n".join(lines) + "\n"

def generate_list(items: Iterable[str], bullet: str = "-") -> str:
    """
    Generates a Markdown list.
    """
    lines = []
    for item in items:
        lines.append(f"{bullet} {item}")
    return "\n".join(lines) + "\n"
