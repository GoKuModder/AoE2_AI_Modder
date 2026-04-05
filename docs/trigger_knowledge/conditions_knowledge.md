# Trigger Knowledge: Conditions
Generated file. Do not hand-edit; run tools/build_trigger_knowledge.py.
Data source: canonical `conditions_knowledge.json`.

## Index
| ID | Name | Method |
|---|---|---|
| 0 | [None](#none) | `none` |
| 1 | [Bring Object To Area](#bring-object-to-area) | `bring_object_to_area` |
| 2 | [Bring Object To Object](#bring-object-to-object) | `bring_object_to_object` |
| 3 | [Own Objects](#own-objects) | `own_objects` |
| 4 | [Own Fewer Objects](#own-fewer-objects) | `own_fewer_objects` |
| 5 | [Objects In Area](#objects-in-area) | `objects_in_area` |
| 6 | [Destroy Object](#destroy-object) | `destroy_object` |
| 7 | [Capture Object](#capture-object) | `capture_object` |
| 8 | [Accumulate Attribute](#accumulate-attribute) | `accumulate_attribute` |
| 9 | [Research Technology](#research-technology) | `research_technology` |
| 10 | [Timer](#timer) | `timer` |
| 11 | [Object Selected](#object-selected) | `object_selected` |
| 12 | [AI Signal](#ai-signal) | `ai_signal` |
| 13 | [Player Defeated](#player-defeated) | `player_defeated` |
| 14 | [Object Has Target](#object-has-target) | `object_has_target` |
| 15 | [Object Visible](#object-visible) | `object_visible` |
| 16 | [Object Not Visible](#object-not-visible) | `object_not_visible` |
| 17 | [Researching Tech](#researching-tech) | `researching_tech` |
| 18 | [Units Garrisoned](#units-garrisoned) | `units_garrisoned` |
| 19 | [Difficulty Level](#difficulty-level) | `difficulty_level` |
| 20 | [Chance](#chance) | `chance` |
| 21 | [Technology State](#technology-state) | `technology_state` |
| 22 | [Variable Value](#variable-value) | `variable_value` |
| 23 | [Object HP](#object-hp) | `object_hp` |
| 24 | [Diplomacy State](#diplomacy-state) | `diplomacy_state` |
| 25 | [Script Call](#script-call) | `script_call` |
| 26 | [Object Selected Multiplayer](#object-selected-multiplayer) | `object_selected_multiplayer` |
| 27 | [Object Visible Multiplayer](#object-visible-multiplayer) | `object_visible_multiplayer` |
| 28 | [Object Has Action](#object-has-action) | `object_has_action` |
| 29 | [Or](#or) | `or_` |
| 30 | [AI Signal Multiplayer](#ai-signal-multiplayer) | `ai_signal_multiplayer` |
| 54 | [Building Is Trading](#building-is-trading) | `building_is_trading` |
| 55 | [Display Timer Triggered](#display-timer-triggered) | `display_timer_triggered` |
| 56 | [Victory Timer](#victory-timer) | `victory_timer` |
| 57 | [And](#and) | `and_` |
| 75 | [Decision Triggered](#decision-triggered) | `decision_triggered` |
| 76 | [Object Attacked](#object-attacked) | `object_attacked` |
| 77 | [Hero Power Cast](#hero-power-cast) | `hero_power_cast` |
| 78 | [Compare Variables](#compare-variables) | `compare_variables` |
| 79 | [Trigger Active](#trigger-active) | `trigger_active` |
| 80 | [Local Tech Researched](#local-tech-researched) | `local_tech_researched` |

## 0. None
`none(self) -> 'Condition'`

... It's called none... What parameters do **you** think it has?! <3

*No parameters.*

**Notes:**
- ... It's called none... What parameters do **you** think it has?! <3

## 1. Bring Object To Area
`bring_object_to_area(self, unit_object: 'int | None' = None, area_x1: 'int | None' = None, area_y1: 'int | None' = None, area_x2: 'int | None' = None, area_y2: 'int | None' = None, inverted: 'int | None' = None) -> 'Condition'`

Parser condition for Bring Object To Area.

**Parameters:**
- `unit_object` (int | None, default=None)
- `area_x1` (int | None, default=None)
- `area_y1` (int | None, default=None)
- `area_x2` (int | None, default=None)
- `area_y2` (int | None, default=None)
- `inverted` (int | None, default=None)

## 2. Bring Object To Object
`bring_object_to_object(self, unit_object: 'int | None' = None, next_object: 'int | None' = None, inverted: 'int | None' = None) -> 'Condition'`

Parser condition for Bring Object To Object.

**Parameters:**
- `unit_object` (int | None, default=None)
- `next_object` (int | None, default=None)
- `inverted` (int | None, default=None)

## 3. Own Objects
`own_objects(self, quantity: 'int | None' = None, object_list: 'int | None' = None, source_player: 'int | None' = None, object_group: 'int | None' = None, object_type: 'int | None' = None, include_changeable_weapon_objects: 'int | None' = None) -> 'Condition'`

Parser condition for Own Objects.

**Parameters:**
- `quantity` (int | None, default=None)
- `object_list` (int | None, default=None)
- `source_player` (int | None, default=None)
- `object_group` (int | None, default=None)
- `object_type` (int | None, default=None)
- `include_changeable_weapon_objects` (int | None, default=None)

## 4. Own Fewer Objects
`own_fewer_objects(self, quantity: 'int | None' = None, object_list: 'int | None' = None, source_player: 'int | None' = None, area_x1: 'int | None' = None, area_y1: 'int | None' = None, area_x2: 'int | None' = None, area_y2: 'int | None' = None, object_group: 'int | None' = None, object_type: 'int | None' = None, include_changeable_weapon_objects: 'int | None' = None) -> 'Condition'`

Parser condition for Own Fewer Objects.

**Parameters:**
- `quantity` (int | None, default=None)
- `object_list` (int | None, default=None)
- `source_player` (int | None, default=None)
- `area_x1` (int | None, default=None)
- `area_y1` (int | None, default=None)
- `area_x2` (int | None, default=None)
- `area_y2` (int | None, default=None)
- `object_group` (int | None, default=None)
- `object_type` (int | None, default=None)
- `include_changeable_weapon_objects` (int | None, default=None)

## 5. Objects In Area
`objects_in_area(self, quantity: 'int | None' = None, object_list: 'int | None' = None, source_player: 'int | None' = None, area_x1: 'int | None' = None, area_y1: 'int | None' = None, area_x2: 'int | None' = None, area_y2: 'int | None' = None, object_group: 'int | None' = None, object_type: 'int | None' = None, inverted: 'int | None' = None, object_state: 'int | None' = None, include_changeable_weapon_objects: 'int | None' = None) -> 'Condition'`

Parser condition for Objects In Area.

**Parameters:**
- `quantity` (int | None, default=None)
- `object_list` (int | None, default=None)
- `source_player` (int | None, default=None)
- `area_x1` (int | None, default=None)
- `area_y1` (int | None, default=None)
- `area_x2` (int | None, default=None)
- `area_y2` (int | None, default=None)
- `object_group` (int | None, default=None)
- `object_type` (int | None, default=None)
- `inverted` (int | None, default=None)
- `object_state` (int | None, default=None)
- `include_changeable_weapon_objects` (int | None, default=None)

## 6. Destroy Object
`destroy_object(self, unit_object: 'int | None' = None, inverted: 'int | None' = None) -> 'Condition'`

Parser condition for Destroy Object.

**Parameters:**
- `unit_object` (int | None, default=None)
- `inverted` (int | None, default=None)

## 7. Capture Object
`capture_object(self, unit_object: 'int | None' = None, source_player: 'int | None' = None, inverted: 'int | None' = None) -> 'Condition'`

Parser condition for Capture Object.

**Parameters:**
- `unit_object` (int | None, default=None)
- `source_player` (int | None, default=None)
- `inverted` (int | None, default=None)

## 8. Accumulate Attribute
`accumulate_attribute(self, quantity: 'int | None' = None, attribute: 'int | None' = None, source_player: 'int | None' = None, inverted: 'int | None' = None) -> 'Condition'`

Parser condition for Accumulate Attribute.

**Parameters:**
- `quantity` (int | None, default=None)
- `attribute` (int | None, default=None)
- `source_player` (int | None, default=None)
- `inverted` (int | None, default=None)

## 9. Research Technology
`research_technology(self, source_player: 'int | None' = None, technology: 'int | None' = None, inverted: 'int | None' = None) -> 'Condition'`

Parser condition for Research Technology.

**Parameters:**
- `source_player` (int | None, default=None)
- `technology` (int | None, default=None)
- `inverted` (int | None, default=None)

## 10. Timer
`timer(self, timer: 'int | None' = None, inverted: 'int | None' = None) -> 'Condition'`

Parser condition for Timer.

**Parameters:**
- `timer` (int | None, default=None)
- `inverted` (int | None, default=None)

## 11. Object Selected
`object_selected(self, unit_object: 'int | None' = None, inverted: 'int | None' = None) -> 'Condition'`

Parser condition for Object Selected.

**Parameters:**
- `unit_object` (int | None, default=None)
- `inverted` (int | None, default=None)

## 12. AI Signal
`ai_signal(self, ai_signal: 'int | None' = None, inverted: 'int | None' = None) -> 'Condition'`

Parser condition for AI Signal.

**Parameters:**
- `ai_signal` (int | None, default=None)
- `inverted` (int | None, default=None)

## 13. Player Defeated
`player_defeated(self, source_player: 'int | None' = None, inverted: 'int | None' = None) -> 'Condition'`

Parser condition for Player Defeated.

**Parameters:**
- `source_player` (int | None, default=None)
- `inverted` (int | None, default=None)

## 14. Object Has Target
`object_has_target(self, unit_object: 'int | None' = None, next_object: 'int | None' = None, object_list: 'int | None' = None, object_group: 'int | None' = None, object_type: 'int | None' = None, inverted: 'int | None' = None) -> 'Condition'`

Parser condition for Object Has Target.

**Parameters:**
- `unit_object` (int | None, default=None)
- `next_object` (int | None, default=None)
- `object_list` (int | None, default=None)
- `object_group` (int | None, default=None)
- `object_type` (int | None, default=None)
- `inverted` (int | None, default=None)

## 15. Object Visible
`object_visible(self, unit_object: 'int | None' = None) -> 'Condition'`

Parser condition for Object Visible.

**Parameters:**
- `unit_object` (int | None, default=None)

## 16. Object Not Visible
`object_not_visible(self, unit_object: 'int | None' = None) -> 'Condition'`

Parser condition for Object Not Visible.

**Parameters:**
- `unit_object` (int | None, default=None)

## 17. Researching Tech
`researching_tech(self, source_player: 'int | None' = None, technology: 'int | None' = None, inverted: 'int | None' = None) -> 'Condition'`

Parser condition for Researching Tech.

**Parameters:**
- `source_player` (int | None, default=None)
- `technology` (int | None, default=None)
- `inverted` (int | None, default=None)

## 18. Units Garrisoned
`units_garrisoned(self, quantity: 'int | None' = None, unit_object: 'int | None' = None, inverted: 'int | None' = None) -> 'Condition'`

Parser condition for Units Garrisoned.

**Parameters:**
- `quantity` (int | None, default=None)
- `unit_object` (int | None, default=None)
- `inverted` (int | None, default=None)

## 19. Difficulty Level
`difficulty_level(self, quantity: 'int | None' = None, inverted: 'int | None' = None) -> 'Condition'`

Parser condition for Difficulty Level.

**Parameters:**
- `quantity` (int | None, default=None)
- `inverted` (int | None, default=None)
- `condition_type` (Any)

## 20. Chance
`chance(self, quantity: 'int | None' = None) -> 'Condition'`

Parser condition for Chance.

**Parameters:**
- `quantity` (int | None, default=None)

## 21. Technology State
`technology_state(self, quantity: 'int | None' = None, source_player: 'int | None' = None, technology: 'int | None' = None, inverted: 'int | None' = None) -> 'Condition'`

Parser condition for Technology State.

**Parameters:**
- `quantity` (int | None, default=None)
- `source_player` (int | None, default=None)
- `technology` (int | None, default=None)
- `inverted` (int | None, default=None)

## 22. Variable Value
`variable_value(self, quantity: 'int | None' = None, inverted: 'int | None' = None, variable: 'int | None' = None, comparison: 'int | None' = None) -> 'Condition'`

Parser condition for Variable Value.

**Parameters:**
- `quantity` (int | None, default=None)
- `inverted` (int | None, default=None)
- `variable` (int | None, default=None)
- `comparison` (int | None, default=None)

## 23. Object HP
`object_hp(self, quantity: 'int | None' = None, unit_object: 'int | None' = None, inverted: 'int | None' = None, comparison: 'int | None' = None) -> 'Condition'`

Parser condition for Object HP.

**Parameters:**
- `quantity` (int | None, default=None)
- `unit_object` (int | None, default=None)
- `inverted` (int | None, default=None)
- `comparison` (int | None, default=None)

## 24. Diplomacy State
`diplomacy_state(self, quantity: 'int | None' = None, source_player: 'int | None' = None, inverted: 'int | None' = None, target_player: 'int | None' = None) -> 'Condition'`

Parser condition for Diplomacy State.

**Parameters:**
- `quantity` (int | None, default=None)
- `source_player` (int | None, default=None)
- `inverted` (int | None, default=None)
- `target_player` (int | None, default=None)

## 25. Script Call
`script_call(self, xs_function: 'str | None' = None) -> 'Condition'`

This condition was added in: 1.40

**Parameters:**
- `xs_function` (str | None, default=None)

**Notes:**
- This condition was added in: 1.40

## 26. Object Selected Multiplayer
`object_selected_multiplayer(self, unit_object: 'int | None' = None, source_player: 'int | None' = None, inverted: 'int | None' = None) -> 'Condition'`

This condition was added in: 1.40

**Parameters:**
- `unit_object` (int | None, default=None)
- `source_player` (int | None, default=None)
- `inverted` (int | None, default=None)

**Notes:**
- This condition was added in: 1.40

## 27. Object Visible Multiplayer
`object_visible_multiplayer(self, unit_object: 'int | None' = None, source_player: 'int | None' = None, inverted: 'int | None' = None) -> 'Condition'`

This condition was added in: 1.40

**Parameters:**
- `unit_object` (int | None, default=None)
- `source_player` (int | None, default=None)
- `inverted` (int | None, default=None)

**Notes:**
- This condition was added in: 1.40

## 28. Object Has Action
`object_has_action(self, unit_object: 'int | None' = None, next_object: 'int | None' = None, object_list: 'int | None' = None, object_group: 'int | None' = None, object_type: 'int | None' = None, inverted: 'int | None' = None, unit_ai_action: 'int | None' = None) -> 'Condition'`

This condition was added in: 1.40

**Parameters:**
- `unit_object` (int | None, default=None)
- `next_object` (int | None, default=None)
- `object_list` (int | None, default=None)
- `object_group` (int | None, default=None)
- `object_type` (int | None, default=None)
- `inverted` (int | None, default=None)
- `unit_ai_action` (int | None, default=None)

**Notes:**
- This condition was added in: 1.40

## 29. Or
`or_(self) -> 'Condition'`

The **OR** condition does not have any attributes This condition was added in: 1.40

*No parameters.*

**Notes:**
- The **OR** condition does not have any attributes
- This condition was added in: 1.40

## 30. AI Signal Multiplayer
`ai_signal_multiplayer(self, ai_signal: 'int | None' = None, inverted: 'int | None' = None) -> 'Condition'`

This condition was added in: 1.40

**Parameters:**
- `ai_signal` (int | None, default=None)
- `inverted` (int | None, default=None)

**Notes:**
- This condition was added in: 1.40

## 54. Building Is Trading
`building_is_trading(self, unit_object: 'int | None' = None, inverted: 'int | None' = None) -> 'Condition'`

This condition was added in: 1.46

**Parameters:**
- `unit_object` (int | None, default=None)
- `inverted` (int | None, default=None)

**Notes:**
- This condition was added in: 1.46

## 55. Display Timer Triggered
`display_timer_triggered(self, timer_id: 'int | None' = None, inverted: 'int | None' = None) -> 'Condition'`

This condition was added in: 1.46

**Parameters:**
- `timer_id` (int | None, default=None)
- `inverted` (int | None, default=None)

**Notes:**
- This condition was added in: 1.46

## 56. Victory Timer
`victory_timer(self, quantity: 'int | None' = None, source_player: 'int | None' = None, inverted: 'int | None' = None, comparison: 'int | None' = None, victory_timer_type: 'int | None' = None) -> 'Condition'`

This condition was added in: 1.46

**Parameters:**
- `quantity` (int | None, default=None)
- `source_player` (int | None, default=None)
- `inverted` (int | None, default=None)
- `comparison` (int | None, default=None)
- `victory_timer_type` (int | None, default=None)

**Notes:**
- This condition was added in: 1.46

## 57. And
`and_(self) -> 'Condition'`

The **AND** condition does not have any attributes This condition was added in: 1.46

*No parameters.*

**Notes:**
- The **AND** condition does not have any attributes
- This condition was added in: 1.46

## 75. Decision Triggered
`decision_triggered(self, inverted: 'int | None' = None, decision_id: 'int | None' = None, decision_option: 'int | None' = None)`

This condition was added in: 1.54 (Trigger version 4.1)

**Parameters:**
- `inverted` (int | None, default=None)
- `decision_id` (int | None, default=None)
- `decision_option` (int | None, default=None)

**Notes:**
- This condition was added in: 1.54 (Trigger version 4.1)

## 76. Object Attacked
`object_attacked(self, object_list: 'int | None' = None, quantity: 'int | None' = None, source_player: 'int | None' = None, object_group: 'int | None' = None, object_type: 'int | None' = None, unit_object: 'int | None' = None, inverted: 'int | None' = None)`

This condition was added in: 1.54 (Trigger version 4.1)

**Parameters:**
- `object_list` (int | None, default=None)
- `quantity` (int | None, default=None)
- `source_player` (int | None, default=None)
- `object_group` (int | None, default=None)
- `object_type` (int | None, default=None)
- `unit_object` (int | None, default=None)
- `inverted` (int | None, default=None)

**Notes:**
- This condition was added in: 1.54 (Trigger version 4.1)

## 77. Hero Power Cast
`hero_power_cast(self, source_player: 'int | None' = None)`

This condition was added in: 1.54 (Trigger version 4.1)

**Parameters:**
- `source_player` (int | None, default=None)

**Notes:**
- This condition was added in: 1.54 (Trigger version 4.1)

## 78. Compare Variables
`compare_variables(self, inverted: 'int | None' = None, variable: 'int | None' = None, comparison: 'int | None' = None, variable2: 'int | None' = None)`

This condition was added in: 1.54 (Trigger version 4.1)

**Parameters:**
- `inverted` (int | None, default=None)
- `variable` (int | None, default=None)
- `comparison` (int | None, default=None)
- `variable2` (int | None, default=None)

**Notes:**
- This condition was added in: 1.54 (Trigger version 4.1)

## 79. Trigger Active
`trigger_active(self, trigger_id: 'int | None' = None, inverted: 'int | None' = None)`

This condition was added in: 1.54 (Trigger version 4.1)

**Parameters:**
- `trigger_id` (int | None, default=None)
- `inverted` (int | None, default=None)

**Notes:**
- This condition was added in: 1.54 (Trigger version 4.1)

## 80. Local Tech Researched
`local_tech_researched(self, local_technology: 'int | None' = None, source_player: 'int | None' = None, unit_object: 'int | None' = None, area_x1: 'int | None' = None, area_y1: 'int | None' = None, area_x2: 'int | None' = None, area_y2: 'int | None' = None, inverted: 'int | None' = None, quantity: 'int | None' = None)`

This condition was added in: 1.55 (Trigger version 4.5)

**Parameters:**
- `local_technology` (int | None, default=None)
- `source_player` (int | None, default=None)
- `unit_object` (int | None, default=None)
- `area_x1` (int | None, default=None)
- `area_y1` (int | None, default=None)
- `area_x2` (int | None, default=None)
- `area_y2` (int | None, default=None)
- `inverted` (int | None, default=None)
- `quantity` (int | None, default=None)

**Notes:**
- This condition was added in: 1.55 (Trigger version 4.5)
