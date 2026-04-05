# .dat / Genie Tooling Agent Guide

Use this guide for AoE2DE `.dat/genie tooling` questions.

## What This Domain Is For

This domain covers base game data relationships, Genie Editor-oriented modding references, unit and technology relationships, and other data-model questions that influence scripts or triggers. The current repo now has a dedicated `.dat` concept dataset and retriever, but it is still not a full `.dat` edit runtime.

This guide also covers how to structure a real `.dat/genie tooling` project: central workspace orchestration, modular `apply_` pipelines, shared ID registries, and data files that stay separate from mutation logic.

The most important concrete reference for this domain is now `GoKu RPG Genie Code`, because it shows a real modular `.dat` project built around `GenieWorkspace`, asset managers, and explicit component linking.

## Canonical Sources In This Repo

Open these first:

- `docs/agent/scenario_builder/DAT_LOOKUP_INDEX.md`
- `docs/agent_database/genie_dat_concepts.json`
- `XS_Training/external_refs/ageofempires.fandom.com/Genie_Editor.md`
- `XS_Training/modding_general/README.md`
- `XS_Training/modding_general/07_genie_editor_xs_bridge.md`
- `docs/trigger_knowledge/genie_registry.json`
- `docs/agent/references/patterns/genie_workflow_patterns.json`

Supporting reference material:

- `XS_Training/modding_general/02_attributes.md`
- `XS_Training/modding_general/03_charge_types_and_unit_class.md`
- `XS_Training/modding_general/04_tasks.md`
- `XS_Training/modding_general/05_technology.md`

Current runtime status:

- dedicated `.dat` retriever exists at `src/retrieval/genie_dat_retriever.py`
- dedicated `.dat` concept dataset exists at `docs/agent_database/genie_dat_concepts.json`
- no dedicated `.dat` validator
- compact implementation datasets also exist in `docs/agent/references/recipes/genie_recipes.json` and `docs/agent/references/patterns/genie_workflow_patterns.json`

Curated external project reference:

- `docs/agent/references/REFERENCE_PROJECTS.md` -> `GoKu RPG Genie Code`

Additional detailed reference:

- `docs/agent/references/REFERENCE_PROJECTS.md` -> `Hide_and_Seek`

## How To Structure A Genie Data Project

For large data-editing projects, use one thin orchestrator and many focused edit modules.

Preferred pattern:

- one top-level entrypoint loads the workspace
- system folders own one area of the mod
- each system exposes one or more `apply_` modules
- config and ID files stay outside the mutation code
- data files such as JSON stay separate from the edit logic that consumes them

This is visible in `GoKu RPG Genie Code/main/main.py`:

- load workspace once
- get managers once
- call major `apply_` modules in sequence
- save the resulting dat file and registry at the end

## GenieWorkspace And Manager Roles

The real project pattern in `GoKu RPG Genie Code` is not "edit one monolithic dat object everywhere." It is:

- `GenieWorkspace.load(...)`
  load the base `.dat`
- `workspace.unit_manager`
  unit and building creation / mutation
- `workspace.graphic_manager`
  graphics and particle-effect creation / mutation
- `workspace.sound_manager`
  sound creation / mutation
- `workspace.tech_manager`
  technology edits
- `workspace.civ_manager`
  civilization-scoped edits

This matters for agent reasoning because it tells the agent which manager owns which mutation surface. If a task is "make a new quest marker unit with a custom particle graphic," the answer is not one manager. It is a linked workflow across `unit_manager` and `graphic_manager`, usually wrapped by one feature-level `apply_` function.

## Split Each System Into Its Own Folder And Module

Use folders as feature boundaries:

- `Classes`
- `World`
- `Inventory_System`
- `Skill_Tree`
- `Mob_Units`
- `Character_General`

Inside each system:

- one module handles orchestration
- subfolders handle narrower units, graphics, sounds, or linked components
- leaf modules apply one concrete edit

Example pattern:

- `Classes/Crusader/apply_crusader_class.py`
  orchestrates the Crusader feature boundary
- narrower modules define the hero, spell objects, linked graphics, or supporting components

