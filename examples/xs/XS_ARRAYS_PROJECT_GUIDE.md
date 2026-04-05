# XS Arrays Project Guide (Including Vector Arrays)

This guide explains how to use XS arrays in a real AoE2 DE project pattern, including vector arrays for position-aware logic.

Companion script (fully linted):
- `examples/xs/xs_arrays_full_project_demo.xs`

## 1) Why arrays matter in XS projects

Arrays are your in-memory database inside XS. Use them to:
- track many units with one rule loop
- keep stable slot-based state (hero slots, summon slots, cooldown slots)
- run deterministic target selection and effect logic

Without arrays, project logic becomes duplicated and error-prone.

## 2) Array API you can rely on

These were validated with an external `xs-check` linter during development.

Create:
- `xsArrayCreateInt(size, default, name)`
- `xsArrayCreateFloat(size, default, name)`
- `xsArrayCreateBool(size, default, name)`
- `xsArrayCreateString(size, default, name)`
- `xsArrayCreateVector(size, default, name)`

Get:
- `xsArrayGetInt(arrayId, index)`
- `xsArrayGetFloat(arrayId, index)`
- `xsArrayGetBool(arrayId, index)`
- `xsArrayGetString(arrayId, index)`
- `xsArrayGetVector(arrayId, index)`
- `xsArrayGetSize(arrayId)`

Set:
- `xsArraySetInt(arrayId, index, value)`
- `xsArraySetFloat(arrayId, index, value)`
- `xsArraySetBool(arrayId, index, value)`
- `xsArraySetString(arrayId, index, value)`
- `xsArraySetVector(arrayId, index, value)`

Resize:
- `xsArrayResizeInt(arrayId, newSize)`
- `xsArrayResizeFloat(arrayId, newSize)`
- `xsArrayResizeBool(arrayId, newSize)`
- `xsArrayResizeString(arrayId, newSize)`
- `xsArrayResizeVector(arrayId, newSize)`

## 3) Project architecture pattern (recommended)

Use a 3-rule structure:

1. `init` rule (runs once)
- create all array IDs
- set defaults
- `xsDisableSelf()`

2. `sync` rule (runs every 1s)
- read scenario inputs (trigger vars, unit existence, hp)
- write normalized values into arrays

3. `decision` rule (runs every 1s)
- read arrays only (no repeated raw world scans if avoidable)
- compute target/result
- write outputs (trigger vars, effect calls)

This keeps scripts maintainable and deterministic.

## 4) Vector arrays in practice

Vector arrays are best for:
- caching unit positions per slot
- distance calculations for nearest-target tie breaks
- zone and radius checks

Common vector flow:
1. `pos = xsGetUnitPosition(unitId)`
2. `xsArraySetVector(aHeroPos, i, pos)`
3. Later read with `xsArrayGetVector(...)`
4. Compute:
- `dx = xsVectorGetX(heroPos) - xsVectorGetX(selfPos)`
- `dy = xsVectorGetY(heroPos) - xsVectorGetY(selfPos)`
- `distSq = dx*dx + dy*dy`

Use squared distance (`distSq`) to avoid sqrt overhead.

## 5) Slot design (hero + summon systems)

For RPG projects, keep fixed slot ranges:
- `0..7` hero slots
- `8..31` summon slots

Store per slot:
- unitId (int)
- owner (int)
- alive (bool)
- hp/hpPct (float)
- position (vector)
- optional role/class tag (int)

Then selection logic can prioritize:
- lowest hpPct heroes first
- or role-based targets (archer vs pike)

## 6) Critical pitfalls (avoid these)

- Do not confuse `unitId` (instance) vs `objectId` (type).
- Guard invalid slots (`unitId < 0`) before unit calls.
- For hpPct, protect division by zero (`maxHp > 0`).
- Keep array sizes constant unless you truly need dynamic resize.
- Avoid writing world logic in multiple places; centralize in sync + decision rules.

## 7) Linter validation (done)

Validated script:
- `examples/xs/xs_arrays_full_project_demo.xs`

Command used:
```bash
"C:\path\to\xs-check.exe" "C:\AoE2DE Modding\Code\AoE2_AI_Modder\examples\xs\xs_arrays_full_project_demo.xs"
```

Result:
- `No errors found`

## 8) How to test quickly in-game

1. Add `xs_arrays_full_project_demo.xs` to your scenario/mod XS load path.
2. Populate trigger vars:
- hero unit IDs at `300..307`
- hero max HP at `320..327` (or leave <=0 for fallback)
- self unit ID at `340`
3. Observe output trigger vars:
- `50` = target player selected
- `51` = mode (`1`)
- `52` = switch pulse increments when target changes

This gives you a clean base to wire into AI behavior switching.
