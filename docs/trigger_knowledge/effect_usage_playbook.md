# Trigger Effect Usage Playbook
Generated file. Do not hand-edit; run tools/build_trigger_knowledge.py.

## 1. Change Diplomacy
**Method**: `change_diplomacy`
**Family**: `diplomacy_ai`
**Primary Role**: Change player relationships or communicate with AI-facing systems.

**How It Is Used**
Use this family for treaties, factions, scripted political actions, AI coordination, or trigger-to-AI handoffs. The effect is usually part of a dedicated diplomacy or encounter module rather than a generic combat trigger.

**Architecture Notes**
Keep diplomacy and AI signaling explicit. Scenarios become easier to reason about when relationship changes are grouped in one subsystem instead of hidden in many unrelated triggers.

**Real Project Usage**
Observed 11 times in the scanned reference projects, primarily in LordsOfDiplomacy - Easy Mode (10 uses), Hide_and_Seek (1 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `diplomacy_state`
- `researching_tech`
- `send_chat`
- `play_sound`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

**Reference Examples**
- `LordsOfDiplomacy - Easy Mode -> Diplomacy\Actions\Alliance\Helper_Functions\form_alliance.py:40`
- `LordsOfDiplomacy - Easy Mode -> Diplomacy\Actions\Alliance\Helper_Functions\form_alliance.py:45`
- `LordsOfDiplomacy - Easy Mode -> Diplomacy\Actions\Neutral\Helper_Functions\form_neutral.py:43`

## 2. Research Technology
**Method**: `research_technology`
**Family**: `tech_edit`
**Primary Role**: Turn technologies into a scenario-controlled interface and progression surface.

**How It Is Used**
Use these effects when technologies are serving as buttons, unlock panels, class menus, or progression displays rather than only vanilla researches. Your projects use this family to move, rename, cost, and gate technologies so the scenario can expose custom systems through the game UI.

**Architecture Notes**
This family is strongest when tech metadata comes from data dictionaries. That keeps UI and balancing changes out of the trigger orchestration code.

**Real Project Usage**
Observed 5 times in the scanned reference projects, primarily in LordsOfDiplomacy - Easy Mode (1 uses), GoKu RPG Project (2 uses), Hide_and_Seek (2 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `researching_tech`
- `technology_state`
- `send_chat`
- `display_timer`
- `activate_trigger`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

**Reference Examples**
- `LordsOfDiplomacy - Easy Mode -> main\Medieval_Europe_1200_AD.py:189`
- `GoKu RPG Project -> main\main_code.py:668`
- `GoKu RPG Project -> main\main_code.py:679`

## 3. Send Chat
**Method**: `send_chat`
**Family**: `feedback`
**Primary Role**: Explain system state to the player through UI, camera, text, or sound.

**How It Is Used**
Use this when a system needs explicit textual confirmation, instruction, or narrative feedback. Your reference projects use it to expose hidden scenario state to players without requiring them to understand internal variable logic. It is also useful for debugging and for player-specific communication because it can be sent to one selected player instead of to everyone.

**Architecture Notes**
Feedback effects should react to meaningful state changes, not replace them. A scenario stays readable when feedback follows a real system event rather than becoming the event itself.

**Real Project Usage**
Observed 40 times in the scanned reference projects, primarily in LordsOfDiplomacy - Easy Mode (18 uses), GoKu RPG Project (17 uses), Hide_and_Seek (5 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `activate_trigger`
- `change_variable`
- `objects_in_area`
- `researching_tech`

**Communication Semantics**
- Audience Scope: `selected_player_only`
- Attention Strength: `low`
- Recommended Frequency: `debug_or_player_specific`
- Best Use: Best for debugging, private player hints, or low-priority player-specific communication that does not need to be broadcast to everyone.

**Reference Examples**
- `LordsOfDiplomacy - Easy Mode -> Clerical_Actions\Initializations\initialize_cleric.py:264`
- `LordsOfDiplomacy - Easy Mode -> Court_Actions\court_actions.py:93`
- `LordsOfDiplomacy - Easy Mode -> Court_Actions\court_actions.py:138`

## 4. Play Sound
**Method**: `play_sound`
**Family**: `feedback`
**Primary Role**: Explain system state to the player through UI, camera, text, or sound.

**How It Is Used**
This is the audio confirmation layer for trigger systems. It is used when abilities fire, interactions succeed, cutscenes advance, or warnings need to feel immediate. In modular designs it usually sits at the end of a successful state transition, not at the front of the check.

**Architecture Notes**
Feedback effects should react to meaningful state changes, not replace them. A scenario stays readable when feedback follows a real system event rather than becoming the event itself.

**Real Project Usage**
Observed 77 times in the scanned reference projects, primarily in LordsOfDiplomacy - Easy Mode (61 uses), GoKu RPG Project (13 uses), Hide_and_Seek (3 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `activate_trigger`
- `change_variable`
- `objects_in_area`
- `researching_tech`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

**Reference Examples**
- `LordsOfDiplomacy - Easy Mode -> Clerical_Actions\Initializations\initialize_cleric.py:233`
- `LordsOfDiplomacy - Easy Mode -> Court_Actions\court_actions.py:97`
- `LordsOfDiplomacy - Easy Mode -> Court_Actions\court_actions.py:134`

## 5. Tribute
**Method**: `tribute`
**Family**: `resource_variable`
**Primary Role**: Move numbers between scenario state, player resources, and trigger-controlled counters.

**How It Is Used**
Use these effects when the scenario behaves like a rule system with explicit state transitions. They are responsible for cooldown counters, mana-like systems, custom resources, progression markers, and any mechanic where one trigger must write a value that another trigger later reads.

**Architecture Notes**
Central registries and data-driven naming are critical here. Without them, a large scenario turns into a collision-prone mess of numeric IDs and unclear write paths.

**Real Project Usage**
Observed 4 times in the scanned reference projects, primarily in GoKu RPG Project (4 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `variable_value`
- `compare_variables`
- `timer`
- `activate_trigger`
- `modify_attribute`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

**Reference Examples**
- `GoKu RPG Project -> Player_Progression\Leveling\leveling.py:192`
- `GoKu RPG Project -> Player_Progression\Leveling\leveling.py:205`
- `GoKu RPG Project -> Upgrade_Store\Scenario_Triggers\Item_Shop\equip-unequip logic.py:141`

## 6. Unlock Gate
**Method**: `unlock_gate`
**Family**: `object_control`
**Primary Role**: Create, remove, move, or command units and objects in the world.

**How It Is Used**
Use this family when the trigger system needs to directly manipulate the playable world. It covers spawning units, issuing orders, moving objects, removing temporary entities, and forcing scripted interactions that the normal AI or player input should not own.

**Architecture Notes**
World-control effects become much easier to balance when the object IDs, areas, and per-level values come from data modules. Keep world mutation code thin and let configuration determine what gets spawned or moved.

**Real Project Usage**
Observed 3 times in the scanned reference projects, primarily in GoKu RPG Project (2 uses), Hide_and_Seek (1 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `objects_in_area`
- `variable_value`
- `timer`
- `play_sound`
- `change_view`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

**Reference Examples**
- `GoKu RPG Project -> Bosses\Regions\Dqarn\Dungeon\Elephants_Dungeon\Post_Boss_Events\events.py:31`
- `GoKu RPG Project -> NPC\Quests\Estea\Elder_Beltherin\The_Path_to_Ethoridar\kill_mounted_bandits.py:20`
- `Hide_and_Seek -> Setup\World\apply_world_setup.py:60`

## 7. Lock Gate
**Method**: `lock_gate`
**Family**: `object_control`
**Primary Role**: Create, remove, move, or command units and objects in the world.

**How It Is Used**
Use this family when the trigger system needs to directly manipulate the playable world. It covers spawning units, issuing orders, moving objects, removing temporary entities, and forcing scripted interactions that the normal AI or player input should not own.

**Architecture Notes**
World-control effects become much easier to balance when the object IDs, areas, and per-level values come from data modules. Keep world mutation code thin and let configuration determine what gets spawned or moved.

**Real Project Usage**
Observed 1 times in the scanned reference projects, primarily in Hide_and_Seek (1 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `objects_in_area`
- `variable_value`
- `timer`
- `play_sound`
- `change_view`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

**Reference Examples**
- `Hide_and_Seek -> Setup\World\apply_world_setup.py:17`

## 8. Activate Trigger
**Method**: `activate_trigger`
**Family**: `orchestration`
**Primary Role**: Shape the trigger graph itself.

**How It Is Used**
This is the main orchestration handoff in your projects. It wakes the next slice of the system after the current trigger has finished checking inputs or applying one step of behavior. Large modular scenarios depend on it to keep systems readable because it lets each trigger own a single responsibility and then pass control onward.

**Architecture Notes**
Good trigger architecture treats orchestration as explicit. Instead of one giant trigger trying to do everything, orchestration effects move control between small, named triggers that each own one slice of behavior.

**Real Project Usage**
Observed 216 times in the scanned reference projects, primarily in LordsOfDiplomacy - Easy Mode (113 uses), GoKu RPG Project (91 uses), Hide_and_Seek (12 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `timer`
- `variable_value`
- `and_`
- `script_call`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

**Reference Examples**
- `LordsOfDiplomacy - Easy Mode -> Clerical_Actions\Actions\Adopt_Population\effect.py:28`
- `LordsOfDiplomacy - Easy Mode -> Clerical_Actions\Initializations\initialize_cleric.py:270`
- `LordsOfDiplomacy - Easy Mode -> Court_Actions\court_actions.py:43`

## 9. Deactivate Trigger
**Method**: `deactivate_trigger`
**Family**: `orchestration`
**Primary Role**: Shape the trigger graph itself.

**How It Is Used**
Use this to close loops, consume one-shot buttons, and retire temporary system states. In real projects it is what prevents old guards, previous phases, or expired cooldown triggers from staying alive after the system has moved on.

**Architecture Notes**
Good trigger architecture treats orchestration as explicit. Instead of one giant trigger trying to do everything, orchestration effects move control between small, named triggers that each own one slice of behavior.

**Real Project Usage**
Observed 77 times in the scanned reference projects, primarily in LordsOfDiplomacy - Easy Mode (46 uses), GoKu RPG Project (23 uses), Hide_and_Seek (8 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `timer`
- `variable_value`
- `and_`
- `script_call`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

**Reference Examples**
- `LordsOfDiplomacy - Easy Mode -> characters.py:233`
- `LordsOfDiplomacy - Easy Mode -> Clerical_Actions\Actions\Adopt_Population\effect.py:31`
- `LordsOfDiplomacy - Easy Mode -> Court_Actions\court_actions.py:49`

## 10. AI Script Goal
**Method**: `ai_script_goal`
**Family**: `diplomacy_ai`
**Primary Role**: Change player relationships or communicate with AI-facing systems.

**How It Is Used**
Use this family for treaties, factions, scripted political actions, AI coordination, or trigger-to-AI handoffs. The effect is usually part of a dedicated diplomacy or encounter module rather than a generic combat trigger.

**Architecture Notes**
Keep diplomacy and AI signaling explicit. Scenarios become easier to reason about when relationship changes are grouped in one subsystem instead of hidden in many unrelated triggers.

**Real Project Usage**
This parser feature is present in AoE2ScenarioParser but was not observed in the scanned local reference projects. Treat it as supported capability with no local canonical usage pattern yet.

**Common Pairings**
- `diplomacy_state`
- `researching_tech`
- `send_chat`
- `play_sound`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

## 11. Create Object
**Method**: `create_object`
**Family**: `object_control`
**Primary Role**: Create, remove, move, or command units and objects in the world.

**How It Is Used**
Use this to materialize system state into world state. It is the spawn point for summons, markers, temporary helpers, encounter units, and other entities that only exist because the trigger system says they should.

**Architecture Notes**
World-control effects become much easier to balance when the object IDs, areas, and per-level values come from data modules. Keep world mutation code thin and let configuration determine what gets spawned or moved.

**Real Project Usage**
Observed 25 times in the scanned reference projects, primarily in LordsOfDiplomacy - Easy Mode (11 uses), GoKu RPG Project (9 uses), Hide_and_Seek (5 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `objects_in_area`
- `variable_value`
- `timer`
- `play_sound`
- `change_view`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

**Reference Examples**
- `LordsOfDiplomacy - Easy Mode -> cut_scenes.py:66`
- `LordsOfDiplomacy - Easy Mode -> Lords\lords_start.py:129`
- `LordsOfDiplomacy - Easy Mode -> Lords\lords_start.py:158`

## 12. Task Object
**Method**: `task_object`
**Family**: `object_control`
**Primary Role**: Create, remove, move, or command units and objects in the world.

**How It Is Used**
This is the core effect for scripted orders. It turns triggers into directors that can force objects toward a target, area, or action without waiting for player or AI initiative. It is especially useful in teleports, summons, escorts, and staged encounters.

**Architecture Notes**
World-control effects become much easier to balance when the object IDs, areas, and per-level values come from data modules. Keep world mutation code thin and let configuration determine what gets spawned or moved.

**Real Project Usage**
Observed 13 times in the scanned reference projects, primarily in LordsOfDiplomacy - Easy Mode (5 uses), GoKu RPG Project (8 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `objects_in_area`
- `variable_value`
- `timer`
- `play_sound`
- `change_view`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

**Reference Examples**
- `LordsOfDiplomacy - Easy Mode -> cut_scenes.py:519`
- `LordsOfDiplomacy - Easy Mode -> Espionage\Actions\Open_Enemy_Gates\apply_open_enemy_gates.py:114`
- `LordsOfDiplomacy - Easy Mode -> Espionage\Actions\Open_Enemy_Gates\apply_open_enemy_gates.py:141`

## 13. Declare Victory
**Method**: `declare_victory`
**Family**: `special`
**Primary Role**: Handle niche scenario actions that do not fit the main families.

**How It Is Used**
Use these only when the scenario specifically needs their engine behavior. They are valid tools, but they should usually appear inside a narrow subsystem rather than as general-purpose building blocks.

**Architecture Notes**
Agents should check whether a more common family already solves the task before choosing one of these effects.

**Real Project Usage**
Observed 6 times in the scanned reference projects, primarily in LordsOfDiplomacy - Easy Mode (2 uses), Hide_and_Seek (4 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `send_chat`
- `play_sound`
- `activate_trigger`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

**Reference Examples**
- `LordsOfDiplomacy - Easy Mode -> game_initialization.py:409`
- `LordsOfDiplomacy - Easy Mode -> Kingdom_Resources\Fame\fame_victory.py:125`
- `Hide_and_Seek -> Round_End\Victory\apply_victory_conditions.py:37`

## 14. Kill Object
**Method**: `kill_object`
**Family**: `object_control`
**Primary Role**: Create, remove, move, or command units and objects in the world.

**How It Is Used**
Use this family when the trigger system needs to directly manipulate the playable world. It covers spawning units, issuing orders, moving objects, removing temporary entities, and forcing scripted interactions that the normal AI or player input should not own.

**Architecture Notes**
World-control effects become much easier to balance when the object IDs, areas, and per-level values come from data modules. Keep world mutation code thin and let configuration determine what gets spawned or moved.

**Real Project Usage**
Observed 9 times in the scanned reference projects, primarily in GoKu RPG Project (8 uses), Hide_and_Seek (1 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `objects_in_area`
- `variable_value`
- `timer`
- `play_sound`
- `change_view`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

**Reference Examples**
- `GoKu RPG Project -> Abilities\Arcanist\Active_Ability_1\thunderstorm.py:58`
- `GoKu RPG Project -> Abilities\Arcanist\Active_Ability_2\pulse_eruption.py:40`
- `GoKu RPG Project -> NPC\Quests\Estea\Captain_Jorand\Clearing_The_Depths\apply_quest.py:48`

## 15. Remove Object
**Method**: `remove_object`
**Family**: `object_control`
**Primary Role**: Create, remove, move, or command units and objects in the world.

**How It Is Used**
Use this to clean up temporary world state after an interaction, effect, summon, or scripted stage completes. In real projects it keeps the map and system state synchronized by removing entities that should no longer participate in the scenario.

**Architecture Notes**
World-control effects become much easier to balance when the object IDs, areas, and per-level values come from data modules. Keep world mutation code thin and let configuration determine what gets spawned or moved.

**Real Project Usage**
Observed 66 times in the scanned reference projects, primarily in LordsOfDiplomacy - Easy Mode (35 uses), GoKu RPG Project (17 uses), Hide_and_Seek (14 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `objects_in_area`
- `variable_value`
- `timer`
- `play_sound`
- `change_view`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

**Reference Examples**
- `LordsOfDiplomacy - Easy Mode -> characters.py:159`
- `LordsOfDiplomacy - Easy Mode -> Clerical_Actions\Initializations\initialize_cleric.py:259`
- `LordsOfDiplomacy - Easy Mode -> Court_Actions\court_actions.py:103`

## 16. Change View
**Method**: `change_view`
**Family**: `feedback`
**Primary Role**: Explain system state to the player through UI, camera, text, or sound.

**How It Is Used**
Use this when the system needs to direct attention to a location or event. It is especially good as a support effect for player-specific notification because the camera move can target a chosen player and make the event harder to miss.

**Architecture Notes**
Feedback effects should react to meaningful state changes, not replace them. A scenario stays readable when feedback follows a real system event rather than becoming the event itself.

**Real Project Usage**
Observed 22 times in the scanned reference projects, primarily in LordsOfDiplomacy - Easy Mode (7 uses), GoKu RPG Project (11 uses), Hide_and_Seek (4 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `activate_trigger`
- `change_variable`
- `objects_in_area`
- `researching_tech`

**Communication Semantics**
- Audience Scope: `selected_player_or_targeted_players`
- Attention Strength: `high`
- Recommended Frequency: `event_driven`
- Best Use: Best as a targeted support effect when a player must notice where an event is happening right now.

**Reference Examples**
- `LordsOfDiplomacy - Easy Mode -> cut_scenes.py:92`
- `LordsOfDiplomacy - Easy Mode -> cut_scenes.py:500`
- `LordsOfDiplomacy - Easy Mode -> cut_scenes.py:718`

## 17. Unload
**Method**: `unload`
**Family**: `object_control`
**Primary Role**: Create, remove, move, or command units and objects in the world.

**How It Is Used**
Use this family when the trigger system needs to directly manipulate the playable world. It covers spawning units, issuing orders, moving objects, removing temporary entities, and forcing scripted interactions that the normal AI or player input should not own.

**Architecture Notes**
World-control effects become much easier to balance when the object IDs, areas, and per-level values come from data modules. Keep world mutation code thin and let configuration determine what gets spawned or moved.

**Real Project Usage**
This parser feature is present in AoE2ScenarioParser but was not observed in the scanned local reference projects. Treat it as supported capability with no local canonical usage pattern yet.

**Common Pairings**
- `objects_in_area`
- `variable_value`
- `timer`
- `play_sound`
- `change_view`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

## 18. Change Ownership
**Method**: `change_ownership`
**Family**: `diplomacy_ai`
**Primary Role**: Change player relationships or communicate with AI-facing systems.

**How It Is Used**
Use this family for treaties, factions, scripted political actions, AI coordination, or trigger-to-AI handoffs. The effect is usually part of a dedicated diplomacy or encounter module rather than a generic combat trigger.

**Architecture Notes**
Keep diplomacy and AI signaling explicit. Scenarios become easier to reason about when relationship changes are grouped in one subsystem instead of hidden in many unrelated triggers.

**Real Project Usage**
Observed 29 times in the scanned reference projects, primarily in LordsOfDiplomacy - Easy Mode (5 uses), GoKu RPG Project (4 uses), Hide_and_Seek (20 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `diplomacy_state`
- `researching_tech`
- `send_chat`
- `play_sound`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

**Reference Examples**
- `LordsOfDiplomacy - Easy Mode -> Lords\lords_start.py:208`
- `LordsOfDiplomacy - Easy Mode -> Provinces\Capture_From_GAIA\Capture_Province_gaia\capture_successfull.py:92`
- `LordsOfDiplomacy - Easy Mode -> Provinces\Capture_Province\capture_successfull.py:78`

## 19. Patrol
**Method**: `patrol`
**Family**: `object_control`
**Primary Role**: Create, remove, move, or command units and objects in the world.

**How It Is Used**
Use this family when the trigger system needs to directly manipulate the playable world. It covers spawning units, issuing orders, moving objects, removing temporary entities, and forcing scripted interactions that the normal AI or player input should not own.

**Architecture Notes**
World-control effects become much easier to balance when the object IDs, areas, and per-level values come from data modules. Keep world mutation code thin and let configuration determine what gets spawned or moved.

**Real Project Usage**
This parser feature is present in AoE2ScenarioParser but was not observed in the scanned local reference projects. Treat it as supported capability with no local canonical usage pattern yet.

**Common Pairings**
- `objects_in_area`
- `variable_value`
- `timer`
- `play_sound`
- `change_view`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

## 20. Display Instructions
**Method**: `display_instructions`
**Family**: `feedback`
**Primary Role**: Explain system state to the player through UI, camera, text, or sound.

**How It Is Used**
Use this for strong shared announcements that should be seen by all players without recurring constantly. It works best for lower-frequency global events, major warnings, tutorials, and milestone messages where a single strong broadcast is better than repeated notification spam.

**Architecture Notes**
Feedback effects should react to meaningful state changes, not replace them. A scenario stays readable when feedback follows a real system event rather than becoming the event itself.

**Real Project Usage**
Observed 32 times in the scanned reference projects, primarily in LordsOfDiplomacy - Easy Mode (17 uses), GoKu RPG Project (2 uses), Hide_and_Seek (13 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `activate_trigger`
- `change_variable`
- `objects_in_area`
- `researching_tech`

**Communication Semantics**
- Audience Scope: `all_players_visible`
- Attention Strength: `high`
- Recommended Frequency: `low_frequency`
- Best Use: Best for rare, important, shared announcements that should reach everyone without constantly flooding the screen.

**Reference Examples**
- `LordsOfDiplomacy - Easy Mode -> cut_scenes.py:680`
- `LordsOfDiplomacy - Easy Mode -> cut_scenes.py:695`
- `LordsOfDiplomacy - Easy Mode -> cut_scenes.py:710`

## 21. Clear Instructions
**Method**: `clear_instructions`
**Family**: `feedback`
**Primary Role**: Explain system state to the player through UI, camera, text, or sound.

**How It Is Used**
Use these effects when a trigger change should be legible to players. Real projects rely on them to teach mechanics, confirm interactions, sell class abilities, and make hidden state transitions visible without exposing internal variable logic directly.

**Architecture Notes**
Feedback effects should react to meaningful state changes, not replace them. A scenario stays readable when feedback follows a real system event rather than becoming the event itself.

**Real Project Usage**
Observed 2 times in the scanned reference projects, primarily in LordsOfDiplomacy - Easy Mode (1 uses), GoKu RPG Project (1 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `activate_trigger`
- `change_variable`
- `objects_in_area`
- `researching_tech`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

**Reference Examples**
- `LordsOfDiplomacy - Easy Mode -> cut_scenes.py:620`
- `GoKu RPG Project -> World\Instructions_Manager\instructions_manager.py:69`

## 22. Freeze Object
**Method**: `freeze_object`
**Family**: `interaction_control`
**Primary Role**: Temporarily allow or forbid player interaction with units or objects.

**How It Is Used**
Use this family for cutscenes, stuns, protected summons, invulnerability windows, interface locking, or scripted sequences where players should not be able to interfere with the system at the wrong time.

**Architecture Notes**
Interaction locks are safest when paired with clear activation and cleanup triggers. The biggest failure mode is forgetting to re-enable the thing that was disabled.

**Real Project Usage**
Observed 7 times in the scanned reference projects, primarily in GoKu RPG Project (7 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `timer`
- `activate_trigger`
- `deactivate_trigger`
- `play_sound`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

**Reference Examples**
- `GoKu RPG Project -> main\main_code.py:199`
- `GoKu RPG Project -> NPC\Quests\Estea\initialize_names.py:37`
- `GoKu RPG Project -> NPC\Quests\Estea\initialize_names.py:40`

## 23. Use Advanced Buttons
**Method**: `use_advanced_buttons`
**Family**: `special`
**Primary Role**: Handle niche scenario actions that do not fit the main families.

**How It Is Used**
Use these only when the scenario specifically needs their engine behavior. They are valid tools, but they should usually appear inside a narrow subsystem rather than as general-purpose building blocks.

**Architecture Notes**
Agents should check whether a more common family already solves the task before choosing one of these effects.

**Real Project Usage**
Observed 1 times in the scanned reference projects, primarily in Hide_and_Seek (1 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `send_chat`
- `play_sound`
- `activate_trigger`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

**Reference Examples**
- `Hide_and_Seek -> Setup\Player_Setup\apply_player_setup.py:669`

## 24. Damage Object
**Method**: `damage_object`
**Family**: `stat_mutation`
**Primary Role**: Change runtime object or class stats in response to scenario logic.

**How It Is Used**
Use this family for buffs, debuffs, scaling systems, class growth, difficulty adjustments, and temporary ability states. In your reference projects stat mutation is one of the main ways triggers turn variables and timers into visible gameplay consequences.

**Architecture Notes**
This family is where data-driven balancing matters most. If numbers are spread through trigger builders, later balance passes become expensive and error-prone. Keep the values in dictionaries and let trigger code only apply them.

**Real Project Usage**
Observed 12 times in the scanned reference projects, primarily in LordsOfDiplomacy - Easy Mode (8 uses), GoKu RPG Project (2 uses), Hide_and_Seek (2 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `variable_value`
- `change_variable`
- `timer`
- `script_call`
- `modify_resource`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

**Reference Examples**
- `LordsOfDiplomacy - Easy Mode -> Espionage\Actions\Poison_Enemy_Army\apply_poison_enemy_army.py:102`
- `LordsOfDiplomacy - Easy Mode -> Espionage\Actions\Poison_Enemy_Army\apply_poison_enemy_army.py:107`
- `LordsOfDiplomacy - Easy Mode -> Espionage\Actions\Poison_Enemy_Army\apply_poison_enemy_army.py:112`

## 25. Place Foundation
**Method**: `place_foundation`
**Family**: `object_control`
**Primary Role**: Create, remove, move, or command units and objects in the world.

**How It Is Used**
Use this family when the trigger system needs to directly manipulate the playable world. It covers spawning units, issuing orders, moving objects, removing temporary entities, and forcing scripted interactions that the normal AI or player input should not own.

**Architecture Notes**
World-control effects become much easier to balance when the object IDs, areas, and per-level values come from data modules. Keep world mutation code thin and let configuration determine what gets spawned or moved.

**Real Project Usage**
This parser feature is present in AoE2ScenarioParser but was not observed in the scanned local reference projects. Treat it as supported capability with no local canonical usage pattern yet.

**Common Pairings**
- `objects_in_area`
- `variable_value`
- `timer`
- `play_sound`
- `change_view`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

## 26. Change Object Name
**Method**: `change_object_name`
**Family**: `identity_visibility`
**Primary Role**: Change what players see and how objects or players are labeled.

**How It Is Used**
Use this family for polish, illusion, staged reveals, and scenario-controlled identity changes. It supports systems where the same gameplay object changes its name, caption, color, or apparent ownership based on scenario state.

**Architecture Notes**
Visibility and identity effects are best used as presentation layers on top of real state changes. Keep the authoritative state in variables or object data and let these effects communicate that state.

**Real Project Usage**
Observed 24 times in the scanned reference projects, primarily in LordsOfDiplomacy - Easy Mode (16 uses), GoKu RPG Project (8 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `change_variable`
- `send_chat`
- `play_sound`
- `change_view`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

**Reference Examples**
- `LordsOfDiplomacy - Easy Mode -> characters.py:185`
- `LordsOfDiplomacy - Easy Mode -> cut_scenes.py:57`
- `LordsOfDiplomacy - Easy Mode -> esponiage_system.py:25`

## 27. Change Object HP
**Method**: `change_object_hp`
**Family**: `stat_mutation`
**Primary Role**: Change runtime object or class stats in response to scenario logic.

**How It Is Used**
Use this family for buffs, debuffs, scaling systems, class growth, difficulty adjustments, and temporary ability states. In your reference projects stat mutation is one of the main ways triggers turn variables and timers into visible gameplay consequences.

**Architecture Notes**
This family is where data-driven balancing matters most. If numbers are spread through trigger builders, later balance passes become expensive and error-prone. Keep the values in dictionaries and let trigger code only apply them.

**Real Project Usage**
Observed 2 times in the scanned reference projects, primarily in Hide_and_Seek (2 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `variable_value`
- `change_variable`
- `timer`
- `script_call`
- `modify_resource`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

**Reference Examples**
- `Hide_and_Seek -> Objectives\Car\Main_Objective\apply_car_spawning.py:92`
- `Hide_and_Seek -> old_code\game.py:208`

## 28. Change Object Attack
**Method**: `change_object_attack`
**Family**: `stat_mutation`
**Primary Role**: Change runtime object or class stats in response to scenario logic.

**How It Is Used**
Use this family for buffs, debuffs, scaling systems, class growth, difficulty adjustments, and temporary ability states. In your reference projects stat mutation is one of the main ways triggers turn variables and timers into visible gameplay consequences.

**Architecture Notes**
This family is where data-driven balancing matters most. If numbers are spread through trigger builders, later balance passes become expensive and error-prone. Keep the values in dictionaries and let trigger code only apply them.

**Real Project Usage**
This parser feature is present in AoE2ScenarioParser but was not observed in the scanned local reference projects. Treat it as supported capability with no local canonical usage pattern yet.

**Common Pairings**
- `variable_value`
- `change_variable`
- `timer`
- `script_call`
- `modify_resource`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

## 29. Stop Object
**Method**: `stop_object`
**Family**: `object_control`
**Primary Role**: Create, remove, move, or command units and objects in the world.

**How It Is Used**
Use this family when the trigger system needs to directly manipulate the playable world. It covers spawning units, issuing orders, moving objects, removing temporary entities, and forcing scripted interactions that the normal AI or player input should not own.

**Architecture Notes**
World-control effects become much easier to balance when the object IDs, areas, and per-level values come from data modules. Keep world mutation code thin and let configuration determine what gets spawned or moved.

**Real Project Usage**
Observed 6 times in the scanned reference projects, primarily in GoKu RPG Project (5 uses), Hide_and_Seek (1 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `objects_in_area`
- `variable_value`
- `timer`
- `play_sound`
- `change_view`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

**Reference Examples**
- `GoKu RPG Project -> Bosses\Boss_System.py:164`
- `GoKu RPG Project -> Bosses\Boss_System.py:189`
- `GoKu RPG Project -> Bosses\Regions\Dqarn\Dungeon\Elephants_Dungeon\Post_Boss_Events\events.py:100`

## 30. Attack Move
**Method**: `attack_move`
**Family**: `object_control`
**Primary Role**: Create, remove, move, or command units and objects in the world.

**How It Is Used**
Use this family when the trigger system needs to directly manipulate the playable world. It covers spawning units, issuing orders, moving objects, removing temporary entities, and forcing scripted interactions that the normal AI or player input should not own.

**Architecture Notes**
World-control effects become much easier to balance when the object IDs, areas, and per-level values come from data modules. Keep world mutation code thin and let configuration determine what gets spawned or moved.

**Real Project Usage**
This parser feature is present in AoE2ScenarioParser but was not observed in the scanned local reference projects. Treat it as supported capability with no local canonical usage pattern yet.

**Common Pairings**
- `objects_in_area`
- `variable_value`
- `timer`
- `play_sound`
- `change_view`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

## 31. Change Object Armor
**Method**: `change_object_armor`
**Family**: `stat_mutation`
**Primary Role**: Change runtime object or class stats in response to scenario logic.

**How It Is Used**
Use this family for buffs, debuffs, scaling systems, class growth, difficulty adjustments, and temporary ability states. In your reference projects stat mutation is one of the main ways triggers turn variables and timers into visible gameplay consequences.

**Architecture Notes**
This family is where data-driven balancing matters most. If numbers are spread through trigger builders, later balance passes become expensive and error-prone. Keep the values in dictionaries and let trigger code only apply them.

**Real Project Usage**
This parser feature is present in AoE2ScenarioParser but was not observed in the scanned local reference projects. Treat it as supported capability with no local canonical usage pattern yet.

**Common Pairings**
- `variable_value`
- `change_variable`
- `timer`
- `script_call`
- `modify_resource`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

## 32. Change Object Range
**Method**: `change_object_range`
**Family**: `stat_mutation`
**Primary Role**: Change runtime object or class stats in response to scenario logic.

**How It Is Used**
Use this family for buffs, debuffs, scaling systems, class growth, difficulty adjustments, and temporary ability states. In your reference projects stat mutation is one of the main ways triggers turn variables and timers into visible gameplay consequences.

**Architecture Notes**
This family is where data-driven balancing matters most. If numbers are spread through trigger builders, later balance passes become expensive and error-prone. Keep the values in dictionaries and let trigger code only apply them.

**Real Project Usage**
This parser feature is present in AoE2ScenarioParser but was not observed in the scanned local reference projects. Treat it as supported capability with no local canonical usage pattern yet.

**Common Pairings**
- `variable_value`
- `change_variable`
- `timer`
- `script_call`
- `modify_resource`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

## 33. Change Object Speed
**Method**: `change_object_speed`
**Family**: `stat_mutation`
**Primary Role**: Change runtime object or class stats in response to scenario logic.

**How It Is Used**
Use this family for buffs, debuffs, scaling systems, class growth, difficulty adjustments, and temporary ability states. In your reference projects stat mutation is one of the main ways triggers turn variables and timers into visible gameplay consequences.

**Architecture Notes**
This family is where data-driven balancing matters most. If numbers are spread through trigger builders, later balance passes become expensive and error-prone. Keep the values in dictionaries and let trigger code only apply them.

**Real Project Usage**
Observed 1 times in the scanned reference projects, primarily in LordsOfDiplomacy - Easy Mode (1 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `variable_value`
- `change_variable`
- `timer`
- `script_call`
- `modify_resource`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

**Reference Examples**
- `LordsOfDiplomacy - Easy Mode -> cut_scenes.py:134`

## 34. Heal Object
**Method**: `heal_object`
**Family**: `stat_mutation`
**Primary Role**: Change runtime object or class stats in response to scenario logic.

**How It Is Used**
Use this family for buffs, debuffs, scaling systems, class growth, difficulty adjustments, and temporary ability states. In your reference projects stat mutation is one of the main ways triggers turn variables and timers into visible gameplay consequences.

**Architecture Notes**
This family is where data-driven balancing matters most. If numbers are spread through trigger builders, later balance passes become expensive and error-prone. Keep the values in dictionaries and let trigger code only apply them.

**Real Project Usage**
Observed 2 times in the scanned reference projects, primarily in GoKu RPG Project (2 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `variable_value`
- `change_variable`
- `timer`
- `script_call`
- `modify_resource`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

**Reference Examples**
- `GoKu RPG Project -> Bosses\Boss_System.py:257`
- `GoKu RPG Project -> World\Binary_Tree_Heal\binary_tree_heal.py:62`

## 35. Teleport Object
**Method**: `teleport_object`
**Family**: `object_control`
**Primary Role**: Create, remove, move, or command units and objects in the world.

**How It Is Used**
Use this when spatial repositioning itself is the mechanic. In projects with portals, scripted movement, or ability travel, teleportation is usually guarded by area or variable checks and paired with cleanup and feedback so the move feels intentional rather than abrupt.

**Architecture Notes**
World-control effects become much easier to balance when the object IDs, areas, and per-level values come from data modules. Keep world mutation code thin and let configuration determine what gets spawned or moved.

**Real Project Usage**
Observed 4 times in the scanned reference projects, primarily in GoKu RPG Project (4 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `objects_in_area`
- `variable_value`
- `timer`
- `play_sound`
- `change_view`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

**Reference Examples**
- `GoKu RPG Project -> Bosses\Boss_System.py:160`
- `GoKu RPG Project -> Bosses\Boss_System.py:185`
- `GoKu RPG Project -> Bosses\Regions\Dqarn\Dungeon\Elephants_Dungeon\Post_Boss_Events\events.py:93`

## 36. Change Object Stance
**Method**: `change_object_stance`
**Family**: `interaction_control`
**Primary Role**: Temporarily allow or forbid player interaction with units or objects.

**How It Is Used**
Use this family for cutscenes, stuns, protected summons, invulnerability windows, interface locking, or scripted sequences where players should not be able to interfere with the system at the wrong time.

**Architecture Notes**
Interaction locks are safest when paired with clear activation and cleanup triggers. The biggest failure mode is forgetting to re-enable the thing that was disabled.

**Real Project Usage**
Observed 11 times in the scanned reference projects, primarily in GoKu RPG Project (11 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `timer`
- `activate_trigger`
- `deactivate_trigger`
- `play_sound`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

**Reference Examples**
- `GoKu RPG Project -> Bosses\Boss_System.py:110`
- `GoKu RPG Project -> Bosses\Boss_System.py:152`
- `GoKu RPG Project -> Mobs\Region\Ethoridar\Castle_Dungeon\abilities.py:147`

## 37. Display Timer
**Method**: `display_timer`
**Family**: `feedback`
**Primary Role**: Explain system state to the player through UI, camera, text, or sound.

**How It Is Used**
This is the player-facing surface for time-based systems. Use it when cooldowns, objectives, waves, or phases should be visible instead of hidden inside internal timer conditions. It is also one of the best tools for high-frequency global-event notification because it is hard to miss and can keep recurring event state visible without relying on chat.

**Architecture Notes**
Feedback effects should react to meaningful state changes, not replace them. A scenario stays readable when feedback follows a real system event rather than becoming the event itself.

**Real Project Usage**
Observed 29 times in the scanned reference projects, primarily in LordsOfDiplomacy - Easy Mode (18 uses), GoKu RPG Project (2 uses), Hide_and_Seek (9 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `activate_trigger`
- `change_variable`
- `objects_in_area`
- `researching_tech`

**Communication Semantics**
- Audience Scope: `all_players_visible`
- Attention Strength: `high`
- Recommended Frequency: `high_frequency`
- Best Use: Best for recurring or high-frequency global-event notification where players need a visible shared event banner or countdown-style message.

**Reference Examples**
- `LordsOfDiplomacy - Easy Mode -> Court_Actions\court_actions.py:143`
- `LordsOfDiplomacy - Easy Mode -> Diplomacy\Actions\Alliance\Helper_Functions\form_alliance.py:104`
- `LordsOfDiplomacy - Easy Mode -> Diplomacy\Actions\Defensive_Pact\Helper_Functions\defensive_pact_timer.py:47`

## 38. Enable Disable Object
**Method**: `enable_disable_object`
**Family**: `interaction_control`
**Primary Role**: Temporarily allow or forbid player interaction with units or objects.

**How It Is Used**
Use this family for cutscenes, stuns, protected summons, invulnerability windows, interface locking, or scripted sequences where players should not be able to interfere with the system at the wrong time.

**Architecture Notes**
Interaction locks are safest when paired with clear activation and cleanup triggers. The biggest failure mode is forgetting to re-enable the thing that was disabled.

**Real Project Usage**
Observed 20 times in the scanned reference projects, primarily in LordsOfDiplomacy - Easy Mode (14 uses), GoKu RPG Project (2 uses), Hide_and_Seek (4 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `timer`
- `activate_trigger`
- `deactivate_trigger`
- `play_sound`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

**Reference Examples**
- `LordsOfDiplomacy - Easy Mode -> characters.py:66`
- `LordsOfDiplomacy - Easy Mode -> characters.py:166`
- `LordsOfDiplomacy - Easy Mode -> characters.py:175`

## 39. Enable Disable Technology
**Method**: `enable_disable_technology`
**Family**: `tech_edit`
**Primary Role**: Turn technologies into a scenario-controlled interface and progression surface.

**How It Is Used**
Use these effects when technologies are serving as buttons, unlock panels, class menus, or progression displays rather than only vanilla researches. Your projects use this family to move, rename, cost, and gate technologies so the scenario can expose custom systems through the game UI.

**Architecture Notes**
This family is strongest when tech metadata comes from data dictionaries. That keeps UI and balancing changes out of the trigger orchestration code.

**Real Project Usage**
Observed 5 times in the scanned reference projects, primarily in LordsOfDiplomacy - Easy Mode (5 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `researching_tech`
- `technology_state`
- `send_chat`
- `display_timer`
- `activate_trigger`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

**Reference Examples**
- `LordsOfDiplomacy - Easy Mode -> Clerical_Actions\Helper_Function\UNUSED_initialize_tech.py:31`
- `LordsOfDiplomacy - Easy Mode -> Court_Actions\court_actions.py:174`
- `LordsOfDiplomacy - Easy Mode -> Diplomacy\Actions\Helper_Functions\display_offer.py:43`

## 40. Change Object Cost
**Method**: `change_object_cost`
**Family**: `stat_mutation`
**Primary Role**: Change runtime object or class stats in response to scenario logic.

**How It Is Used**
Use this family for buffs, debuffs, scaling systems, class growth, difficulty adjustments, and temporary ability states. In your reference projects stat mutation is one of the main ways triggers turn variables and timers into visible gameplay consequences.

**Architecture Notes**
This family is where data-driven balancing matters most. If numbers are spread through trigger builders, later balance passes become expensive and error-prone. Keep the values in dictionaries and let trigger code only apply them.

**Real Project Usage**
Observed 9 times in the scanned reference projects, primarily in LordsOfDiplomacy - Easy Mode (6 uses), GoKu RPG Project (3 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `variable_value`
- `change_variable`
- `timer`
- `script_call`
- `modify_resource`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

**Reference Examples**
- `LordsOfDiplomacy - Easy Mode -> characters.py:91`
- `LordsOfDiplomacy - Easy Mode -> Clerical_Actions\Initializations\initialize_cleric.py:77`
- `LordsOfDiplomacy - Easy Mode -> Diplomacy\Intializations\initialize_diplomat_and_building.py:46`

## 41. Set Player Visibility
**Method**: `set_player_visibility`
**Family**: `identity_visibility`
**Primary Role**: Change what players see and how objects or players are labeled.

**How It Is Used**
Use this family for polish, illusion, staged reveals, and scenario-controlled identity changes. It supports systems where the same gameplay object changes its name, caption, color, or apparent ownership based on scenario state.

**Architecture Notes**
Visibility and identity effects are best used as presentation layers on top of real state changes. Keep the authoritative state in variables or object data and let these effects communicate that state.

**Real Project Usage**
Observed 11 times in the scanned reference projects, primarily in LordsOfDiplomacy - Easy Mode (10 uses), GoKu RPG Project (1 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `change_variable`
- `send_chat`
- `play_sound`
- `change_view`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

**Reference Examples**
- `LordsOfDiplomacy - Easy Mode -> Diplomacy\Actions\Alliance\Helper_Functions\form_alliance.py:50`
- `LordsOfDiplomacy - Easy Mode -> Diplomacy\Actions\Alliance\Helper_Functions\form_alliance.py:55`
- `LordsOfDiplomacy - Easy Mode -> Diplomacy\Actions\Neutral\Helper_Functions\form_neutral.py:53`

## 42. Change Object Icon
**Method**: `change_object_icon`
**Family**: `identity_visibility`
**Primary Role**: Change what players see and how objects or players are labeled.

**How It Is Used**
Use this family for polish, illusion, staged reveals, and scenario-controlled identity changes. It supports systems where the same gameplay object changes its name, caption, color, or apparent ownership based on scenario state.

**Architecture Notes**
Visibility and identity effects are best used as presentation layers on top of real state changes. Keep the authoritative state in variables or object data and let these effects communicate that state.

**Real Project Usage**
This parser feature is present in AoE2ScenarioParser but was not observed in the scanned local reference projects. Treat it as supported capability with no local canonical usage pattern yet.

**Common Pairings**
- `change_variable`
- `send_chat`
- `play_sound`
- `change_view`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

## 43. Replace Object
**Method**: `replace_object`
**Family**: `object_control`
**Primary Role**: Create, remove, move, or command units and objects in the world.

**How It Is Used**
Use this family when the trigger system needs to directly manipulate the playable world. It covers spawning units, issuing orders, moving objects, removing temporary entities, and forcing scripted interactions that the normal AI or player input should not own.

**Architecture Notes**
World-control effects become much easier to balance when the object IDs, areas, and per-level values come from data modules. Keep world mutation code thin and let configuration determine what gets spawned or moved.

**Real Project Usage**
Observed 26 times in the scanned reference projects, primarily in LordsOfDiplomacy - Easy Mode (4 uses), GoKu RPG Project (16 uses), Hide_and_Seek (6 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `objects_in_area`
- `variable_value`
- `timer`
- `play_sound`
- `change_view`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

**Reference Examples**
- `LordsOfDiplomacy - Easy Mode -> Espionage\Actions\Open_Enemy_Gates\apply_open_enemy_gates.py:92`
- `LordsOfDiplomacy - Easy Mode -> Espionage\Actions\Open_Enemy_Gates\apply_open_enemy_gates.py:146`
- `LordsOfDiplomacy - Easy Mode -> game_initialization.py:258`

## 44. Change Object Description
**Method**: `change_object_description`
**Family**: `identity_visibility`
**Primary Role**: Change what players see and how objects or players are labeled.

**How It Is Used**
Use this family for polish, illusion, staged reveals, and scenario-controlled identity changes. It supports systems where the same gameplay object changes its name, caption, color, or apparent ownership based on scenario state.

**Architecture Notes**
Visibility and identity effects are best used as presentation layers on top of real state changes. Keep the authoritative state in variables or object data and let these effects communicate that state.

**Real Project Usage**
Observed 15 times in the scanned reference projects, primarily in LordsOfDiplomacy - Easy Mode (6 uses), GoKu RPG Project (6 uses), Hide_and_Seek (3 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `change_variable`
- `send_chat`
- `play_sound`
- `change_view`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

**Reference Examples**
- `LordsOfDiplomacy - Easy Mode -> characters.py:80`
- `LordsOfDiplomacy - Easy Mode -> Clerical_Actions\Initializations\initialize_cleric.py:40`
- `LordsOfDiplomacy - Easy Mode -> Diplomacy\Intializations\initialize_diplomat_and_building.py:38`

## 45. Change Player Name
**Method**: `change_player_name`
**Family**: `identity_visibility`
**Primary Role**: Change what players see and how objects or players are labeled.

**How It Is Used**
Use this family for polish, illusion, staged reveals, and scenario-controlled identity changes. It supports systems where the same gameplay object changes its name, caption, color, or apparent ownership based on scenario state.

**Architecture Notes**
Visibility and identity effects are best used as presentation layers on top of real state changes. Keep the authoritative state in variables or object data and let these effects communicate that state.

**Real Project Usage**
This parser feature is present in AoE2ScenarioParser but was not observed in the scanned local reference projects. Treat it as supported capability with no local canonical usage pattern yet.

**Common Pairings**
- `change_variable`
- `send_chat`
- `play_sound`
- `change_view`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

## 46. Change Train Location
**Method**: `change_train_location`
**Family**: `tech_edit`
**Primary Role**: Turn technologies into a scenario-controlled interface and progression surface.

**How It Is Used**
Use these effects when technologies are serving as buttons, unlock panels, class menus, or progression displays rather than only vanilla researches. Your projects use this family to move, rename, cost, and gate technologies so the scenario can expose custom systems through the game UI.

**Architecture Notes**
This family is strongest when tech metadata comes from data dictionaries. That keeps UI and balancing changes out of the trigger orchestration code.

**Real Project Usage**
Observed 7 times in the scanned reference projects, primarily in LordsOfDiplomacy - Easy Mode (6 uses), GoKu RPG Project (1 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `researching_tech`
- `technology_state`
- `send_chat`
- `display_timer`
- `activate_trigger`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

**Reference Examples**
- `LordsOfDiplomacy - Easy Mode -> characters.py:85`
- `LordsOfDiplomacy - Easy Mode -> Clerical_Actions\Initializations\initialize_cleric.py:33`
- `LordsOfDiplomacy - Easy Mode -> Diplomacy\Intializations\initialize_diplomat_and_building.py:31`

## 47. Change Research Location
**Method**: `change_research_location`
**Family**: `tech_edit`
**Primary Role**: Turn technologies into a scenario-controlled interface and progression surface.

**How It Is Used**
Use these effects when technologies are serving as buttons, unlock panels, class menus, or progression displays rather than only vanilla researches. Your projects use this family to move, rename, cost, and gate technologies so the scenario can expose custom systems through the game UI.

**Architecture Notes**
This family is strongest when tech metadata comes from data dictionaries. That keeps UI and balancing changes out of the trigger orchestration code.

**Real Project Usage**
This parser feature is present in AoE2ScenarioParser but was not observed in the scanned local reference projects. Treat it as supported capability with no local canonical usage pattern yet.

**Common Pairings**
- `researching_tech`
- `technology_state`
- `send_chat`
- `display_timer`
- `activate_trigger`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

## 48. Change Civilization Name
**Method**: `change_civilization_name`
**Family**: `identity_visibility`
**Primary Role**: Change what players see and how objects or players are labeled.

**How It Is Used**
Use this family for polish, illusion, staged reveals, and scenario-controlled identity changes. It supports systems where the same gameplay object changes its name, caption, color, or apparent ownership based on scenario state.

**Architecture Notes**
Visibility and identity effects are best used as presentation layers on top of real state changes. Keep the authoritative state in variables or object data and let these effects communicate that state.

**Real Project Usage**
Observed 3 times in the scanned reference projects, primarily in LordsOfDiplomacy - Easy Mode (3 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `change_variable`
- `send_chat`
- `play_sound`
- `change_view`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

**Reference Examples**
- `LordsOfDiplomacy - Easy Mode -> characters.py:180`
- `LordsOfDiplomacy - Easy Mode -> Lords\pick_lords.py:118`
- `LordsOfDiplomacy - Easy Mode -> Lords\Unused\old_apply_lords.py:150`

## 49. Create Garrisoned Object
**Method**: `create_garrisoned_object`
**Family**: `object_control`
**Primary Role**: Create, remove, move, or command units and objects in the world.

**How It Is Used**
Use this family when the trigger system needs to directly manipulate the playable world. It covers spawning units, issuing orders, moving objects, removing temporary entities, and forcing scripted interactions that the normal AI or player input should not own.

**Architecture Notes**
World-control effects become much easier to balance when the object IDs, areas, and per-level values come from data modules. Keep world mutation code thin and let configuration determine what gets spawned or moved.

**Real Project Usage**
Observed 15 times in the scanned reference projects, primarily in LordsOfDiplomacy - Easy Mode (6 uses), GoKu RPG Project (7 uses), Hide_and_Seek (2 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `objects_in_area`
- `variable_value`
- `timer`
- `play_sound`
- `change_view`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

**Reference Examples**
- `LordsOfDiplomacy - Easy Mode -> Lords\lords_start.py:75`
- `LordsOfDiplomacy - Easy Mode -> Lords\lords_start.py:80`
- `LordsOfDiplomacy - Easy Mode -> Lords\lords_start.py:85`

## 50. Acknowledge AI Signal
**Method**: `acknowledge_ai_signal`
**Family**: `diplomacy_ai`
**Primary Role**: Change player relationships or communicate with AI-facing systems.

**How It Is Used**
Use this family for treaties, factions, scripted political actions, AI coordination, or trigger-to-AI handoffs. The effect is usually part of a dedicated diplomacy or encounter module rather than a generic combat trigger.

**Architecture Notes**
Keep diplomacy and AI signaling explicit. Scenarios become easier to reason about when relationship changes are grouped in one subsystem instead of hidden in many unrelated triggers.

**Real Project Usage**
This parser feature is present in AoE2ScenarioParser but was not observed in the scanned local reference projects. Treat it as supported capability with no local canonical usage pattern yet.

**Common Pairings**
- `diplomacy_state`
- `researching_tech`
- `send_chat`
- `play_sound`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

## 51. Modify Attribute
**Method**: `modify_attribute`
**Family**: `stat_mutation`
**Primary Role**: Change runtime object or class stats in response to scenario logic.

**How It Is Used**
This is one of the main gameplay mutation effects in your reference projects. It is used to turn scenario state into stat changes: buffs, debuffs, class scaling, temporary transformations, respawn adjustments, and balance-driven runtime tuning. It is the clearest example of why the trigger layer should read values from dictionaries instead of burying numbers inside long builder functions.

**Architecture Notes**
An agent should almost always look for the data source behind a `modify_attribute` call. The call itself is usually the endpoint of a larger data-driven design, not the place where balance truth should live.

**Real Project Usage**
Observed 390 times in the scanned reference projects, primarily in LordsOfDiplomacy - Easy Mode (109 uses), GoKu RPG Project (189 uses), Hide_and_Seek (92 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `variable_value`
- `timer`
- `change_variable`
- `script_call`
- `modify_resource`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

**Reference Examples**
- `LordsOfDiplomacy - Easy Mode -> characters.py:101`
- `LordsOfDiplomacy - Easy Mode -> characters.py:112`
- `LordsOfDiplomacy - Easy Mode -> characters.py:191`

## 52. Modify Resource
**Method**: `modify_resource`
**Family**: `resource_variable`
**Primary Role**: Move numbers between scenario state, player resources, and trigger-controlled counters.

**How It Is Used**
Use this to implement mana-like systems, costs, custom progression currencies, and player-facing economy effects. In your projects it often works alongside variable systems so one number controls internal logic while another number is exposed to the player as a resource-like mechanic.

**Architecture Notes**
Central registries and data-driven naming are critical here. Without them, a large scenario turns into a collision-prone mess of numeric IDs and unclear write paths.

**Real Project Usage**
Observed 85 times in the scanned reference projects, primarily in LordsOfDiplomacy - Easy Mode (31 uses), GoKu RPG Project (42 uses), Hide_and_Seek (12 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `variable_value`
- `compare_variables`
- `timer`
- `activate_trigger`
- `modify_attribute`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

**Reference Examples**
- `LordsOfDiplomacy - Easy Mode -> Diplomacy\Actions\Neutral\Helper_Functions\form_neutral.py:66`
- `LordsOfDiplomacy - Easy Mode -> Diplomacy\Actions\Neutral\Helper_Functions\form_neutral.py:72`
- `LordsOfDiplomacy - Easy Mode -> Diplomacy\Actions\War\Helper_Functions\form_war.py:78`

## 53. Modify Resource By Variable
**Method**: `modify_resource_by_variable`
**Family**: `resource_variable`
**Primary Role**: Move numbers between scenario state, player resources, and trigger-controlled counters.

**How It Is Used**
Use these effects when the scenario behaves like a rule system with explicit state transitions. They are responsible for cooldown counters, mana-like systems, custom resources, progression markers, and any mechanic where one trigger must write a value that another trigger later reads.

**Architecture Notes**
Central registries and data-driven naming are critical here. Without them, a large scenario turns into a collision-prone mess of numeric IDs and unclear write paths.

**Real Project Usage**
Observed 12 times in the scanned reference projects, primarily in LordsOfDiplomacy - Easy Mode (5 uses), GoKu RPG Project (7 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `variable_value`
- `compare_variables`
- `timer`
- `activate_trigger`
- `modify_attribute`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

**Reference Examples**
- `LordsOfDiplomacy - Easy Mode -> game_initialization.py:233`
- `LordsOfDiplomacy - Easy Mode -> Kingdom_Resources\helper_function.py:92`
- `LordsOfDiplomacy - Easy Mode -> Kingdom_Resources\Merchant_Opinion\merchant_opinion.py:180`

## 54. Set Building Gather Point
**Method**: `set_building_gather_point`
**Family**: `object_control`
**Primary Role**: Create, remove, move, or command units and objects in the world.

**How It Is Used**
Use this family when the trigger system needs to directly manipulate the playable world. It covers spawning units, issuing orders, moving objects, removing temporary entities, and forcing scripted interactions that the normal AI or player input should not own.

**Architecture Notes**
World-control effects become much easier to balance when the object IDs, areas, and per-level values come from data modules. Keep world mutation code thin and let configuration determine what gets spawned or moved.

**Real Project Usage**
This parser feature is present in AoE2ScenarioParser but was not observed in the scanned local reference projects. Treat it as supported capability with no local canonical usage pattern yet.

**Common Pairings**
- `objects_in_area`
- `variable_value`
- `timer`
- `play_sound`
- `change_view`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

## 55. Script Call
**Method**: `script_call`
**Family**: `resource_variable`
**Primary Role**: Move numbers between scenario state, player resources, and trigger-controlled counters.

**How It Is Used**
This effect is the trigger-to-XS execution bridge. Your projects use it when triggers should hand off computed work, object processing, or custom logic to XS, then continue with trigger-side orchestration or presentation. It keeps heavy logic out of the trigger layer while still allowing triggers to own sequencing and player feedback.

**Architecture Notes**
Use this when XS is the right home for calculation or object iteration. Do not use it as a substitute for simple trigger-side work that is clearer without a bridge.

**Real Project Usage**
Observed 159 times in the scanned reference projects, primarily in LordsOfDiplomacy - Easy Mode (75 uses), GoKu RPG Project (66 uses), Hide_and_Seek (18 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `script_call`
- `variable_value`
- `activate_trigger`
- `deactivate_trigger`
- `send_chat`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

**Reference Examples**
- `LordsOfDiplomacy - Easy Mode -> characters.py:225`
- `LordsOfDiplomacy - Easy Mode -> Clerical_Actions\Helper_Function\UNUSED_initialize_tech.py:78`
- `LordsOfDiplomacy - Easy Mode -> Court_Actions\court_actions.py:222`

## 56. Change Variable
**Method**: `change_variable`
**Family**: `resource_variable`
**Primary Role**: Move numbers between scenario state, player resources, and trigger-controlled counters.

**How It Is Used**
This is the write side of the scenario state machine. It advances quests, flips cooldown flags, stores per-player state, and records what later triggers should see through `variable_value` or other variable conditions. In practice this is one of the most important effects for keeping a scenario modular and explicit.

**Architecture Notes**
If the variable registry is clean, `change_variable` becomes a readable transition log for the whole scenario. If the registry is chaotic, this effect becomes a source of hidden coupling.

**Real Project Usage**
Observed 128 times in the scanned reference projects, primarily in LordsOfDiplomacy - Easy Mode (63 uses), GoKu RPG Project (23 uses), Hide_and_Seek (42 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `variable_value`
- `compare_variables`
- `activate_trigger`
- `deactivate_trigger`
- `modify_attribute`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

**Reference Examples**
- `LordsOfDiplomacy - Easy Mode -> characters.py:203`
- `LordsOfDiplomacy - Easy Mode -> characters.py:207`
- `LordsOfDiplomacy - Easy Mode -> characters.py:211`

## 57. Clear Timer
**Method**: `clear_timer`
**Family**: `orchestration`
**Primary Role**: Shape the trigger graph itself.

**How It Is Used**
Use this family to control which trigger modules are alive at a given moment. In large scenarios these effects are the glue between systems: one trigger finishes its responsibility, then activates the next stage and deactivates the old loop or guard trigger.

**Architecture Notes**
Good trigger architecture treats orchestration as explicit. Instead of one giant trigger trying to do everything, orchestration effects move control between small, named triggers that each own one slice of behavior.

**Real Project Usage**
Observed 2 times in the scanned reference projects, primarily in LordsOfDiplomacy - Easy Mode (1 uses), GoKu RPG Project (1 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `timer`
- `variable_value`
- `and_`
- `script_call`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

**Reference Examples**
- `LordsOfDiplomacy - Easy Mode -> Kingdom_Resources\Fame\fame_victory.py:169`
- `GoKu RPG Project -> NPC\Quests\quests.py:203`

## 58. Change Object Player Color
**Method**: `change_object_player_color`
**Family**: `identity_visibility`
**Primary Role**: Change what players see and how objects or players are labeled.

**How It Is Used**
Use this family for polish, illusion, staged reveals, and scenario-controlled identity changes. It supports systems where the same gameplay object changes its name, caption, color, or apparent ownership based on scenario state.

**Architecture Notes**
Visibility and identity effects are best used as presentation layers on top of real state changes. Keep the authoritative state in variables or object data and let these effects communicate that state.

**Real Project Usage**
This parser feature is present in AoE2ScenarioParser but was not observed in the scanned local reference projects. Treat it as supported capability with no local canonical usage pattern yet.

**Common Pairings**
- `change_variable`
- `send_chat`
- `play_sound`
- `change_view`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

## 59. Change Object Civilization Name
**Method**: `change_object_civilization_name`
**Family**: `identity_visibility`
**Primary Role**: Change what players see and how objects or players are labeled.

**How It Is Used**
Use this family for polish, illusion, staged reveals, and scenario-controlled identity changes. It supports systems where the same gameplay object changes its name, caption, color, or apparent ownership based on scenario state.

**Architecture Notes**
Visibility and identity effects are best used as presentation layers on top of real state changes. Keep the authoritative state in variables or object data and let these effects communicate that state.

**Real Project Usage**
Observed 3 times in the scanned reference projects, primarily in GoKu RPG Project (3 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `change_variable`
- `send_chat`
- `play_sound`
- `change_view`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

**Reference Examples**
- `GoKu RPG Project -> NPC\Names\npc_names.py:142`
- `GoKu RPG Project -> Upgrade_Store\Scenario_Triggers\Initializations\initialize_shop_description.py:97`
- `GoKu RPG Project -> Upgrade_Store\Scenario_Triggers\Initializations\initialize_shop_description.py:106`

## 60. Change Object Player Name
**Method**: `change_object_player_name`
**Family**: `identity_visibility`
**Primary Role**: Change what players see and how objects or players are labeled.

**How It Is Used**
Use this family for polish, illusion, staged reveals, and scenario-controlled identity changes. It supports systems where the same gameplay object changes its name, caption, color, or apparent ownership based on scenario state.

**Architecture Notes**
Visibility and identity effects are best used as presentation layers on top of real state changes. Keep the authoritative state in variables or object data and let these effects communicate that state.

**Real Project Usage**
Observed 1 times in the scanned reference projects, primarily in GoKu RPG Project (1 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `change_variable`
- `send_chat`
- `play_sound`
- `change_view`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

**Reference Examples**
- `GoKu RPG Project -> Upgrade_Store\Scenario_Triggers\Initializations\initialize_shop_description.py:88`

## 61. Disable Unit Targeting
**Method**: `disable_unit_targeting`
**Family**: `interaction_control`
**Primary Role**: Temporarily allow or forbid player interaction with units or objects.

**How It Is Used**
Use this family for cutscenes, stuns, protected summons, invulnerability windows, interface locking, or scripted sequences where players should not be able to interfere with the system at the wrong time.

**Architecture Notes**
Interaction locks are safest when paired with clear activation and cleanup triggers. The biggest failure mode is forgetting to re-enable the thing that was disabled.

**Real Project Usage**
Observed 33 times in the scanned reference projects, primarily in LordsOfDiplomacy - Easy Mode (14 uses), GoKu RPG Project (8 uses), Hide_and_Seek (11 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `timer`
- `activate_trigger`
- `deactivate_trigger`
- `play_sound`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

**Reference Examples**
- `LordsOfDiplomacy - Easy Mode -> Clerical_Actions\Initializations\initialize_cleric.py:24`
- `LordsOfDiplomacy - Easy Mode -> Clerical_Actions\Initializations\initialize_cleric.py:140`
- `LordsOfDiplomacy - Easy Mode -> Diplomacy\Diplomacy_Panel\base_units\deploy_units.py:93`

## 62. Enable Unit Targeting
**Method**: `enable_unit_targeting`
**Family**: `interaction_control`
**Primary Role**: Temporarily allow or forbid player interaction with units or objects.

**How It Is Used**
Use this family for cutscenes, stuns, protected summons, invulnerability windows, interface locking, or scripted sequences where players should not be able to interfere with the system at the wrong time.

**Architecture Notes**
Interaction locks are safest when paired with clear activation and cleanup triggers. The biggest failure mode is forgetting to re-enable the thing that was disabled.

**Real Project Usage**
Observed 4 times in the scanned reference projects, primarily in GoKu RPG Project (4 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `timer`
- `activate_trigger`
- `deactivate_trigger`
- `play_sound`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

**Reference Examples**
- `GoKu RPG Project -> Abilities\Crusader\Active_Ability_1\valors_call.py:34`
- `GoKu RPG Project -> Bosses\Boss_System.py:114`
- `GoKu RPG Project -> Skill_Tree\Skill_Tree_Ability.py:146`

## 63. Change Technology Cost
**Method**: `change_technology_cost`
**Family**: `tech_edit`
**Primary Role**: Turn technologies into a scenario-controlled interface and progression surface.

**How It Is Used**
Use these effects when technologies are serving as buttons, unlock panels, class menus, or progression displays rather than only vanilla researches. Your projects use this family to move, rename, cost, and gate technologies so the scenario can expose custom systems through the game UI.

**Architecture Notes**
This family is strongest when tech metadata comes from data dictionaries. That keeps UI and balancing changes out of the trigger orchestration code.

**Real Project Usage**
Observed 7 times in the scanned reference projects, primarily in LordsOfDiplomacy - Easy Mode (5 uses), GoKu RPG Project (1 uses), Hide_and_Seek (1 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `researching_tech`
- `technology_state`
- `send_chat`
- `display_timer`
- `activate_trigger`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

**Reference Examples**
- `LordsOfDiplomacy - Easy Mode -> Clerical_Actions\Helper_Function\UNUSED_initialize_tech.py:62`
- `LordsOfDiplomacy - Easy Mode -> Court_Actions\court_actions.py:205`
- `LordsOfDiplomacy - Easy Mode -> Diplomacy\Actions\Helper_Functions\display_offer.py:73`

## 64. Change Technology Research Time
**Method**: `change_technology_research_time`
**Family**: `tech_edit`
**Primary Role**: Turn technologies into a scenario-controlled interface and progression surface.

**How It Is Used**
Use these effects when technologies are serving as buttons, unlock panels, class menus, or progression displays rather than only vanilla researches. Your projects use this family to move, rename, cost, and gate technologies so the scenario can expose custom systems through the game UI.

**Architecture Notes**
This family is strongest when tech metadata comes from data dictionaries. That keeps UI and balancing changes out of the trigger orchestration code.

**Real Project Usage**
Observed 5 times in the scanned reference projects, primarily in LordsOfDiplomacy - Easy Mode (5 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `researching_tech`
- `technology_state`
- `send_chat`
- `display_timer`
- `activate_trigger`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

**Reference Examples**
- `LordsOfDiplomacy - Easy Mode -> Clerical_Actions\Helper_Function\UNUSED_initialize_tech.py:57`
- `LordsOfDiplomacy - Easy Mode -> Court_Actions\court_actions.py:200`
- `LordsOfDiplomacy - Easy Mode -> Diplomacy\Actions\Helper_Functions\display_offer.py:68`

## 65. Change Technology Name
**Method**: `change_technology_name`
**Family**: `tech_edit`
**Primary Role**: Turn technologies into a scenario-controlled interface and progression surface.

**How It Is Used**
Use these effects when technologies are serving as buttons, unlock panels, class menus, or progression displays rather than only vanilla researches. Your projects use this family to move, rename, cost, and gate technologies so the scenario can expose custom systems through the game UI.

**Architecture Notes**
This family is strongest when tech metadata comes from data dictionaries. That keeps UI and balancing changes out of the trigger orchestration code.

**Real Project Usage**
Observed 5 times in the scanned reference projects, primarily in LordsOfDiplomacy - Easy Mode (5 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `researching_tech`
- `technology_state`
- `send_chat`
- `display_timer`
- `activate_trigger`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

**Reference Examples**
- `LordsOfDiplomacy - Easy Mode -> Clerical_Actions\Helper_Function\UNUSED_initialize_tech.py:46`
- `LordsOfDiplomacy - Easy Mode -> Court_Actions\court_actions.py:189`
- `LordsOfDiplomacy - Easy Mode -> Diplomacy\Actions\Helper_Functions\display_offer.py:58`

## 66. Change Technology Description
**Method**: `change_technology_description`
**Family**: `tech_edit`
**Primary Role**: Turn technologies into a scenario-controlled interface and progression surface.

**How It Is Used**
Use these effects when technologies are serving as buttons, unlock panels, class menus, or progression displays rather than only vanilla researches. Your projects use this family to move, rename, cost, and gate technologies so the scenario can expose custom systems through the game UI.

**Architecture Notes**
This family is strongest when tech metadata comes from data dictionaries. That keeps UI and balancing changes out of the trigger orchestration code.

**Real Project Usage**
Observed 4 times in the scanned reference projects, primarily in LordsOfDiplomacy - Easy Mode (4 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `researching_tech`
- `technology_state`
- `send_chat`
- `display_timer`
- `activate_trigger`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

**Reference Examples**
- `LordsOfDiplomacy - Easy Mode -> Clerical_Actions\Helper_Function\UNUSED_initialize_tech.py:51`
- `LordsOfDiplomacy - Easy Mode -> Court_Actions\court_actions.py:194`
- `LordsOfDiplomacy - Easy Mode -> Diplomacy\Actions\Helper_Functions\display_offer.py:63`

## 67. Enable Technology Stacking
**Method**: `enable_technology_stacking`
**Family**: `tech_edit`
**Primary Role**: Turn technologies into a scenario-controlled interface and progression surface.

**How It Is Used**
Use these effects when technologies are serving as buttons, unlock panels, class menus, or progression displays rather than only vanilla researches. Your projects use this family to move, rename, cost, and gate technologies so the scenario can expose custom systems through the game UI.

**Architecture Notes**
This family is strongest when tech metadata comes from data dictionaries. That keeps UI and balancing changes out of the trigger orchestration code.

**Real Project Usage**
Observed 5 times in the scanned reference projects, primarily in LordsOfDiplomacy - Easy Mode (5 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `researching_tech`
- `technology_state`
- `send_chat`
- `display_timer`
- `activate_trigger`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

**Reference Examples**
- `LordsOfDiplomacy - Easy Mode -> Clerical_Actions\Helper_Function\UNUSED_initialize_tech.py:36`
- `LordsOfDiplomacy - Easy Mode -> Court_Actions\court_actions.py:179`
- `LordsOfDiplomacy - Easy Mode -> Diplomacy\Actions\Helper_Functions\display_offer.py:48`

## 68. Disable Technology Stacking
**Method**: `disable_technology_stacking`
**Family**: `tech_edit`
**Primary Role**: Turn technologies into a scenario-controlled interface and progression surface.

**How It Is Used**
Use these effects when technologies are serving as buttons, unlock panels, class menus, or progression displays rather than only vanilla researches. Your projects use this family to move, rename, cost, and gate technologies so the scenario can expose custom systems through the game UI.

**Architecture Notes**
This family is strongest when tech metadata comes from data dictionaries. That keeps UI and balancing changes out of the trigger orchestration code.

**Real Project Usage**
This parser feature is present in AoE2ScenarioParser but was not observed in the scanned local reference projects. Treat it as supported capability with no local canonical usage pattern yet.

**Common Pairings**
- `researching_tech`
- `technology_state`
- `send_chat`
- `display_timer`
- `activate_trigger`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

## 69. Acknowledge Multiplayer AI Signal
**Method**: `acknowledge_multiplayer_ai_signal`
**Family**: `diplomacy_ai`
**Primary Role**: Change player relationships or communicate with AI-facing systems.

**How It Is Used**
Use this family for treaties, factions, scripted political actions, AI coordination, or trigger-to-AI handoffs. The effect is usually part of a dedicated diplomacy or encounter module rather than a generic combat trigger.

**Architecture Notes**
Keep diplomacy and AI signaling explicit. Scenarios become easier to reason about when relationship changes are grouped in one subsystem instead of hidden in many unrelated triggers.

**Real Project Usage**
This parser feature is present in AoE2ScenarioParser but was not observed in the scanned local reference projects. Treat it as supported capability with no local canonical usage pattern yet.

**Common Pairings**
- `diplomacy_state`
- `researching_tech`
- `send_chat`
- `play_sound`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

## 70. Disable Object Selection
**Method**: `disable_object_selection`
**Family**: `interaction_control`
**Primary Role**: Temporarily allow or forbid player interaction with units or objects.

**How It Is Used**
Use this family for cutscenes, stuns, protected summons, invulnerability windows, interface locking, or scripted sequences where players should not be able to interfere with the system at the wrong time.

**Architecture Notes**
Interaction locks are safest when paired with clear activation and cleanup triggers. The biggest failure mode is forgetting to re-enable the thing that was disabled.

**Real Project Usage**
Observed 32 times in the scanned reference projects, primarily in LordsOfDiplomacy - Easy Mode (10 uses), GoKu RPG Project (8 uses), Hide_and_Seek (14 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `timer`
- `activate_trigger`
- `deactivate_trigger`
- `play_sound`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

**Reference Examples**
- `LordsOfDiplomacy - Easy Mode -> cut_scenes.py:115`
- `LordsOfDiplomacy - Easy Mode -> Espionage\Actions\Open_Enemy_Gates\apply_open_enemy_gates.py:98`
- `LordsOfDiplomacy - Easy Mode -> main\Lords_of_Diplomacy.py:185`

## 71. Enable Object Selection
**Method**: `enable_object_selection`
**Family**: `interaction_control`
**Primary Role**: Temporarily allow or forbid player interaction with units or objects.

**How It Is Used**
Use this family for cutscenes, stuns, protected summons, invulnerability windows, interface locking, or scripted sequences where players should not be able to interfere with the system at the wrong time.

**Architecture Notes**
Interaction locks are safest when paired with clear activation and cleanup triggers. The biggest failure mode is forgetting to re-enable the thing that was disabled.

**Real Project Usage**
Observed 13 times in the scanned reference projects, primarily in LordsOfDiplomacy - Easy Mode (4 uses), GoKu RPG Project (4 uses), Hide_and_Seek (5 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `timer`
- `activate_trigger`
- `deactivate_trigger`
- `play_sound`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

**Reference Examples**
- `LordsOfDiplomacy - Easy Mode -> cut_scenes.py:118`
- `LordsOfDiplomacy - Easy Mode -> cut_scenes.py:431`
- `LordsOfDiplomacy - Easy Mode -> cut_scenes.py:763`

## 72. Change Color Mood
**Method**: `change_color_mood`
**Family**: `identity_visibility`
**Primary Role**: Change what players see and how objects or players are labeled.

**How It Is Used**
Use this family for polish, illusion, staged reveals, and scenario-controlled identity changes. It supports systems where the same gameplay object changes its name, caption, color, or apparent ownership based on scenario state.

**Architecture Notes**
Visibility and identity effects are best used as presentation layers on top of real state changes. Keep the authoritative state in variables or object data and let these effects communicate that state.

**Real Project Usage**
Observed 4 times in the scanned reference projects, primarily in LordsOfDiplomacy - Easy Mode (2 uses), Hide_and_Seek (2 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `change_variable`
- `send_chat`
- `play_sound`
- `change_view`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

**Reference Examples**
- `LordsOfDiplomacy - Easy Mode -> main\remove_resources.py:48`
- `LordsOfDiplomacy - Easy Mode -> Seasons\apply_seasons.py:26`
- `Hide_and_Seek -> Abilities\Hunter\Active_Ability_1\blood_thirst.py:50`

## 9999. add_train_location
**Method**: `add_train_location`
**Family**: `tech_edit`
**Primary Role**: Turn technologies into a scenario-controlled interface and progression surface.

**How It Is Used**
Use these effects when technologies are serving as buttons, unlock panels, class menus, or progression displays rather than only vanilla researches. Your projects use this family to move, rename, cost, and gate technologies so the scenario can expose custom systems through the game UI.

**Architecture Notes**
This family is strongest when tech metadata comes from data dictionaries. That keeps UI and balancing changes out of the trigger orchestration code.

**Real Project Usage**
This parser feature is present in AoE2ScenarioParser but was not observed in the scanned local reference projects. Treat it as supported capability with no local canonical usage pattern yet.

**Common Pairings**
- `researching_tech`
- `technology_state`
- `send_chat`
- `display_timer`
- `activate_trigger`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

## 9999. change_object_caption
**Method**: `change_object_caption`
**Family**: `identity_visibility`
**Primary Role**: Change what players see and how objects or players are labeled.

**How It Is Used**
Use this family for polish, illusion, staged reveals, and scenario-controlled identity changes. It supports systems where the same gameplay object changes its name, caption, color, or apparent ownership based on scenario state.

**Architecture Notes**
Visibility and identity effects are best used as presentation layers on top of real state changes. Keep the authoritative state in variables or object data and let these effects communicate that state.

**Real Project Usage**
Observed 17 times in the scanned reference projects, primarily in GoKu RPG Project (6 uses), Hide_and_Seek (11 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `change_variable`
- `send_chat`
- `play_sound`
- `change_view`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

**Reference Examples**
- `GoKu RPG Project -> Bosses\Dialogue\boss_dialogue.py:90`
- `GoKu RPG Project -> NPC\Dialogue\npc_dialogue.py:113`
- `GoKu RPG Project -> Player_Progression\Leveling\leveling.py:294`

## 9999. change_object_visibility
**Method**: `change_object_visibility`
**Family**: `identity_visibility`
**Primary Role**: Change what players see and how objects or players are labeled.

**How It Is Used**
Use this family for polish, illusion, staged reveals, and scenario-controlled identity changes. It supports systems where the same gameplay object changes its name, caption, color, or apparent ownership based on scenario state.

**Architecture Notes**
Visibility and identity effects are best used as presentation layers on top of real state changes. Keep the authoritative state in variables or object data and let these effects communicate that state.

**Real Project Usage**
Observed 4 times in the scanned reference projects, primarily in GoKu RPG Project (4 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `change_variable`
- `send_chat`
- `play_sound`
- `change_view`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

**Reference Examples**
- `GoKu RPG Project -> NPC\Quests\Estea\Captain_Jorand\Clearing_The_Depths\apply_quest.py:52`
- `GoKu RPG Project -> NPC\Quests\Estea\Captain_Jorand\Forest_Cleanup\apply_quest.py:41`
- `GoKu RPG Project -> NPC\Quests\Estea\Elder_Beltherin\Speak_to_Captain_Jorand\apply_quest.py:29`

## 9999. change_player_color
**Method**: `change_player_color`
**Family**: `identity_visibility`
**Primary Role**: Change what players see and how objects or players are labeled.

**How It Is Used**
Use this family for polish, illusion, staged reveals, and scenario-controlled identity changes. It supports systems where the same gameplay object changes its name, caption, color, or apparent ownership based on scenario state.

**Architecture Notes**
Visibility and identity effects are best used as presentation layers on top of real state changes. Keep the authoritative state in variables or object data and let these effects communicate that state.

**Real Project Usage**
This parser feature is present in AoE2ScenarioParser but was not observed in the scanned local reference projects. Treat it as supported capability with no local canonical usage pattern yet.

**Common Pairings**
- `change_variable`
- `send_chat`
- `play_sound`
- `change_view`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

## 9999. change_technology_hotkey
**Method**: `change_technology_hotkey`
**Family**: `tech_edit`
**Primary Role**: Turn technologies into a scenario-controlled interface and progression surface.

**How It Is Used**
Use these effects when technologies are serving as buttons, unlock panels, class menus, or progression displays rather than only vanilla researches. Your projects use this family to move, rename, cost, and gate technologies so the scenario can expose custom systems through the game UI.

**Architecture Notes**
This family is strongest when tech metadata comes from data dictionaries. That keeps UI and balancing changes out of the trigger orchestration code.

**Real Project Usage**
This parser feature is present in AoE2ScenarioParser but was not observed in the scanned local reference projects. Treat it as supported capability with no local canonical usage pattern yet.

**Common Pairings**
- `researching_tech`
- `technology_state`
- `send_chat`
- `display_timer`
- `activate_trigger`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

## 9999. change_technology_icon
**Method**: `change_technology_icon`
**Family**: `tech_edit`
**Primary Role**: Turn technologies into a scenario-controlled interface and progression surface.

**How It Is Used**
Use these effects when technologies are serving as buttons, unlock panels, class menus, or progression displays rather than only vanilla researches. Your projects use this family to move, rename, cost, and gate technologies so the scenario can expose custom systems through the game UI.

**Architecture Notes**
This family is strongest when tech metadata comes from data dictionaries. That keeps UI and balancing changes out of the trigger orchestration code.

**Real Project Usage**
This parser feature is present in AoE2ScenarioParser but was not observed in the scanned local reference projects. Treat it as supported capability with no local canonical usage pattern yet.

**Common Pairings**
- `researching_tech`
- `technology_state`
- `send_chat`
- `display_timer`
- `activate_trigger`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

## 9999. change_technology_location
**Method**: `change_technology_location`
**Family**: `tech_edit`
**Primary Role**: Turn technologies into a scenario-controlled interface and progression surface.

**How It Is Used**
Your reference projects use technology relocation as part of a custom interface pattern. The technology is not just a normal research; it becomes a positioned button or menu element inside a scenario-controlled UI.

**Architecture Notes**
This family is strongest when tech metadata comes from data dictionaries. That keeps UI and balancing changes out of the trigger orchestration code.

**Real Project Usage**
Observed 15 times in the scanned reference projects, primarily in LordsOfDiplomacy - Easy Mode (15 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `researching_tech`
- `technology_state`
- `send_chat`
- `display_timer`
- `activate_trigger`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

**Reference Examples**
- `LordsOfDiplomacy - Easy Mode -> Clerical_Actions\Helper_Function\UNUSED_initialize_tech.py:40`
- `LordsOfDiplomacy - Easy Mode -> Court_Actions\court_actions.py:183`
- `LordsOfDiplomacy - Easy Mode -> Diplomacy\Actions\Alliance\apply_alliance.py:251`

## 9999. count_units_into_variable
**Method**: `count_units_into_variable`
**Family**: `resource_variable`
**Primary Role**: Move numbers between scenario state, player resources, and trigger-controlled counters.

**How It Is Used**
Use these effects when the scenario behaves like a rule system with explicit state transitions. They are responsible for cooldown counters, mana-like systems, custom resources, progression markers, and any mechanic where one trigger must write a value that another trigger later reads.

**Architecture Notes**
Central registries and data-driven naming are critical here. Without them, a large scenario turns into a collision-prone mess of numeric IDs and unclear write paths.

**Real Project Usage**
This parser feature is present in AoE2ScenarioParser but was not observed in the scanned local reference projects. Treat it as supported capability with no local canonical usage pattern yet.

**Common Pairings**
- `variable_value`
- `compare_variables`
- `timer`
- `activate_trigger`
- `modify_attribute`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

## 9999. create_decision
**Method**: `create_decision`
**Family**: `persistence`
**Primary Role**: Store scenario-side state in key-value or decision systems.

**How It Is Used**
Use this family when the scenario wants a persistence-like or indexed-state layer that is not just one flat variable registry. It is useful for data-driven systems, loot or inventory state, and situations where triggers need to create or query structured records.

**Architecture Notes**
This family matters most when the rest of the project is already modular. If the data model is unclear, adding persistence effects will only make the system harder to reason about.

**Real Project Usage**
This parser feature is present in AoE2ScenarioParser but was not observed in the scanned local reference projects. Treat it as supported capability with no local canonical usage pattern yet.

**Common Pairings**
- `variable_value`
- `compare_variables`
- `create_decision`
- `load_key_value`
- `store_key_value`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

## 9999. create_object_armor
**Method**: `create_object_armor`
**Family**: `stat_mutation`
**Primary Role**: Change runtime object or class stats in response to scenario logic.

**How It Is Used**
Use this family for buffs, debuffs, scaling systems, class growth, difficulty adjustments, and temporary ability states. In your reference projects stat mutation is one of the main ways triggers turn variables and timers into visible gameplay consequences.

**Architecture Notes**
This family is where data-driven balancing matters most. If numbers are spread through trigger builders, later balance passes become expensive and error-prone. Keep the values in dictionaries and let trigger code only apply them.

**Real Project Usage**
This parser feature is present in AoE2ScenarioParser but was not observed in the scanned local reference projects. Treat it as supported capability with no local canonical usage pattern yet.

**Common Pairings**
- `variable_value`
- `change_variable`
- `timer`
- `script_call`
- `modify_resource`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

## 9999. create_object_attack
**Method**: `create_object_attack`
**Family**: `stat_mutation`
**Primary Role**: Change runtime object or class stats in response to scenario logic.

**How It Is Used**
Use this family for buffs, debuffs, scaling systems, class growth, difficulty adjustments, and temporary ability states. In your reference projects stat mutation is one of the main ways triggers turn variables and timers into visible gameplay consequences.

**Architecture Notes**
This family is where data-driven balancing matters most. If numbers are spread through trigger builders, later balance passes become expensive and error-prone. Keep the values in dictionaries and let trigger code only apply them.

**Real Project Usage**
This parser feature is present in AoE2ScenarioParser but was not observed in the scanned local reference projects. Treat it as supported capability with no local canonical usage pattern yet.

**Common Pairings**
- `variable_value`
- `change_variable`
- `timer`
- `script_call`
- `modify_resource`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

## 9999. delete_key
**Method**: `delete_key`
**Family**: `persistence`
**Primary Role**: Store scenario-side state in key-value or decision systems.

**How It Is Used**
Use this family when the scenario wants a persistence-like or indexed-state layer that is not just one flat variable registry. It is useful for data-driven systems, loot or inventory state, and situations where triggers need to create or query structured records.

**Architecture Notes**
This family matters most when the rest of the project is already modular. If the data model is unclear, adding persistence effects will only make the system harder to reason about.

**Real Project Usage**
This parser feature is present in AoE2ScenarioParser but was not observed in the scanned local reference projects. Treat it as supported capability with no local canonical usage pattern yet.

**Common Pairings**
- `variable_value`
- `compare_variables`
- `create_decision`
- `load_key_value`
- `store_key_value`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

## 9999. disable_object_deletion
**Method**: `disable_object_deletion`
**Family**: `interaction_control`
**Primary Role**: Temporarily allow or forbid player interaction with units or objects.

**How It Is Used**
Use this family for cutscenes, stuns, protected summons, invulnerability windows, interface locking, or scripted sequences where players should not be able to interfere with the system at the wrong time.

**Architecture Notes**
Interaction locks are safest when paired with clear activation and cleanup triggers. The biggest failure mode is forgetting to re-enable the thing that was disabled.

**Real Project Usage**
Observed 29 times in the scanned reference projects, primarily in LordsOfDiplomacy - Easy Mode (16 uses), GoKu RPG Project (4 uses), Hide_and_Seek (9 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `timer`
- `activate_trigger`
- `deactivate_trigger`
- `play_sound`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

**Reference Examples**
- `LordsOfDiplomacy - Easy Mode -> characters.py:71`
- `LordsOfDiplomacy - Easy Mode -> Clerical_Actions\Initializations\initialize_cleric.py:28`
- `LordsOfDiplomacy - Easy Mode -> Clerical_Actions\Initializations\initialize_cleric.py:144`

## 9999. disable_unit_attackable
**Method**: `disable_unit_attackable`
**Family**: `interaction_control`
**Primary Role**: Temporarily allow or forbid player interaction with units or objects.

**How It Is Used**
Use this family for cutscenes, stuns, protected summons, invulnerability windows, interface locking, or scripted sequences where players should not be able to interfere with the system at the wrong time.

**Architecture Notes**
Interaction locks are safest when paired with clear activation and cleanup triggers. The biggest failure mode is forgetting to re-enable the thing that was disabled.

**Real Project Usage**
Observed 12 times in the scanned reference projects, primarily in GoKu RPG Project (3 uses), Hide_and_Seek (9 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `timer`
- `activate_trigger`
- `deactivate_trigger`
- `play_sound`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

**Reference Examples**
- `GoKu RPG Project -> Skill_Tree\Classes_Skill_Tree\Cleric\Active\Active_Ability_3\guardians_embrace.py:324`
- `GoKu RPG Project -> Skill_Tree\Skill_Tree_Ability.py:203`
- `GoKu RPG Project -> Skill_Tree\Skill_Tree_Ability.py:298`

## 9999. enable_object_deletion
**Method**: `enable_object_deletion`
**Family**: `interaction_control`
**Primary Role**: Temporarily allow or forbid player interaction with units or objects.

**How It Is Used**
Use this family for cutscenes, stuns, protected summons, invulnerability windows, interface locking, or scripted sequences where players should not be able to interfere with the system at the wrong time.

**Architecture Notes**
Interaction locks are safest when paired with clear activation and cleanup triggers. The biggest failure mode is forgetting to re-enable the thing that was disabled.

**Real Project Usage**
This parser feature is present in AoE2ScenarioParser but was not observed in the scanned local reference projects. Treat it as supported capability with no local canonical usage pattern yet.

**Common Pairings**
- `timer`
- `activate_trigger`
- `deactivate_trigger`
- `play_sound`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

## 9999. enable_unit_attackable
**Method**: `enable_unit_attackable`
**Family**: `interaction_control`
**Primary Role**: Temporarily allow or forbid player interaction with units or objects.

**How It Is Used**
Use this family for cutscenes, stuns, protected summons, invulnerability windows, interface locking, or scripted sequences where players should not be able to interfere with the system at the wrong time.

**Architecture Notes**
Interaction locks are safest when paired with clear activation and cleanup triggers. The biggest failure mode is forgetting to re-enable the thing that was disabled.

**Real Project Usage**
Observed 2 times in the scanned reference projects, primarily in GoKu RPG Project (2 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `timer`
- `activate_trigger`
- `deactivate_trigger`
- `play_sound`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

**Reference Examples**
- `GoKu RPG Project -> Skill_Tree\Skill_Tree_Ability.py:149`
- `GoKu RPG Project -> Skill_Tree\Skill_Tree_Ability.py:223`

## 9999. initiate_research
**Method**: `initiate_research`
**Family**: `tech_edit`
**Primary Role**: Turn technologies into a scenario-controlled interface and progression surface.

**How It Is Used**
Use these effects when technologies are serving as buttons, unlock panels, class menus, or progression displays rather than only vanilla researches. Your projects use this family to move, rename, cost, and gate technologies so the scenario can expose custom systems through the game UI.

**Architecture Notes**
This family is strongest when tech metadata comes from data dictionaries. That keeps UI and balancing changes out of the trigger orchestration code.

**Real Project Usage**
This parser feature is present in AoE2ScenarioParser but was not observed in the scanned local reference projects. Treat it as supported capability with no local canonical usage pattern yet.

**Common Pairings**
- `researching_tech`
- `technology_state`
- `send_chat`
- `display_timer`
- `activate_trigger`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

## 9999. load_key_value
**Method**: `load_key_value`
**Family**: `persistence`
**Primary Role**: Store scenario-side state in key-value or decision systems.

**How It Is Used**
Use this family when the scenario wants a persistence-like or indexed-state layer that is not just one flat variable registry. It is useful for data-driven systems, loot or inventory state, and situations where triggers need to create or query structured records.

**Architecture Notes**
This family matters most when the rest of the project is already modular. If the data model is unclear, adding persistence effects will only make the system harder to reason about.

**Real Project Usage**
This parser feature is present in AoE2ScenarioParser but was not observed in the scanned local reference projects. Treat it as supported capability with no local canonical usage pattern yet.

**Common Pairings**
- `variable_value`
- `compare_variables`
- `create_decision`
- `load_key_value`
- `store_key_value`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

## 9999. modify_attribute_by_variable
**Method**: `modify_attribute_by_variable`
**Family**: `stat_mutation`
**Primary Role**: Change runtime object or class stats in response to scenario logic.

**How It Is Used**
Use this family for buffs, debuffs, scaling systems, class growth, difficulty adjustments, and temporary ability states. In your reference projects stat mutation is one of the main ways triggers turn variables and timers into visible gameplay consequences.

**Architecture Notes**
This family is where data-driven balancing matters most. If numbers are spread through trigger builders, later balance passes become expensive and error-prone. Keep the values in dictionaries and let trigger code only apply them.

**Real Project Usage**
Observed 1 times in the scanned reference projects, primarily in GoKu RPG Project (1 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `variable_value`
- `change_variable`
- `timer`
- `script_call`
- `modify_resource`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

**Reference Examples**
- `GoKu RPG Project -> Leveling_System.py:162`

## 9999. modify_attribute_for_class
**Method**: `modify_attribute_for_class`
**Family**: `stat_mutation`
**Primary Role**: Change runtime object or class stats in response to scenario logic.

**How It Is Used**
Use this family for buffs, debuffs, scaling systems, class growth, difficulty adjustments, and temporary ability states. In your reference projects stat mutation is one of the main ways triggers turn variables and timers into visible gameplay consequences.

**Architecture Notes**
This family is where data-driven balancing matters most. If numbers are spread through trigger builders, later balance passes become expensive and error-prone. Keep the values in dictionaries and let trigger code only apply them.

**Real Project Usage**
This parser feature is present in AoE2ScenarioParser but was not observed in the scanned local reference projects. Treat it as supported capability with no local canonical usage pattern yet.

**Common Pairings**
- `variable_value`
- `change_variable`
- `timer`
- `script_call`
- `modify_resource`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

## 9999. modify_object_attribute
**Method**: `modify_object_attribute`
**Family**: `stat_mutation`
**Primary Role**: Change runtime object or class stats in response to scenario logic.

**How It Is Used**
Use this family for buffs, debuffs, scaling systems, class growth, difficulty adjustments, and temporary ability states. In your reference projects stat mutation is one of the main ways triggers turn variables and timers into visible gameplay consequences.

**Architecture Notes**
This family is where data-driven balancing matters most. If numbers are spread through trigger builders, later balance passes become expensive and error-prone. Keep the values in dictionaries and let trigger code only apply them.

**Real Project Usage**
Observed 2 times in the scanned reference projects, primarily in GoKu RPG Project (2 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `variable_value`
- `change_variable`
- `timer`
- `script_call`
- `modify_resource`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

**Reference Examples**
- `GoKu RPG Project -> Skill_Tree\Skill_Tree_Ability.py:96`
- `GoKu RPG Project -> Skill_Tree\Skill_Tree_Ability.py:187`

## 9999. modify_object_attribute_by_variable
**Method**: `modify_object_attribute_by_variable`
**Family**: `stat_mutation`
**Primary Role**: Change runtime object or class stats in response to scenario logic.

**How It Is Used**
Use this family for buffs, debuffs, scaling systems, class growth, difficulty adjustments, and temporary ability states. In your reference projects stat mutation is one of the main ways triggers turn variables and timers into visible gameplay consequences.

**Architecture Notes**
This family is where data-driven balancing matters most. If numbers are spread through trigger builders, later balance passes become expensive and error-prone. Keep the values in dictionaries and let trigger code only apply them.

**Real Project Usage**
This parser feature is present in AoE2ScenarioParser but was not observed in the scanned local reference projects. Treat it as supported capability with no local canonical usage pattern yet.

**Common Pairings**
- `variable_value`
- `change_variable`
- `timer`
- `script_call`
- `modify_resource`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

## 9999. modify_variable_by_attribute
**Method**: `modify_variable_by_attribute`
**Family**: `resource_variable`
**Primary Role**: Move numbers between scenario state, player resources, and trigger-controlled counters.

**How It Is Used**
Use these effects when the scenario behaves like a rule system with explicit state transitions. They are responsible for cooldown counters, mana-like systems, custom resources, progression markers, and any mechanic where one trigger must write a value that another trigger later reads.

**Architecture Notes**
Central registries and data-driven naming are critical here. Without them, a large scenario turns into a collision-prone mess of numeric IDs and unclear write paths.

**Real Project Usage**
Observed 4 times in the scanned reference projects, primarily in GoKu RPG Project (4 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `variable_value`
- `compare_variables`
- `timer`
- `activate_trigger`
- `modify_attribute`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

**Reference Examples**
- `GoKu RPG Project -> Abilities\Berserker\Active_Ability_2\bloodlust_frenzy.py:96`
- `GoKu RPG Project -> Abilities\Ranger\Active_Ability_2\soul_siphon.py:63`
- `GoKu RPG Project -> Leveling_System.py:171`

## 9999. modify_variable_by_resource
**Method**: `modify_variable_by_resource`
**Family**: `resource_variable`
**Primary Role**: Move numbers between scenario state, player resources, and trigger-controlled counters.

**How It Is Used**
Use these effects when the scenario behaves like a rule system with explicit state transitions. They are responsible for cooldown counters, mana-like systems, custom resources, progression markers, and any mechanic where one trigger must write a value that another trigger later reads.

**Architecture Notes**
Central registries and data-driven naming are critical here. Without them, a large scenario turns into a collision-prone mess of numeric IDs and unclear write paths.

**Real Project Usage**
Observed 2 times in the scanned reference projects, primarily in GoKu RPG Project (2 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `variable_value`
- `compare_variables`
- `timer`
- `activate_trigger`
- `modify_attribute`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

**Reference Examples**
- `GoKu RPG Project -> Player_Progression\Attributes\balance_mana.py:78`
- `GoKu RPG Project -> Player_Progression\Attributes\balance_mana.py:112`

## 9999. modify_variable_by_variable
**Method**: `modify_variable_by_variable`
**Family**: `resource_variable`
**Primary Role**: Move numbers between scenario state, player resources, and trigger-controlled counters.

**How It Is Used**
Use these effects when the scenario behaves like a rule system with explicit state transitions. They are responsible for cooldown counters, mana-like systems, custom resources, progression markers, and any mechanic where one trigger must write a value that another trigger later reads.

**Architecture Notes**
Central registries and data-driven naming are critical here. Without them, a large scenario turns into a collision-prone mess of numeric IDs and unclear write paths.

**Real Project Usage**
This parser feature is present in AoE2ScenarioParser but was not observed in the scanned local reference projects. Treat it as supported capability with no local canonical usage pattern yet.

**Common Pairings**
- `variable_value`
- `compare_variables`
- `timer`
- `activate_trigger`
- `modify_attribute`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

## 9999. none
**Method**: `none`
**Family**: `special`
**Primary Role**: Handle niche scenario actions that do not fit the main families.

**How It Is Used**
Use these only when the scenario specifically needs their engine behavior. They are valid tools, but they should usually appear inside a narrow subsystem rather than as general-purpose building blocks.

**Architecture Notes**
Agents should check whether a more common family already solves the task before choosing one of these effects.

**Real Project Usage**
This parser feature is present in AoE2ScenarioParser but was not observed in the scanned local reference projects. Treat it as supported capability with no local canonical usage pattern yet.

**Common Pairings**
- `send_chat`
- `play_sound`
- `activate_trigger`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

## 9999. research_local_technology
**Method**: `research_local_technology`
**Family**: `tech_edit`
**Primary Role**: Turn technologies into a scenario-controlled interface and progression surface.

**How It Is Used**
Use these effects when technologies are serving as buttons, unlock panels, class menus, or progression displays rather than only vanilla researches. Your projects use this family to move, rename, cost, and gate technologies so the scenario can expose custom systems through the game UI.

**Architecture Notes**
This family is strongest when tech metadata comes from data dictionaries. That keeps UI and balancing changes out of the trigger orchestration code.

**Real Project Usage**
This parser feature is present in AoE2ScenarioParser but was not observed in the scanned local reference projects. Treat it as supported capability with no local canonical usage pattern yet.

**Common Pairings**
- `researching_tech`
- `technology_state`
- `send_chat`
- `display_timer`
- `activate_trigger`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

## 9999. set_object_cost
**Method**: `set_object_cost`
**Family**: `stat_mutation`
**Primary Role**: Change runtime object or class stats in response to scenario logic.

**How It Is Used**
Use this family for buffs, debuffs, scaling systems, class growth, difficulty adjustments, and temporary ability states. In your reference projects stat mutation is one of the main ways triggers turn variables and timers into visible gameplay consequences.

**Architecture Notes**
This family is where data-driven balancing matters most. If numbers are spread through trigger builders, later balance passes become expensive and error-prone. Keep the values in dictionaries and let trigger code only apply them.

**Real Project Usage**
Observed 8 times in the scanned reference projects, primarily in Hide_and_Seek (8 uses). Use the example paths as the first place to inspect the surrounding trigger architecture.

**Common Pairings**
- `variable_value`
- `change_variable`
- `timer`
- `script_call`
- `modify_resource`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

**Reference Examples**
- `Hide_and_Seek -> Setup\Player_Setup\apply_player_setup.py:700`
- `Hide_and_Seek -> Setup\Player_Setup\apply_player_setup.py:706`
- `Hide_and_Seek -> Setup\Player_Setup\apply_player_setup.py:712`

## 9999. store_key_value
**Method**: `store_key_value`
**Family**: `persistence`
**Primary Role**: Store scenario-side state in key-value or decision systems.

**How It Is Used**
Use this family when the scenario wants a persistence-like or indexed-state layer that is not just one flat variable registry. It is useful for data-driven systems, loot or inventory state, and situations where triggers need to create or query structured records.

**Architecture Notes**
This family matters most when the rest of the project is already modular. If the data model is unclear, adding persistence effects will only make the system harder to reason about.

**Real Project Usage**
This parser feature is present in AoE2ScenarioParser but was not observed in the scanned local reference projects. Treat it as supported capability with no local canonical usage pattern yet.

**Common Pairings**
- `variable_value`
- `compare_variables`
- `create_decision`
- `load_key_value`
- `store_key_value`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.

## 9999. train_unit
**Method**: `train_unit`
**Family**: `object_control`
**Primary Role**: Create, remove, move, or command units and objects in the world.

**How It Is Used**
Use this family when the trigger system needs to directly manipulate the playable world. It covers spawning units, issuing orders, moving objects, removing temporary entities, and forcing scripted interactions that the normal AI or player input should not own.

**Architecture Notes**
World-control effects become much easier to balance when the object IDs, areas, and per-level values come from data modules. Keep world mutation code thin and let configuration determine what gets spawned or moved.

**Real Project Usage**
This parser feature is present in AoE2ScenarioParser but was not observed in the scanned local reference projects. Treat it as supported capability with no local canonical usage pattern yet.

**Common Pairings**
- `objects_in_area`
- `variable_value`
- `timer`
- `play_sound`
- `change_view`

**Communication Semantics**
- Audience Scope: `varies_by_parameters`
- Attention Strength: `medium`
- Recommended Frequency: `depends_on_system`
- Best Use: Use the effect according to its gameplay role and only treat it as a communication tool when the effect is actually player-facing.
