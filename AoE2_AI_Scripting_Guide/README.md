# AoE2 AI Scripting Guide for LLM Agents

Goal: provide an LLM-safe reference for writing `.per` AI scripts that focus on:

- player interaction
- military control
- map movement

Out of scope (intentionally excluded):

- building placement
- unit training
- technology research

## What to read first

1. `01_RULES_AND_SYNTAX.md`
2. `05_LLM_SAFE_WORKFLOW.md`
3. `06_LLM_COMMAND_ALLOWLIST.md`
4. `07_RETRIEVAL_INDEX.md`
5. Domain modules:
   - `02_PLAYER_INTERACTION.md`
   - `03_MILITARY_CONTROL.md`
   - `04_MAP_MOVEMENT_AND_DUC.md`

## Included script templates

- `templates/interaction_taunt_router.per`
- `templates/military_attack_controller.per`
- `templates/map_movement_duc.per`

## Version safety

The guide marks commands by engine family:

- `AoC` = classic core commands
- `UP` = UserPatch/advanced DUC style
- `DE` = Definitive Edition-only additions

Always verify command version compatibility before final integration.
