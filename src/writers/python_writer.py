from pathlib import Path
from typing import Any

def write_python_module(path: Path, var_name: str, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    content = f"{var_name} = {repr(payload)}\n"
    path.write_text(content, encoding="utf-8")
