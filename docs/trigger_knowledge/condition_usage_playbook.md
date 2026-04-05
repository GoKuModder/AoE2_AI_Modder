# Trigger Condition Usage Playbook
Generated file. Do not hand-edit; run tools/build_trigger_knowledge.py.

## 0. None
**Method**: `none`
**Family**: `null`
**Primary Role**: Sentinel or placeholder condition.

**How It Is Used**
Use this only when a trigger needs a syntactic placeholder or when tooling expects a condition object but the design does not require a real gate. It is not a gameplay condition and should not be treated as meaningful scenario logic.

**Architecture Notes**
If this appears in production trigger generation, it usually means the real gate lives elsewhere or the system is still scaffolding its trigger graph.

**Real Project Usage**
This parser feature is present in AoE2ScenarioParser but was not observed in the scanned local reference projects. Treat it as supported capability with no local canonical usage pattern yet.

**Common Pairings**
- `activate_trigger`
- `deactivate_trigger`

## 1. Bring Object To Area
**Method**: `bring_object_to_area`
**Family**: `movement_area`
**Primary Role**: Detect that a specific object reached a designed interaction point.

**How It Is Used**
Use these conditions when the scenario logic depends on a named unit, hero, or token physically entering a destination or reaching another object. In real projects they sit near quest, boss, teleport, or handoff systems where one tracked object must arrive somewhere before the next trigger stage unlocks.

**Architecture Notes**
This family is strongest when the tracked object is stable and unique. If the system cares about any qualifying unit rather than one known unit, area-count conditions are usually a better fit.

