# 07 - Retrieval Index for LLM Agents

Use this file as the first lookup map before generating `.per` code.

## Query -> File map

- "taunt dialogue", "player responses", "chat branch"
  - `02_PLAYER_INTERACTION.md`
  - `templates/interaction_taunt_router.per`

- "attack wave", "military phase", "retreat logic"
  - `03_MILITARY_CONTROL.md`
  - `templates/military_attack_controller.per`

- "scout movement", "duc movement", "map navigation"
  - `04_MAP_MOVEMENT_AND_DUC.md`
  - `templates/map_movement_duc.per`

- "what commands are allowed", "forbidden commands", "strict mode"
  - `06_LLM_COMMAND_ALLOWLIST.md`

- "safe generation steps", "validation checklist", "anti-loop"
  - `05_LLM_SAFE_WORKFLOW.md`

## Retrieval strategy (recommended)

1. Identify task class: `interaction | military | movement`.
2. Load matching module + matching template.
3. Load `06_LLM_COMMAND_ALLOWLIST.md` and filter command set.
4. Generate minimal patch using template edits only.
5. Validate with checklist in `05_LLM_SAFE_WORKFLOW.md`.

## High-signal keywords

- Interaction: `taunt-detected`, `acknowledge-taunt`, `chat-to-player`
- Military: `attack-now`, `defend-soldier-count`, `up-retreat-now`
- Movement: `up-find-player`, `up-target-point`, `up-clean-search`

## Fast fail conditions

Reject output immediately if:

- contains blocked commands from allowlist file
- lacks state gating before major actions
- includes repeated high-impact action with no timer/goal guard
