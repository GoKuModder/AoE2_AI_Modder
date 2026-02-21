# Genie Editor -> XS Bridge Notes

Reference source:

- `XS_Training/external_refs/ageofempires.fandom.com/Genie_Editor.md`

## Scope

Genie Editor is data-layer authoring. XS is runtime scripting.

- Use Genie Editor for baseline unit/task/tech definitions.
- Use XS to modify many of those values during play.

## Important naming in this project

- `objectId`: unit type ID in data (Genie ID)
- `unitId`: placed unit reference ID on map

Do not mix these when calling XS functions.

## What maps cleanly to XS

### Attributes

- Runtime changes to many object attributes -> `xsEffectAmount(...)`
- Read object template attribute -> `xsGetObjectAttribute(playerId, objectId, attribute, damageClass)`
- Read per-instance attribute -> `xsGetUnitAttribute(unitId, attribute, damageClass)`
- Read/write HP per instance -> `xsGetUnitHitpoints(unitId)`, `xsSetUnitHitpoints(unitId, value)`

### Tasks (including Aura/Stingers)

- Configure task fields -> `xsTaskAmount(taskFieldId, value)`
- Reset global task struct -> `xsResetTaskAmount()`
- Insert/update task -> `xsTask(objectOrClassId, actionType, targetObjectOrClassId, playerId)`
- Remove task -> `xsRemoveTask(objectOrClassId, actionType, targetObjectOrClassId, playerId)`

For new mechanics from your notes:

- Aura = Task `155` (+ Combat Ability `32`)
- Stingers = Task `157` (+ Combat Ability `128`)
- HP transform = Task `158`

### Technology modifications

- Runtime tech edits -> `xsEffectAmount(cModifyTech, techId, subCommand, value, player)`
- Prefer set/multiply subcommands from current DE behavior.

## What does not map 1:1 to XS runtime

- Structural DAT-only authoring (new base units, graphics tables, language IDs, button layout wiring) is still Genie Editor territory.
- XS can trigger/modify behavior, but does not replace full data file authoring.

## Practical workflow for RPG spells

1. Define base ability plumbing in Genie Editor (buttons, charge type, task defaults, visuals).
2. Use XS rules for dynamic logic (conditions, cooldown checks, custom thresholds, per-unit gating).
3. Use trigger variables for UI/FX handoff when needed.
