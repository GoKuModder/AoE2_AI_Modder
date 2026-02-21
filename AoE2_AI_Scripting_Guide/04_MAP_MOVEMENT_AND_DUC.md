# 04 - Map Movement and DUC

This module focuses on direct unit control (DUC), scouting, and coordinate-driven movement.

## High-value commands

### Search and targeting

- `up-find-player` (UP)
- `up-find-local` (UP)
- `up-find-remote` (UP)
- `up-clean-search` (UP)
- `up-target-point` (UP)
- `up-target-objects` (UP)

### Point/position utilities

- `up-get-point` (UP)
- `up-point-distance` (UP)
- `up-path-distance` (UP)
- `up-point-terrain` (UP)
- `up-point-explored` (UP)
- `up-bound-point` (UP)

### Group controls

- `up-create-group` (UP)
- `up-set-group` (UP)
- `up-group-size` (UP)
- `up-set-target-point` (UP)
- `up-reset-group` (UP)

## LLM-safe pattern: simple scout move loop

```per
(defconst gl-scout-active 300)
(defconst gl-scout-waypoint-x 301)

(defrule
    (goal gl-scout-active 0)
=>
    (set-goal gl-scout-active 1)
    (set-goal gl-scout-waypoint-x 0)
)

(defrule
    (goal gl-scout-active 1)
=>
    (up-find-player enemy find-closest temporary-goal)
    (up-target-point position-self-x action-move -1 -1)
)
```

## LLM-safe pattern: controlled local scout target selection

```per
(defrule
    (goal gl-scout-active 1)
=>
    (up-find-local c: scout-cavalry-line c: 40)
    (up-clean-search search-local object-data-distance search-order-asc)
    (up-set-target-point scout-group-x)
)
```

## Anti-error checklist

- Always clear or re-sort search context when reusing target lists.
- Keep movement goals bounded; avoid uninitialized waypoint coordinates.
- Use separate rules for acquire-target and move-to-target for readability.
