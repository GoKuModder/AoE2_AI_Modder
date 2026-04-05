# Knowledge Map

This file explains how the AoE2DE knowledge base is organized and which files should be treated as canonical for different kinds of agent work.

## File Classes

### Primary Human-Readable Guides

These teach an agent how to use the repo:

- `AGENT_START_HERE.md`
- `docs/README.md`
- `docs/agent/README.md`
- `docs/agent/scenario_builder/README.md`
- `docs/agent/scenario_builder/WHERE_TO_FIND_THINGS.md`
- `docs/agent/scenario_builder/TRIGGER_LOOKUP_INDEX.md`
- `docs/agent/scenario_builder/PARSER_MANAGERS_GUIDE.md`
- `docs/agent/scenario_builder/XS_PROJECT_FILES_GUIDE.md`
- `docs/agent/scenario_builder/GENIE_WORKFLOW_GUIDE.md`
- `docs/agent/scenario_builder/DAT_LOOKUP_INDEX.md`
- `docs/agent/scenario_builder/MAP_IDEA_TO_IMPLEMENTATION.md`
- `docs/agent/navigation/RETRIEVAL_RULES.md`
- `docs/agent/navigation/CROSS_DOMAIN_WORKFLOWS.md`
- `docs/agent/references/REFERENCE_PROJECTS.md`
- `docs/agent/domains/XS_AGENT_GUIDE.md`
- `docs/agent/domains/AI_SCRIPT_AGENT_GUIDE.md`
- `docs/agent/domains/TRIGGER_AGENT_GUIDE.md`
- `docs/agent/domains/TRIGGER_CONDITIONS_EFFECTS_GUIDE.md`
- `docs/agent/domains/DAT_AGENT_GUIDE.md`

### Generated Knowledge Artifacts

These are structured retrieval truth:

- `docs/agent/routing/`
- `docs/ai_scripting_knowledge/`
- `docs/xs_knowledge/`
- `docs/trigger_knowledge/`
- `docs/agent_database/`
- `docs/agent/references/patterns/`

### Raw Training / Source Material

These are deeper references and should not be the first thing an agent opens:

- `AoE2_AI_Scripting_Guide/`
- `XS_Training/`
- `AI_Scripting/`
- `examples/`

### Runtime / Implementation Code

These show what is already operationalized:

- `src/retrieval/`
- `src/integration/`
- `src/builds/`
- `tools/`

### Curated External Project References

These are trusted local examples for mining patterns and evaluation cases:

- `docs/agent/references/REFERENCE_PROJECTS.md`
- `docs/agent/references/reference_projects.json`

## Canonical Truth Policy

- Use markdown guides to understand routing, scope, and how to answer.
- Use generated JSON / JSONL artifacts for precise retrieval and machine-readable truth.
- Use raw source corpora for supporting explanation, examples, and uncovered edge cases.
- Use runtime Python modules to understand available retrieval or validation behavior.

Examples and source documents are supporting material. Generated artifacts and documented routing rules are the main truth for agent retrieval.

## Domain Map

## Scenario Builder

- Open first:
  - `docs/agent/scenario_builder/WHERE_TO_FIND_THINGS.md`
  - `docs/agent/scenario_builder/TRIGGER_LOOKUP_INDEX.md`
- `docs/agent/scenario_builder/PARSER_MANAGERS_GUIDE.md`
  - `docs/agent/scenario_builder/XS_PROJECT_FILES_GUIDE.md`
  - `docs/agent/scenario_builder/GENIE_WORKFLOW_GUIDE.md`
  - `docs/agent/scenario_builder/DAT_LOOKUP_INDEX.md`
  - `docs/agent/scenario_builder/MAP_IDEA_TO_IMPLEMENTATION.md`
- Role:
  - task-oriented entrypoints for implementation-heavy scenario work
  - exact file mapping for trigger conditions, trigger effects, parser managers, XS variables, and XS file generation
  - workflow for turning a map idea document into modular implementation work

## XS

- Open first:
  - `docs/agent/domains/XS_AGENT_GUIDE.md`
  - `docs/xs_knowledge/README.md`
  - `docs/agent_database/xs_functions_catalog.json`
- Canonical generated data:
  - `docs/agent_database/xs_functions_catalog.json`
  - `docs/agent_database/xs_constants_catalog.json`
  - `docs/xs_knowledge/metadata_index.json`
  - `docs/xs_knowledge/document_store.jsonl`
  - `docs/agent/references/patterns/trigger_xs_patterns.json`