The goal is the same as in trigger projects: add or remove a feature by adding or removing one top-level `apply_` call instead of editing unrelated systems.

## The `apply_` Hierarchy For Genie Work

The `apply_` pattern matters just as much for `.dat` work as it does for triggers.

Use it hierarchically:

- root entrypoint applies major systems
- system-level `apply_` functions apply one domain, class, or world subsystem
- leaf functions create or modify specific units, graphics, sounds, techs, or links between them

Examples from your genie project:

- `main/main.py`
  root orchestration
- `Classes/Ranger/apply_ranger_class.py`
  class-level orchestration
- `World/Potions/apply_potions.py`
  system-level composition of units plus graphics
- `Inventory_System/apply_inventory_system.py`
  orchestration over items, characters, and slot placeholders

This keeps the edit graph understandable and makes it much easier to debug which system introduced a regression.

## Data-Driven Programming In Genie Projects

Separate data from mutation logic whenever possible.

Use code for:

- loading the workspace
- copying templates
- mutating unit, graphic, sound, tech, or civ fields
- linking components together
- saving outputs

Use separate data files for:

- item registries
- resource mappings
- stable IDs
- graphic lookup data
- logs and reverse-engineered outputs

Examples from your project:

- `config/ids.py`
  shared constants and reused IDs
- `main/items_resources_data.json`
  item-to-resource mapping data
- generated or reverse-engineered outputs
  support lookup and recovery rather than direct mutation logic

## Why Data Separation Matters For Balancing And Maintenance

In `.dat` projects, balancing and maintenance become painful if numbers and IDs are buried inside mutation code.

If data is mixed into edit modules:

- changing balance means editing code instead of configuration
- comparing item or class values is harder
- repeated values drift across modules
- agents have to inspect many files to answer one question

If data is separated:

- balance changes become localized
- IDs and mappings become reusable across systems
- repeated edits become easier to audit
- retrieval becomes cheaper because the balance surface is explicit

## Shared ID And Constant Registries

Use a central file for stable IDs and constants that multiple modules need.

In `GoKu RPG Genie Code`, `config/ids.py` is the pattern:

- globally reused graphic IDs live in one place
- world-object references are centralized
- leaf modules can import the same constants instead of duplicating magic numbers

Preferred rule:

- one shared registry for truly global constants
- local modules may define temporary internals, but not shared canonical IDs

## Template-Copy And Link Patterns

Many genie workflows are "copy an existing object, assign a new ID, change fields, then link it to related graphics or sounds."

Typical pattern:

1. load the workspace once
2. pick a known base object
3. deep-copy the base object
4. assign a new stable ID
5. mutate only the required fields
6. link graphics, sounds, or tasks
7. save the workspace and registry

This pattern appears clearly in the graphics-to-genie tooling flow and in many of the class/world systems.

Concrete examples from `GoKu RPG Genie Code`:

- `Character_General/Pick_Class/pick_class_unit.py`
  create the unit from a stable base unit
- `Character_General/Pick_Class/pick_class_graphics.py`
  create the standing graphic
- `Character_General/Pick_Class/apply_pick_class.py`
  link `unit.standing_sprite_id1 = graphic.id`

## Component Linking Is A First-Class Workflow

Many features in a real genie project are linked component graphs, not isolated assets.

Typical chain:

- main unit
- dead unit
- standing / dying / projectile / glow graphics
- sounds
- optional tech or task hooks

This is shown explicitly in `Classes/Crusader/Heavenly_Bastion/link_components.py`:

1. create the graphics
2. create the main unit
3. create the dead unit
4. link the dead unit to the graphics
5. link the main unit to the dead unit

Agents should treat linking order as part of the implementation pattern, not as cleanup after the fact.

## Save Outputs And Registries Explicitly

`GoKu RPG Genie Code/main/main.py` also shows an important discipline:

- save the final `.dat`
- save the mod-target `.dat`
- save a registry output

This should be generalized as:

- one explicit output save step for the built `.dat`
- one optional registry or audit artifact
- configurable output paths rather than one developer PC path hardcoded as the general rule

