# Draft: GitHub Upload + Agent Index Readiness (AoE2_AI_Modder)

## User Question
- Is this library/repo properly indexed so it can be uploaded to GitHub and used by agents elsewhere?

## What I Checked (local workspace)
- Repo root exists and is a git repository.
- Index/knowledge artifacts exist under:
  - `docs/agent_database/` (e.g. `database_manifest.json`, `agent_query_map.json`)
  - `docs/ai_scripting_knowledge/` (e.g. `metadata_index.json`, `document_store.jsonl`, `retrieval_manifest.json`)
- Retrieval code exists under `src/retrieval/`.
- Git state indicates many key files are currently untracked.

## Findings (so far)
- Agent-facing indexing: PRESENT (manifests + catalogs + retriever/validator).
- GitHub readiness: NOT YET (large portion of repo content is untracked locally, so it would not be uploaded until added+committed).
- Portability risk: `docs/ai_scripting_knowledge/retrieval_manifest.json` contains an absolute local path in `sources.guide_dir`.
- Shareability risk: root `.gitignore` ignores `*.jsonl`, which likely prevents committing `docs/ai_scripting_knowledge/document_store.jsonl` unless force-added; retriever expects it at runtime.
- Packaging: no clear top-level package metadata found (e.g. no root `pyproject.toml`), so “pip-installable library” is likely not set up yet.

## Open Question
- How do you want other agents to consume this?
  - A) `git clone` + run scripts locally
  - B) install as a Python package (`pip install ...`)

## XS Scripting Documentation Snapshot
- There is substantial XS reference material under `XS_Training/`.
  - `XS_Training/SOURCE_PAGE_INDEX.md` inventories captured sources (ugc.aoe2.rocks XS pages + Divy1211/AoE2DE_UGC_Guide markdown).
  - `XS_Training/modding_general/06_scenario_editor_and_xs.md` summarizes engine additions and XS API deltas.
  - `XS_Training/RPG_SPELL_DESIGN_FOUNDATION.md` is a curated, opinionated distillation into a practical XS “spell system” architecture with known pitfalls.
- Separate from XS, the repo has strong `.per` AI scripting documentation in `AoE2_AI_Scripting_Guide/` (rules/syntax + allowlist + retrieval index + templates).
- Potential doc gap: XS materials are more “reference dump + curated foundation” than a single cohesive quickstart tailored to this repo’s tooling/agents.

## User Priority (confirmed)
- Primary goal is agent retrieval accuracy for XS scripting (agents should be able to look up correct XS functions/constants and generate correct XS code).
