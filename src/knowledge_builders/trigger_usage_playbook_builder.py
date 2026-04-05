from typing import Any, Dict, List


CONDITION_FAMILY_DATA: Dict[str, Dict[str, Any]] = {
    "null": {
        "primary_role": "Sentinel or placeholder condition.",
        "how_it_is_used": "Use this only when a trigger needs a syntactic placeholder or when tooling expects a condition object but the design does not require a real gate. It is not a gameplay condition and should not be treated as meaningful scenario logic.",
        "architecture_notes": "If this appears in production trigger generation, it usually means the real gate lives elsewhere or the system is still scaffolding its trigger graph.",
        "common_pairings": ["activate_trigger", "deactivate_trigger"],
    },
    "movement_area": {
        "primary_role": "Detect that a specific object reached a designed interaction point.",
        "how_it_is_used": "Use these conditions when the scenario logic depends on a named unit, hero, or token physically entering a destination or reaching another object. In real projects they sit near quest, boss, teleport, or handoff systems where one tracked object must arrive somewhere before the next trigger stage unlocks.",
        "architecture_notes": "This family is strongest when the tracked object is stable and unique. If the system cares about any qualifying unit rather than one known unit, area-count conditions are usually a better fit.",
        "common_pairings": ["activate_trigger", "change_variable", "teleport_object", "send_chat"],
    },
    "area_population": {
        "primary_role": "Treat map areas as gameplay sensors.",
        "how_it_is_used": "These conditions turn a rectangle on the map into a reusable detector. They are commonly used for portals, pressure plates, interaction zones, quest regions, and ability hit or entry zones. In large projects they usually sit at the front of a modular system and decide whether the rest of the chain should run.",
        "architecture_notes": "Use area conditions when the map itself is part of the gameplay API. Keep the coordinates centralized or derived from shared data so balancing or map edits do not require rewriting trigger logic.",
        "common_pairings": ["and_", "or_", "activate_trigger", "deactivate_trigger", "play_sound", "change_view"],
    },
    "object_state": {
        "primary_role": "Inspect the runtime state of a particular object or set of objects.",
        "how_it_is_used": "Use these conditions when progression depends on what a unit is doing or what happened to it. They are suitable for ability systems, escort logic, survival checks, target-tracking, interaction locks, and other cases where trigger logic must react to object state rather than raw area presence.",
        "architecture_notes": "These conditions are most maintainable when the tracked objects are already registered by the surrounding system. If object identity is unstable, pair them with variable or creation logic that keeps references synchronized.",
        "common_pairings": ["modify_attribute", "remove_object", "task_object", "create_object", "change_variable"],
    },
    "economy_progress": {
        "primary_role": "Gate logic on progression, economy, technology, or threshold state.",
        "how_it_is_used": "Use these conditions to turn the trigger graph into a progression system. They work as prerequisites for quests, unlocks, upgrade paths, resource thresholds, and UI-like technology buttons. The surrounding trigger system usually checks one of these conditions first and only then applies the effects that mutate state or expose the next step.",
        "architecture_notes": "This family becomes much easier to tune when the threshold values live in dictionaries or config modules instead of being hardcoded inline in trigger builder functions.",
        "common_pairings": ["and_", "change_variable", "activate_trigger", "research_technology", "modify_resource", "enable_disable_technology"],
    },
    "timing_state": {
        "primary_role": "Provide the heartbeat and sequencing layer for trigger systems.",
        "how_it_is_used": "Use these conditions when a system needs delays, loops, cooldowns, countdown completions, or stage sequencing. In real projects timer-style conditions are what make abilities pulse, phases advance, cutscenes tick, and temporary locks expire.",
        "architecture_notes": "Timer conditions are usually not the whole gate by themselves. They become powerful when combined with variable, area, or script-call checks so the system can sequence complex behavior without turning into one giant trigger.",
        "common_pairings": ["and_", "activate_trigger", "deactivate_trigger", "change_variable", "display_timer", "script_call"],
    },
    "bridge": {
        "primary_role": "Connect trigger logic to external systems such as XS, AI, or engine-side event channels.",
        "how_it_is_used": "Use bridge conditions when the trigger layer should not own the final decision by itself. Instead of duplicating logic in triggers, the scenario can ask XS or another signal source for the answer and then let triggers handle orchestration, visuals, and follow-up state changes.",
        "architecture_notes": "This family is most valuable when triggers stay thin and XS or signal-producing systems stay authoritative for the calculation. Avoid scattering bridge checks everywhere; centralize them around clear handoff points.",
        "common_pairings": ["script_call", "change_variable", "activate_trigger", "deactivate_trigger", "send_chat"],
    },
    "variables": {
        "primary_role": "Implement scenario state machines and balanceable trigger state.",
        "how_it_is_used": "Variable conditions are the backbone of modular trigger projects. They are used for cooldown flags, quest steps, class state, per-player progression, phase markers, and bridge state shared with XS. In practice they let a scenario behave like a small application with explicit state instead of a pile of ad hoc trigger checks.",
        "architecture_notes": "This family only scales if variable ownership is centralized. Use a registry such as `aoe_variables.py` so systems read and write named values instead of inventing IDs locally.",
        "common_pairings": ["change_variable", "modify_variable_by_variable", "timer", "activate_trigger", "deactivate_trigger"],
    },
    "diplomacy": {
        "primary_role": "Gate logic on relationship state between players.",
        "how_it_is_used": "Use diplomacy conditions for treaty systems, alliance actions, conversion of neutrality states into gameplay branches, and scenarios where political state is itself the mechanic. This family usually belongs in a dedicated diplomacy module instead of being mixed into unrelated combat logic.",
        "architecture_notes": "Diplomacy systems become readable when the trigger layer separates the check, the state transition, and the user-facing feedback into different triggers or helper functions.",
        "common_pairings": ["change_diplomacy", "send_chat", "play_sound", "activate_trigger"],
    },
    "logic": {
        "primary_role": "Compose smaller conditions into meaningful scenario rules.",
        "how_it_is_used": "Use logical conditions when one gameplay event should only fire if several different subsystems agree. In real projects they stop the trigger graph from exploding into duplicated variants by collecting area, timer, variable, and technology checks into one gate.",
        "architecture_notes": "Logical conditions work best when each input condition already has a clear responsibility. If the surrounding trigger is hard to read, the problem is usually poor system decomposition rather than the `and_` or `or_` call itself.",
        "common_pairings": ["variable_value", "timer", "objects_in_area", "researching_tech", "activate_trigger"],
    },
}


