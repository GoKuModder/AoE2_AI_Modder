# 06 - LLM Command Allowlist (Strict)

Purpose: force LLM outputs to use only safe commands for your RPG AI scope.

Scope allowed:

- player interaction
- military control
- map movement/DUC

Scope blocked:

- build/train/research/economy automation

## How to use this file

When prompting an LLM, include this rule:

"Only use commands from `06_LLM_COMMAND_ALLOWLIST.md`. If a needed command is not in allowlist, stop and ask."

---

## A) Allowed Commands (Core)

### A1. Player interaction

- `taunt-detected` - detect player taunt input.
- `acknowledge-taunt` - consume taunt so it does not re-fire repeatedly.
- `chat-to-player` - send message to one player.
- `chat-to-all` - broadcast message.
- `chat-to-allies` - ally-only message.
- `chat-to-enemies` - enemy-only message.
- `taunt` - AI sends taunt value.
- `set-stance` - change diplomacy stance.
- `players-stance` / `stance-toward` - read diplomacy relation.

### A2. State and logic

- `defrule` - rule container.
- `defconst` - constants.
- `goal` / `set-goal` - local state machine.
- `shared-goal` / `set-shared-goal` - shared state.
- `and` / `or` / `not` - logic composition.
- `timer-triggered` / `enable-timer` / `disable-timer` - timing control.
- `do-nothing` - explicit no-op branch.

### A3. Military control

- `attack-now` - trigger attack phase.
- `defend-soldier-count` - readiness/defense gate.
- `attack-soldier-count` - attack readiness gate.
- `warboat-count` - naval readiness gate.
- `town-under-attack` - defense panic trigger.
- `set-strategic-number` - controlled behavior tuning.

### A4. DUC and movement (UP style)

- `up-find-player`
- `up-find-local`
- `up-find-remote`
- `up-clean-search`
- `up-target-point`
- `up-target-objects`
- `up-get-point`
- `up-point-distance`
- `up-path-distance`
- `up-point-terrain`
- `up-point-explored`
- `up-bound-point`
- `up-create-group`
- `up-set-group`
- `up-group-size`
- `up-set-target-point`
- `up-reset-group`
- `up-set-attack-stance`
- `up-set-defense-priority`
- `up-set-offense-priority`
- `up-retreat-now`

### A5. Debug and observability

- `chat-local-to-self`
- `log`
- `log-trace`

---

## B) Hard-Blocked Commands (Do Not Use)

These conflict with your requested scope.

- `build`, `build-forward`, `build-gate`, `build-wall`
- `train`
- `research`, `can-research`, `research-available`, `research-completed`
- economy automation not required for this guide (`buy-commodity`, `sell-commodity`, etc.)

If generated code includes blocked commands, reject and regenerate.

---

## C) Output Quality Contract for LLMs

Every generated snippet must satisfy all:

1. Uses only allowlisted commands.
2. Includes at least one state gate (`goal` or timer) before major actions.
3. No unbounded repeated `attack-now` every tick.
4. Taunt handlers must call `acknowledge-taunt`.
5. Movement rules must clean/reset search context before retargeting.

---

## D) Minimal safe template contract

LLM should start from `templates/*.per` and only modify:

- `defconst` IDs
- goal values
- taunt values
- thresholds and intervals

This lowers syntax risk and keeps behavior auditable.
