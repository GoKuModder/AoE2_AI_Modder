# 02 - Player Interaction

This module focuses on communication, taunt handling, and diplomacy-facing reactions.

## High-value commands

### Chat and taunts

- `taunt-detected` (Fact, AoC)
- `acknowledge-taunt` (Action, AoC)
- `chat-to-player` (Action, AoC)
- `chat-to-all` (Action, AoC)
- `chat-to-allies` (Action, AoC)
- `chat-to-enemies` (Action, AoC)
- `taunt` (Action, AoC)

### Player identity and status

- `player-human` (Fact, AoC)
- `player-computer` (Fact, AoC)
- `player-in-game` (Fact, AoC)
- `players-score` (Fact, AoC)

### Diplomacy

- `set-stance` (Action, AoC)
- `players-stance` (Fact, AoC)
- `stance-toward` (Fact, AoC)

## LLM-safe pattern: taunt choice router

Use taunts as finite-state inputs for quests/dialogue choices.

```per
(defconst gl-dialogue-state 100)
(defconst gl-dialogue-choice 101)

(defrule
    (goal gl-dialogue-state 10)
    (taunt-detected any-player 1)
=>
    (set-goal gl-dialogue-choice 1)
    (set-goal gl-dialogue-state 11)
    (chat-to-all "Choice 1 accepted")
    (acknowledge-taunt this-any-player 1)
)

(defrule
    (goal gl-dialogue-state 10)
    (taunt-detected any-player 2)
=>
    (set-goal gl-dialogue-choice 2)
    (set-goal gl-dialogue-state 11)
    (chat-to-all "Choice 2 accepted")
    (acknowledge-taunt this-any-player 2)
)
```

## Anti-error checklist

- Always acknowledge handled taunts to avoid repeated triggers.
- Use a dialogue state goal to avoid processing choices outside valid windows.
- Keep one taunt value per branch (`1`, `2`, `3`, etc.).