**Real Project Usage**
Observed 1 times in the scanned reference projects, primarily in GoKu RPG Project (1 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `activate_trigger`
- `change_variable`
- `teleport_object`
- `send_chat`

**Reference Examples**
- `GoKu RPG Project -> Bosses\Boss_System.py:180`

## 2. Bring Object To Object
**Method**: `bring_object_to_object`
**Family**: `movement_area`
**Primary Role**: Detect that a specific object reached a designed interaction point.

**How It Is Used**
Use these conditions when the scenario logic depends on a named unit, hero, or token physically entering a destination or reaching another object. In real projects they sit near quest, boss, teleport, or handoff systems where one tracked object must arrive somewhere before the next trigger stage unlocks.

**Architecture Notes**
This family is strongest when the tracked object is stable and unique. If the system cares about any qualifying unit rather than one known unit, area-count conditions are usually a better fit.

**Real Project Usage**
This parser feature is present in AoE2ScenarioParser but was not observed in the scanned local reference projects. Treat it as supported capability with no local canonical usage pattern yet.

**Common Pairings**
- `activate_trigger`
- `change_variable`
- `teleport_object`
- `send_chat`

## 3. Own Objects
**Method**: `own_objects`
**Family**: `area_population`
**Primary Role**: Treat map areas as gameplay sensors.

**How It Is Used**
These conditions turn a rectangle on the map into a reusable detector. They are commonly used for portals, pressure plates, interaction zones, quest regions, and ability hit or entry zones. In large projects they usually sit at the front of a modular system and decide whether the rest of the chain should run.

**Architecture Notes**
Use area conditions when the map itself is part of the gameplay API. Keep the coordinates centralized or derived from shared data so balancing or map edits do not require rewriting trigger logic.

**Real Project Usage**
Observed 18 times in the scanned reference projects, primarily in LordsOfDiplomacy - Easy Mode (14 uses), GoKu RPG Project (3 uses), Hide_and_Seek (1 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `and_`
- `or_`
- `activate_trigger`
- `deactivate_trigger`
- `play_sound`
- `change_view`

**Reference Examples**
- `LordsOfDiplomacy - Easy Mode -> characters.py:154`
- `LordsOfDiplomacy - Easy Mode -> Clerical_Actions\Initializations\initialize_cleric.py:200`
- `LordsOfDiplomacy - Easy Mode -> Clerical_Actions\Initializations\initialize_cleric.py:254`

## 4. Own Fewer Objects
**Method**: `own_fewer_objects`
**Family**: `area_population`
**Primary Role**: Treat map areas as gameplay sensors.

**How It Is Used**
These conditions turn a rectangle on the map into a reusable detector. They are commonly used for portals, pressure plates, interaction zones, quest regions, and ability hit or entry zones. In large projects they usually sit at the front of a modular system and decide whether the rest of the chain should run.

**Architecture Notes**
Use area conditions when the map itself is part of the gameplay API. Keep the coordinates centralized or derived from shared data so balancing or map edits do not require rewriting trigger logic.

**Real Project Usage**
Observed 7 times in the scanned reference projects, primarily in LordsOfDiplomacy - Easy Mode (4 uses), GoKu RPG Project (3 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `and_`
- `or_`
- `activate_trigger`
- `deactivate_trigger`
- `play_sound`
- `change_view`

**Reference Examples**
- `LordsOfDiplomacy - Easy Mode -> game_initialization.py:401`
- `LordsOfDiplomacy - Easy Mode -> Provinces\Capture_From_GAIA\Capture_Province_gaia\start_capture_process.py:129`
- `LordsOfDiplomacy - Easy Mode -> Provinces\Capture_Province\start_capture_process.py:174`

## 5. Objects In Area
**Method**: `objects_in_area`
**Family**: `area_population`
**Primary Role**: Treat map areas as gameplay sensors.

**How It Is Used**
This is the most reusable zone-sensor condition in the reference projects. It is used for teleports, interaction pads, boss areas, tutorial spaces, and ability-driven regions. The condition turns a rectangular area into a modular gameplay boundary that other systems can reuse without knowing the whole map script.

**Architecture Notes**
For maintainable scenarios, area coordinates should be treated as data. That lets the same trigger architecture survive balancing passes or map revisions without rewriting the surrounding logic modules.

**Real Project Usage**
Observed 40 times in the scanned reference projects, primarily in LordsOfDiplomacy - Easy Mode (22 uses), GoKu RPG Project (18 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `and_`
- `or_`
- `activate_trigger`
- `change_view`
- `teleport_object`

**Reference Examples**
- `LordsOfDiplomacy - Easy Mode -> Court_Actions\court_actions.py:78`
- `LordsOfDiplomacy - Easy Mode -> cut_scenes.py:256`
- `LordsOfDiplomacy - Easy Mode -> cut_scenes.py:303`

## 6. Destroy Object
**Method**: `destroy_object`
**Family**: `object_state`
**Primary Role**: Inspect the runtime state of a particular object or set of objects.

**How It Is Used**
Use these conditions when progression depends on what a unit is doing or what happened to it. They are suitable for ability systems, escort logic, survival checks, target-tracking, interaction locks, and other cases where trigger logic must react to object state rather than raw area presence.

**Architecture Notes**
These conditions are most maintainable when the tracked objects are already registered by the surrounding system. If object identity is unstable, pair them with variable or creation logic that keeps references synchronized.

**Real Project Usage**
Observed 11 times in the scanned reference projects, primarily in GoKu RPG Project (11 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `modify_attribute`
- `remove_object`
- `task_object`
- `create_object`
- `change_variable`

**Reference Examples**
- `GoKu RPG Project -> Bosses\Boss_System.py:67`
- `GoKu RPG Project -> Bosses\Boss_System.py:252`
- `GoKu RPG Project -> Bosses\Regions\Dqarn\Dungeon\Elephants_Dungeon\Post_Boss_Events\events.py:26`

## 7. Capture Object
**Method**: `capture_object`
**Family**: `object_state`
**Primary Role**: Inspect the runtime state of a particular object or set of objects.

**How It Is Used**
Use these conditions when progression depends on what a unit is doing or what happened to it. They are suitable for ability systems, escort logic, survival checks, target-tracking, interaction locks, and other cases where trigger logic must react to object state rather than raw area presence.

**Architecture Notes**
These conditions are most maintainable when the tracked objects are already registered by the surrounding system. If object identity is unstable, pair them with variable or creation logic that keeps references synchronized.

**Real Project Usage**
Observed 3 times in the scanned reference projects, primarily in LordsOfDiplomacy - Easy Mode (3 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `modify_attribute`
- `remove_object`
- `task_object`
- `create_object`
- `change_variable`

**Reference Examples**
- `LordsOfDiplomacy - Easy Mode -> Provinces\Capture_From_GAIA\Capture_Province_gaia\start_capture_process.py:50`
- `LordsOfDiplomacy - Easy Mode -> Provinces\Capture_Province\start_capture_process.py:49`
- `LordsOfDiplomacy - Easy Mode -> Provinces\OLD_conquer_province.py:250`

## 8. Accumulate Attribute
**Method**: `accumulate_attribute`
**Family**: `economy_progress`
**Primary Role**: Gate logic on progression, economy, technology, or threshold state.

**How It Is Used**
Use this when a system unlocks on a threshold rather than a one-time event. In project-scale scenarios it works well for economy gates, score-like progression, custom currencies, or persistent class-resource systems where the number matters more than any single moment of gain.

**Architecture Notes**
This family becomes much easier to tune when the threshold values live in dictionaries or config modules instead of being hardcoded inline in trigger builder functions.

**Real Project Usage**
Observed 18 times in the scanned reference projects, primarily in LordsOfDiplomacy - Easy Mode (3 uses), GoKu RPG Project (14 uses), Hide_and_Seek (1 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `and_`
- `change_variable`
- `activate_trigger`
- `research_technology`
- `modify_resource`
- `enable_disable_technology`

**Reference Examples**
- `LordsOfDiplomacy - Easy Mode -> Diplomacy\Auto_War\Neutral\neutral_kills_autowar.py:50`
- `LordsOfDiplomacy - Easy Mode -> Kingdom_Resources\helper_function.py:36`
- `LordsOfDiplomacy - Easy Mode -> Kingdom_Resources\helper_function.py:63`

## 9. Research Technology
**Method**: `research_technology`
**Family**: `economy_progress`
**Primary Role**: Gate logic on progression, economy, technology, or threshold state.

**How It Is Used**
Use these conditions to turn the trigger graph into a progression system. They work as prerequisites for quests, unlocks, upgrade paths, resource thresholds, and UI-like technology buttons. The surrounding trigger system usually checks one of these conditions first and only then applies the effects that mutate state or expose the next step.

**Architecture Notes**
This family becomes much easier to tune when the threshold values live in dictionaries or config modules instead of being hardcoded inline in trigger builder functions.

**Real Project Usage**
Observed 1 times in the scanned reference projects, primarily in LordsOfDiplomacy - Easy Mode (1 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `and_`
- `change_variable`
- `activate_trigger`
- `research_technology`
- `modify_resource`
- `enable_disable_technology`

**Reference Examples**
- `LordsOfDiplomacy - Easy Mode -> World\remove_deer.py:52`

## 10. Timer
**Method**: `timer`
**Family**: `timing_state`
**Primary Role**: Provide the heartbeat and sequencing layer for trigger systems.

**How It Is Used**
This is the heartbeat condition in your projects. It drives cooldown expiration, periodic mana or status ticks, cutscene sequencing, staged tutorials, and delayed system reactivation. It is not just a delay helper; it is the mechanism that turns separate trigger modules into time-aware systems.

**Architecture Notes**
A timer gate is usually most useful when paired with another check that says why the trigger should still matter. That keeps loops and cooldown triggers from firing blindly after the owning system has already moved on.

**Real Project Usage**
Observed 143 times in the scanned reference projects, primarily in LordsOfDiplomacy - Easy Mode (80 uses), GoKu RPG Project (42 uses), Hide_and_Seek (21 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `variable_value`
- `and_`
- `activate_trigger`
- `deactivate_trigger`
- `display_timer`

**Reference Examples**
- `LordsOfDiplomacy - Easy Mode -> Clerical_Actions\Actions\Adopt_Population\effect.py:19`
- `LordsOfDiplomacy - Easy Mode -> Court_Actions\court_actions.py:129`
- `LordsOfDiplomacy - Easy Mode -> Court_Actions\court_actions.py:161`

## 11. Object Selected
**Method**: `object_selected`
**Family**: `object_state`
**Primary Role**: Inspect the runtime state of a particular object or set of objects.

**How It Is Used**
Use these conditions when progression depends on what a unit is doing or what happened to it. They are suitable for ability systems, escort logic, survival checks, target-tracking, interaction locks, and other cases where trigger logic must react to object state rather than raw area presence.

**Architecture Notes**
These conditions are most maintainable when the tracked objects are already registered by the surrounding system. If object identity is unstable, pair them with variable or creation logic that keeps references synchronized.

**Real Project Usage**
This parser feature is present in AoE2ScenarioParser but was not observed in the scanned local reference projects. Treat it as supported capability with no local canonical usage pattern yet.

**Common Pairings**
- `modify_attribute`
- `remove_object`
- `task_object`
- `create_object`
- `change_variable`

## 12. AI Signal
**Method**: `ai_signal`
**Family**: `bridge`
**Primary Role**: Connect trigger logic to external systems such as XS, AI, or engine-side event channels.

**How It Is Used**
Use bridge conditions when the trigger layer should not own the final decision by itself. Instead of duplicating logic in triggers, the scenario can ask XS or another signal source for the answer and then let triggers handle orchestration, visuals, and follow-up state changes.

**Architecture Notes**
This family is most valuable when triggers stay thin and XS or signal-producing systems stay authoritative for the calculation. Avoid scattering bridge checks everywhere; centralize them around clear handoff points.

**Real Project Usage**
This parser feature is present in AoE2ScenarioParser but was not observed in the scanned local reference projects. Treat it as supported capability with no local canonical usage pattern yet.

**Common Pairings**
- `script_call`
- `change_variable`
- `activate_trigger`
- `deactivate_trigger`
- `send_chat`

## 13. Player Defeated
**Method**: `player_defeated`
**Family**: `timing_state`
**Primary Role**: Provide the heartbeat and sequencing layer for trigger systems.

**How It Is Used**
Use these conditions when a system needs delays, loops, cooldowns, countdown completions, or stage sequencing. In real projects timer-style conditions are what make abilities pulse, phases advance, cutscenes tick, and temporary locks expire.

**Architecture Notes**
Timer conditions are usually not the whole gate by themselves. They become powerful when combined with variable, area, or script-call checks so the system can sequence complex behavior without turning into one giant trigger.

**Real Project Usage**
Observed 1 times in the scanned reference projects, primarily in LordsOfDiplomacy - Easy Mode (1 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `and_`
- `activate_trigger`
- `deactivate_trigger`
- `change_variable`
- `display_timer`
- `script_call`

**Reference Examples**
- `LordsOfDiplomacy - Easy Mode -> World\player_defeated_diplomacy.py:26`

## 14. Object Has Target
**Method**: `object_has_target`
**Family**: `object_state`
**Primary Role**: Inspect the runtime state of a particular object or set of objects.

**How It Is Used**
Use these conditions when progression depends on what a unit is doing or what happened to it. They are suitable for ability systems, escort logic, survival checks, target-tracking, interaction locks, and other cases where trigger logic must react to object state rather than raw area presence.

**Architecture Notes**
These conditions are most maintainable when the tracked objects are already registered by the surrounding system. If object identity is unstable, pair them with variable or creation logic that keeps references synchronized.

**Real Project Usage**
This parser feature is present in AoE2ScenarioParser but was not observed in the scanned local reference projects. Treat it as supported capability with no local canonical usage pattern yet.

**Common Pairings**
- `modify_attribute`
- `remove_object`
- `task_object`
- `create_object`
- `change_variable`

## 15. Object Visible
**Method**: `object_visible`
**Family**: `object_state`
**Primary Role**: Inspect the runtime state of a particular object or set of objects.

**How It Is Used**
Use these conditions when progression depends on what a unit is doing or what happened to it. They are suitable for ability systems, escort logic, survival checks, target-tracking, interaction locks, and other cases where trigger logic must react to object state rather than raw area presence.

**Architecture Notes**
These conditions are most maintainable when the tracked objects are already registered by the surrounding system. If object identity is unstable, pair them with variable or creation logic that keeps references synchronized.

**Real Project Usage**
This parser feature is present in AoE2ScenarioParser but was not observed in the scanned local reference projects. Treat it as supported capability with no local canonical usage pattern yet.

**Common Pairings**
- `modify_attribute`
- `remove_object`
- `task_object`
- `create_object`
- `change_variable`

## 16. Object Not Visible
**Method**: `object_not_visible`
**Family**: `object_state`
**Primary Role**: Inspect the runtime state of a particular object or set of objects.

**How It Is Used**
Use these conditions when progression depends on what a unit is doing or what happened to it. They are suitable for ability systems, escort logic, survival checks, target-tracking, interaction locks, and other cases where trigger logic must react to object state rather than raw area presence.

**Architecture Notes**
These conditions are most maintainable when the tracked objects are already registered by the surrounding system. If object identity is unstable, pair them with variable or creation logic that keeps references synchronized.

**Real Project Usage**
This parser feature is present in AoE2ScenarioParser but was not observed in the scanned local reference projects. Treat it as supported capability with no local canonical usage pattern yet.

**Common Pairings**
- `modify_attribute`
- `remove_object`
- `task_object`
- `create_object`
- `change_variable`

## 17. Researching Tech
**Method**: `researching_tech`
**Family**: `economy_progress`
**Primary Role**: Gate logic on progression, economy, technology, or threshold state.

**How It Is Used**
Your reference projects use this as a trigger-friendly button press or menu interaction. The scenario exposes technologies as player actions, then `researching_tech` detects that interaction and hands control to the modular trigger system that performs the actual gameplay logic.

**Architecture Notes**
This pattern is valuable because it gives players a clean UI surface while keeping the real logic in triggers and XS. It is one of the clearest examples of data-driven scenario interfaces.

**Real Project Usage**
Observed 14 times in the scanned reference projects, primarily in LordsOfDiplomacy - Easy Mode (14 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `change_technology_location`
- `change_technology_cost`
- `activate_trigger`
- `deactivate_trigger`
- `send_chat`

**Reference Examples**
- `LordsOfDiplomacy - Easy Mode -> Court_Actions\court_actions.py:88`
- `LordsOfDiplomacy - Easy Mode -> Diplomacy\Actions\Alliance\apply_alliance.py:66`
- `LordsOfDiplomacy - Easy Mode -> Diplomacy\Actions\Alliance\apply_alliance.py:239`

## 18. Units Garrisoned
**Method**: `units_garrisoned`
**Family**: `object_state`
**Primary Role**: Inspect the runtime state of a particular object or set of objects.

**How It Is Used**
Use these conditions when progression depends on what a unit is doing or what happened to it. They are suitable for ability systems, escort logic, survival checks, target-tracking, interaction locks, and other cases where trigger logic must react to object state rather than raw area presence.

**Architecture Notes**
These conditions are most maintainable when the tracked objects are already registered by the surrounding system. If object identity is unstable, pair them with variable or creation logic that keeps references synchronized.

**Real Project Usage**
This parser feature is present in AoE2ScenarioParser but was not observed in the scanned local reference projects. Treat it as supported capability with no local canonical usage pattern yet.

**Common Pairings**
- `modify_attribute`
- `remove_object`
- `task_object`
- `create_object`
- `change_variable`

## 19. Difficulty Level
**Method**: `difficulty_level`
**Family**: `economy_progress`
**Primary Role**: Gate logic on progression, economy, technology, or threshold state.

**How It Is Used**
Use these conditions to turn the trigger graph into a progression system. They work as prerequisites for quests, unlocks, upgrade paths, resource thresholds, and UI-like technology buttons. The surrounding trigger system usually checks one of these conditions first and only then applies the effects that mutate state or expose the next step.

**Architecture Notes**
This family becomes much easier to tune when the threshold values live in dictionaries or config modules instead of being hardcoded inline in trigger builder functions.

**Real Project Usage**
This parser feature is present in AoE2ScenarioParser but was not observed in the scanned local reference projects. Treat it as supported capability with no local canonical usage pattern yet.

**Common Pairings**
- `and_`
- `change_variable`
- `activate_trigger`
- `research_technology`
- `modify_resource`
- `enable_disable_technology`

## 20. Chance
**Method**: `chance`
**Family**: `economy_progress`
**Primary Role**: Gate logic on progression, economy, technology, or threshold state.

**How It Is Used**
Use these conditions to turn the trigger graph into a progression system. They work as prerequisites for quests, unlocks, upgrade paths, resource thresholds, and UI-like technology buttons. The surrounding trigger system usually checks one of these conditions first and only then applies the effects that mutate state or expose the next step.

**Architecture Notes**
This family becomes much easier to tune when the threshold values live in dictionaries or config modules instead of being hardcoded inline in trigger builder functions.

**Real Project Usage**
Observed 3 times in the scanned reference projects, primarily in Hide_and_Seek (3 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `and_`
- `change_variable`
- `activate_trigger`
- `research_technology`
- `modify_resource`
- `enable_disable_technology`

**Reference Examples**
- `Hide_and_Seek -> old_code\game.py:189`
- `Hide_and_Seek -> old_code\game.py:261`
- `Hide_and_Seek -> old_code\game.py:326`

## 21. Technology State
**Method**: `technology_state`
**Family**: `economy_progress`
**Primary Role**: Gate logic on progression, economy, technology, or threshold state.

**How It Is Used**
Use these conditions to turn the trigger graph into a progression system. They work as prerequisites for quests, unlocks, upgrade paths, resource thresholds, and UI-like technology buttons. The surrounding trigger system usually checks one of these conditions first and only then applies the effects that mutate state or expose the next step.

**Architecture Notes**
This family becomes much easier to tune when the threshold values live in dictionaries or config modules instead of being hardcoded inline in trigger builder functions.

**Real Project Usage**
This parser feature is present in AoE2ScenarioParser but was not observed in the scanned local reference projects. Treat it as supported capability with no local canonical usage pattern yet.

**Common Pairings**
- `and_`
- `change_variable`
- `activate_trigger`
- `research_technology`
- `modify_resource`
- `enable_disable_technology`

## 22. Variable Value
**Method**: `variable_value`
**Family**: `variables`
**Primary Role**: Implement scenario state machines and balanceable trigger state.

**How It Is Used**
This is the core trigger-state gate in your reference projects. It is used to represent cooldown flags, quest stages, class-state toggles, respawn permissions, and other per-player progression markers. In practice, a large modular scenario keeps the real gameplay state in variables and uses `variable_value` to decide which branch of the trigger graph is currently legal.

**Architecture Notes**
If an agent is building a scalable scenario, this should usually be one of the first conditions it reaches for after creating a central variable registry. The condition is especially strong when combined with dictionary-driven balance data and with `change_variable` effects that advance state explicitly.

**Real Project Usage**
Observed 172 times in the scanned reference projects, primarily in LordsOfDiplomacy - Easy Mode (18 uses), GoKu RPG Project (8 uses), Hide_and_Seek (146 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `change_variable`
- `timer`
- `activate_trigger`
- `deactivate_trigger`
- `script_call`

**Reference Examples**
- `LordsOfDiplomacy - Easy Mode -> Diplomacy\Actions\Helper_Functions\required_reputation.py:16`
- `LordsOfDiplomacy - Easy Mode -> Diplomacy\Actions\Helper_Functions\required_reputation.py:32`
- `LordsOfDiplomacy - Easy Mode -> Espionage\Actions\Open_Enemy_Gates\apply_open_enemy_gates.py:31`

## 23. Object HP
**Method**: `object_hp`
**Family**: `object_state`
**Primary Role**: Inspect the runtime state of a particular object or set of objects.

**How It Is Used**
Use these conditions when progression depends on what a unit is doing or what happened to it. They are suitable for ability systems, escort logic, survival checks, target-tracking, interaction locks, and other cases where trigger logic must react to object state rather than raw area presence.

**Architecture Notes**
These conditions are most maintainable when the tracked objects are already registered by the surrounding system. If object identity is unstable, pair them with variable or creation logic that keeps references synchronized.

**Real Project Usage**
Observed 3 times in the scanned reference projects, primarily in GoKu RPG Project (3 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `modify_attribute`
- `remove_object`
- `task_object`
- `create_object`
- `change_variable`

**Reference Examples**
- `GoKu RPG Project -> Bosses\Boss_System.py:222`
- `GoKu RPG Project -> Bosses\Boss_System.py:239`
- `GoKu RPG Project -> Skill_Tree\Skill_Tree_Ability.py:113`

## 24. Diplomacy State
**Method**: `diplomacy_state`
**Family**: `diplomacy`
**Primary Role**: Gate logic on relationship state between players.

**How It Is Used**
Use diplomacy conditions for treaty systems, alliance actions, conversion of neutrality states into gameplay branches, and scenarios where political state is itself the mechanic. This family usually belongs in a dedicated diplomacy module instead of being mixed into unrelated combat logic.

**Architecture Notes**
Diplomacy systems become readable when the trigger layer separates the check, the state transition, and the user-facing feedback into different triggers or helper functions.

**Real Project Usage**
This parser feature is present in AoE2ScenarioParser but was not observed in the scanned local reference projects. Treat it as supported capability with no local canonical usage pattern yet.

**Common Pairings**
- `change_diplomacy`
- `send_chat`
- `play_sound`
- `activate_trigger`

## 25. Script Call
**Method**: `script_call`
**Family**: `bridge`
**Primary Role**: Connect trigger logic to external systems such as XS, AI, or engine-side event channels.

**How It Is Used**
Use this when the final decision should come from XS instead of from the trigger layer itself. In your projects it appears at bridge points where the trigger graph asks XS for a computed answer, then reacts with trigger-side orchestration, UI, or object manipulation. It is the cleanest way to keep calculations and trigger presentation separated.

**Architecture Notes**
This condition is strongest when the XS function has a clear, stable responsibility and the surrounding trigger owns only the reaction. If the trigger also recomputes the same logic locally, the bridge is being used poorly.

**Real Project Usage**
Observed 62 times in the scanned reference projects, primarily in LordsOfDiplomacy - Easy Mode (46 uses), GoKu RPG Project (12 uses), Hide_and_Seek (4 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `script_call`
- `change_variable`
- `activate_trigger`
- `deactivate_trigger`
- `send_chat`

**Reference Examples**
- `LordsOfDiplomacy - Easy Mode -> Clerical_Actions\Actions\Adopt_Population\piety_cost.py:33`
- `LordsOfDiplomacy - Easy Mode -> custom_functions.py:247`
- `LordsOfDiplomacy - Easy Mode -> custom_functions.py:290`

## 26. Object Selected Multiplayer
**Method**: `object_selected_multiplayer`
**Family**: `object_state`
**Primary Role**: Inspect the runtime state of a particular object or set of objects.

**How It Is Used**
Use these conditions when progression depends on what a unit is doing or what happened to it. They are suitable for ability systems, escort logic, survival checks, target-tracking, interaction locks, and other cases where trigger logic must react to object state rather than raw area presence.

**Architecture Notes**
These conditions are most maintainable when the tracked objects are already registered by the surrounding system. If object identity is unstable, pair them with variable or creation logic that keeps references synchronized.

**Real Project Usage**
Observed 1 times in the scanned reference projects, primarily in GoKu RPG Project (1 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `modify_attribute`
- `remove_object`
- `task_object`
- `create_object`
- `change_variable`

**Reference Examples**
- `GoKu RPG Project -> Abilities\Hotkeys_Class.py:75`

## 27. Object Visible Multiplayer
**Method**: `object_visible_multiplayer`
**Family**: `object_state`
**Primary Role**: Inspect the runtime state of a particular object or set of objects.

**How It Is Used**
Use these conditions when progression depends on what a unit is doing or what happened to it. They are suitable for ability systems, escort logic, survival checks, target-tracking, interaction locks, and other cases where trigger logic must react to object state rather than raw area presence.

**Architecture Notes**
These conditions are most maintainable when the tracked objects are already registered by the surrounding system. If object identity is unstable, pair them with variable or creation logic that keeps references synchronized.

**Real Project Usage**
This parser feature is present in AoE2ScenarioParser but was not observed in the scanned local reference projects. Treat it as supported capability with no local canonical usage pattern yet.

**Common Pairings**
- `modify_attribute`
- `remove_object`
- `task_object`
- `create_object`
- `change_variable`

## 28. Object Has Action
**Method**: `object_has_action`
**Family**: `object_state`
**Primary Role**: Inspect the runtime state of a particular object or set of objects.

**How It Is Used**
Use these conditions when progression depends on what a unit is doing or what happened to it. They are suitable for ability systems, escort logic, survival checks, target-tracking, interaction locks, and other cases where trigger logic must react to object state rather than raw area presence.

**Architecture Notes**
These conditions are most maintainable when the tracked objects are already registered by the surrounding system. If object identity is unstable, pair them with variable or creation logic that keeps references synchronized.

**Real Project Usage**
This parser feature is present in AoE2ScenarioParser but was not observed in the scanned local reference projects. Treat it as supported capability with no local canonical usage pattern yet.

**Common Pairings**
- `modify_attribute`
- `remove_object`
- `task_object`
- `create_object`
- `change_variable`

## 29. Or
**Method**: `or_`
**Family**: `logic`
**Primary Role**: Compose smaller conditions into meaningful scenario rules.

**How It Is Used**
Use `or_` when a system should respond to several alternative paths without duplicating the full effect body. In a modular scenario this is the condition that keeps branch logic readable when different classes, buttons, or locations can all wake the same system.

**Architecture Notes**
Logical conditions work best when each input condition already has a clear responsibility. If the surrounding trigger is hard to read, the problem is usually poor system decomposition rather than the `and_` or `or_` call itself.

**Real Project Usage**
Observed 12 times in the scanned reference projects, primarily in LordsOfDiplomacy - Easy Mode (3 uses), GoKu RPG Project (9 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `variable_value`
- `timer`
- `objects_in_area`
- `researching_tech`
- `activate_trigger`

**Reference Examples**
- `LordsOfDiplomacy - Easy Mode -> Provinces\Capture_From_GAIA\Capture_Province_gaia\interrupt_capture.py:108`
- `LordsOfDiplomacy - Easy Mode -> Provinces\Capture_Province\interrupt_capture.py:146`
- `LordsOfDiplomacy - Easy Mode -> World\starting_ship.py:50`

## 30. AI Signal Multiplayer
**Method**: `ai_signal_multiplayer`
**Family**: `bridge`
**Primary Role**: Connect trigger logic to external systems such as XS, AI, or engine-side event channels.

**How It Is Used**
Use bridge conditions when the trigger layer should not own the final decision by itself. Instead of duplicating logic in triggers, the scenario can ask XS or another signal source for the answer and then let triggers handle orchestration, visuals, and follow-up state changes.

**Architecture Notes**
This family is most valuable when triggers stay thin and XS or signal-producing systems stay authoritative for the calculation. Avoid scattering bridge checks everywhere; centralize them around clear handoff points.

**Real Project Usage**
This parser feature is present in AoE2ScenarioParser but was not observed in the scanned local reference projects. Treat it as supported capability with no local canonical usage pattern yet.

**Common Pairings**
- `script_call`
- `change_variable`
- `activate_trigger`
- `deactivate_trigger`
- `send_chat`

## 54. Building Is Trading
**Method**: `building_is_trading`
**Family**: `object_state`
**Primary Role**: Inspect the runtime state of a particular object or set of objects.

**How It Is Used**
Use these conditions when progression depends on what a unit is doing or what happened to it. They are suitable for ability systems, escort logic, survival checks, target-tracking, interaction locks, and other cases where trigger logic must react to object state rather than raw area presence.

**Architecture Notes**
These conditions are most maintainable when the tracked objects are already registered by the surrounding system. If object identity is unstable, pair them with variable or creation logic that keeps references synchronized.

**Real Project Usage**
This parser feature is present in AoE2ScenarioParser but was not observed in the scanned local reference projects. Treat it as supported capability with no local canonical usage pattern yet.

**Common Pairings**
- `modify_attribute`
- `remove_object`
- `task_object`
- `create_object`
- `change_variable`

## 55. Display Timer Triggered
**Method**: `display_timer_triggered`
**Family**: `timing_state`
**Primary Role**: Provide the heartbeat and sequencing layer for trigger systems.

**How It Is Used**
Use these conditions when a system needs delays, loops, cooldowns, countdown completions, or stage sequencing. In real projects timer-style conditions are what make abilities pulse, phases advance, cutscenes tick, and temporary locks expire.

**Architecture Notes**
Timer conditions are usually not the whole gate by themselves. They become powerful when combined with variable, area, or script-call checks so the system can sequence complex behavior without turning into one giant trigger.

**Real Project Usage**
This parser feature is present in AoE2ScenarioParser but was not observed in the scanned local reference projects. Treat it as supported capability with no local canonical usage pattern yet.

**Common Pairings**
- `and_`
- `activate_trigger`
- `deactivate_trigger`
- `change_variable`
- `display_timer`
- `script_call`

## 56. Victory Timer
**Method**: `victory_timer`
**Family**: `timing_state`
**Primary Role**: Provide the heartbeat and sequencing layer for trigger systems.

**How It Is Used**
Use these conditions when a system needs delays, loops, cooldowns, countdown completions, or stage sequencing. In real projects timer-style conditions are what make abilities pulse, phases advance, cutscenes tick, and temporary locks expire.

**Architecture Notes**
Timer conditions are usually not the whole gate by themselves. They become powerful when combined with variable, area, or script-call checks so the system can sequence complex behavior without turning into one giant trigger.

**Real Project Usage**
This parser feature is present in AoE2ScenarioParser but was not observed in the scanned local reference projects. Treat it as supported capability with no local canonical usage pattern yet.

**Common Pairings**
- `and_`
- `activate_trigger`
- `deactivate_trigger`
- `change_variable`
- `display_timer`
- `script_call`

## 57. And
**Method**: `and_`
**Family**: `logic`
**Primary Role**: Compose smaller conditions into meaningful scenario rules.

**How It Is Used**
Use `and_` to collect independent subsystem checks into one explicit gate. In your projects it is what turns area checks, timer checks, variable state, and tech interactions into one readable system rule instead of many duplicated trigger variants.

**Architecture Notes**
Logical conditions work best when each input condition already has a clear responsibility. If the surrounding trigger is hard to read, the problem is usually poor system decomposition rather than the `and_` or `or_` call itself.

**Real Project Usage**
Observed 58 times in the scanned reference projects, primarily in LordsOfDiplomacy - Easy Mode (25 uses), GoKu RPG Project (33 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `variable_value`
- `timer`
- `objects_in_area`
- `researching_tech`
- `activate_trigger`

**Reference Examples**
- `LordsOfDiplomacy - Easy Mode -> Clerical_Actions\Actions\Adopt_Population\piety_cost.py:18`
- `LordsOfDiplomacy - Easy Mode -> cut_scenes.py:217`
- `LordsOfDiplomacy - Easy Mode -> cut_scenes.py:255`

## 75. Decision Triggered
**Method**: `decision_triggered`
**Family**: `timing_state`
**Primary Role**: Provide the heartbeat and sequencing layer for trigger systems.

**How It Is Used**
Use these conditions when a system needs delays, loops, cooldowns, countdown completions, or stage sequencing. In real projects timer-style conditions are what make abilities pulse, phases advance, cutscenes tick, and temporary locks expire.

**Architecture Notes**
Timer conditions are usually not the whole gate by themselves. They become powerful when combined with variable, area, or script-call checks so the system can sequence complex behavior without turning into one giant trigger.

**Real Project Usage**
This parser feature is present in AoE2ScenarioParser but was not observed in the scanned local reference projects. Treat it as supported capability with no local canonical usage pattern yet.

**Common Pairings**
- `and_`
- `activate_trigger`
- `deactivate_trigger`
- `change_variable`
- `display_timer`
- `script_call`

## 76. Object Attacked
**Method**: `object_attacked`
**Family**: `object_state`
**Primary Role**: Inspect the runtime state of a particular object or set of objects.

**How It Is Used**
Use these conditions when progression depends on what a unit is doing or what happened to it. They are suitable for ability systems, escort logic, survival checks, target-tracking, interaction locks, and other cases where trigger logic must react to object state rather than raw area presence.

**Architecture Notes**
These conditions are most maintainable when the tracked objects are already registered by the surrounding system. If object identity is unstable, pair them with variable or creation logic that keeps references synchronized.

**Real Project Usage**
This parser feature is present in AoE2ScenarioParser but was not observed in the scanned local reference projects. Treat it as supported capability with no local canonical usage pattern yet.

**Common Pairings**
- `modify_attribute`
- `remove_object`
- `task_object`
- `create_object`
- `change_variable`

## 77. Hero Power Cast
**Method**: `hero_power_cast`
**Family**: `bridge`
**Primary Role**: Connect trigger logic to external systems such as XS, AI, or engine-side event channels.

**How It Is Used**
Use bridge conditions when the trigger layer should not own the final decision by itself. Instead of duplicating logic in triggers, the scenario can ask XS or another signal source for the answer and then let triggers handle orchestration, visuals, and follow-up state changes.

**Architecture Notes**
This family is most valuable when triggers stay thin and XS or signal-producing systems stay authoritative for the calculation. Avoid scattering bridge checks everywhere; centralize them around clear handoff points.

**Real Project Usage**
This parser feature is present in AoE2ScenarioParser but was not observed in the scanned local reference projects. Treat it as supported capability with no local canonical usage pattern yet.

**Common Pairings**
- `script_call`
- `change_variable`
- `activate_trigger`
- `deactivate_trigger`
- `send_chat`

## 78. Compare Variables
**Method**: `compare_variables`
**Family**: `variables`
**Primary Role**: Implement scenario state machines and balanceable trigger state.

**How It Is Used**
Use this when the scenario state is relational rather than absolute. It is useful for comparing counters, rankings, mirrored player state, or progression tracks where the question is not 'did value hit X' but 'which value is greater or whether two states match.'

**Architecture Notes**
This family only scales if variable ownership is centralized. Use a registry such as `aoe_variables.py` so systems read and write named values instead of inventing IDs locally.

**Real Project Usage**
This parser feature is present in AoE2ScenarioParser but was not observed in the scanned local reference projects. Treat it as supported capability with no local canonical usage pattern yet.

**Common Pairings**
- `change_variable`
- `modify_variable_by_variable`
- `timer`
- `activate_trigger`
- `deactivate_trigger`

## 79. Trigger Active
**Method**: `trigger_active`
**Family**: `timing_state`
**Primary Role**: Provide the heartbeat and sequencing layer for trigger systems.

**How It Is Used**
Use these conditions when a system needs delays, loops, cooldowns, countdown completions, or stage sequencing. In real projects timer-style conditions are what make abilities pulse, phases advance, cutscenes tick, and temporary locks expire.

**Architecture Notes**
Timer conditions are usually not the whole gate by themselves. They become powerful when combined with variable, area, or script-call checks so the system can sequence complex behavior without turning into one giant trigger.

**Real Project Usage**
This parser feature is present in AoE2ScenarioParser but was not observed in the scanned local reference projects. Treat it as supported capability with no local canonical usage pattern yet.

**Common Pairings**
- `and_`
- `activate_trigger`
- `deactivate_trigger`
- `change_variable`
- `display_timer`
- `script_call`

## 80. Local Tech Researched
**Method**: `local_tech_researched`
**Family**: `economy_progress`
**Primary Role**: Gate logic on progression, economy, technology, or threshold state.

**How It Is Used**
Use these conditions to turn the trigger graph into a progression system. They work as prerequisites for quests, unlocks, upgrade paths, resource thresholds, and UI-like technology buttons. The surrounding trigger system usually checks one of these conditions first and only then applies the effects that mutate state or expose the next step.

**Architecture Notes**
This family becomes much easier to tune when the threshold values live in dictionaries or config modules instead of being hardcoded inline in trigger builder functions.

**Real Project Usage**
This parser feature is present in AoE2ScenarioParser but was not observed in the scanned local reference projects. Treat it as supported capability with no local canonical usage pattern yet.

**Common Pairings**
- `and_`
- `change_variable`
- `activate_trigger`
- `research_technology`
- `modify_resource`
- `enable_disable_technology`
