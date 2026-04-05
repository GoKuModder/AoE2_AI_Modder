# Trigger Knowledge: Real Project Usage
Generated file. Do not hand-edit; run tools/build_trigger_knowledge.py.

This file summarizes how AoE2ScenarioParser trigger conditions and effects are used in the local reference projects.

Reference projects scanned:
- `LordsOfDiplomacy - Easy Mode`
- `GoKu RPG Project` (excluding `Difficulty`)
- `Hide_and_Seek`

- Conditions observed in real projects: **18 / 41**
- Effects observed in real projects: **67 / 102**

## Most Used Conditions
- `variable_value` (172 uses): lords_of_diplomacy_easy_mode, goku_rpg_project, hide_and_seek
- `timer` (143 uses): lords_of_diplomacy_easy_mode, goku_rpg_project, hide_and_seek
- `script_call` (62 uses): lords_of_diplomacy_easy_mode, goku_rpg_project, hide_and_seek
- `and_` (58 uses): lords_of_diplomacy_easy_mode, goku_rpg_project
- `objects_in_area` (40 uses): lords_of_diplomacy_easy_mode, goku_rpg_project
- `accumulate_attribute` (18 uses): lords_of_diplomacy_easy_mode, goku_rpg_project, hide_and_seek
- `own_objects` (18 uses): lords_of_diplomacy_easy_mode, goku_rpg_project, hide_and_seek
- `researching_tech` (14 uses): lords_of_diplomacy_easy_mode
- `or_` (12 uses): lords_of_diplomacy_easy_mode, goku_rpg_project
- `destroy_object` (11 uses): goku_rpg_project

## Most Used Effects
- `modify_attribute` (390 uses): lords_of_diplomacy_easy_mode, goku_rpg_project, hide_and_seek
- `activate_trigger` (216 uses): lords_of_diplomacy_easy_mode, goku_rpg_project, hide_and_seek
- `script_call` (159 uses): lords_of_diplomacy_easy_mode, goku_rpg_project, hide_and_seek
- `change_variable` (128 uses): lords_of_diplomacy_easy_mode, goku_rpg_project, hide_and_seek
- `modify_resource` (85 uses): lords_of_diplomacy_easy_mode, goku_rpg_project, hide_and_seek
- `deactivate_trigger` (77 uses): lords_of_diplomacy_easy_mode, goku_rpg_project, hide_and_seek
- `play_sound` (77 uses): lords_of_diplomacy_easy_mode, goku_rpg_project, hide_and_seek
- `remove_object` (66 uses): lords_of_diplomacy_easy_mode, goku_rpg_project, hide_and_seek
- `send_chat` (40 uses): lords_of_diplomacy_easy_mode, goku_rpg_project, hide_and_seek
- `disable_unit_targeting` (33 uses): lords_of_diplomacy_easy_mode, goku_rpg_project, hide_and_seek

## How To Use The JSON
- Use `condition_project_usage.json` when the question is about how a condition is used in real projects.
- Use `effect_project_usage.json` when the question is about how an effect is used in real projects.
- Join these usage datasets with `conditions_knowledge.json` and `effects_knowledge.json` for signatures and parameters.