CONDITION_FAMILY_BY_NAME: Dict[str, str] = {
    "none": "null",
    "bring_object_to_area": "movement_area",
    "bring_object_to_object": "movement_area",
    "own_objects": "area_population",
    "own_fewer_objects": "area_population",
    "objects_in_area": "area_population",
    "destroy_object": "object_state",
    "capture_object": "object_state",
    "accumulate_attribute": "economy_progress",
    "research_technology": "economy_progress",
    "timer": "timing_state",
    "object_selected": "object_state",
    "ai_signal": "bridge",
    "player_defeated": "timing_state",
    "object_has_target": "object_state",
    "object_visible": "object_state",
    "object_not_visible": "object_state",
    "researching_tech": "economy_progress",
    "units_garrisoned": "object_state",
    "difficulty_level": "economy_progress",
    "chance": "economy_progress",
    "technology_state": "economy_progress",
    "variable_value": "variables",
    "object_hp": "object_state",
    "diplomacy_state": "diplomacy",
    "script_call": "bridge",
    "object_selected_multiplayer": "object_state",
    "object_visible_multiplayer": "object_state",
    "object_has_action": "object_state",
    "or_": "logic",
    "ai_signal_multiplayer": "bridge",
    "building_is_trading": "object_state",
    "display_timer_triggered": "timing_state",
    "victory_timer": "timing_state",
    "and_": "logic",
    "decision_triggered": "timing_state",
    "object_attacked": "object_state",
    "hero_power_cast": "bridge",
    "compare_variables": "variables",
    "trigger_active": "timing_state",
    "local_tech_researched": "economy_progress",
}


