# 01 - Rules and Syntax

## Core structure

AoE2 AI scripts are rule-based. A minimal rule uses:

```per
(defrule
    (condition-1)
    (condition-2)
=>
    (action-1)
    (action-2)
)
```

## Safe rule-writing conventions

1. Keep one purpose per rule (routing, combat, movement).
2. Gate actions with goals/timers to prevent repeated spam.
3. Use explicit thresholds (`>=`, `>`, `=`) instead of implicit assumptions.
4. Prefer deterministic state machines over random branching.

## State management primitives

- `set-goal` / `goal`
- `set-shared-goal` / `shared-goal`
- `enable-timer`, `disable-timer`, `timer-triggered`
- `set-signal` when integrating with broader script flow

## Logic operators

- `and`, `or`, `not`
- also available: `nand`, `nor`, `xor`, `xnor`

Use simple `and/or/not` unless advanced boolean compression is required.

## Version-awareness rule

Before using a command, label it by version:

- AoC: broadest compatibility
- UP: advanced DUC and search/control commands
- DE: DE-only additions (including some FE commands)

If uncertain, build fallback rules around AoC alternatives.
