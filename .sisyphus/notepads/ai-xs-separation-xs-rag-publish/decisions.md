# Decisions

Append-only. Record decisions that affect architecture, interfaces, or compatibility.

- Publish baseline: document git-install only (no PyPI claim) and include quick sanity commands (`py -3 tools/build_ai_scripting_knowledge.py`, `py -3 -m unittest ...`).
- License baseline: use MIT template with an explicit `<COPYRIGHT_HOLDER>` placeholder to avoid guessing ownership.

- Task 2 keeps bridge contract validation strict (exact required keys + `int` values, excluding `bool`) and raises `BridgeContractError("bridge_contract_error")` for all invalid payload shapes to keep error behavior deterministic for callers.
- The interop API surface is intentionally minimal: `bridge_variable_ids()`, `validate_bridge_payload()`, and `build_bridge_trigger_update_snippet()`; no existing bridge scripts were modified to preserve runtime behavior.
- Task 4 introduces a file-backed XS build pipeline rooted at `XS_Training/` with outputs in `docs/xs_knowledge/` (`metadata_index.json`, `document_store.jsonl`, `retrieval_manifest.json`) and no external database dependencies.
- XS chunk ordering is fixed by sorting normalized source paths from `SOURCE_PAGE_INDEX.md`, then chunking markdown in heading order (`::h0`, `::h1`, ...), which guarantees stable row order across repeated runs on identical inputs.
- Task 7 adds a deterministic-first symbol API `lookup_symbol()` in `src/retrieval/xs_script_retriever.py` that performs exact normalized lookup against function/constant catalogs before any chunk search path.
- Unknown symbols return a typed not-found payload with `found: false` and `error_code: "XS_SYMBOL_NOT_FOUND"` instead of `None` to keep downstream handling explicit.
- Task 8 keeps `search()` API shape unchanged (`list[XSRetrievalResult]`) while adding symbol precedence, by encoding result class in `title` prefixes (`xs-symbol:`, `xs-command:`) and ranking with explicit priority tiers.
- Task 10 introduces `src/eval/xs_retrieval_eval.py` plus `tools/eval_xs_retrieval.py`; CLI emits JSON summary and exits non-zero only when `recall@k`/`MRR` thresholds fail.
- Golden set format is file-based (`docs/agent_database/xs_eval.json`) with mixed `answerable` and `miss` case kinds so retrieval quality and false-positive behavior are both evaluated locally.
- Task 9 formalizes XS retrieval context shape as `{query, commands_detected, retrieved[]}` with retrieved rows constrained to `{source, title, score, text}`.
- `XSScriptKnowledgeRetriever.build_context()` now self-validates its emitted payload and raises a deterministic `ValueError` containing validator code/path/message when internal schema drift is detected.
- Task 12 hardens regression intent in tests (without production changes) by pinning hybrid retrieval ordering semantics and eval threshold exit-code semantics as explicit unit-test contracts.
- Task 14 ships only runtime-required XS artifacts as package data via `[tool.setuptools.package-data]`, avoiding `data-files` and avoiding bundling training/source corpora.
- Task 14 packages XS data under `src/data/xs/` with `agent_database/` and `xs_knowledge/` subdirectories included via setuptools package-data rules.
- `XSScriptKnowledgeRetriever()` now defaults to packaged resources via `importlib.resources`, but accepts optional `dataset_dir` for custom data (maintains backwards compatibility).
- Eval defaults changed to `None` (packaged resources) with CLI flag overrides for `--dataset-dir` and `--golden`.
- Task 14 verification confirmed: wheel builds successfully, imports work from installed package, packaged data loads via importlib.resources, all tests pass.