CONDITION_OVERRIDES: Dict[str, Dict[str, Any]] = {
    "variable_value": {
        "how_it_is_used": "This is the core trigger-state gate in your reference projects. It is used to represent cooldown flags, quest stages, class-state toggles, respawn permissions, and other per-player progression markers. In practice, a large modular scenario keeps the real gameplay state in variables and uses `variable_value` to decide which branch of the trigger graph is currently legal.",
        "architecture_notes": "If an agent is building a scalable scenario, this should usually be one of the first conditions it reaches for after creating a central variable registry. The condition is especially strong when combined with dictionary-driven balance data and with `change_variable` effects that advance state explicitly.",
        "common_pairings": ["change_variable", "timer", "activate_trigger", "deactivate_trigger", "script_call"],
    },
    "timer": {
        "how_it_is_used": "This is the heartbeat condition in your projects. It drives cooldown expiration, periodic mana or status ticks, cutscene sequencing, staged tutorials, and delayed system reactivation. It is not just a delay helper; it is the mechanism that turns separate trigger modules into time-aware systems.",
        "architecture_notes": "A timer gate is usually most useful when paired with another check that says why the trigger should still matter. That keeps loops and cooldown triggers from firing blindly after the owning system has already moved on.",
        "common_pairings": ["variable_value", "and_", "activate_trigger", "deactivate_trigger", "display_timer"],
    },
    "script_call": {
        "how_it_is_used": "Use this when the final decision should come from XS instead of from the trigger layer itself. In your projects it appears at bridge points where the trigger graph asks XS for a computed answer, then reacts with trigger-side orchestration, UI, or object manipulation. It is the cleanest way to keep calculations and trigger presentation separated.",
        "architecture_notes": "This condition is strongest when the XS function has a clear, stable responsibility and the surrounding trigger owns only the reaction. If the trigger also recomputes the same logic locally, the bridge is being used poorly.",
        "common_pairings": ["script_call", "change_variable", "activate_trigger", "deactivate_trigger", "send_chat"],
    },
    "objects_in_area": {
        "how_it_is_used": "This is the most reusable zone-sensor condition in the reference projects. It is used for teleports, interaction pads, boss areas, tutorial spaces, and ability-driven regions. The condition turns a rectangular area into a modular gameplay boundary that other systems can reuse without knowing the whole map script.",
        "architecture_notes": "For maintainable scenarios, area coordinates should be treated as data. That lets the same trigger architecture survive balancing passes or map revisions without rewriting the surrounding logic modules.",
        "common_pairings": ["and_", "or_", "activate_trigger", "change_view", "teleport_object"],
    },
    "accumulate_attribute": {
        "how_it_is_used": "Use this when a system unlocks on a threshold rather than a one-time event. In project-scale scenarios it works well for economy gates, score-like progression, custom currencies, or persistent class-resource systems where the number matters more than any single moment of gain.",
    },
    "researching_tech": {
        "how_it_is_used": "Your reference projects use this as a trigger-friendly button press or menu interaction. The scenario exposes technologies as player actions, then `researching_tech` detects that interaction and hands control to the modular trigger system that performs the actual gameplay logic.",
        "architecture_notes": "This pattern is valuable because it gives players a clean UI surface while keeping the real logic in triggers and XS. It is one of the clearest examples of data-driven scenario interfaces.",
        "common_pairings": ["change_technology_location", "change_technology_cost", "activate_trigger", "deactivate_trigger", "send_chat"],
    },
    "and_": {
        "how_it_is_used": "Use `and_` to collect independent subsystem checks into one explicit gate. In your projects it is what turns area checks, timer checks, variable state, and tech interactions into one readable system rule instead of many duplicated trigger variants.",
    },
    "or_": {
        "how_it_is_used": "Use `or_` when a system should respond to several alternative paths without duplicating the full effect body. In a modular scenario this is the condition that keeps branch logic readable when different classes, buttons, or locations can all wake the same system.",
    },
    "compare_variables": {
        "how_it_is_used": "Use this when the scenario state is relational rather than absolute. It is useful for comparing counters, rankings, mirrored player state, or progression tracks where the question is not 'did value hit X' but 'which value is greater or whether two states match.'",
    },
}


