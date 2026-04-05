# Parser Managers Guide

Use this guide when the task is not just "which trigger effect exists?" but "how do I actually build or edit the scenario with AoE2ScenarioParser managers?"

This guide is backed by your real projects, especially:

- `LordsOfDiplomacy - Easy Mode`
- `GoKu RPG Project`

## What This Guide Covers

- `UnitManager`
- `MapManager`
- how these managers fit into a modular scenario project
- which tasks belong to parser-manager code versus trigger code versus XS code

## Core Rule

Use parser managers for scenario data and editor-object manipulation.

Use triggers for gameplay state and event flow.

Use XS for runtime calculations, bridge logic, and engine-side script behavior that should not be fully owned by triggers.

## UnitManager

`UnitManager` is the main tool for placing, finding, filtering, removing, or reassigning units and map objects in the scenario file.

Real usage patterns from your projects include:

- placing editor units and markers with `add_unit`
- collecting or clearing units with `get_units_in_area`
- removing units with `remove_unit`
- finding pre-placed units by type with `filter_units_by_const`
- changing ownership with `change_ownership`
- iterating player-owned units with `get_player_units`

### Best Use Cases For UnitManager

- place map markers, blockers, NPCs, buildings, quest objects, revealers, relics, shops, and decorative units
- remove unwanted pre-placed units from source scenarios
- scan or convert placed scenario objects during initialization
- set up physical map content before trigger logic starts using it

### Real Project Examples

From `LordsOfDiplomacy - Easy Mode`:

- `deploy_units.py`
  uses `unit_manager.add_unit(...)` repeatedly to place haystacks, relics, flags, army tents, map revealers, and region markers

From `GoKu RPG Project`:

- `main/main_code.py`
  uses `unit_manager.get_units_in_area(...)` and `unit_manager.remove_unit(...)` to clear regions
- `main/main_code.py`
  uses `unit_manager.add_unit(...)` to place blockers on specific terrain
- `main/main_code.py`
  uses `unit_manager.filter_units_by_const(...)` and `unit_manager.change_ownership(...)` to convert placed units

### UnitManager Architecture Guidance

- keep mass placement or cleanup in dedicated placement/setup modules
- do not mix large placement loops directly into unrelated trigger logic modules
- pass `unit_manager` into systems that truly need scenario-object access
- let trigger systems consume the placed result instead of also owning the placement pass

## MapManager

`MapManager` is the main tool for reading or mutating map-level terrain and tile information.

Real usage patterns from your projects include:

- iterating `map_manager.terrain`
- checking terrain IDs to place blockers or content conditionally
- reading rectangular tile regions with helpers like `get_square_2d`

### Best Use Cases For MapManager

- terrain-driven placement
- region scanning
- creating or reading tile-based gameplay layouts
- finding map areas that should spawn blockers, objects, or markers

### Real Project Examples

From `LordsOfDiplomacy - Easy Mode`:

- `deploy_units.py`
  uses `source_scenario.map_manager.get_square_2d(...)` to inspect tile regions before placement
- `game_initialization.py`
  reads `source_scenario.map_manager.terrain`

From `GoKu RPG Project`:

- `main/main_code.py`
  iterates `map_manager.terrain` and places blockers on black terrain tiles
- systems such as teleportation, revealers, quests, and shop placement receive `map_manager` when the mechanic depends on physical map layout

### MapManager Architecture Guidance

- use `map_manager` in world/setup systems, not in every gameplay module
- keep terrain scanning close to placement code or region-definition code
- avoid burying tile-geometry logic inside unrelated combat or quest code

## When To Use Which Layer

- place or remove scenario objects
  `UnitManager`
- inspect or react to terrain / tiles
  `MapManager`
- create event flow, state machines, cooldowns, quests, UI notifications
  triggers
- compute runtime script behavior, bridge state, or repeated XS-side calculations
  XS

## Common Mistakes

- do not use triggers for mass pre-game unit placement that belongs in scenario-build code
- do not use `UnitManager` as a replacement for trigger state logic
- do not spread terrain scanning everywhere when one setup module can define the map layout once
- do not make parser managers the owner of balance data; keep balancing in dictionaries or config layers

## If A Map Idea Mentions Physical Content

Use this mapping:

- "spawn buildings, NPCs, relics, blockers, markers"
  `UnitManager`
- "scan terrain, detect black tiles, inspect map rectangles"
  `MapManager`
- "fire quest logic, events, and state changes"
  triggers
- "runtime engine calculations or bridge logic"
  XS