If the project config does not already define the final `.dat` output location, the agent should ask the user where the file should be written.

## Keep Systems Callable In And Out

A genie project should let you include or exclude a whole feature by toggling one high-level `apply_` call.

That means:

- `apply_crusader_class` should be callable without forcing unrelated world edits
- `apply_potions` should be callable without touching class systems
- inventory or skill-tree systems should remain modular

This is especially important once the mod grows large, because it lets you:

- isolate regressions
- test one subsystem at a time
- reuse parts of the project in other mods

## Common Task Types

## Primary Files To Open First

- exact `.dat` field or data-model question
  Open `docs/agent/scenario_builder/DAT_LOOKUP_INDEX.md`
- dedicated `.dat` concept lookup dataset
  Open `docs/agent_database/genie_dat_concepts.json`
- broad Genie Editor or `.dat` question
  Open `XS_Training/external_refs/ageofempires.fandom.com/Genie_Editor.md`
- question about unit / tech / task / class relationships
  Open the matching file in `XS_Training/modding_general/`
- question about object IDs or names
  Open `docs/trigger_knowledge/genie_registry.json`
- question that crosses into XS or triggers
  Open `docs/agent/navigation/CROSS_DOMAIN_WORKFLOWS.md`

## Common Task Types

- identify unit, building, hero, or object IDs
- understand train-location and technology relationships
- understand tasks, unit classes, attributes, and charge-related references
- connect data-model changes to XS, AI, or trigger behavior
- explain how to architect a modular `.dat` editing project
- explain how shared IDs and data files should be separated from edit logic

## Core Recipes

### Recipe: object identity lookup

1. Search `docs/trigger_knowledge/genie_registry.json`.
2. Use the registry for stable ID-to-name lookup.
3. Use the broader modding docs only if you need gameplay or editor meaning.

### Recipe: `.dat` concept lookup

1. Open this guide.
2. Open `docs/agent/scenario_builder/DAT_LOOKUP_INDEX.md`.
3. Open `docs/agent_database/genie_dat_concepts.json`.
4. Search the relevant `XS_Training/modding_general/` file only if the compact concept dataset is insufficient.
5. If the question is really about trigger-side or script-side behavior, route to that domain guide after grounding the data concept.

### Recipe: architecture question about genie project structure

1. Start with this guide.
2. Open `docs/agent/scenario_builder/GENIE_WORKFLOW_GUIDE.md` if the question is implementation-heavy rather than conceptual.
2. Open `docs/agent/references/patterns/genie_workflow_patterns.json` if the question is about reusable architecture patterns.
3. Use `docs/agent/references/REFERENCE_PROJECTS.md` to choose `GoKu RPG Genie Code` as the primary example.
4. Explain the architecture in terms of:
   - top-level workspace entrypoint
   - manager ownership by asset type
   - system folders
   - `apply_` hierarchy
   - component-linking workflow
   - shared ID registry
   - separate JSON or config data
5. Only then open project files for concrete examples.

### Recipe: cross-domain data question

1. Identify whether the user is editing XS, AI scripts, or triggers.
2. Answer the domain-specific part from that guide.
3. Use `.dat/genie tooling` references to explain the underlying data relationships.

## Known Pitfalls / Engine Quirks

- This repo does not yet provide a full `.dat` editing runtime.
- The genie registry is useful for IDs and names, but it is not a full substitute for a structured `.dat` schema.
- Some `.dat` knowledge still lives in narrative markdown rather than machine-readable datasets.
- Many `.dat` questions are really cross-domain questions once the user starts writing XS, AI, or trigger logic.
- Do not scatter shared graphic or unit IDs across many modules when they should live in a central config layer.
- Do not put large balancing datasets directly into mutation code if a JSON or config file can hold them cleanly.
- Do not treat one giant `main.py` as the whole architecture; the real structure should live in reusable `apply_` modules.

## Cross-Domain Dependencies

- `XS`
  Use when data-model relationships affect XS logic or constants.
- `AI scripts`
  Use when AI behavior depends on unit or technology relationships.
- `scenario triggers`
  Use when data-model meaning affects trigger object IDs, effects, or attribute choices.