EFFECT_FAMILY_DATA: Dict[str, Dict[str, Any]] = {
    "orchestration": {
        "primary_role": "Shape the trigger graph itself.",
        "how_it_is_used": "Use this family to control which trigger modules are alive at a given moment. In large scenarios these effects are the glue between systems: one trigger finishes its responsibility, then activates the next stage and deactivates the old loop or guard trigger.",
        "architecture_notes": "Good trigger architecture treats orchestration as explicit. Instead of one giant trigger trying to do everything, orchestration effects move control between small, named triggers that each own one slice of behavior.",
        "common_pairings": ["timer", "variable_value", "and_", "script_call"],
    },
    "feedback": {
        "primary_role": "Explain system state to the player through UI, camera, text, or sound.",
        "how_it_is_used": "Use these effects when a trigger change should be legible to players. Real projects rely on them to teach mechanics, confirm interactions, sell class abilities, and make hidden state transitions visible without exposing internal variable logic directly.",
        "architecture_notes": "Feedback effects should react to meaningful state changes, not replace them. A scenario stays readable when feedback follows a real system event rather than becoming the event itself.",
        "common_pairings": ["activate_trigger", "change_variable", "objects_in_area", "researching_tech"],
    },
    "object_control": {
        "primary_role": "Create, remove, move, or command units and objects in the world.",
        "how_it_is_used": "Use this family when the trigger system needs to directly manipulate the playable world. It covers spawning units, issuing orders, moving objects, removing temporary entities, and forcing scripted interactions that the normal AI or player input should not own.",
        "architecture_notes": "World-control effects become much easier to balance when the object IDs, areas, and per-level values come from data modules. Keep world mutation code thin and let configuration determine what gets spawned or moved.",
        "common_pairings": ["objects_in_area", "variable_value", "timer", "play_sound", "change_view"],
    },
    "stat_mutation": {
        "primary_role": "Change runtime object or class stats in response to scenario logic.",
        "how_it_is_used": "Use this family for buffs, debuffs, scaling systems, class growth, difficulty adjustments, and temporary ability states. In your reference projects stat mutation is one of the main ways triggers turn variables and timers into visible gameplay consequences.",
        "architecture_notes": "This family is where data-driven balancing matters most. If numbers are spread through trigger builders, later balance passes become expensive and error-prone. Keep the values in dictionaries and let trigger code only apply them.",
        "common_pairings": ["variable_value", "change_variable", "timer", "script_call", "modify_resource"],
    },
    "resource_variable": {
        "primary_role": "Move numbers between scenario state, player resources, and trigger-controlled counters.",
        "how_it_is_used": "Use these effects when the scenario behaves like a rule system with explicit state transitions. They are responsible for cooldown counters, mana-like systems, custom resources, progression markers, and any mechanic where one trigger must write a value that another trigger later reads.",
        "architecture_notes": "Central registries and data-driven naming are critical here. Without them, a large scenario turns into a collision-prone mess of numeric IDs and unclear write paths.",
        "common_pairings": ["variable_value", "compare_variables", "timer", "activate_trigger", "modify_attribute"],
    },
    "diplomacy_ai": {
        "primary_role": "Change player relationships or communicate with AI-facing systems.",
        "how_it_is_used": "Use this family for treaties, factions, scripted political actions, AI coordination, or trigger-to-AI handoffs. The effect is usually part of a dedicated diplomacy or encounter module rather than a generic combat trigger.",
        "architecture_notes": "Keep diplomacy and AI signaling explicit. Scenarios become easier to reason about when relationship changes are grouped in one subsystem instead of hidden in many unrelated triggers.",
        "common_pairings": ["diplomacy_state", "researching_tech", "send_chat", "play_sound"],
    },
    "tech_edit": {
        "primary_role": "Turn technologies into a scenario-controlled interface and progression surface.",
        "how_it_is_used": "Use these effects when technologies are serving as buttons, unlock panels, class menus, or progression displays rather than only vanilla researches. Your projects use this family to move, rename, cost, and gate technologies so the scenario can expose custom systems through the game UI.",
        "architecture_notes": "This family is strongest when tech metadata comes from data dictionaries. That keeps UI and balancing changes out of the trigger orchestration code.",
        "common_pairings": ["researching_tech", "technology_state", "send_chat", "display_timer", "activate_trigger"],
    },
    "identity_visibility": {
        "primary_role": "Change what players see and how objects or players are labeled.",
        "how_it_is_used": "Use this family for polish, illusion, staged reveals, and scenario-controlled identity changes. It supports systems where the same gameplay object changes its name, caption, color, or apparent ownership based on scenario state.",
        "architecture_notes": "Visibility and identity effects are best used as presentation layers on top of real state changes. Keep the authoritative state in variables or object data and let these effects communicate that state.",
        "common_pairings": ["change_variable", "send_chat", "play_sound", "change_view"],
    },
    "interaction_control": {
        "primary_role": "Temporarily allow or forbid player interaction with units or objects.",
        "how_it_is_used": "Use this family for cutscenes, stuns, protected summons, invulnerability windows, interface locking, or scripted sequences where players should not be able to interfere with the system at the wrong time.",
        "architecture_notes": "Interaction locks are safest when paired with clear activation and cleanup triggers. The biggest failure mode is forgetting to re-enable the thing that was disabled.",
        "common_pairings": ["timer", "activate_trigger", "deactivate_trigger", "play_sound"],
    },
    "persistence": {
        "primary_role": "Store scenario-side state in key-value or decision systems.",
        "how_it_is_used": "Use this family when the scenario wants a persistence-like or indexed-state layer that is not just one flat variable registry. It is useful for data-driven systems, loot or inventory state, and situations where triggers need to create or query structured records.",
        "architecture_notes": "This family matters most when the rest of the project is already modular. If the data model is unclear, adding persistence effects will only make the system harder to reason about.",
        "common_pairings": ["variable_value", "compare_variables", "create_decision", "load_key_value", "store_key_value"],
    },
    "special": {
        "primary_role": "Handle niche scenario actions that do not fit the main families.",
        "how_it_is_used": "Use these only when the scenario specifically needs their engine behavior. They are valid tools, but they should usually appear inside a narrow subsystem rather than as general-purpose building blocks.",
        "architecture_notes": "Agents should check whether a more common family already solves the task before choosing one of these effects.",
        "common_pairings": ["send_chat", "play_sound", "activate_trigger"],
    },
}


