# Trigger Agent Guide

Use this guide for AoE2DE `scenario triggers` tasks, especially condition, effect, attribute, variable, and object-ID questions.

## What This Domain Is For

This domain covers scenario trigger knowledge that is useful for AoE2ScenarioParser-oriented work and scenario-editor reasoning. Current repo coverage includes exhaustive parser condition and effect lookup, attribute lookup, real-project usage datasets, and genie object lookup.

This guide also covers the architecture patterns that make large trigger-heavy projects maintainable: modular folder structure, class-per-system design, data-driven configuration, trigger-variable registries, and XS integration boundaries.

## Canonical Sources In This Repo

Open these first:

- `docs/agent/domains/TRIGGER_CONDITIONS_EFFECTS_GUIDE.md`
- `docs/trigger_knowledge/condition_usage_playbook.md`
- `docs/trigger_knowledge/effect_usage_playbook.md`
- `docs/trigger_knowledge/conditions_knowledge.md`
- `docs/trigger_knowledge/conditions_knowledge.json`
- `docs/trigger_knowledge/effects_knowledge.md`
- `docs/trigger_knowledge/effects_knowledge.json`
- `docs/trigger_knowledge/attributes_knowledge.md`
- `docs/trigger_knowledge/attributes_dataset.json`
- `docs/trigger_knowledge/project_usage_knowledge.md`
- `docs/trigger_knowledge/condition_project_usage.json`
- `docs/trigger_knowledge/effect_project_usage.json`
- `docs/trigger_knowledge/genie_registry.json`
- `docs/agent/references/patterns/trigger_xs_patterns.json`

Runtime / builder support:

- `src/builds/trigger_knowledge_build.py`
- `src/integration/aoe2_introspection.py`

Supporting source material:

- `XS_Training/github.com/Divy1211/AoE2DE_UGC_Guide/docs/scenarios/`
- `XS_Training/ugc.aoe2.rocks/`

Curated external project reference:

- `docs/agent/references/REFERENCE_PROJECTS.md` -> `LordsOfDiplomacy - Easy Mode`

Additional mixed-system references:

- `docs/agent/references/REFERENCE_PROJECTS.md` -> `GoKu RPG Project`
- `docs/agent/references/REFERENCE_PROJECTS.md` -> `Hide_and_Seek`

## How To Structure A Large Trigger Project

For large projects, do not keep everything in one trigger script generator file.

Preferred pattern:

- one folder per gameplay system
- one module per sub-system or feature slice
- one class or focused builder object per system when the logic has state or repeated behavior
- one thin top-level entrypoint that imports and applies systems in order

Good examples from your reference projects:

- `LordsOfDiplomacy - Easy Mode`
  combines root orchestration with domain folders like `Diplomacy`, `Kingdom_Resources`, `Provinces`, `World`, and `XS_Scripts`
- `GoKu RPG Project`
  splits systems into `Abilities`, `Bosses`, `NPC`, `Player_Progression`, `Skill_Tree`, `World`, and `XS_Scripts`

The point of this structure is not style for its own sake. It allows each trigger system to be understood, tested, and balanced without reopening unrelated logic.

## Split Each System Into Its Own Folder, Module, And Class

Use a hierarchy like this:

- system folder
  contains the feature boundary, for example a quest, diplomacy action, province system, or class ability group
- module
  contains the actual trigger construction logic for that sub-feature
- class or focused helper object
  owns repeated setup, trigger retrieval, or computed values for that sub-feature

Typical examples:

- a quest folder containing `dictionary.py`, one or more trigger-building modules, and optional helper classes
- an ability folder containing balance data, trigger-logic functions, and a `Spell`-style class that standardizes trigger setup

Use classes when:

- the system has repeated lifecycle steps
- the system needs cached derived values
- the system has activation / deactivation / cooldown style logic

Use plain modules when:

- the system is mostly a stateless builder or a small composition layer

## Data-Driven Python Programming

Trigger-heavy projects should keep data separate from code whenever possible.

Use code for:

- creating triggers
- composing systems
- connecting systems together
- validating assumptions

Use data for:

- balance values
- descriptions
- IDs
- progression tables
- per-level increments
- per-class or per-player mappings

This is the pattern already visible in your projects:

- `dictionary.py` files hold the balance and configuration layer
- code modules consume that data to build triggers
- shared registries like `aoe_variables.py` and `dictionaries_variables.py` hold cross-system IDs and mappings

## Why Data-Driven Programming Matters For Balancing

Balancing is where tightly coupled trigger code becomes expensive.

If values are embedded directly in trigger-building code:

- tuning requires editing logic files instead of changing configuration
- it becomes harder to compare classes, spells, quests, or region systems
- AI assistance becomes weaker because the balance surface is mixed with implementation details

If values live in data dictionaries:

- balance changes are localized
- the logic can stay stable while numbers change
- you can reason about scaling, cooldowns, durations, costs, and thresholds more cleanly
- agents can retrieve balance truth without re-parsing large logic modules

This is why `dictionary.py` is not just a convenience file. In these projects, it is the balancing surface.

## The `apply_` Function Hierarchy

The `apply_` pattern is one of the main architecture signals in your projects.

Use it hierarchically:

- top-level entrypoint calls broad `apply_` functions for major systems
- system-level `apply_` functions call narrower `apply_` functions for sub-systems
- leaf `apply_` functions modify triggers, units, techs, or graphics directly

Examples:

- `GoKu RPG Genie Code/main/main.py`
  acts as the top-level orchestrator and calls major `apply_` modules
- `Classes/Crusader/apply_crusader_class.py`
  applies the class, then delegates to narrower sub-components like unit setup and spell-related pieces
- `GoKu RPG Project/Abilities/Crusader/apply_crusader_spells.py`
  loops through players and spell levels, while leaf functions handle the per-spell trigger effects

This gives you composability:

- a whole system can be included or excluded by calling or not calling its `apply_` module
- sub-systems can be reused elsewhere
- orchestration remains readable because each `apply_` module represents one meaningful layer

## Each Class Or System Should Be Callable In And Out

A strong modular trigger project makes each system independently includable.

That means:

- one class or system should not require unrelated folders to be imported just to run
- the top-level builder should decide what gets applied
- a feature can be disabled by removing one `apply_` call, not by editing many unrelated files

This is especially important for:

- quests
- abilities
- diplomacy actions
- province perks
- regional boss systems

Modularity at the call boundary is what makes later refactors and balancing practical.

## How To Declare XS Variables

When a trigger-heavy project also uses XS, keep XS variable declarations centralized.

Common pattern from your references:

- generate or declare XS variables in one place
- keep a mapping from numeric IDs to semantic names
- let systems consume those names instead of inventing ad hoc variable references

In `LordsOfDiplomacy - Easy Mode/xs_scripts.py`, XS variables are generated in one place and written to the XS file with a stable naming pattern like `xsVariableN`. The important lesson is centralization, not the exact string format.

Preferred rule:

- one registry layer owns XS variable naming
- feature modules ask for variables through helper functions or mappings
- feature modules do not hardcode scattered XS variable IDs unless they are globally fixed bridge constants

## How To Use `aoe_variables`

Use `aoe_variables.py` as the scenario-variable registry layer for trigger systems.

Its job is to:

- reserve scenario variable IDs
- assign human-readable names
- store mappings that other systems reuse
- prevent ID collisions between systems

In your projects, `apply_aoe_variables(trigger_manager)` is the pattern to emulate:

- one function creates the variables
- shared mappings are filled while variables are registered
- downstream systems import the mappings instead of inventing their own variable numbering

Rule of thumb:

- create variables centrally
- consume them locally
- never let each system allocate IDs independently

## `dictionary.py` Plus Class Module Pattern

Some folders intentionally contain both:

- `dictionary.py`
- one or more logic modules or class modules

That split is important.

Use `dictionary.py` for:

- numbers
- descriptions
- thresholds
- scaling
- identifiers
- other balance-facing data

Use the logic or class module for:

- reading the dictionary
- creating triggers
- applying the effect
- wiring lifecycle behavior

Example from `GoKu RPG Project`:

- `Abilities/Crusader/Active_Ability_1/dictionary.py`
  defines the spell data, costs, durations, cooldowns, and scaling
- `Abilities/Crusader/apply_crusader_spells.py`
  consumes that data and builds the actual trigger logic through reusable objects and functions

For balancing work, the dictionary layer is usually the first file to open.

## Primary Files To Open First

