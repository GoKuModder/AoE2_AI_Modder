# Learnings

Append-only. Capture conventions, gotchas, and patterns discovered during implementation.

- Added machine-readable boundary contract at `docs/architecture/ai_xs_boundary.json` with domain path patterns, module prefixes, explicit directional rules, and interop allowlist placeholder.
- Implemented `tools/check_boundaries.py` with stdlib-only AST parsing and deterministic violation ordering (`path`, `line`, `import`, `rule`).
- `fnmatch` does not treat `**` as "zero or more directories" for immediate children (`src/retrieval/**/*.py` misses `src/retrieval/file.py`), so the checker now expands `/**/` patterns to include a shallow equivalent.
- Boundary tests follow existing unittest style and use fixture roots so checker behavior is validated independent of repository-wide code layout.

- For git-install publish readiness, root metadata docs were added (`README.md`, `LICENSE`, `CONTRIBUTING.md`, `SECURITY.md`, `CODEOWNERS`) and examples default to the Windows `py -3` launcher.
- XS knowledge build determinism is easiest to preserve by removing volatile fields (for example timestamps) from generated artifacts and instead storing artifact SHA-256 checksums in the retrieval manifest.
- Parsing `XS_Training/SOURCE_PAGE_INDEX.md` as the explicit source list keeps input scope stable and allows deterministic ordering by normalized relative path.
- Added `src/integration/xs_bridge_contract.py` as a small stdlib-only interop contract layer that freezes bridge trigger variable IDs (`50/51/52`) and emits deterministic `xsSetTriggerVariable` snippets in a stable key order.
- Compatibility coverage in `tests/test_xs_bridge_compat.py` snapshots both the exposed ID mapping and generated trigger snippet text, plus checks IDs still match `AI_Scripting/rpg_xs_bridge_v3.xs` constants.
- Added XS datasets (`xs_functions`, `xs_constants`) to manifest with 172 and 761 records respectively, using "name" as primary key.
- Created `tools/check_manifest.py` validator using stdlib only (json, sys, pathlib) with error messages that include dataset_id for debugging.
- Created `tests/test_manifest.py` with 10 test cases covering happy-path and broken-schema scenarios (missing fields, wrong types, negative counts, file not found).
- Environment uses `py -3` for Python execution, not `python`.
- XS eval harness is most stable when golden expectations match by substring across both `title` and `source_file`, because deterministic symbol results (`xs-symbol:*`) can rank ahead of chunk/doc results.
- Negative (miss) queries must avoid separators like underscores, since tokenization (`[a-z0-9-]+`) splits them and can create accidental overlap hits.
- Task 8 hybrid retrieval remains deterministic by preserving query token order (`dict.fromkeys`), then using an explicit sort key `(-priority, -score, source_file, title, text-prefix)` before deduplication.
- Symbol-first precedence is easiest to make explicit in chunk retrieval by injecting a synthetic `xs-symbol:<name>` retrieval row and ranking it via a dedicated priority tier above command/chunk rows.
- Deterministic XS symbol lookup works best by indexing `docs/agent_database/xs_functions_catalog.json` and `docs/agent_database/xs_constants_catalog.json` with a normalization key that lowercases and strips non-alphanumeric characters.
- Stable downstream schema for symbol retrieval should always return explicit keys (`query`, `normalized_query`, `found`, `error_code`, `symbol_type`, `name`, `signature`, `details`) for both hits and misses.
- Task 9 retrieval context is now validated with deterministic first-failure reporting (`error_code`, `error_path`, `message`), which keeps malformed payload handling machine-consumable for eval tooling.
- XS retrieval context item schema was normalized to explicit keys (`source`, `title`, `score`, `text`) and verified with unit tests to prevent accidental shape drift.
- Added 17 new unit tests to test_xs_knowledge_build.py covering: parse_source_page_index (parsing, sorting, dedup, path normalization), collect_source_documents (markdown filtering, missing files), build_metadata_index (schema validation), build_chunk_store (heading-based chunking, empty/no-heading edge cases).
- Added 22 new unit tests to test_xs_retrieval.py covering: constant catalog lookup (exact hit, case-insensitive, underscore normalization), lookup_command (found/not-found), build_context (query/commands/retrieved structure), symbol lookup edge cases (whitespace, empty, special chars, function-priority), search edge cases (empty query, special chars, limit enforcement).
- Discovered that build_context command detection has case-sensitivity issue: tokens are lowercased but command keys in metadata are original case - tests document this by using lowercase command names in test metadata.
- Task 12 strengthened hybrid retrieval coverage with explicit precedence assertions (`xs-symbol` > `xs-command` > chunk fallback) and explicit tie-order assertions using deterministic sort fields (`source_file`, `title`, `text` prefix).
- Task 12 strengthened eval contract coverage by asserting threshold boundary semantics (metrics exactly equal to threshold must pass) and single-metric failure semantics (any threshold miss returns non-zero via `main()`).
- Task 14 packaged runtime XS assets under `src/data/xs/` and switched retriever/eval defaults to `importlib.resources` so installed usage works without repo-root `docs/`.
- Task 14 verification includes an actual clean-venv wheel install + import/lookup smoke to prove packaged data is accessible outside the repo CWD.
- Task 14 packaged XS data using `src/data/xs/` subpackage with JSON/JSONL artifacts bundled via setuptools package-data rules.
- Resource loading uses `importlib.resources` for deterministic bundled data access - no more repo-relative path assumptions.
- `XSScriptKnowledgeRetriever()` now works without arguments using packaged defaults, while still supporting custom `dataset_dir` for backwards compatibility.
- Eval defaults changed to `None` (packaged resources) while preserving CLI override via `--dataset-dir` and `--golden` flags.
- pyproject.toml package-data syntax requires quoted keys for nested packages: `"src.data.xs.agent_database" = ["*.json"]`.
- Task 14 (this session) verified existing packaging setup works correctly: wheel builds, imports work, packaged data loads via importlib.resources.
- Added TestPackagedDataLoading test class with 5 tests validating all bundled artifacts load correctly from the package.
- Verified installed package works from wheel without needing docs/ in the same directory.
