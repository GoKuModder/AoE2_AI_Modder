# Trigger Knowledge: Effects
Generated file. Do not hand-edit; run tools/build_trigger_knowledge.py.
Data source: canonical `effects_knowledge.json`.

## Index
| ID | Name | Method |
|---|---|---|
| 1 | [Change Diplomacy](#change-diplomacy) | `change_diplomacy` |
| 2 | [Research Technology](#research-technology) | `research_technology` |
| 3 | [Send Chat](#send-chat) | `send_chat` |
| 4 | [Play Sound](#play-sound) | `play_sound` |
| 5 | [Tribute](#tribute) | `tribute` |
| 6 | [Unlock Gate](#unlock-gate) | `unlock_gate` |
| 7 | [Lock Gate](#lock-gate) | `lock_gate` |
| 8 | [Activate Trigger](#activate-trigger) | `activate_trigger` |
| 9 | [Deactivate Trigger](#deactivate-trigger) | `deactivate_trigger` |
| 10 | [AI Script Goal](#ai-script-goal) | `ai_script_goal` |
| 11 | [Create Object](#create-object) | `create_object` |
| 12 | [Task Object](#task-object) | `task_object` |
| 13 | [Declare Victory](#declare-victory) | `declare_victory` |
| 14 | [Kill Object](#kill-object) | `kill_object` |
| 15 | [Remove Object](#remove-object) | `remove_object` |
| 16 | [Change View](#change-view) | `change_view` |
| 17 | [Unload](#unload) | `unload` |
| 18 | [Change Ownership](#change-ownership) | `change_ownership` |
| 19 | [Patrol](#patrol) | `patrol` |
| 20 | [Display Instructions](#display-instructions) | `display_instructions` |
| 21 | [Clear Instructions](#clear-instructions) | `clear_instructions` |
| 22 | [Freeze Object](#freeze-object) | `freeze_object` |
| 23 | [Use Advanced Buttons](#use-advanced-buttons) | `use_advanced_buttons` |
| 24 | [Damage Object](#damage-object) | `damage_object` |
| 25 | [Place Foundation](#place-foundation) | `place_foundation` |
| 26 | [Change Object Name](#change-object-name) | `change_object_name` |
| 27 | [Change Object HP](#change-object-hp) | `change_object_hp` |
| 28 | [Change Object Attack](#change-object-attack) | `change_object_attack` |
| 29 | [Stop Object](#stop-object) | `stop_object` |
| 30 | [Attack Move](#attack-move) | `attack_move` |
| 31 | [Change Object Armor](#change-object-armor) | `change_object_armor` |
| 32 | [Change Object Range](#change-object-range) | `change_object_range` |
| 33 | [Change Object Speed](#change-object-speed) | `change_object_speed` |
| 34 | [Heal Object](#heal-object) | `heal_object` |
| 35 | [Teleport Object](#teleport-object) | `teleport_object` |
| 36 | [Change Object Stance](#change-object-stance) | `change_object_stance` |
| 37 | [Display Timer](#display-timer) | `display_timer` |
| 38 | [Enable Disable Object](#enable-disable-object) | `enable_disable_object` |
| 39 | [Enable Disable Technology](#enable-disable-technology) | `enable_disable_technology` |
| 40 | [Change Object Cost](#change-object-cost) | `change_object_cost` |
| 41 | [Set Player Visibility](#set-player-visibility) | `set_player_visibility` |
| 42 | [Change Object Icon](#change-object-icon) | `change_object_icon` |
| 43 | [Replace Object](#replace-object) | `replace_object` |
| 44 | [Change Object Description](#change-object-description) | `change_object_description` |
| 45 | [Change Player Name](#change-player-name) | `change_player_name` |
| 46 | [Change Train Location](#change-train-location) | `change_train_location` |
| 47 | [Change Research Location](#change-research-location) | `change_research_location` |
| 48 | [Change Civilization Name](#change-civilization-name) | `change_civilization_name` |
| 49 | [Create Garrisoned Object](#create-garrisoned-object) | `create_garrisoned_object` |
| 50 | [Acknowledge AI Signal](#acknowledge-ai-signal) | `acknowledge_ai_signal` |
| 51 | [Modify Attribute](#modify-attribute) | `modify_attribute` |
| 52 | [Modify Resource](#modify-resource) | `modify_resource` |
| 53 | [Modify Resource By Variable](#modify-resource-by-variable) | `modify_resource_by_variable` |
| 54 | [Set Building Gather Point](#set-building-gather-point) | `set_building_gather_point` |
| 55 | [Script Call](#script-call) | `script_call` |
| 56 | [Change Variable](#change-variable) | `change_variable` |
| 57 | [Clear Timer](#clear-timer) | `clear_timer` |
| 58 | [Change Object Player Color](#change-object-player-color) | `change_object_player_color` |
| 59 | [Change Object Civilization Name](#change-object-civilization-name) | `change_object_civilization_name` |
| 60 | [Change Object Player Name](#change-object-player-name) | `change_object_player_name` |
| 61 | [Disable Unit Targeting](#disable-unit-targeting) | `disable_unit_targeting` |
| 62 | [Enable Unit Targeting](#enable-unit-targeting) | `enable_unit_targeting` |
| 63 | [Change Technology Cost](#change-technology-cost) | `change_technology_cost` |
| 64 | [Change Technology Research Time](#change-technology-research-time) | `change_technology_research_time` |
| 65 | [Change Technology Name](#change-technology-name) | `change_technology_name` |
| 66 | [Change Technology Description](#change-technology-description) | `change_technology_description` |
| 67 | [Enable Technology Stacking](#enable-technology-stacking) | `enable_technology_stacking` |
| 68 | [Disable Technology Stacking](#disable-technology-stacking) | `disable_technology_stacking` |
| 69 | [Acknowledge Multiplayer AI Signal](#acknowledge-multiplayer-ai-signal) | `acknowledge_multiplayer_ai_signal` |
| 70 | [Disable Object Selection](#disable-object-selection) | `disable_object_selection` |
| 71 | [Enable Object Selection](#enable-object-selection) | `enable_object_selection` |
| 72 | [Change Color Mood](#change-color-mood) | `change_color_mood` |
| 9999 | [add_train_location](#add_train_location) | `add_train_location` |
| 9999 | [change_object_caption](#change_object_caption) | `change_object_caption` |
| 9999 | [change_object_visibility](#change_object_visibility) | `change_object_visibility` |
| 9999 | [change_player_color](#change_player_color) | `change_player_color` |
| 9999 | [change_technology_hotkey](#change_technology_hotkey) | `change_technology_hotkey` |
| 9999 | [change_technology_icon](#change_technology_icon) | `change_technology_icon` |
| 9999 | [change_technology_location](#change_technology_location) | `change_technology_location` |
| 9999 | [count_units_into_variable](#count_units_into_variable) | `count_units_into_variable` |
| 9999 | [create_decision](#create_decision) | `create_decision` |
| 9999 | [create_object_armor](#create_object_armor) | `create_object_armor` |
| 9999 | [create_object_attack](#create_object_attack) | `create_object_attack` |
| 9999 | [delete_key](#delete_key) | `delete_key` |
| 9999 | [disable_object_deletion](#disable_object_deletion) | `disable_object_deletion` |
| 9999 | [disable_unit_attackable](#disable_unit_attackable) | `disable_unit_attackable` |
| 9999 | [enable_object_deletion](#enable_object_deletion) | `enable_object_deletion` |
| 9999 | [enable_unit_attackable](#enable_unit_attackable) | `enable_unit_attackable` |
| 9999 | [initiate_research](#initiate_research) | `initiate_research` |
| 9999 | [load_key_value](#load_key_value) | `load_key_value` |
| 9999 | [modify_attribute_by_variable](#modify_attribute_by_variable) | `modify_attribute_by_variable` |
| 9999 | [modify_attribute_for_class](#modify_attribute_for_class) | `modify_attribute_for_class` |
| 9999 | [modify_object_attribute](#modify_object_attribute) | `modify_object_attribute` |
| 9999 | [modify_object_attribute_by_variable](#modify_object_attribute_by_variable) | `modify_object_attribute_by_variable` |
| 9999 | [modify_variable_by_attribute](#modify_variable_by_attribute) | `modify_variable_by_attribute` |
| 9999 | [modify_variable_by_resource](#modify_variable_by_resource) | `modify_variable_by_resource` |
| 9999 | [modify_variable_by_variable](#modify_variable_by_variable) | `modify_variable_by_variable` |
| 9999 | [none](#none) | `none` |
| 9999 | [research_local_technology](#research_local_technology) | `research_local_technology` |
| 9999 | [set_object_cost](#set_object_cost) | `set_object_cost` |
| 9999 | [store_key_value](#store_key_value) | `store_key_value` |
| 9999 | [train_unit](#train_unit) | `train_unit` |

## 1. Change Diplomacy
`change_diplomacy(self, diplomacy: 'int | None' = None, source_player: 'int | None' = None, target_player: 'int | None' = None) -> 'Effect'`

This effect can be used to change the diplomacy stance of the soruce players with the target player

**Parameters:**
- `diplomacy` (int | None)
- `source_player` (int | None)
- `target_player` (int | None)

## 2. Research Technology
`research_technology(self, source_player: 'int | None' = None, technology: 'int | None' = None, force_research_technology: 'int | None' = None) -> 'Effect'`

This effect can automatically research a technology for the specified player.

**Parameters:**
- `source_player` (int | None)
- `technology` (int | None)
- `force_research_technology` (int | None)

## 3. Send Chat
`send_chat(self, source_player: 'int | None' = None, string_id: 'int | None' = None, message: 'str | None' = None, sound_name: 'str | None' = None) -> 'Effect'`

This effect can be used to display messages in chat

**Parameters:**
- `source_player` (int | None)
- `string_id` (int | None)
- `message` (str | None)
- `sound_name` (str | None)

## 4. Play Sound
`play_sound(self, source_player: 'int | None' = None, location_x: 'int | None' = None, location_y: 'int | None' = None, location_object_reference: 'int | None' = None, sound_name: 'str | None' = None) -> 'Effect'`

This effect can be used to play a specified sound

**Parameters:**
- `source_player` (int | None)
- `location_x` (int | None)
- `location_y` (int | None)
- `location_object_reference` (int | None)
- `sound_name` (str | None)

## 5. Tribute
`tribute(self, quantity: 'int | None' = None, tribute_list: 'int | None' = None, source_player: 'int | None' = None, target_player: 'int | None' = None) -> 'Effect'`

This effect can be used to tribute resources from one player to another

**Parameters:**
- `quantity` (int | None)
- `tribute_list` (int | None)
- `source_player` (int | None)
- `target_player` (int | None)

## 6. Unlock Gate
`unlock_gate(self, selected_object_ids: 'int | List[int] | None' = None) -> 'Effect'`

This effect can be used to unlock a locked gate

**Parameters:**
- `selected_object_ids` (int | List[int] | None)

## 7. Lock Gate
`lock_gate(self, selected_object_ids: 'int | List[int] | None' = None) -> 'Effect'`

This effect can be used to lock an unlocked gate

**Parameters:**
- `selected_object_ids` (int | List[int] | None)

## 8. Activate Trigger
`activate_trigger(self, trigger_id: 'int | None' = None) -> 'Effect'`

This effect can be used to activate a trigger

**Parameters:**
- `trigger_id` (int | None)

## 9. Deactivate Trigger
`deactivate_trigger(self, trigger_id: 'int | None' = None) -> 'Effect'`

This effect can be used to activate a trigger

**Parameters:**
- `trigger_id` (int | None)

## 10. AI Script Goal
`ai_script_goal(self, ai_script_goal: 'int | None' = None) -> 'Effect'`

This effect is used to communicate with the AI. An AI Trigger NUMBER set with this effect can be detected in an AI script using `event-detected trigger NUMBER`

**Parameters:**
- `ai_script_goal` (int | None)

## 11. Create Object
`create_object(self, object_list_unit_id: 'int | None' = None, source_player: 'int | None' = None, location_x: 'int | None' = None, location_y: 'int | None' = None, facet: 'int | None' = None, disable_sound: 'int | None' = None) -> 'Effect'`

This effect can be used to create a unit or building for the specified player

**Parameters:**
- `object_list_unit_id` (int | None)
- `source_player` (int | None)
- `location_x` (int | None)
- `location_y` (int | None)
- `facet` (int | None)
- `disable_sound` (int | None)

## 12. Task Object
`task_object(self, object_list_unit_id: 'int | None' = None, source_player: 'int | None' = None, location_x: 'int | None' = None, location_y: 'int | None' = None, location_object_reference: 'int | None' = None, area_x1: 'int | None' = None, area_y1: 'int | None' = None, area_x2: 'int | None' = None, area_y2: 'int | None' = None, object_group: 'int | None' = None, object_type: 'int | None' = None, action_type: 'int | None' = None, selected_object_ids: 'int | List[int] | None' = None, disable_garrison_unload_sound: 'int | None' = None, max_units_affected: 'int | None' = None, issue_group_command: 'int | None' = None, queue_action: 'int | None' = None) -> 'Effect'`

This effect can be used to task certain units of the specified player to (it basically simulates a right click at the specified location or unit) move to a specified locaiton, or perform an action on another unit. The units affected by this effect are determined by the configurations of the effect

**Parameters:**
- `object_list_unit_id` (int | None)
- `source_player` (int | None)
- `location_x` (int | None)
- `location_y` (int | None)
- `location_object_reference` (int | None)
- `area_x1` (int | None)
- `area_y1` (int | None)
- `area_x2` (int | None)
- `area_y2` (int | None)
- `object_group` (int | None)
- `object_type` (int | None)
- `action_type` (int | None)
- `selected_object_ids` (int | List[int] | None)
- `disable_garrison_unload_sound` (int | None)
- `max_units_affected` (int | None)
- `issue_group_command` (int | None)
- `queue_action` (int | None)

## 13. Declare Victory
`declare_victory(self, source_player: 'int | None' = None, enabled: 'int | None' = None) -> 'Effect'`

This effect can be used to grant victory or defeat to a specifed player

**Parameters:**
- `source_player` (int | None)
- `enabled` (int | None)

## 14. Kill Object
`kill_object(self, object_list_unit_id: 'int | None' = None, source_player: 'int | None' = None, area_x1: 'int | None' = None, area_y1: 'int | None' = None, area_x2: 'int | None' = None, area_y2: 'int | None' = None, object_group: 'int | None' = None, object_type: 'int | None' = None, selected_object_ids: 'int | List[int] | None' = None, max_units_affected: 'int | None' = None) -> 'Effect'`

This effect can be used to kill certain units of the specified player. The units affected by this effect are determined by the configurations of the effect

**Parameters:**
- `object_list_unit_id` (int | None)
- `source_player` (int | None)
- `area_x1` (int | None)
- `area_y1` (int | None)
- `area_x2` (int | None)
- `area_y2` (int | None)
- `object_group` (int | None)
- `object_type` (int | None)
- `selected_object_ids` (int | List[int] | None)
- `max_units_affected` (int | None)

## 15. Remove Object
`remove_object(self, object_list_unit_id: 'int | None' = None, source_player: 'int | None' = None, area_x1: 'int | None' = None, area_y1: 'int | None' = None, area_x2: 'int | None' = None, area_y2: 'int | None' = None, object_group: 'int | None' = None, object_type: 'int | None' = None, object_state: 'int | None' = None, selected_object_ids: 'int | List[int] | None' = None, max_units_affected: 'int | None' = None) -> 'Effect'`

This effect can be used to remove certain units of the specified player from the map. The units affected by this effect are determined by the configurations of the effect

**Parameters:**
- `object_list_unit_id` (int | None)
- `source_player` (int | None)
- `area_x1` (int | None)
- `area_y1` (int | None)
- `area_x2` (int | None)
- `area_y2` (int | None)
- `object_group` (int | None)
- `object_type` (int | None)
- `object_state` (int | None)
- `selected_object_ids` (int | List[int] | None)
- `max_units_affected` (int | None)

## 16. Change View
`change_view(self, quantity: 'int | None' = None, source_player: 'int | None' = None, location_x: 'int | None' = None, location_y: 'int | None' = None, scroll: 'int | None' = None) -> 'Effect'`

This effect can be used to move the camera of the player to a specified location

**Parameters:**
- `quantity` (int | None)
- `source_player` (int | None)
- `location_x` (int | None)
- `location_y` (int | None)
- `scroll` (int | None)

## 17. Unload
`unload(self, object_list_unit_id: 'int | None' = None, source_player: 'int | None' = None, location_x: 'int | None' = None, location_y: 'int | None' = None, location_object_reference: 'int | None' = None, area_x1: 'int | None' = None, area_y1: 'int | None' = None, area_x2: 'int | None' = None, area_y2: 'int | None' = None, object_group: 'int | None' = None, object_type: 'int | None' = None, selected_object_ids: 'int | List[int] | None' = None, max_units_affected: 'int | None' = None) -> 'Effect'`

This effect can be used to ungarisson objects from a unit or building. The units affected by this effect are determined by the configurations of the effect

**Parameters:**
- `object_list_unit_id` (int | None)
- `source_player` (int | None)
- `location_x` (int | None)
- `location_y` (int | None)
- `location_object_reference` (int | None)
- `area_x1` (int | None)
- `area_y1` (int | None)
- `area_x2` (int | None)
- `area_y2` (int | None)
- `object_group` (int | None)
- `object_type` (int | None)
- `selected_object_ids` (int | List[int] | None)
- `max_units_affected` (int | None)

## 18. Change Ownership
`change_ownership(self, object_list_unit_id: 'int | None' = None, source_player: 'int | None' = None, target_player: 'int | None' = None, area_x1: 'int | None' = None, area_y1: 'int | None' = None, area_x2: 'int | None' = None, area_y2: 'int | None' = None, object_group: 'int | None' = None, object_type: 'int | None' = None, flash_object: 'int | None' = None, selected_object_ids: 'int | List[int] | None' = None, max_units_affected: 'int | None' = None) -> 'Effect'`

This effect can be used to convert units of the source player to the target player. The units affected by this effect are determined by the configurations of the effect

**Parameters:**
- `object_list_unit_id` (int | None)
- `source_player` (int | None)
- `target_player` (int | None)
- `area_x1` (int | None)
- `area_y1` (int | None)
- `area_x2` (int | None)
- `area_y2` (int | None)
- `object_group` (int | None)
- `object_type` (int | None)
- `flash_object` (int | None)
- `selected_object_ids` (int | List[int] | None)
- `max_units_affected` (int | None)

## 19. Patrol
`patrol(self, object_list_unit_id: 'int | None' = None, source_player: 'int | None' = None, location_x: 'int | None' = None, location_y: 'int | None' = None, area_x1: 'int | None' = None, area_y1: 'int | None' = None, area_x2: 'int | None' = None, area_y2: 'int | None' = None, object_group: 'int | None' = None, object_type: 'int | None' = None, selected_object_ids: 'int | List[int] | None' = None, max_units_affected: 'int | None' = None) -> 'Effect'`

This effect can be used to make units of a specified player patrol from one location to another. The units affected by this effect are determined by the configurations of the effect

**Parameters:**
- `object_list_unit_id` (int | None)
- `source_player` (int | None)
- `location_x` (int | None)
- `location_y` (int | None)
- `area_x1` (int | None)
- `area_y1` (int | None)
- `area_x2` (int | None)
- `area_y2` (int | None)
- `object_group` (int | None)
- `object_type` (int | None)
- `selected_object_ids` (int | List[int] | None)
- `max_units_affected` (int | None)

## 20. Display Instructions
`display_instructions(self, object_list_unit_id: 'int | None' = None, source_player: 'int | None' = None, string_id: 'int | None' = None, display_time: 'int | None' = None, instruction_panel_position: 'int | None' = None, play_sound: 'int | None' = None, message: 'str | None' = None, sound_name: 'str | None' = None) -> 'Effect'`

This effect can be used to display instructions on the screen. An icon of a unit may also be displayed along with the instructions

**Parameters:**
- `object_list_unit_id` (int | None)
- `source_player` (int | None)
- `string_id` (int | None)
- `display_time` (int | None)
- `instruction_panel_position` (int | None)
- `play_sound` (int | None)
- `message` (str | None)
- `sound_name` (str | None)

## 21. Clear Instructions
`clear_instructions(self, instruction_panel_position: 'int | None' = None) -> 'Effect'`

This effect can be used to clear instructions on the screen before the timer for that instruction is up.

**Parameters:**
- `instruction_panel_position` (int | None)

## 22. Freeze Object
`freeze_object(self, object_list_unit_id: 'int | None' = None, source_player: 'int | None' = None, area_x1: 'int | None' = None, area_y1: 'int | None' = None, area_x2: 'int | None' = None, area_y2: 'int | None' = None, object_group: 'int | None' = None, object_type: 'int | None' = None, selected_object_ids: 'int | List[int] | None' = None, max_units_affected: 'int | None' = None) -> 'Effect'`

This effect does not actually freeze the objects but sets them to a no attack stance. The units affected by this effect are determined by the configurations of the effect

**Parameters:**
- `object_list_unit_id` (int | None)
- `source_player` (int | None)
- `area_x1` (int | None)
- `area_y1` (int | None)
- `area_x2` (int | None)
- `area_y2` (int | None)
- `object_group` (int | None)
- `object_type` (int | None)
- `selected_object_ids` (int | List[int] | None)
- `max_units_affected` (int | None)

## 23. Use Advanced Buttons
`use_advanced_buttons(self) -> 'Effect'`

Enables Advanced Buttons

*No parameters.*

## 24. Damage Object
`damage_object(self, quantity: 'int | None' = None, object_list_unit_id: 'int | None' = None, source_player: 'int | None' = None, area_x1: 'int | None' = None, area_y1: 'int | None' = None, area_x2: 'int | None' = None, area_y2: 'int | None' = None, object_group: 'int | None' = None, object_type: 'int | None' = None, selected_object_ids: 'int | List[int] | None' = None, max_units_affected: 'int | None' = None) -> 'Effect'`

This effect can be used to deal damage to units of a given player. The units affected by this effect are determined by the configurations of the effect

**Parameters:**
- `quantity` (int | None)
- `object_list_unit_id` (int | None)
- `source_player` (int | None)
- `area_x1` (int | None)
- `area_y1` (int | None)
- `area_x2` (int | None)
- `area_y2` (int | None)
- `object_group` (int | None)
- `object_type` (int | None)
- `selected_object_ids` (int | List[int] | None)
- `max_units_affected` (int | None)

## 25. Place Foundation
`place_foundation(self, object_list_unit_id: 'int | None' = None, source_player: 'int | None' = None, location_x: 'int | None' = None, location_y: 'int | None' = None) -> 'Effect'`

This effect can be used to automatically place down a building foundation for a specific player

**Parameters:**
- `object_list_unit_id` (int | None)
- `source_player` (int | None)
- `location_x` (int | None)
- `location_y` (int | None)

## 26. Change Object Name
`change_object_name(self, object_list_unit_id: 'int | None' = None, source_player: 'int | None' = None, string_id: 'int | None' = None, area_x1: 'int | None' = None, area_y1: 'int | None' = None, area_x2: 'int | None' = None, area_y2: 'int | None' = None, message: 'str | None' = None, selected_object_ids: 'int | List[int] | None' = None, max_units_affected: 'str | None' = None) -> 'Effect'`

This effect can be used to change the names of existing units of a given player to the specified name. The units affected by this effect are determined by the configurations of the effect

**Parameters:**
- `object_list_unit_id` (int | None)
- `source_player` (int | None)
- `string_id` (int | None)
- `area_x1` (int | None)
- `area_y1` (int | None)
- `area_x2` (int | None)
- `area_y2` (int | None)
- `message` (str | None)
- `selected_object_ids` (int | List[int] | None)
- `max_units_affected` (str | None)

## 27. Change Object HP
`change_object_hp(self, quantity: 'int | None' = None, object_list_unit_id: 'int | None' = None, source_player: 'int | None' = None, area_x1: 'int | None' = None, area_y1: 'int | None' = None, area_x2: 'int | None' = None, area_y2: 'int | None' = None, object_group: 'int | None' = None, object_type: 'int | None' = None, operation: 'int | None' = None, selected_object_ids: 'int | List[int] | None' = None, max_units_affected: 'int | None' = None) -> 'Effect'`

This effect can be used to change the max HP of existing units of a given player to the specified value. The units affected by this effect are determined by the configurations of the effect

**Parameters:**
- `quantity` (int | None)
- `object_list_unit_id` (int | None)
- `source_player` (int | None)
- `area_x1` (int | None)
- `area_y1` (int | None)
- `area_x2` (int | None)
- `area_y2` (int | None)
- `object_group` (int | None)
- `object_type` (int | None)
- `operation` (int | None)
- `selected_object_ids` (int | List[int] | None)
- `max_units_affected` (int | None)

## 28. Change Object Attack
`change_object_attack(self, armour_attack_quantity: 'int | None' = None, armour_attack_class: 'int | None' = None, object_list_unit_id: 'int | None' = None, source_player: 'int | None' = None, area_x1: 'int | None' = None, area_y1: 'int | None' = None, area_x2: 'int | None' = None, area_y2: 'int | None' = None, object_group: 'int | None' = None, object_type: 'int | None' = None, operation: 'int | None' = None, selected_object_ids: 'int | List[int] | None' = None, max_units_affected: 'int | None' = None) -> 'Effect'`

This effect can be used to change the attack of existing units of a given player to the specified value. The units affected by this effect are determined by the configurations of the effect

**Parameters:**
- `armour_attack_quantity` (int | None)
- `armour_attack_class` (int | None)
- `object_list_unit_id` (int | None)
- `source_player` (int | None)
- `area_x1` (int | None)
- `area_y1` (int | None)
- `area_x2` (int | None)
- `area_y2` (int | None)
- `object_group` (int | None)
- `object_type` (int | None)
- `operation` (int | None)
- `selected_object_ids` (int | List[int] | None)
- `max_units_affected` (int | None)

## 29. Stop Object
`stop_object(self, object_list_unit_id: 'int | None' = None, source_player: 'int | None' = None, area_x1: 'int | None' = None, area_y1: 'int | None' = None, area_x2: 'int | None' = None, area_y2: 'int | None' = None, object_group: 'int | None' = None, object_type: 'int | None' = None, selected_object_ids: 'int | List[int] | None' = None, max_units_affected: 'int | None' = None) -> 'Effect'`

This effect can be used to stop units of a given player. The units affected by this effect are determined by the configurations of the effect

**Parameters:**
- `object_list_unit_id` (int | None)
- `source_player` (int | None)
- `area_x1` (int | None)
- `area_y1` (int | None)
- `area_x2` (int | None)
- `area_y2` (int | None)
- `object_group` (int | None)
- `object_type` (int | None)
- `selected_object_ids` (int | List[int] | None)
- `max_units_affected` (int | None)

## 30. Attack Move
`attack_move(self, object_list_unit_id: 'int | None' = None, source_player: 'int | None' = None, location_x: 'int | None' = None, location_y: 'int | None' = None, location_object_reference: 'int | None' = None, area_x1: 'int | None' = None, area_y1: 'int | None' = None, area_x2: 'int | None' = None, area_y2: 'int | None' = None, object_group: 'int | None' = None, object_type: 'int | None' = None, selected_object_ids: 'int | List[int] | None' = None, max_units_affected: 'int | None' = None) -> 'Effect'`

This effect can be used to command units of a given player to attack move to a location. The units affected by this effect are determined by the configurations of the effect

**Parameters:**
- `object_list_unit_id` (int | None)
- `source_player` (int | None)
- `location_x` (int | None)
- `location_y` (int | None)
- `location_object_reference` (int | None)
- `area_x1` (int | None)
- `area_y1` (int | None)
- `area_x2` (int | None)
- `area_y2` (int | None)
- `object_group` (int | None)
- `object_type` (int | None)
- `selected_object_ids` (int | List[int] | None)
- `max_units_affected` (int | None)

## 31. Change Object Armor
`change_object_armor(self, armour_attack_quantity: 'int | None' = None, armour_attack_class: 'int | None' = None, object_list_unit_id: 'int | None' = None, source_player: 'int | None' = None, area_x1: 'int | None' = None, area_y1: 'int | None' = None, area_x2: 'int | None' = None, area_y2: 'int | None' = None, object_group: 'int | None' = None, object_type: 'int | None' = None, operation: 'int | None' = None, selected_object_ids: 'int | List[int] | None' = None, max_units_affected: 'int | None' = None) -> 'Effect'`

This effect can be used to change the armour of existing units of a given player to the specified value. The units affected by this effect are determined by the configurations of the effect

**Parameters:**
- `armour_attack_quantity` (int | None)
- `armour_attack_class` (int | None)
- `object_list_unit_id` (int | None)
- `source_player` (int | None)
- `area_x1` (int | None)
- `area_y1` (int | None)
- `area_x2` (int | None)
- `area_y2` (int | None)
- `object_group` (int | None)
- `object_type` (int | None)
- `operation` (int | None)
- `selected_object_ids` (int | List[int] | None)
- `max_units_affected` (int | None)

## 32. Change Object Range
`change_object_range(self, quantity: 'int | None' = None, object_list_unit_id: 'int | None' = None, source_player: 'int | None' = None, area_x1: 'int | None' = None, area_y1: 'int | None' = None, area_x2: 'int | None' = None, area_y2: 'int | None' = None, object_group: 'int | None' = None, object_type: 'int | None' = None, operation: 'int | None' = None, selected_object_ids: 'int | List[int] | None' = None, max_units_affected: 'int | None' = None) -> 'Effect'`

This effect can be used to change the range of existing units of a given player to the specified value. The units affected by this effect are determined by the configurations of the effect

**Parameters:**
- `quantity` (int | None)
- `object_list_unit_id` (int | None)
- `source_player` (int | None)
- `area_x1` (int | None)
- `area_y1` (int | None)
- `area_x2` (int | None)
- `area_y2` (int | None)
- `object_group` (int | None)
- `object_type` (int | None)
- `operation` (int | None)
- `selected_object_ids` (int | List[int] | None)
- `max_units_affected` (int | None)

## 33. Change Object Speed
`change_object_speed(self, quantity: 'int | None' = None, object_list_unit_id: 'int | None' = None, source_player: 'int | None' = None, area_x1: 'int | None' = None, area_y1: 'int | None' = None, area_x2: 'int | None' = None, area_y2: 'int | None' = None, object_group: 'int | None' = None, object_type: 'int | None' = None, selected_object_ids: 'int | List[int] | None' = None, max_units_affected: 'int | None' = None) -> 'Effect'`

This effect can be used to change the speed of existing units of a given player to the specified value. The units affected by this effect are determined by the configurations of the effect

**Parameters:**
- `quantity` (int | None)
- `object_list_unit_id` (int | None)
- `source_player` (int | None)
- `area_x1` (int | None)
- `area_y1` (int | None)
- `area_x2` (int | None)
- `area_y2` (int | None)
- `object_group` (int | None)
- `object_type` (int | None)
- `selected_object_ids` (int | List[int] | None)
- `max_units_affected` (int | None)

## 34. Heal Object
`heal_object(self, quantity: 'int | None' = None, object_list_unit_id: 'int | None' = None, source_player: 'int | None' = None, area_x1: 'int | None' = None, area_y1: 'int | None' = None, area_x2: 'int | None' = None, area_y2: 'int | None' = None, object_group: 'int | None' = None, object_type: 'int | None' = None, selected_object_ids: 'int | List[int] | None' = None, max_units_affected: 'int | None' = None) -> 'Effect'`

This effect can be used to heal existing units of a given player by the specifed HP amount. The units affected by this effect are determined by the configurations of the effect

**Parameters:**
- `quantity` (int | None)
- `object_list_unit_id` (int | None)
- `source_player` (int | None)
- `area_x1` (int | None)
- `area_y1` (int | None)
- `area_x2` (int | None)
- `area_y2` (int | None)
- `object_group` (int | None)
- `object_type` (int | None)
- `selected_object_ids` (int | List[int] | None)
- `max_units_affected` (int | None)

## 35. Teleport Object
`teleport_object(self, object_list_unit_id: 'int | None' = None, source_player: 'int | None' = None, location_x: 'int | None' = None, location_y: 'int | None' = None, area_x1: 'int | None' = None, area_y1: 'int | None' = None, area_x2: 'int | None' = None, area_y2: 'int | None' = None, object_group: 'int | None' = None, object_type: 'int | None' = None, selected_object_ids: 'int | List[int] | None' = None, max_units_affected: 'int | None' = None) -> 'Effect'`

This effect can be used to teleport units of a player from one area of the map to another location on the map. The units affected by this effect are determined by the configurations of the effect

**Parameters:**
- `object_list_unit_id` (int | None)
- `source_player` (int | None)
- `location_x` (int | None)
- `location_y` (int | None)
- `area_x1` (int | None)
- `area_y1` (int | None)
- `area_x2` (int | None)
- `area_y2` (int | None)
- `object_group` (int | None)
- `object_type` (int | None)
- `selected_object_ids` (int | List[int] | None)
- `max_units_affected` (int | None)

## 36. Change Object Stance
`change_object_stance(self, object_list_unit_id: 'int | None' = None, source_player: 'int | None' = None, area_x1: 'int | None' = None, area_y1: 'int | None' = None, area_x2: 'int | None' = None, area_y2: 'int | None' = None, object_group: 'int | None' = None, object_type: 'int | None' = None, attack_stance: 'int | None' = None, selected_object_ids: 'int | List[int] | None' = None, max_units_affected: 'int | None' = None) -> 'Effect'`

This effect can be used to change the stance of units of a given player to the given stance. The units affected by this effect are determined by the configurations of the effect

**Parameters:**
- `object_list_unit_id` (int | None)
- `source_player` (int | None)
- `area_x1` (int | None)
- `area_y1` (int | None)
- `area_x2` (int | None)
- `area_y2` (int | None)
- `object_group` (int | None)
- `object_type` (int | None)
- `attack_stance` (int | None) -> **Dataset: AttackStance**
- `selected_object_ids` (int | List[int] | None)
- `max_units_affected` (int | None)

## 37. Display Timer
`display_timer(self, string_id: 'int | None' = None, display_time: 'int | None' = None, time_unit: 'int | None' = None, timer: 'int | None' = None, reset_timer: 'int | None' = None, message: 'str | None' = None) -> 'Effect'`

This effect can be used to display a timer on screen

**Parameters:**
- `string_id` (int | None)
- `display_time` (int | None)
- `time_unit` (int | None) -> **Dataset: TimeUnit**
- `timer` (int | None)
- `reset_timer` (int | None)
- `message` (str | None)

## 38. Enable Disable Object
`enable_disable_object(self, object_list_unit_id: 'int | None' = None, source_player: 'int | None' = None, enabled: 'int | None' = None) -> 'Effect'`

This effect can be used to enable/disable any unit for a specific player. Note that sometimes, simply enabling a unit wont allow you to train them, because if it is not a default unit, the game doesn't know which building to train the unit in. Thus, A train location and a train button ([Change Train Location](./<effect_id_ref 46> "Jump to: Change Train Location")), a cost ([Change Object Cost](./<effect_id_ref 40> "Jump to: Change Object Cost")), and optionally a discription ([Change Object Description](./<effect_id_ref 44> "Jump to: Change Object Description")), of the unit are needed to also be set using additional effects to allow training the enabled unit.

**Parameters:**
- `object_list_unit_id` (int | None)
- `source_player` (int | None)
- `enabled` (int | None)

## 39. Enable Disable Technology
`enable_disable_technology(self, source_player: 'int | None' = None, technology: 'int | None' = None, enabled: 'int | None' = None) -> 'Effect'`

This effect can be used to enable/disable any technology for a specific player. Similar to units, when a non default technology is enabled, its train location and button ([Change Research Location](./<effect_id_ref 47> "Jump to: Change Research Location")), costs ([Change Technology Cost](./<effect_id_ref 63> "Jump to: Change Technology Cost")), and optionally a description ([Change Technology Description](./<effect_id_ref 66> "Jump to: Change Technology Description")), must be set using additional effects for someone to research it.

**Parameters:**
- `source_player` (int | None)
- `technology` (int | None)
- `enabled` (int | None)

## 40. Change Object Cost
`change_object_cost(self, object_list_unit_id: 'int | None' = None, source_player: 'int | None' = None, resource_1: 'int | None' = None, resource_1_quantity: 'int | None' = None, resource_2: 'int | None' = None, resource_2_quantity: 'int | None' = None, resource_3: 'int | None' = None, resource_3_quantity: 'int | None' = None) -> 'Effect'`

This effect can be used to change the cost of a specifed unit for a particular player

**Parameters:**
- `object_list_unit_id` (int | None)
- `source_player` (int | None)
- `resource_1` (int | None)
- `resource_1_quantity` (int | None)
- `resource_2` (int | None)
- `resource_2_quantity` (int | None)
- `resource_3` (int | None)
- `resource_3_quantity` (int | None)

## 41. Set Player Visibility
`set_player_visibility(self, source_player: 'int | None' = None, target_player: 'int | None' = None, visibility_state: 'int | None' = None) -> 'Effect'`

This trigger sets the visibility of the target player for the source player

**Parameters:**
- `source_player` (int | None)
- `target_player` (int | None)
- `visibility_state` (int | None)

## 42. Change Object Icon
`change_object_icon(self, object_list_unit_id: 'int | None' = None, source_player: 'int | None' = None, area_x1: 'int | None' = None, area_y1: 'int | None' = None, area_x2: 'int | None' = None, area_y2: 'int | None' = None, object_group: 'int | None' = None, object_type: 'int | None' = None, object_list_unit_id_2: 'int | None' = None, selected_object_ids: 'int | List[int] | None' = None, max_units_affected: 'int | None' = None) -> 'Effect'`

This effect can be used to change the icon of existing units of a given player to the 2nd unit's icon. The units affected by this effect are determined by the configurations of the effect

**Parameters:**
- `object_list_unit_id` (int | None)
- `source_player` (int | None)
- `area_x1` (int | None)
- `area_y1` (int | None)
- `area_x2` (int | None)
- `area_y2` (int | None)
- `object_group` (int | None)
- `object_type` (int | None)
- `object_list_unit_id_2` (int | None)
- `selected_object_ids` (int | List[int] | None)
- `max_units_affected` (int | None)

## 43. Replace Object
`replace_object(self, object_list_unit_id: 'int | None' = None, source_player: 'int | None' = None, target_player: 'int | None' = None, area_x1: 'int | None' = None, area_y1: 'int | None' = None, area_x2: 'int | None' = None, area_y2: 'int | None' = None, object_group: 'int | None' = None, object_type: 'int | None' = None, object_list_unit_id_2: 'int | None' = None, selected_object_ids: 'int | List[int] | None' = None, facet2: 'int | None' = None, max_units_affected: 'int | None' = None) -> 'Effect'`

This effect can be used to replace existing units of a given player with another unit. The units affected by this effect are determined by the configurations of the effect

**Parameters:**
- `object_list_unit_id` (int | None)
- `source_player` (int | None)
- `target_player` (int | None)
- `area_x1` (int | None)
- `area_y1` (int | None)
- `area_x2` (int | None)
- `area_y2` (int | None)
- `object_group` (int | None)
- `object_type` (int | None)
- `object_list_unit_id_2` (int | None)
- `selected_object_ids` (int | List[int] | None)
- `facet2` (int | None)
- `max_units_affected` (int | None)

## 44. Change Object Description
`change_object_description(self, object_list_unit_id: 'int | None' = None, source_player: 'int | None' = None, string_id: 'int | None' = None, message: 'str | None' = None) -> 'Effect'`

This effect can be used to change the description of a specifed unit for a particular player

**Parameters:**
- `object_list_unit_id` (int | None)
- `source_player` (int | None)
- `string_id` (int | None)
- `message` (str | None)

## 45. Change Player Name
`change_player_name(self, source_player: 'int | None' = None, string_id: 'int | None' = None, message: 'str | None' = None) -> 'Effect'`

This effect can be used to change the name of a player to any desired name

**Parameters:**
- `source_player` (int | None)
- `string_id` (int | None)
- `message` (str | None)

## 46. Change Train Location
`change_train_location(self, object_list_unit_id: 'int | None' = None, source_player: 'int | None' = None, object_list_unit_id_2: 'int | None' = None, button_location: 'int | None' = None) -> 'Effect'`

This effect can be used to change the train location of a specifed unit for a particular player to another unit. The train location of Archers is Archery Range

**Parameters:**
- `object_list_unit_id` (int | None)
- `source_player` (int | None)
- `object_list_unit_id_2` (int | None)
- `button_location` (int | None)

## 47. Change Research Location
`change_research_location(self, source_player: 'int | None' = None, technology: 'int | None' = None, object_list_unit_id_2: 'int | None' = None, button_location: 'int | None' = None) -> 'Effect'`

This effect can be used to change the research location of a specifed technology for a particular player to another unit. The research location of Loom is the Town Centre

**Parameters:**
- `source_player` (int | None)
- `technology` (int | None)
- `object_list_unit_id_2` (int | None)
- `button_location` (int | None)

## 48. Change Civilization Name
`change_civilization_name(self, source_player: 'int | None' = None, string_id: 'int | None' = None, message: 'str | None' = None) -> 'Effect'`

This effect can be used to change the name of the civilization of a player to any desired name

**Parameters:**
- `source_player` (int | None)
- `string_id` (int | None)
- `message` (str | None)

## 49. Create Garrisoned Object
`create_garrisoned_object(self, object_list_unit_id: 'int | None' = None, source_player: 'int | None' = None, area_x1: 'int | None' = None, area_y1: 'int | None' = None, area_x2: 'int | None' = None, area_y2: 'int | None' = None, object_list_unit_id_2: 'int | None' = None, selected_object_ids: 'int | List[int] | None' = None, max_units_affected: 'int | None' = None, disable_sound: 'int | None' = None) -> 'Effect'`

This effect creates the unit chosen in the 2nd list inside the selected object or the unit chosen in the 1st list. The unit that the created unit is garrisoned inside does not need to be of the same player.

**Parameters:**
- `object_list_unit_id` (int | None)
- `source_player` (int | None)
- `area_x1` (int | None)
- `area_y1` (int | None)
- `area_x2` (int | None)
- `area_y2` (int | None)
- `object_list_unit_id_2` (int | None)
- `selected_object_ids` (int | List[int] | None)
- `max_units_affected` (int | None)
- `disable_sound` (int | None)

## 50. Acknowledge AI Signal
`acknowledge_ai_signal(self, ai_signal_value: 'int | None' = None) -> 'Effect'`

When `set-signal` is used in an AI file, this effect is used to unset it so it can be reused. This only works in Single Player games. Refer to the [Acknowledge Multiplayer AI Signal](./<effect_id_ref 69> "Jump to: Acknowledge Multiplayer AI Signal") effect for the multiplayer version of this effect

**Parameters:**
- `ai_signal_value` (int | None)

## 51. Modify Attribute
`modify_attribute(self, quantity: 'int | None' = None, armour_attack_quantity: 'int | None' = None, armour_attack_class: 'int | None' = None, object_list_unit_id: 'int | None' = None, source_player: 'int | None' = None, operation: 'int | None' = None, object_attributes: 'int | None' = None, message: 'str | None' = None) -> 'Effect'`

This effect can be used to modify any attribute of a specified unit. Note that this effects the unit itself, not just existing units. This means that even new units created will have the modified attribute. Refer to the [Attributes](../../../../general/attributes "Jump to: Game Mechanics > Attributes") section of the guide to see a list of modifiable attributes and what each of them does

**Parameters:**
- `quantity` (int | None)
- `armour_attack_quantity` (int | None)
- `armour_attack_class` (int | None)
- `object_list_unit_id` (int | None)
- `source_player` (int | None)
- `operation` (int | None)
- `object_attributes` (int | None)
- `message` (str | None)

## 52. Modify Resource
`modify_resource(self, quantity: 'int | None' = None, tribute_list: 'int | None' = None, source_player: 'int | None' = None, operation: 'int | None' = None) -> 'Effect'`

This effect can be used to modify the resource amounts of a particular player by specified amounts. Refer to the [Resources](../../../../general/resources/resources "Jump to: Game Mechanics > Resources") section of the guide to see all the resources that can be modified and their purposes

**Parameters:**
- `quantity` (int | None)
- `tribute_list` (int | None)
- `source_player` (int | None)
- `operation` (int | None)

## 53. Modify Resource By Variable
`modify_resource_by_variable(self, tribute_list: 'int | None' = None, source_player: 'int | None' = None, operation: 'int | None' = None, variable: 'int | None' = None) -> 'Effect'`

This effect can be used to modify the resource amounts of a particular player by the value of another variable. Refer to the [Resources](../../../../general/resources/resources "Jump to: Game Mechanics > Resources") section of the guide to see all the resources that can be modified and their purposes

**Parameters:**
- `tribute_list` (int | None)
- `source_player` (int | None)
- `operation` (int | None)
- `variable` (int | None)

## 54. Set Building Gather Point
`set_building_gather_point(self, object_list_unit_id: 'int | None' = None, source_player: 'int | None' = None, location_x: 'int | None' = None, location_y: 'int | None' = None, area_x1: 'int | None' = None, area_y1: 'int | None' = None, area_x2: 'int | None' = None, area_y2: 'int | None' = None, selected_object_ids: 'int | List[int] | None' = None, max_units_affected: 'int | None' = None) -> 'Effect'`

This effect can be used to set a gather point for specified buildings of a given player. The units affected by this effect are determined by the configurations of the effect

**Parameters:**
- `object_list_unit_id` (int | None)
- `source_player` (int | None)
- `location_x` (int | None)
- `location_y` (int | None)
- `area_x1` (int | None)
- `area_y1` (int | None)
- `area_x2` (int | None)
- `area_y2` (int | None)
- `selected_object_ids` (int | List[int] | None)
- `max_units_affected` (int | None)

## 55. Script Call
`script_call(self, string_id: 'int | None' = None, message: 'str | None' = None) -> 'Effect'`

This effect allows us to write or call functions from an XS Script. While the script call effect can be used to both call functions and write small scripts, it is advised to always use a function call and never use this effect for writing scripts. Refer to the [XS Scripting](../../../../general/xs/beginner/ "Jump to: XS Scripting: A Beginner's Guide")

**Parameters:**
- `string_id` (int | None)
- `message` (str | None)

## 56. Change Variable
`change_variable(self, quantity: 'int | None' = None, operation: 'int | None' = None, variable: 'int | None' = None, message: 'str | None' = None) -> 'Effect'`

This effect can be used to change the value of a variable.

**Parameters:**
- `quantity` (int | None)
- `operation` (int | None)
- `variable` (int | None)
- `message` (str | None)

## 57. Clear Timer
`clear_timer(self, timer: 'int | None' = None) -> 'Effect'`

This effect can be used to remove a displayed timer from the screen

**Parameters:**
- `timer` (int | None)

## 58. Change Object Player Color
`change_object_player_color(self, object_list_unit_id: 'int | None' = None, source_player: 'int | None' = None, area_x1: 'int | None' = None, area_y1: 'int | None' = None, area_x2: 'int | None' = None, area_y2: 'int | None' = None, player_color: 'int | None' = None, selected_object_ids: 'int | List[int] | None' = None, max_units_affected: 'int | None' = None) -> 'Effect'`

This effect can be used to change the colour of specified objects of a given player. The units affected by this effect are determined by the configurations of the effect

**Parameters:**
- `object_list_unit_id` (int | None)
- `source_player` (int | None)
- `area_x1` (int | None)
- `area_y1` (int | None)
- `area_x2` (int | None)
- `area_y2` (int | None)
- `player_color` (int | None)
- `selected_object_ids` (int | List[int] | None)
- `max_units_affected` (int | None)

## 59. Change Object Civilization Name
`change_object_civilization_name(self, source_player: 'int | None' = None, string_id: 'int | None' = None, area_x1: 'int | None' = None, area_y1: 'int | None' = None, area_x2: 'int | None' = None, area_y2: 'int | None' = None, message: 'str | None' = None, selected_object_ids: 'int | List[int] | None' = None, max_units_affected: 'int | None' = None) -> 'Effect'`

This effect can be used to change the civilization name of specified objects of a given player. The units affected by this effect are determined by the configurations of the effect

**Parameters:**
- `source_player` (int | None)
- `string_id` (int | None)
- `area_x1` (int | None)
- `area_y1` (int | None)
- `area_x2` (int | None)
- `area_y2` (int | None)
- `message` (str | None)
- `selected_object_ids` (int | List[int] | None)
- `max_units_affected` (int | None)

## 60. Change Object Player Name
`change_object_player_name(self, object_list_unit_id: 'int | None' = None, source_player: 'int | None' = None, string_id: 'int | None' = None, area_x1: 'int | None' = None, area_y1: 'int | None' = None, area_x2: 'int | None' = None, area_y2: 'int | None' = None, message: 'str | None' = None, selected_object_ids: 'int | List[int] | None' = None, max_units_affected: 'int | None' = None) -> 'Effect'`

This effect can be used to change the player name of specified objects of a given player. The units affected by this effect are determined by the configurations of the effect

**Parameters:**
- `object_list_unit_id` (int | None)
- `source_player` (int | None)
- `string_id` (int | None)
- `area_x1` (int | None)
- `area_y1` (int | None)
- `area_x2` (int | None)
- `area_y2` (int | None)
- `message` (str | None)
- `selected_object_ids` (int | List[int] | None)
- `max_units_affected` (int | None)

## 61. Disable Unit Targeting
`disable_unit_targeting(self, object_list_unit_id: 'int | None' = None, source_player: 'int | None' = None, area_x1: 'int | None' = None, area_y1: 'int | None' = None, area_x2: 'int | None' = None, area_y2: 'int | None' = None, selected_object_ids: 'int | List[int] | None' = None, max_units_affected: 'int | None' = None) -> 'Effect'`

This effect makes it so that the specified units of the given player cannot be targeted (basically, you can't perform any right click actions from another unit on these units anymore) by other units. The units affected by this effect are determined by the configurations of the effect

**Parameters:**
- `object_list_unit_id` (int | None)
- `source_player` (int | None)
- `area_x1` (int | None)
- `area_y1` (int | None)
- `area_x2` (int | None)
- `area_y2` (int | None)
- `selected_object_ids` (int | List[int] | None)
- `max_units_affected` (int | None)

## 62. Enable Unit Targeting
`enable_unit_targeting(self, object_list_unit_id: 'int | None' = None, source_player: 'int | None' = None, area_x1: 'int | None' = None, area_y1: 'int | None' = None, area_x2: 'int | None' = None, area_y2: 'int | None' = None, selected_object_ids: 'int | List[int] | None' = None, max_units_affected: 'int | None' = None) -> 'Effect'`

This effect makes it so that the specified units of the given player can be targeted by other units. Refer to the [Disable Unit Targeting](./<effect_id_ref 61> "Jump to: Disable Unit Targeting") effect. The units affected by this effect are determined by the configurations of the effect

**Parameters:**
- `object_list_unit_id` (int | None)
- `source_player` (int | None)
- `area_x1` (int | None)
- `area_y1` (int | None)
- `area_x2` (int | None)
- `area_y2` (int | None)
- `selected_object_ids` (int | List[int] | None)
- `max_units_affected` (int | None)

## 63. Change Technology Cost
`change_technology_cost(self, source_player: 'int | None' = None, technology: 'int | None' = None, resource_1: 'int | None' = None, resource_1_quantity: 'int | None' = None, resource_2: 'int | None' = None, resource_2_quantity: 'int | None' = None, resource_3: 'int | None' = None, resource_3_quantity: 'int | None' = None) -> 'Effect'`

This effect can be used to change a technology's cost for a particular player

**Parameters:**
- `source_player` (int | None)
- `technology` (int | None)
- `resource_1` (int | None)
- `resource_1_quantity` (int | None)
- `resource_2` (int | None)
- `resource_2_quantity` (int | None)
- `resource_3` (int | None)
- `resource_3_quantity` (int | None)

## 64. Change Technology Research Time
`change_technology_research_time(self, quantity: 'int | None' = None, source_player: 'int | None' = None, technology: 'int | None' = None) -> 'Effect'`

This effect can be used to change a technology's research time for a particular player

**Parameters:**
- `quantity` (int | None)
- `source_player` (int | None)
- `technology` (int | None)

## 65. Change Technology Name
`change_technology_name(self, source_player: 'int | None' = None, technology: 'int | None' = None, string_id: 'int | None' = None, message: 'str | None' = None) -> 'Effect'`

This effect can be used to change a technology's name for a particular player

**Parameters:**
- `source_player` (int | None)
- `technology` (int | None)
- `string_id` (int | None)
- `message` (str | None)

## 66. Change Technology Description
`change_technology_description(self, source_player: 'int | None' = None, technology: 'int | None' = None, string_id: 'int | None' = None, message: 'str | None' = None) -> 'Effect'`

This effect can be used to change a technology's Description for a particular player

**Parameters:**
- `source_player` (int | None)
- `technology` (int | None)
- `string_id` (int | None)
- `message` (str | None)

## 67. Enable Technology Stacking
`enable_technology_stacking(self, source_player: 'int | None' = None, technology: 'int | None' = None, quantity: 'int | None' = None) -> 'Effect'`

This effect enables 256x tech mode for the specified technology and player

**Parameters:**
- `source_player` (int | None)
- `technology` (int | None)
- `quantity` (int | None)

## 68. Disable Technology Stacking
`disable_technology_stacking(self, source_player: 'int | None' = None, technology: 'int | None' = None) -> 'Effect'`

This effect disables 256x tech mode for the specified technology and player. Refer to the [Enable Technology Stacking](./<effect_id_ref 67> "Jump to: Enable Technology Stacking") effect

**Parameters:**
- `source_player` (int | None)
- `technology` (int | None)

## 69. Acknowledge Multiplayer AI Signal
`acknowledge_multiplayer_ai_signal(self, ai_signal_value: 'int | None' = None) -> 'Effect'`

When `set-signal` is used in an AI file, this effect is used to unset it so it can be reused. This only works in Multiplayer games. Refer to the [Acknowledge AI Signal](./<effect_id_ref 50> "Jump to: Acknowledge AI Signal") effect for the single player version of this effect.

**Parameters:**
- `ai_signal_value` (int | None)

## 70. Disable Object Selection
`disable_object_selection(self, object_list_unit_id: 'int | None' = None, source_player: 'int | None' = None, area_x1: 'int | None' = None, area_y1: 'int | None' = None, area_x2: 'int | None' = None, area_y2: 'int | None' = None, selected_object_ids: 'int | List[int] | None' = None, max_units_affected: 'int | None' = None) -> 'Effect'`

This effect makes specified units of the given player unselectable. The units affected by this effect are determined by the configurations of the effect

**Parameters:**
- `object_list_unit_id` (int | None)
- `source_player` (int | None)
- `area_x1` (int | None)
- `area_y1` (int | None)
- `area_x2` (int | None)
- `area_y2` (int | None)
- `selected_object_ids` (int | List[int] | None)
- `max_units_affected` (int | None)

## 71. Enable Object Selection
`enable_object_selection(self, object_list_unit_id: 'int | None' = None, source_player: 'int | None' = None, area_x1: 'int | None' = None, area_y1: 'int | None' = None, area_x2: 'int | None' = None, area_y2: 'int | None' = None, selected_object_ids: 'int | List[int] | None' = None, max_units_affected: 'int | None' = None) -> 'Effect'`

This effect makes specified units of the given player selectable. Refer to the [Disable Object Selection](./<effect_id_ref 70> "Jump to: Disable Object Selection") effect. The units affected by this effect are determined by the configurations of the effect

**Parameters:**
- `object_list_unit_id` (int | None)
- `source_player` (int | None)
- `area_x1` (int | None)
- `area_y1` (int | None)
- `area_x2` (int | None)
- `area_y2` (int | None)
- `selected_object_ids` (int | List[int] | None)
- `max_units_affected` (int | None)

## 72. Change Color Mood
`change_color_mood(self, quantity: 'int | None' = None, color_mood: 'int | None' = None)`

This effect can change the colour mood of the map

**Parameters:**
- `quantity` (int | None)
- `color_mood` (int | None) -> **Dataset: ColorMood**

## 9999. add_train_location
`add_train_location(self, object_list_unit_id: 'int | None' = None, source_player: 'int | None' = None, object_list_unit_id_2: 'int | None' = None, button_location: 'int | None' = None, train_time: 'int | None' = None, hotkey: 'int | None' = None)`

*No description provided.*

**Parameters:**
- `object_list_unit_id` (int | None)
- `source_player` (int | None)
- `object_list_unit_id_2` (int | None)
- `button_location` (int | None)
- `train_time` (int | None)
- `hotkey` (int | None)

## 9999. change_object_caption
`change_object_caption(self, object_list_unit_id: 'int | None' = None, source_player: 'int | None' = None, string_id: 'int | None' = None, message: 'str | None' = None, area_x1: 'int | None' = None, area_y1: 'int | None' = None, area_x2: 'int | None' = None, area_y2: 'int | None' = None, selected_object_ids: 'int | List[int] | None' = None)`

*No description provided.*

**Parameters:**
- `object_list_unit_id` (int | None)
- `source_player` (int | None)
- `string_id` (int | None)
- `message` (str | None)
- `area_x1` (int | None)
- `area_y1` (int | None)
- `area_x2` (int | None)
- `area_y2` (int | None)
- `selected_object_ids` (int | List[int] | None)

## 9999. change_object_visibility
`change_object_visibility(self, source_player: 'int | None' = None, target_player: 'int | None' = None, area_x1: 'int | None' = None, area_y1: 'int | None' = None, area_x2: 'int | None' = None, area_y2: 'int | None' = None, visibility_state: 'int | None' = None, max_units_affected: 'int | None' = None, selected_object_ids: 'int | None' = None)`

*No description provided.*

**Parameters:**
- `source_player` (int | None)
- `target_player` (int | None)
- `area_x1` (int | None)
- `area_y1` (int | None)
- `area_x2` (int | None)
- `area_y2` (int | None)
- `visibility_state` (int | None)
- `max_units_affected` (int | None)
- `selected_object_ids` (int | None)

## 9999. change_player_color
`change_player_color(self, source_player: 'int | None' = None, player_color: 'int | None' = None)`

*No description provided.*

**Parameters:**
- `source_player` (int | None)
- `player_color` (int | None)

## 9999. change_technology_hotkey
`change_technology_hotkey(self, technology: 'int | None' = None, source_player: 'int | None' = None, quantity: 'int | None' = None) -> 'Effect'`

*No description provided.*

**Parameters:**
- `technology` (int | None)
- `source_player` (int | None)
- `quantity` (int | None)

## 9999. change_technology_icon
`change_technology_icon(self, technology: 'int | None' = None, source_player: 'int | None' = None, quantity: 'int | None' = None) -> 'Effect'`

*No description provided.*

**Parameters:**
- `technology` (int | None)
- `source_player` (int | None)
- `quantity` (int | None)

## 9999. change_technology_location
`change_technology_location(self, source_player: 'int | None' = None, technology: 'int | None' = None, object_list_unit_id_2: 'int | None' = None, button_location: 'int | None' = None) -> 'Effect'`

*No description provided.*

**Parameters:**
- `source_player` (int | None)
- `technology` (int | None)
- `object_list_unit_id_2` (int | None)
- `button_location` (int | None)

## 9999. count_units_into_variable
`count_units_into_variable(self, object_list_unit_id: 'int | None' = None, source_player: 'int | None' = None, area_x1: 'int | None' = None, area_y1: 'int | None' = None, area_x2: 'int | None' = None, area_y2: 'int | None' = None, object_group: 'int | None' = None, variable2: 'int | None' = None)`

*No description provided.*

**Parameters:**
- `object_list_unit_id` (int | None)
- `source_player` (int | None)
- `area_x1` (int | None)
- `area_y1` (int | None)
- `area_x2` (int | None)
- `area_y2` (int | None)
- `object_group` (int | None)
- `variable2` (int | None)

## 9999. create_decision
`create_decision(self, decision_id: 'int | None' = None, string_id: 'int | None' = None, message: 'str | None' = None, string_id_option1: 'int | None' = None, message_option1: 'str | None' = None, string_id_option2: 'int | None' = None, message_option2: 'str | None' = None)`

*No description provided.*

**Parameters:**
- `decision_id` (int | None)
- `string_id` (int | None)
- `message` (str | None)
- `string_id_option1` (int | None)
- `message_option1` (str | None)
- `string_id_option2` (int | None)
- `message_option2` (str | None)

## 9999. create_object_armor
`create_object_armor(self, armour_attack_quantity: 'int | None' = None, armour_attack_class: 'int | None' = None, object_list_unit_id: 'int | None' = None, source_player: 'int | None' = None, area_x1: 'int | None' = None, area_y1: 'int | None' = None, area_x2: 'int | None' = None, area_y2: 'int | None' = None, object_group: 'int | None' = None, object_type: 'int | None' = None, operation: 'int | None' = None, selected_object_ids: 'int | List[int] | None' = None, max_units_affected: 'int | None' = None)`

*No description provided.*

**Parameters:**
- `armour_attack_quantity` (int | None)
- `armour_attack_class` (int | None)
- `object_list_unit_id` (int | None)
- `source_player` (int | None)
- `area_x1` (int | None)
- `area_y1` (int | None)
- `area_x2` (int | None)
- `area_y2` (int | None)
- `object_group` (int | None)
- `object_type` (int | None)
- `operation` (int | None)
- `selected_object_ids` (int | List[int] | None)
- `max_units_affected` (int | None)

## 9999. create_object_attack
`create_object_attack(self, armour_attack_quantity: 'int | None' = None, armour_attack_class: 'int | None' = None, object_list_unit_id: 'int | None' = None, source_player: 'int | None' = None, area_x1: 'int | None' = None, area_y1: 'int | None' = None, area_x2: 'int | None' = None, area_y2: 'int | None' = None, object_group: 'int | None' = None, object_type: 'int | None' = None, operation: 'int | None' = None, selected_object_ids: 'int | List[int] | None' = None, max_units_affected: 'int | None' = None)`

*No description provided.*

**Parameters:**
- `armour_attack_quantity` (int | None)
- `armour_attack_class` (int | None)
- `object_list_unit_id` (int | None)
- `source_player` (int | None)
- `area_x1` (int | None)
- `area_y1` (int | None)
- `area_x2` (int | None)
- `area_y2` (int | None)
- `object_group` (int | None)
- `object_type` (int | None)
- `operation` (int | None)
- `selected_object_ids` (int | List[int] | None)
- `max_units_affected` (int | None)

## 9999. delete_key
`delete_key(self, message: 'str | None' = None) -> 'Effect'`

*No description provided.*

**Parameters:**
- `message` (str | None)

## 9999. disable_object_deletion
`disable_object_deletion(self, object_list_unit_id: 'int | None' = None, source_player: 'int | None' = None, area_x1: 'int | None' = None, area_y1: 'int | None' = None, area_x2: 'int | None' = None, area_y2: 'int | None' = None, selected_object_ids: 'int | List[int] | None' = None, max_units_affected: 'int | None' = None)`

*No description provided.*

**Parameters:**
- `object_list_unit_id` (int | None)
- `source_player` (int | None)
- `area_x1` (int | None)
- `area_y1` (int | None)
- `area_x2` (int | None)
- `area_y2` (int | None)
- `selected_object_ids` (int | List[int] | None)
- `max_units_affected` (int | None)

## 9999. disable_unit_attackable
`disable_unit_attackable(self, object_list_unit_id: 'int | None' = None, source_player: 'int | None' = None, area_x1: 'int | None' = None, area_y1: 'int | None' = None, area_x2: 'int | None' = None, area_y2: 'int | None' = None, selected_object_ids: 'int | List[int] | None' = None, max_units_affected: 'int | None' = None) -> 'Effect'`

*No description provided.*

**Parameters:**
- `object_list_unit_id` (int | None)
- `source_player` (int | None)
- `area_x1` (int | None)
- `area_y1` (int | None)
- `area_x2` (int | None)
- `area_y2` (int | None)
- `selected_object_ids` (int | List[int] | None)
- `max_units_affected` (int | None)

## 9999. enable_object_deletion
`enable_object_deletion(self, object_list_unit_id: 'int | None' = None, source_player: 'int | None' = None, area_x1: 'int | None' = None, area_y1: 'int | None' = None, area_x2: 'int | None' = None, area_y2: 'int | None' = None, selected_object_ids: 'int | List[int] | None' = None, max_units_affected: 'int | None' = None)`

*No description provided.*

**Parameters:**
- `object_list_unit_id` (int | None)
- `source_player` (int | None)
- `area_x1` (int | None)
- `area_y1` (int | None)
- `area_x2` (int | None)
- `area_y2` (int | None)
- `selected_object_ids` (int | List[int] | None)
- `max_units_affected` (int | None)

## 9999. enable_unit_attackable
`enable_unit_attackable(self, object_list_unit_id: 'int | None' = None, source_player: 'int | None' = None, area_x1: 'int | None' = None, area_y1: 'int | None' = None, area_x2: 'int | None' = None, area_y2: 'int | None' = None, selected_object_ids: 'int | List[int] | None' = None, max_units_affected: 'int | None' = None) -> 'Effect'`

*No description provided.*

**Parameters:**
- `object_list_unit_id` (int | None)
- `source_player` (int | None)
- `area_x1` (int | None)
- `area_y1` (int | None)
- `area_x2` (int | None)
- `area_y2` (int | None)
- `selected_object_ids` (int | List[int] | None)
- `max_units_affected` (int | None)

## 9999. initiate_research
`initiate_research(self, source_player: 'int | None' = None, technology: 'int | None' = None, selected_object_ids: 'int | List[int] | None' = None)`

*No description provided.*

**Parameters:**
- `source_player` (int | None)
- `technology` (int | None)
- `selected_object_ids` (int | List[int] | None)

## 9999. load_key_value
`load_key_value(self, variable: 'int | None' = None, message: 'str | None' = None, quantity: 'int | None' = None) -> 'Effect'`

*No description provided.*

**Parameters:**
- `variable` (int | None)
- `message` (str | None)
- `quantity` (int | None)

## 9999. modify_attribute_by_variable
`modify_attribute_by_variable(self, object_list_unit_id: 'int | None' = None, source_player: 'int | None' = None, operation: 'int | None' = None, object_attributes: 'int | None' = None, variable: 'int | None' = None, message: 'str | None' = None, armour_attack_class: 'int | None' = None)`

*No description provided.*

**Parameters:**
- `object_list_unit_id` (int | None)
- `source_player` (int | None)
- `operation` (int | None)
- `object_attributes` (int | None)
- `variable` (int | None)
- `message` (str | None)
- `armour_attack_class` (int | None)

## 9999. modify_attribute_for_class
`modify_attribute_for_class(self, object_group2: 'int | None' = None, object_type2: 'int | None' = None, source_player: 'int | None' = None, object_attributes: 'int | None' = None, message: 'int | None' = None, operation: 'int | None' = None, quantity: 'int | float | None' = None, armour_attack_quantity: 'int | None' = None, armour_attack_class: 'int | None' = None)`

*No description provided.*

**Parameters:**
- `object_group2` (int | None)
- `object_type2` (int | None)
- `source_player` (int | None)
- `object_attributes` (int | None)
- `message` (int | None)
- `operation` (int | None)
- `quantity` (int | float | None)
- `armour_attack_quantity` (int | None)
- `armour_attack_class` (int | None)

## 9999. modify_object_attribute
`modify_object_attribute(self, object_list_unit_id: 'int | None' = None, source_player: 'int | None' = None, object_attributes: 'int | None' = None, selected_object_ids: 'int | List[int] | None' = None, area_x1: 'int | None' = None, area_y1: 'int | None' = None, area_x2: 'int | None' = None, area_y2: 'int | None' = None, operation: 'int | None' = None, message: 'str | None' = None, quantity: 'int | float | None' = None, armour_attack_quantity: 'int | None' = None, armour_attack_class: 'int | None' = None)`

*No description provided.*

**Parameters:**
- `object_list_unit_id` (int | None)
- `source_player` (int | None)
- `object_attributes` (int | None)
- `selected_object_ids` (int | List[int] | None)
- `area_x1` (int | None)
- `area_y1` (int | None)
- `area_x2` (int | None)
- `area_y2` (int | None)
- `operation` (int | None)
- `message` (str | None)
- `quantity` (int | float | None)
- `armour_attack_quantity` (int | None)
- `armour_attack_class` (int | None)

## 9999. modify_object_attribute_by_variable
`modify_object_attribute_by_variable(self, object_list_unit_id: 'int | None' = None, source_player: 'int | None' = None, object_attributes: 'int | None' = None, selected_object_ids: 'int | List[int] | None' = None, area_x1: 'int | None' = None, area_y1: 'int | None' = None, area_x2: 'int | None' = None, area_y2: 'int | None' = None, operation: 'int | None' = None, message: 'str | None' = None, variable: 'int | None' = None, armour_attack_class: 'int | None' = None)`

*No description provided.*

**Parameters:**
- `object_list_unit_id` (int | None)
- `source_player` (int | None)
- `object_attributes` (int | None)
- `selected_object_ids` (int | List[int] | None)
- `area_x1` (int | None)
- `area_y1` (int | None)
- `area_x2` (int | None)
- `area_y2` (int | None)
- `operation` (int | None)
- `message` (str | None)
- `variable` (int | None)
- `armour_attack_class` (int | None)

## 9999. modify_variable_by_attribute
`modify_variable_by_attribute(self, object_list_unit_id: 'int | None' = None, source_player: 'int | None' = None, operation: 'int | None' = None, object_attributes: 'int | None' = None, variable: 'int | None' = None, message: 'str | None' = None, armour_attack_class: 'int | None' = None)`

*No description provided.*

**Parameters:**
- `object_list_unit_id` (int | None)
- `source_player` (int | None)
- `operation` (int | None)
- `object_attributes` (int | None)
- `variable` (int | None)
- `message` (str | None)
- `armour_attack_class` (int | None)

## 9999. modify_variable_by_resource
`modify_variable_by_resource(self, tribute_list: 'int | None' = None, source_player: 'int | None' = None, operation: 'int | None' = None, variable: 'int | None' = None) -> 'Effect'`

*No description provided.*

**Parameters:**
- `tribute_list` (int | None)
- `source_player` (int | None)
- `operation` (int | None)
- `variable` (int | None)

## 9999. modify_variable_by_variable
`modify_variable_by_variable(self, variable: 'int | None' = None, operation: 'int | None' = None, variable2: 'int | None' = None)`

*No description provided.*

**Parameters:**
- `variable` (int | None)
- `operation` (int | None)
- `variable2` (int | None)

## 9999. none
`none(self) -> 'Effect'`

*No description provided.*

*No parameters.*

## 9999. research_local_technology
`research_local_technology(self, local_technology: 'int | None' = None, source_player: 'int | None' = None, selected_object_ids: 'int | List[int] | None' = None, area_x1: 'int | None' = None, area_y1: 'int | None' = None, area_x2: 'int | None' = None, area_y2: 'int | None' = None, object_list_unit_id_2: 'int | None' = None)`

*No description provided.*

**Parameters:**
- `local_technology` (int | None)
- `source_player` (int | None)
- `selected_object_ids` (int | List[int] | None)
- `area_x1` (int | None)
- `area_y1` (int | None)
- `area_x2` (int | None)
- `area_y2` (int | None)
- `object_list_unit_id_2` (int | None)

## 9999. set_object_cost
`set_object_cost(self, object_list_unit_id: 'int | None' = None, source_player: 'int | None' = None, quantity: 'int | None' = None, tribute_list: 'int | None' = None) -> 'Effect'`

*No description provided.*

**Parameters:**
- `object_list_unit_id` (int | None)
- `source_player` (int | None)
- `quantity` (int | None)
- `tribute_list` (int | None)

## 9999. store_key_value
`store_key_value(self, variable: 'int | None' = None, message: 'str | None' = None) -> 'Effect'`

*No description provided.*

**Parameters:**
- `variable` (int | None)
- `message` (str | None)

## 9999. train_unit
`train_unit(self, quantity: 'int | None' = None, object_list_unit_id: 'int | None' = None, source_player: 'int | None' = None, location_x: 'int | None' = None, location_y: 'int | None' = None, area_x1: 'int | None' = None, area_y1: 'int | None' = None, area_x2: 'int | None' = None, area_y2: 'int | None' = None, selected_object_ids: 'int | List[int] | None' = None, max_units_affected: 'int | None' = None)`

*No description provided.*

**Parameters:**
- `quantity` (int | None)
- `object_list_unit_id` (int | None)
- `source_player` (int | None)
- `location_x` (int | None)
- `location_y` (int | None)
- `area_x1` (int | None)
- `area_y1` (int | None)
- `area_x2` (int | None)
- `area_y2` (int | None)
- `selected_object_ids` (int | List[int] | None)
- `max_units_affected` (int | None)