- trigger effect lookup
  Open `docs/trigger_knowledge/effects_knowledge.json`
- trigger condition lookup
  Open `docs/trigger_knowledge/conditions_knowledge.json`
- deep explanation of how a condition or effect is used
  Open `docs/trigger_knowledge/condition_usage_playbook.md` or `docs/trigger_knowledge/effect_usage_playbook.md`
- trigger attribute lookup
  Open `docs/trigger_knowledge/attributes_dataset.json`
- real project condition/effect usage lookup
  Open `docs/trigger_knowledge/condition_project_usage.json` or `docs/trigger_knowledge/effect_project_usage.json`
- object or genie ID lookup
  Open `docs/trigger_knowledge/genie_registry.json`
- parser integration question
  Open `src/integration/aoe2_introspection.py`

## Common Task Types

- find the method or parameter list for a trigger effect
- find the method or parameter list for a trigger condition
- map an attribute ID to the parser enum and usage hint
- look up a genie object name or ID
- understand which trigger-side concept maps to parser support
- explain how a condition or effect is used in real scenario projects
- connect trigger logic to XS or AI scripts
- explain how to structure a large trigger project
- explain how variable registries and balancing dictionaries should be organized

## Core Recipes

### Recipe: effect lookup

1. Search `docs/trigger_knowledge/effects_knowledge.json` by effect name or method name.
2. Use the JSON for machine-readable fields.
3. Use `effects_knowledge.md` if you need a human-readable explanation.

### Recipe: condition lookup

1. Search `docs/trigger_knowledge/conditions_knowledge.json` by condition name or method name.
2. Use the JSON for machine-readable fields.
3. Use `conditions_knowledge.md` if you need a human-readable explanation.

### Recipe: how a condition or effect is used in a real project

1. Start with `docs/agent/domains/TRIGGER_CONDITIONS_EFFECTS_GUIDE.md`.
2. Open `docs/trigger_knowledge/condition_project_usage.json` or `docs/trigger_knowledge/effect_project_usage.json`.
3. Match by `internal_name`.
4. Prefer `LordsOfDiplomacy - Easy Mode` examples first, then `GoKu RPG Project`, then `Hide_and_Seek`.
5. Join the usage entry with `conditions_knowledge.json` or `effects_knowledge.json` before answering.

### Recipe: attribute lookup

1. Search `docs/trigger_knowledge/attributes_dataset.json` by attribute ID or parser enum.
2. Preserve both the UGC-facing name and the parser enum when relevant.
3. Use the usage hint to explain how the attribute is typically applied.

### Recipe: object ID lookup

1. Search `docs/trigger_knowledge/genie_registry.json`.
2. Use the registry for IDs, names, aliases, and source facets.
3. If the task becomes data-model-heavy instead of trigger-heavy, switch to `docs/agent/domains/DAT_AGENT_GUIDE.md`.

### Recipe: architecture question about trigger project structure

1. Start with this guide.
2. Open `docs/agent/references/patterns/trigger_xs_patterns.json` if the question is about reusable architecture patterns.
3. Use `docs/agent/references/REFERENCE_PROJECTS.md` to choose the best example project.
4. Explain the architecture in terms of:
   - orchestration layer
   - system folders
   - `apply_` hierarchy
   - variable registry layer
   - dictionary-driven balance layer
5. Only then open project files for concrete examples.

## Known Pitfalls / Engine Quirks

- Not every parser condition or effect appears in the scanned reference projects; check `usage_status` before implying a pattern is common.
- UGC names and parser enum names may differ; preserve both when useful.
- Do not treat trigger effect documentation as proof of `.dat` relationships.
- Object IDs may be shared across gameplay discussions, trigger workflows, and data-mod questions; route carefully.
- Do not mix balancing data directly into large trigger-construction functions when a dictionary-driven layout is feasible.
- Do not let each system invent its own variable IDs independently; central registries scale better.
- Do not confuse â€œone feature folderâ€ with â€œone giant fileâ€; modular systems still need submodules and reusable helpers.

## Cross-Domain Dependencies

- `XS`
  Use for script-call or trigger-variable workflows.
- `AI scripts`
  Use when triggers set AI goals, send AI signals, or interact with AI state.
- `.dat/genie tooling`
  Use when the trigger question is really about the underlying unit, tech, or data relationship rather than editor-side syntax.

