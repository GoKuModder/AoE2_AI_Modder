# Genie Workflow Guide

Use this guide when the task is implementation-oriented `.dat` modding, not just a broad Genie Editor question.

This guide is primarily backed by:

- `GoKu RPG Genie Code`

For exact field questions, open `docs/agent/scenario_builder/DAT_LOOKUP_INDEX.md` and `docs/agent_database/genie_dat_concepts.json` after this guide.

## What This Guide Covers

- `GenieWorkspace` orchestration
- manager roles such as `unit_manager`, `graphic_manager`, `sound_manager`, `tech_manager`, and `civ_manager`
- copy-and-mutate asset workflows
- linking units, graphics, sounds, and dead-unit chains
- output save workflow and registry generation

## One Workspace, Many Managers

The core project pattern is:

1. load `GenieWorkspace` once
2. get the managers once
3. call high-level `apply_` modules for each system
4. save the final `.dat`
5. save a registry or audit artifact

This pattern is shown clearly in `GoKu RPG Genie Code/main/main.py`.

## Manager Roles

- `unit_manager`
  create or copy units/buildings/projectiles and edit unit-side fields
- `graphic_manager`
  add or mutate graphics and particle effects
- `sound_manager`
  create or wire sound assets
- `tech_manager`
  edit or create technologies and related tech behavior
- `civ_manager`
  edit civilization-scoped data

Rule of thumb:

- use the manager that owns the asset type
- use high-level `apply_` modules to connect several managers into one gameplay feature

## Asset Creation Pattern

The repeated genie workflow is:

1. choose a stable base asset
2. create a new asset from that base or add a new one through the manager
3. assign the new name and key fields
4. create dependent graphics or sounds
5. link the components explicitly

Examples from `GoKu RPG Genie Code`:

- `pick_class_unit.py`
  creates a unit from a base unit
- `pick_class_graphics.py`
  creates the linked standing graphic
- `apply_pick_class.py`
  links `unit.standing_sprite_id1 = graphic.id`

## Component Linking Pattern

Many genie features are not one object. They are a linked set:

- main unit
- dead unit
- graphics
- sounds
- build / projectile / hero / glow / particle assets

This is shown very clearly in:

- `Classes/Crusader/Heavenly_Bastion/link_components.py`

The link order matters:

1. create graphics
2. create unit and related secondary units
3. link the secondary unit to graphics
4. link the main unit to the secondary unit or other component IDs

Treat linking as a first-class workflow, not an afterthought.

## Feature Folder Pattern

A mature genie feature folder usually looks like this:

- one `apply_` module
- one or more unit modules
- one or more graphics modules
- one or more sound modules
- optional helper module for linking or shared logic

This is visible across:

- `Classes/*`
- `World/*`
- `Character_General/*`

## Output Rules

Do not treat one local save path as canonical repo knowledge.

Preferred rule:

- if the project already defines the input and output `.dat` locations, use that config
- otherwise ask the user where the modified `.dat` should be written

Good generalized workflow:

1. load the configured base `.dat`
2. apply systems
3. save the output `.dat`
4. save a registry or audit output if the tooling supports it

## Best Files To Open

- exact `.dat` concept or field lookup
  `docs/agent/scenario_builder/DAT_LOOKUP_INDEX.md`
- `.dat` project architecture
  `docs/agent/domains/DAT_AGENT_GUIDE.md`
- compact `.dat` concept dataset
  `docs/agent_database/genie_dat_concepts.json`
- structured genie architecture patterns
  `docs/agent/references/patterns/genie_workflow_patterns.json`
- end-to-end scenario/mod workflow
  `docs/agent/scenario_builder/MAP_IDEA_TO_IMPLEMENTATION.md`