EFFECT_FAMILY_BY_NAME: Dict[str, str] = {
    "change_diplomacy": "diplomacy_ai",
    "research_technology": "tech_edit",
    "send_chat": "feedback",
    "play_sound": "feedback",
    "tribute": "resource_variable",
    "unlock_gate": "object_control",
    "lock_gate": "object_control",
    "activate_trigger": "orchestration",
    "deactivate_trigger": "orchestration",
    "ai_script_goal": "diplomacy_ai",
    "create_object": "object_control",
    "task_object": "object_control",
    "declare_victory": "special",
    "kill_object": "object_control",
    "remove_object": "object_control",
    "change_view": "feedback",
    "unload": "object_control",
    "change_ownership": "diplomacy_ai",
    "patrol": "object_control",
    "display_instructions": "feedback",
    "clear_instructions": "feedback",
    "freeze_object": "interaction_control",
    "use_advanced_buttons": "special",
    "damage_object": "stat_mutation",
    "place_foundation": "object_control",
    "change_object_name": "identity_visibility",
    "change_object_hp": "stat_mutation",
    "change_object_attack": "stat_mutation",
    "stop_object": "object_control",
    "attack_move": "object_control",
    "change_object_armor": "stat_mutation",
    "change_object_range": "stat_mutation",
    "change_object_speed": "stat_mutation",
    "heal_object": "stat_mutation",
    "teleport_object": "object_control",
    "change_object_stance": "interaction_control",
    "display_timer": "feedback",
    "enable_disable_object": "interaction_control",
    "enable_disable_technology": "tech_edit",
    "change_object_cost": "stat_mutation",
    "set_player_visibility": "identity_visibility",
    "change_object_icon": "identity_visibility",
    "replace_object": "object_control",
    "change_object_description": "identity_visibility",
    "change_player_name": "identity_visibility",
    "change_train_location": "tech_edit",
    "change_research_location": "tech_edit",
    "change_civilization_name": "identity_visibility",
    "create_garrisoned_object": "object_control",
    "acknowledge_ai_signal": "diplomacy_ai",
    "modify_attribute": "stat_mutation",
    "modify_resource": "resource_variable",
    "modify_resource_by_variable": "resource_variable",
    "set_building_gather_point": "object_control",
    "script_call": "resource_variable",
    "change_variable": "resource_variable",
    "clear_timer": "orchestration",
    "change_object_player_color": "identity_visibility",
    "change_object_civilization_name": "identity_visibility",
    "change_object_player_name": "identity_visibility",
    "disable_unit_targeting": "interaction_control",
    "enable_unit_targeting": "interaction_control",
    "change_technology_cost": "tech_edit",
    "change_technology_research_time": "tech_edit",
    "change_technology_name": "tech_edit",
    "change_technology_description": "tech_edit",
    "enable_technology_stacking": "tech_edit",
    "disable_technology_stacking": "tech_edit",
    "acknowledge_multiplayer_ai_signal": "diplomacy_ai",
    "disable_object_selection": "interaction_control",
    "enable_object_selection": "interaction_control",
    "change_color_mood": "identity_visibility",
    "add_train_location": "tech_edit",
    "change_object_caption": "identity_visibility",
    "change_object_visibility": "identity_visibility",
    "change_player_color": "identity_visibility",
    "change_technology_hotkey": "tech_edit",
    "change_technology_icon": "tech_edit",
    "change_technology_location": "tech_edit",
    "count_units_into_variable": "resource_variable",
    "create_decision": "persistence",
    "create_object_armor": "stat_mutation",
    "create_object_attack": "stat_mutation",
    "delete_key": "persistence",
    "disable_object_deletion": "interaction_control",
    "disable_unit_attackable": "interaction_control",
    "enable_object_deletion": "interaction_control",
    "enable_unit_attackable": "interaction_control",
    "initiate_research": "tech_edit",
    "load_key_value": "persistence",
    "modify_attribute_by_variable": "stat_mutation",
    "modify_attribute_for_class": "stat_mutation",
    "modify_object_attribute": "stat_mutation",
    "modify_object_attribute_by_variable": "stat_mutation",
    "modify_variable_by_attribute": "resource_variable",
    "modify_variable_by_resource": "resource_variable",
    "modify_variable_by_variable": "resource_variable",
    "none": "special",
    "research_local_technology": "tech_edit",
    "set_object_cost": "stat_mutation",
    "store_key_value": "persistence",
    "train_unit": "object_control",
}


