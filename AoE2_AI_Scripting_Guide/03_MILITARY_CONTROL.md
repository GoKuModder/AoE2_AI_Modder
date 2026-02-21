# 03 - Military Control

This module covers attack timing, pressure cycles, and retreat/defense behavior.

## High-value commands

### AoC core

- `attack-now` (Action)
- `attack-soldier-count` (Fact)
- `defend-soldier-count` (Fact)
- `warboat-count` (Fact)
- `town-under-attack` (Fact)
- `set-strategic-number` (Action)

### UP/advanced control

- `up-modify-sn` (Fact/Action)
- `up-set-timer` (Action)
- `up-timer-status` (Fact)
- `up-retreat-now` (Action)
- `up-set-defense-priority` (Action)
- `up-set-offense-priority` (Action)
- `up-set-attack-stance` (Action)

## LLM-safe pattern: land attack cycle

```per
(defconst gl-land-attack-delay 200)
(defconst gl-land-attack-requirement 201)
(defconst gl-land-attack-percentage 202)

(defrule
    (goal gl-land-attack-delay 0)
=>
    (set-goal gl-land-attack-delay 900)
    (set-goal gl-land-attack-requirement 20)
    (set-goal gl-land-attack-percentage 65)
)

(defrule
    (game-time > 900)
    (defend-soldier-count g:>= gl-land-attack-requirement)
=>
    (up-modify-sn sn-percent-attack-soldiers g:= gl-land-attack-percentage)
    (chat-local-to-self "land attack")
    (attack-now)
)
```

## LLM-safe pattern: emergency defense/retreat

```per
(defrule
    (town-under-attack)
=>
    (up-set-defense-priority 100)
    (up-set-offense-priority 0)
)

(defrule
    (defend-soldier-count < 6)
=>
    (up-retreat-now)
)
```

## Anti-error checklist

- Never fire `attack-now` every tick without cooldown gating.
- Keep offense and defense priorities explicit during phase switches.
- Separate naval and land attack rules; do not multiplex both in one trigger.
