# Where To Find Things

Use this file when the repo feels too broad and you need an exact answer to "where is the information for X?"

## Fast Retrieval Runtime

- one low-token retriever across recipes plus exact lookup datasets
  `src/retrieval/aoe_unified_retriever.py`
- compact implementation recipes only
  `src/retrieval/aoe_compact_retriever.py`

## Triggers

- where are conditions?
  `docs/trigger_knowledge/conditions_knowledge.json`
- where are effects?
  `docs/trigger_knowledge/effects_knowledge.json`

- trigger architecture and modular project structure
  `docs/agent/domains/TRIGGER_AGENT_GUIDE.md`
- trigger conditions and effects teaching
  `docs/agent/domains/TRIGGER_CONDITIONS_EFFECTS_GUIDE.md`
- trigger conditions dataset
  `docs/trigger_knowledge/conditions_knowledge.json`
- trigger effects dataset
  `docs/trigger_knowledge/effects_knowledge.json`
- deep condition usage explanations
  `docs/trigger_knowledge/condition_usage_playbook.md`
- deep effect usage explanations
  `docs/trigger_knowledge/effect_usage_playbook.md`
- real-project condition usage
  `docs/trigger_knowledge/condition_project_usage.json`
- real-project effect usage
  `docs/trigger_knowledge/effect_project_usage.json`
- trigger attributes
  `docs/trigger_knowledge/attributes_dataset.json`

## AoE2ScenarioParser Managers

- how to use `UnitManager` and `MapManager`
  `docs/agent/scenario_builder/PARSER_MANAGERS_GUIDE.md`
- parser managers guide
  `docs/agent/scenario_builder/PARSER_MANAGERS_GUIDE.md`
- trusted project references for manager usage
  `LordsOfDiplomacy - Easy Mode`
  `GoKu RPG Project`

## XS In Scenario Projects

- XS scripting domain guide
  `docs/agent/domains/XS_AGENT_GUIDE.md`
- XS variables and XS file generation in scenario projects
  `docs/agent/scenario_builder/XS_PROJECT_FILES_GUIDE.md`
- xs project files guide
  `docs/agent/scenario_builder/XS_PROJECT_FILES_GUIDE.md`
- structured trigger-plus-XS architecture patterns
  `docs/agent/references/patterns/trigger_xs_patterns.json`
- exact XS functions
  `docs/agent_database/xs_functions_catalog.json`
- exact XS constants
  `docs/agent_database/xs_constants_catalog.json`
- curated XS examples
  `examples/xs/README.md`

## Scenario Variable Registries

- trigger variable architecture, `aoe_variables`, `dictionary.py`, `apply_` hierarchy
  `docs/agent/domains/TRIGGER_AGENT_GUIDE.md`
- trigger-plus-XS project architecture patterns
  `docs/agent/references/patterns/trigger_xs_patterns.json`

## End-To-End Scenario Build Workflow

- how to turn a map idea doc into modular implementation steps
  `docs/agent/scenario_builder/MAP_IDEA_TO_IMPLEMENTATION.md`
- map idea to implementation
  `docs/agent/scenario_builder/MAP_IDEA_TO_IMPLEMENTATION.md`
- compact scenario implementation recipes
  `docs/agent/references/recipes/scenario_recipes.json`
- compact parser manager patterns
  `docs/agent/references/recipes/parser_manager_patterns.json`

## `.dat` / Genie Workflows

- where are `.dat` fields and data-model concepts?
  `docs/agent/scenario_builder/DAT_LOOKUP_INDEX.md`
- compact `.dat` concept dataset
  `docs/agent_database/genie_dat_concepts.json`
- how to use `GenieWorkspace` and asset managers
  `docs/agent/scenario_builder/GENIE_WORKFLOW_GUIDE.md`
- genie workflow guide
  `docs/agent/scenario_builder/GENIE_WORKFLOW_GUIDE.md`
- broad `.dat` architecture and references
  `docs/agent/domains/DAT_AGENT_GUIDE.md`
- structured genie architecture patterns
  `docs/agent/references/patterns/genie_workflow_patterns.json`
- compact genie implementation recipes
  `docs/agent/references/recipes/genie_recipes.json`

## If The Task Is "Build The Whole Map"

Open in this order:

1. `docs/agent/scenario_builder/MAP_IDEA_TO_IMPLEMENTATION.md`
2. `docs/agent/scenario_builder/WHERE_TO_FIND_THINGS.md`
3. `docs/agent/domains/TRIGGER_AGENT_GUIDE.md`
4. `docs/agent/scenario_builder/PARSER_MANAGERS_GUIDE.md`
5. `docs/agent/scenario_builder/XS_PROJECT_FILES_GUIDE.md`
6. `docs/agent/scenario_builder/GENIE_WORKFLOW_GUIDE.md` if the idea includes `.dat` edits
7. `docs/agent/domains/TRIGGER_CONDITIONS_EFFECTS_GUIDE.md`