EFFECT_OVERRIDES: Dict[str, Dict[str, Any]] = {
    "modify_attribute": {
        "how_it_is_used": "This is one of the main gameplay mutation effects in your reference projects. It is used to turn scenario state into stat changes: buffs, debuffs, class scaling, temporary transformations, respawn adjustments, and balance-driven runtime tuning. It is the clearest example of why the trigger layer should read values from dictionaries instead of burying numbers inside long builder functions.",
        "architecture_notes": "An agent should almost always look for the data source behind a `modify_attribute` call. The call itself is usually the endpoint of a larger data-driven design, not the place where balance truth should live.",
        "common_pairings": ["variable_value", "timer", "change_variable", "script_call", "modify_resource"],
    },
    "activate_trigger": {
        "how_it_is_used": "This is the main orchestration handoff in your projects. It wakes the next slice of the system after the current trigger has finished checking inputs or applying one step of behavior. Large modular scenarios depend on it to keep systems readable because it lets each trigger own a single responsibility and then pass control onward.",
    },
    "deactivate_trigger": {
        "how_it_is_used": "Use this to close loops, consume one-shot buttons, and retire temporary system states. In real projects it is what prevents old guards, previous phases, or expired cooldown triggers from staying alive after the system has moved on.",
    },
    "change_variable": {
        "how_it_is_used": "This is the write side of the scenario state machine. It advances quests, flips cooldown flags, stores per-player state, and records what later triggers should see through `variable_value` or other variable conditions. In practice this is one of the most important effects for keeping a scenario modular and explicit.",
        "architecture_notes": "If the variable registry is clean, `change_variable` becomes a readable transition log for the whole scenario. If the registry is chaotic, this effect becomes a source of hidden coupling.",
        "common_pairings": ["variable_value", "compare_variables", "activate_trigger", "deactivate_trigger", "modify_attribute"],
    },
    "script_call": {
        "how_it_is_used": "This effect is the trigger-to-XS execution bridge. Your projects use it when triggers should hand off computed work, object processing, or custom logic to XS, then continue with trigger-side orchestration or presentation. It keeps heavy logic out of the trigger layer while still allowing triggers to own sequencing and player feedback.",
        "architecture_notes": "Use this when XS is the right home for calculation or object iteration. Do not use it as a substitute for simple trigger-side work that is clearer without a bridge.",
        "common_pairings": ["script_call", "variable_value", "activate_trigger", "deactivate_trigger", "send_chat"],
    },
    "modify_resource": {
        "how_it_is_used": "Use this to implement mana-like systems, costs, custom progression currencies, and player-facing economy effects. In your projects it often works alongside variable systems so one number controls internal logic while another number is exposed to the player as a resource-like mechanic.",
    },
    "play_sound": {
        "how_it_is_used": "This is the audio confirmation layer for trigger systems. It is used when abilities fire, interactions succeed, cutscenes advance, or warnings need to feel immediate. In modular designs it usually sits at the end of a successful state transition, not at the front of the check.",
    },
    "send_chat": {
        "how_it_is_used": "Use this when a system needs explicit textual confirmation, instruction, or narrative feedback. Your reference projects use it to expose hidden scenario state to players without requiring them to understand internal variable logic.",
    },
    "remove_object": {
        "how_it_is_used": "Use this to clean up temporary world state after an interaction, effect, summon, or scripted stage completes. In real projects it keeps the map and system state synchronized by removing entities that should no longer participate in the scenario.",
    },
    "task_object": {
        "how_it_is_used": "This is the core effect for scripted orders. It turns triggers into directors that can force objects toward a target, area, or action without waiting for player or AI initiative. It is especially useful in teleports, summons, escorts, and staged encounters.",
    },
    "create_object": {
        "how_it_is_used": "Use this to materialize system state into world state. It is the spawn point for summons, markers, temporary helpers, encounter units, and other entities that only exist because the trigger system says they should.",
    },
    "teleport_object": {
        "how_it_is_used": "Use this when spatial repositioning itself is the mechanic. In projects with portals, scripted movement, or ability travel, teleportation is usually guarded by area or variable checks and paired with cleanup and feedback so the move feels intentional rather than abrupt.",
    },
    "display_timer": {
        "how_it_is_used": "This is the player-facing surface for time-based systems. Use it when cooldowns, objectives, waves, or phases should be visible instead of hidden inside internal timer conditions. It is also one of the best tools for high-frequency global-event notification because it is hard to miss and can keep recurring event state visible without relying on chat.",
    },
    "display_instructions": {
        "how_it_is_used": "Use this for strong shared announcements that should be seen by all players without recurring constantly. It works best for lower-frequency global events, major warnings, tutorials, and milestone messages where a single strong broadcast is better than repeated notification spam.",
    },
    "change_technology_location": {
        "how_it_is_used": "Your reference projects use technology relocation as part of a custom interface pattern. The technology is not just a normal research; it becomes a positioned button or menu element inside a scenario-controlled UI.",
    },
    "send_chat": {
        "how_it_is_used": "Use this when a system needs explicit textual confirmation, instruction, or narrative feedback. Your reference projects use it to expose hidden scenario state to players without requiring them to understand internal variable logic. It is also useful for debugging and for player-specific communication because it can be sent to one selected player instead of to everyone.",
    },
    "change_view": {
        "how_it_is_used": "Use this when the system needs to direct attention to a location or event. It is especially good as a support effect for player-specific notification because the camera move can target a chosen player and make the event harder to miss.",
    },
}


