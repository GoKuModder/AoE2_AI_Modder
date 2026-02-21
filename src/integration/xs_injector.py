from __future__ import annotations

from pathlib import Path
from typing import Any


_ARRAY_TYPES = {
    "int": {
        "create": "xsArrayCreateInt",
        "get": "xsArrayGetInt",
    },
    "float": {
        "create": "xsArrayCreateFloat",
        "get": "xsArrayGetFloat",
    },
    "bool": {
        "create": "xsArrayCreateBool",
        "get": "xsArrayGetBool",
    },
    "string": {
        "create": "xsArrayCreateString",
        "get": "xsArrayGetString",
    },
    "vector": {
        "create": "xsArrayCreateVector",
        "get": "xsArrayGetVector",
    },
}


def _normalize_array_type(array_type: str) -> str:
    key = array_type.strip().lower()
    if key not in _ARRAY_TYPES:
        raise ValueError(
            f"Unsupported array type '{array_type}'. "
            f"Supported: {', '.join(sorted(_ARRAY_TYPES.keys()))}"
        )
    return key


def _format_xs_literal(array_type: str, value: Any) -> str:
    kind = _normalize_array_type(array_type)
    if kind == "int":
        return str(int(value))
    if kind == "float":
        v = float(value)
        if "." not in str(v):
            return f"{v:.1f}"
        return str(v)
    if kind == "bool":
        return "true" if bool(value) else "false"
    if kind == "string":
        escaped = str(value).replace('"', '\\"')
        return f'"{escaped}"'
    # vector
    return str(value)


def make_xs_array_create_statement(
    *,
    array_id_var: str,
    array_type: str,
    size: int,
    default_value: Any,
    debug_name: str,
) -> str:
    """Build one XS statement that creates an array.

    Example output:
      myArr = xsArrayCreateInt(8, -1, "hero_ids");
    """
    kind = _normalize_array_type(array_type)
    fn = _ARRAY_TYPES[kind]["create"]
    default_literal = _format_xs_literal(kind, default_value)
    safe_name = debug_name.replace('"', "")
    return f"{array_id_var} = {fn}({int(size)}, {default_literal}, \"{safe_name}\");"


def make_xs_array_get_statement(
    *,
    out_var: str,
    array_type: str,
    array_id_var: str,
    index_expr: str,
) -> str:
    """Build one XS statement that retrieves a value from an array.

    Example output:
      heroId = xsArrayGetInt(aHeroIds, i);
    """
    kind = _normalize_array_type(array_type)
    fn = _ARRAY_TYPES[kind]["get"]
    return f"{out_var} = {fn}({array_id_var}, {index_expr});"


def inject_xs_code(existing_code: str, snippet: str, marker: str | None = None) -> str:
    """Inject snippet into XS code.

    If marker is provided, inserts after first line containing marker.
    Otherwise appends snippet at file end.
    """
    normalized_snippet = snippet.rstrip() + "\n"

    if marker is None:
        base = existing_code.rstrip() + "\n\n"
        return base + normalized_snippet

    lines = existing_code.splitlines()
    for i, line in enumerate(lines):
        if marker in line:
            lines.insert(i + 1, normalized_snippet.rstrip("\n"))
            return "\n".join(lines) + "\n"

    raise ValueError(f"Marker '{marker}' not found in XS code")


def inject_xs_file(
    *,
    xs_path: Path,
    snippet: str,
    marker: str | None = None,
    output_path: Path | None = None,
) -> Path:
    """Read XS file, inject snippet, and write output file."""
    source = xs_path.read_text(encoding="utf-8", errors="replace")
    updated = inject_xs_code(source, snippet, marker=marker)
    target = output_path or xs_path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(updated, encoding="utf-8")
    return target


def build_array_create_and_get_snippet(
    *,
    array_id_var: str,
    value_var: str,
    array_type: str,
    size: int,
    default_value: Any,
    debug_name: str,
    index_expr: str,
) -> str:
    """Build a 2-line snippet: create array + get value by index."""
    create_line = make_xs_array_create_statement(
        array_id_var=array_id_var,
        array_type=array_type,
        size=size,
        default_value=default_value,
        debug_name=debug_name,
    )
    get_line = make_xs_array_get_statement(
        out_var=value_var,
        array_type=array_type,
        array_id_var=array_id_var,
        index_expr=index_expr,
    )
    return create_line + "\n" + get_line + "\n"
