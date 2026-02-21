# AI/XS Boundary Contract

This document defines path-based domain ownership and import constraints between AI and XS Python code.

## Domains

- AI domain
  - Paths: `src/retrieval/**/*.py`, `src/builds/ai_scripting_knowledge_build.py`, `src/knowledge_builders/ai_scripting_builder.py`, `tools/build_ai_scripting_knowledge.py`
  - Module prefixes: `src.retrieval`, `src.builds.ai_scripting_knowledge_build`, `src.knowledge_builders.ai_scripting_builder`, `tools.build_ai_scripting_knowledge`
- XS domain
  - Paths: `src/integration/**/*.py`, `tools/generate_xs_array_injection_demo.py`
  - Module prefixes: `src.integration`, `tools.generate_xs_array_injection_demo`
- Shared domain
  - Paths: `src/common/**/*.py`, `src/writers/**/*.py`, `src/knowledge_builders/utils.py`, `src/interop/**/*.py`, `tests/**/*.py`, `tools/check_boundaries.py`
  - Module prefixes: `src.common`, `src.writers`, `src.knowledge_builders.utils`, `src.interop`, `tools.check_boundaries`

## Boundary Rules

- `no_direct_ai_to_xs_import`: AI modules must not directly import XS modules.
- `no_direct_xs_to_ai_import`: XS modules must not directly import AI modules.

Both rules can be bypassed only through explicit interop allowlist patterns in `docs/architecture/ai_xs_boundary.json` under `interop_allowlist.module_patterns`.

## Violation Format

Each violation is reported with deterministic fields:

- `path`: repository-relative file path
- `line`: import line number
- `import`: resolved imported module
- `rule`: violated rule name

Example:

```text
src/retrieval/consumer.py:12 import=src.integration.xs_injector rule=no_direct_ai_to_xs_import
```

## Checker Entry Point

Run:

```bash
python tools/check_boundaries.py
```

Optional flags:

- `--root <path>`: repository root to scan
- `--contract <path>`: boundary JSON contract path
- `--paths <path1> <path2> ...`: scan scope override