EFFECT_COMMUNICATION_DEFAULT = {
    "audience_scope": "varies_by_parameters",
    "attention_strength": "medium",
    "recommended_frequency": "depends_on_system",
    "best_use": "Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.",
}


EFFECT_COMMUNICATION_OVERRIDES: Dict[str, Dict[str, str]] = {
    "display_timer": {
        "audience_scope": "all_players_visible",
        "attention_strength": "high",
        "recommended_frequency": "high_frequency",
        "best_use": "Best for recurring or high-frequency global-event notification where players need a visible shared event banner or countdown-style message.",
    },
    "display_instructions": {
        "audience_scope": "all_players_visible",
        "attention_strength": "high",
        "recommended_frequency": "low_frequency",
        "best_use": "Best for rare, important, shared announcements that should reach everyone without constantly flooding the screen.",
    },
    "send_chat": {
        "audience_scope": "selected_player_only",
        "attention_strength": "low",
        "recommended_frequency": "debug_or_player_specific",
        "best_use": "Best for debugging, private player hints, or low-priority player-specific communication that does not need to be broadcast to everyone.",
    },
    "change_view": {
        "audience_scope": "selected_player_or_targeted_players",
        "attention_strength": "high",
        "recommended_frequency": "event_driven",
        "best_use": "Best as a targeted support effect when a player must notice where an event is happening right now.",
    },
}


