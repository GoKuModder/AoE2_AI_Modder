# `.dat` Lookup Index

Use this file when the question is specifically about `.dat` knowledge and you need a direct answer to "where is the information for this data surface?"

## Fast Retrieval Runtime

- dedicated `.dat` retriever
  `src/retrieval/genie_dat_retriever.py`
- unified low-token retriever across all domains
  `src/retrieval/aoe_unified_retriever.py`

## Open These First

1. `docs/agent/domains/DAT_AGENT_GUIDE.md`
2. `docs/agent/scenario_builder/GENIE_WORKFLOW_GUIDE.md`
3. `docs/agent_database/genie_dat_concepts.json`

## Where The Main `.dat` Knowledge Lives

- deep domain guide for `.dat` and genie tooling
  `docs/agent/domains/DAT_AGENT_GUIDE.md`
- implementation workflow guide for real genie projects
  `docs/agent/scenario_builder/GENIE_WORKFLOW_GUIDE.md`
- compact `.dat` recipes
  `docs/agent/references/recipes/genie_recipes.json`
- structured architecture patterns
  `docs/agent/references/patterns/genie_workflow_patterns.json`
- exact object lookup by game id or name
  `docs/trigger_knowledge/genie_registry.json`
- compact data-model concept lookup
  `docs/agent_database/genie_dat_concepts.json`

## Where To Find Specific Things

- where is `standing_sprite_id1`, `standing_sprite_id2`, or `dead_unit_id` explained?
  `docs/agent_database/genie_dat_concepts.json`
  entry: `unit_sprite_link_fields`
- where are non-particle graphic fields like `file_name`, `layer`, `frame_count`, or `sequence_type` explained?
  `docs/agent_database/genie_dat_concepts.json`
  entry: `graphic_non_particle_fields`
- where is `particle_effect_name` explained?
  `docs/agent_database/genie_dat_concepts.json`
  entry: `graphic_particle_effect_fields`
- where is `add_delta` explained?
  `docs/agent_database/genie_dat_concepts.json`
  entry: `graphic_wrapper_delta_pattern`
- where is `civ_manager.add_resource` and the global resource-slot rule explained?
  `docs/agent_database/genie_dat_concepts.json`
  entry: `civ_global_resource_slots`
- where are effect command chains like `resource_modifier`, `modify_tech`, and `enable_disable_unit` explained?
  `docs/agent_database/genie_dat_concepts.json`
  entry: `effect_command_unlock_chain`
- where are tech fields like `set_required_tech`, `set_cost`, and `add_research_location` explained?
  `docs/agent_database/genie_dat_concepts.json`
  entry: `tech_definition_and_research_location`
- where is the full item pipeline from resource to effect to tech to unit explained?
  `docs/agent_database/genie_dat_concepts.json`
  entry: `item_resource_effect_tech_pipeline`
- where are production-side concepts like tasks or train locations explained?
  `docs/agent_database/genie_dat_concepts.json`
  entry: `task_and_train_location_wiring`
- where are shared ids, balance data, and dat output-path rules explained?
  `docs/agent_database/genie_dat_concepts.json`
  entry: `balance_registry_and_output_policy`

## Trusted Project Evidence

Primary `.dat` reference project:

- `GoKu RPG Genie Code`

Best evidence files from that project:

- `main/main.py`
- `config/ids.py`
- `Inventory_System/Items/apply_items.py`
- `Inventory_System/Items/resource.py`
- `Inventory_System/Items/effect.py`
- `Inventory_System/Items/technology.py`
- `Inventory_System/Items/enable_techs.py`
- `Character_General/Pick_Class/apply_pick_class.py`
- `Character_General/Pick_Class/pick_class_graphics.py`
- `Classes/Crusader/Heavenly_Bastion/link_components.py`

## Practical Read Order

- broad question about `.dat` architecture
  `docs/agent/domains/DAT_AGENT_GUIDE.md`
- concrete implementation question
  `docs/agent/scenario_builder/GENIE_WORKFLOW_GUIDE.md`
- exact field or data-model concept question
  `docs/agent_database/genie_dat_concepts.json`
- concrete "how do I build it" question
  `docs/agent/references/recipes/genie_recipes.json`
- object id / name question
  `docs/trigger_knowledge/genie_registry.json`

## Output Path Rule

Generalized repo guidance should not encode one developer PC path as the default answer.

- if the project already defines input/output `.dat` paths, use that config
- otherwise ask the user where the modified `.dat` should be written