- Supporting source material:
  - `XS_Training/`
  - `examples/xs/`
- Runtime modules:
  - `src/retrieval/xs_script_retriever.py`
  - `src/retrieval/xs_script_validator.py`

## AI scripts

- Open first:
  - `docs/agent/domains/AI_SCRIPT_AGENT_GUIDE.md`
  - `docs/ai_scripting_knowledge/README.md`
  - `AoE2_AI_Scripting_Guide/README.md`
- Canonical generated data:
  - `docs/ai_scripting_knowledge/metadata_index.json`
  - `docs/ai_scripting_knowledge/document_store.jsonl`
- Supporting source material:
  - `AoE2_AI_Scripting_Guide/`
  - `AI_Scripting/`
- Runtime modules:
  - `src/retrieval/ai_script_retriever.py`
  - `src/retrieval/ai_script_validator.py`

## Scenario triggers

- Open first:
  - `docs/agent/domains/TRIGGER_AGENT_GUIDE.md`
  - `docs/agent/domains/TRIGGER_CONDITIONS_EFFECTS_GUIDE.md`
  - `docs/trigger_knowledge/condition_usage_playbook.md`
  - `docs/trigger_knowledge/effect_usage_playbook.md`
  - `docs/trigger_knowledge/conditions_knowledge.md`
  - `docs/trigger_knowledge/effects_knowledge.md`
  - `docs/trigger_knowledge/attributes_knowledge.md`
  - `docs/trigger_knowledge/project_usage_knowledge.md`
- Canonical generated data:
  - `docs/trigger_knowledge/conditions_knowledge.json`
  - `docs/trigger_knowledge/effects_knowledge.json`
  - `docs/trigger_knowledge/condition_usage_playbook.json`
  - `docs/trigger_knowledge/effect_usage_playbook.json`
  - `docs/trigger_knowledge/attributes_dataset.json`
  - `docs/trigger_knowledge/genie_registry.json`
  - `docs/trigger_knowledge/condition_project_usage.json`
  - `docs/trigger_knowledge/effect_project_usage.json`
  - `docs/agent/references/patterns/trigger_xs_patterns.json`
  - `docs/agent/references/recipes/scenario_recipes.json`
  - `docs/agent/references/recipes/parser_manager_patterns.json`
- Supporting source material:
  - `XS_Training/github.com/Divy1211/AoE2DE_UGC_Guide/docs/scenarios/`
  - `XS_Training/ugc.aoe2.rocks/`
- Runtime modules:
  - `src/builds/trigger_knowledge_build.py`
  - `src/integration/aoe2_introspection.py`

## .dat/genie tooling

- Open first:
  - `docs/agent/domains/DAT_AGENT_GUIDE.md`
  - `docs/agent/scenario_builder/DAT_LOOKUP_INDEX.md`
  - `docs/agent/scenario_builder/GENIE_WORKFLOW_GUIDE.md`
  - `XS_Training/external_refs/ageofempires.fandom.com/Genie_Editor.md`
  - `XS_Training/modding_general/07_genie_editor_xs_bridge.md`
- Current canonical generated data:
  - `docs/agent_database/genie_dat_concepts.json`
  - `docs/trigger_knowledge/genie_registry.json`
  - `docs/agent/references/patterns/genie_workflow_patterns.json`
  - `docs/agent/references/recipes/genie_recipes.json`
- Supporting source material:
  - `XS_Training/modding_general/`
  - `XS_Training/external_refs/ageofempires.fandom.com/Genie_Editor.md`
- Runtime status:
  - dedicated `.dat` concept retriever exists
  - compact implementation recipes and patterns exist
  - still not a full `.dat` edit runtime

## Examples Versus Truth Sources

- Example scripts in `AI_Scripting/` and `examples/xs/` show patterns, not exhaustive truth.
- Large markdown corpora in `AoE2_AI_Scripting_Guide/` and `XS_Training/` provide explanation, but not always the fastest retrieval path.
- Structured files in `docs/agent_database/`, `docs/xs_knowledge/`, `docs/ai_scripting_knowledge/`, and `docs/trigger_knowledge/` are the best first stop for precise lookup.

## If You Only Have Time To Open One File

- `XS`: `docs/agent/domains/XS_AGENT_GUIDE.md`
- `AI scripts`: `docs/agent/domains/AI_SCRIPT_AGENT_GUIDE.md`
- `scenario triggers`: `docs/agent/domains/TRIGGER_AGENT_GUIDE.md`
- `.dat/genie tooling`: `docs/agent/domains/DAT_AGENT_GUIDE.md`

