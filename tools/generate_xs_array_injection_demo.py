#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

root_dir = Path(__file__).parent.parent
if str(root_dir) not in sys.path:
    sys.path.insert(0, str(root_dir))

from src.integration.xs_injector import (
    build_array_create_and_get_snippet,
    inject_xs_code,
)


def main() -> int:
    out_xs = root_dir / "XS_Scripting" / "xs_array_injection_demo_generated.xs"

    snippet = build_array_create_and_get_snippet(
        array_id_var="aInjectedIds",
        value_var="injectedValue",
        array_type="int",
        size=4,
        default_value=-1,
        debug_name="injected_ids",
        index_expr="0",
    )

    base = (
        "// xs_array_injection_demo_generated.xs\n"
        "int aInjectedIds = -1;\n"
        "\n"
        "rule xs_injection_demo\n"
        "active\n"
        "minInterval 1\n"
        "maxInterval 1\n"
        "{\n"
        "    int injectedValue = -1;\n"
        "    // INJECT_HERE\n"
        "    xsDisableSelf();\n"
        "}\n"
    )

    indented_snippet = "\n".join("    " + line for line in snippet.strip().splitlines())
    generated = inject_xs_code(base, indented_snippet, marker="INJECT_HERE")

    out_xs.write_text(generated, encoding="utf-8")
    print(str(out_xs))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
