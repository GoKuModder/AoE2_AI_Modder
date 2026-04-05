# Docs

This folder is split by role so agents do not need to infer which files are onboarding material and which files are raw retrieval data.

## Top-Level Folders

- `docs/agent/`
  Agent-facing guidance, routing rules, domain guides, and curated references.
- `docs/agent/scenario_builder/`
  Task-oriented scenario-building docs for triggers, parser managers, XS project files, and map-idea execution workflow.
  This now also includes implementation-oriented `.dat` / Genie workflow docs.
- `docs/agent/references/recipes/`
  Compact recipe datasets intended for low-token retrieval of common implementation workflows.
- `docs/agent_database/`
  Structured retrieval catalogs and manifest-level data.
- `docs/ai_scripting_knowledge/`
  Generated AI scripting datasets and supporting readme files.
- `docs/xs_knowledge/`
  Generated XS datasets and supporting readme files.
- `docs/trigger_knowledge/`
  Generated trigger condition, effect, attribute, real-project usage, and genie object knowledge.
- `docs/architecture/`
  Internal architectural boundary notes and related metadata.
- `examples/`
  Curated example scripts that demonstrate practical XS patterns.

## Read Order

- Open `docs/agent/README.md` if you want the agent-facing hierarchy.
- Open `AGENT_START_HERE.md` if you want the shortest path into the knowledge base.
- Open `docs/agent/scenario_builder/WHERE_TO_FIND_THINGS.md` if you want the fastest path to implementation-oriented scenario docs.
- Open the generated knowledge folders only after the agent navigation docs have routed you there.