def _build_real_usage_summary(usage_entry: Dict[str, Any]) -> str:
    if usage_entry["usage_count"] <= 0:
        return "This parser feature is present in AoE2ScenarioParser but was not observed in the scanned local reference projects. Treat it as supported capability with no local canonical usage pattern yet."

    project_bits = []
    for summary in usage_entry["project_summaries"][:3]:
        project_bits.append(
            f"{summary['project_title']} ({summary['usage_count']} uses)"
        )
    projects_text = ", ".join(project_bits)
    return (
        f"Observed {usage_entry['usage_count']} times in the scanned reference projects, primarily in {projects_text}. "
        "Use the example paths as the first place to inspect the surrounding trigger architecture."
    )


def _build_examples(usage_entry: Dict[str, Any]) -> List[str]:
    examples = []
    for example in usage_entry["examples"][:3]:
        examples.append(
            f"{example['project_title']} -> {example['path']}:{example['line_number']}"
        )
    return examples


def _enrich_entries(
    knowledge_entries: List[Dict[str, Any]],
    usage_entries: List[Dict[str, Any]],
    family_by_name: Dict[str, str],
    family_data: Dict[str, Dict[str, Any]],
    overrides: Dict[str, Dict[str, Any]],
    id_key: str,
) -> List[Dict[str, Any]]:
    usage_map = {entry["internal_name"]: entry for entry in usage_entries}
    enriched = []

    for knowledge in knowledge_entries:
        name = knowledge["internal_name"]
        usage = usage_map[name]
        family = family_by_name[name]
        base = family_data[family]
        override = overrides.get(name, {})

        enriched.append(
            {
                id_key: knowledge[id_key],
                "internal_name": name,
                "display_name": knowledge["display_name"],
                "family": family,
                "primary_role": override.get("primary_role", base["primary_role"]),
                "how_it_is_used": override.get("how_it_is_used", base["how_it_is_used"]),
                "architecture_notes": override.get(
                    "architecture_notes", base["architecture_notes"]
                ),
                "common_pairings": override.get(
                    "common_pairings", base["common_pairings"]
                ),
                "real_project_usage_summary": _build_real_usage_summary(usage),
                "observed_usage_count": usage["usage_count"],
                "used_in_projects": usage["used_in_projects"],
                "reference_examples": _build_examples(usage),
            }
        )

    return enriched


def build_condition_playbook(
    condition_entries: List[Dict[str, Any]],
    usage_entries: List[Dict[str, Any]],
) -> List[Dict[str, Any]]:
    return _enrich_entries(
        condition_entries,
        usage_entries,
        CONDITION_FAMILY_BY_NAME,
        CONDITION_FAMILY_DATA,
        CONDITION_OVERRIDES,
        "condition_id",
    )


def build_effect_playbook(
    effect_entries: List[Dict[str, Any]],
    usage_entries: List[Dict[str, Any]],
) -> List[Dict[str, Any]]:
    entries = _enrich_entries(
        effect_entries,
        usage_entries,
        EFFECT_FAMILY_BY_NAME,
        EFFECT_FAMILY_DATA,
        EFFECT_OVERRIDES,
        "effect_id",
    )
    for entry in entries:
        semantics = dict(EFFECT_COMMUNICATION_DEFAULT)
        semantics.update(EFFECT_COMMUNICATION_OVERRIDES.get(entry["internal_name"], {}))
        entry.update(semantics)
    return entries
