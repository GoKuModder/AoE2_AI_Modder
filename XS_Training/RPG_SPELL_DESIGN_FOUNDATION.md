# RPG Spell Design Foundation (XS)

This document distills the captured XS docs into a practical design baseline for RPG-style spells.

Primary references in this folder:

- `SOURCE_PAGE_INDEX.md` (full page inventory)
- `github.com/Divy1211/AoE2DE_UGC_Guide/docs/general/xs/programmer.md`
- `github.com/Divy1211/AoE2DE_UGC_Guide/docs/general/xs/functions.md`
- `github.com/Divy1211/AoE2DE_UGC_Guide/docs/general/xs/constants.md`
- `github.com/Divy1211/AoE2DE_UGC_Guide/docs/general/xs/tricks.md`
- `github.com/Divy1211/AoE2DE_UGC_Guide/docs/general/xs/bugs/*.md`

## XS notation clarification (critical)

For this XS knowledge base, use the guide's naming exactly:

- `objectId` = unit ID in Genie Editor (unit type ID)
- `unitId` = unit reference ID of a placed unit instance on the map

Example:

- Militia has `objectId = 74`.
- If you place two militia units on the map, each placed militia has a different `unitId`.

Important:

- This distinction is specific to XS guide notation used here.
- In other contexts, `unitId` may be called `referenceId`, but in this database we keep the guide terminology for consistency.

## 1) What XS can do for spells

XS is enough to build a robust spell layer using:

- Rule scheduler (`rule`, intervals, priorities, group toggles)
- Runtime reads (`xsGetUnit*`, `xsGetObject*`, `xsGetPlayer*`, map/time queries)
- Runtime writes (`xsEffectAmount`, `xsSetUnitHitpoints`, `xsSetUnitCharge`, `xsSetPlayerAttribute`)
- Task system (`xsTaskAmount`, `xsTask`, `xsRemoveTask`) for behavior-like effects (including aura patterns)
- Arrays for state (`xsArrayCreate*`, `xsArraySet*`, `xsArrayGet*`)

This is enough to implement:

- Targeted nukes
- Damage-over-time and heal-over-time
- Buff/debuff windows
- Area denial / aura zones
- Cooldowns, charges, and cast gating

## 2) XS constraints that must shape spell design

From `programmer.md` and bug pages:

- Expression type is biased by first operand; order math carefully.
- Unary negative is unreliable (`-x`); prefer `0-x`.
- Explicit casts are unreliable.
- Vector constructor has limitations with variables/expressions; prefer `xsVectorSet`.
- `return` statements should use parentheses (`return (value);`).
- `xsResearchTechnology` can crash if called twice for same tech/player (`bugs/Important.md`).
- Several `xsEffectAmount` variants for tech cost/time are obsolete; use `cModifyTech` + subcommands (`tricks.md`, `bugs/Individual Tech Modifiers.md`).
- Crash edges exist for invalid IDs/players and certain chat patterns (`bugs/Crashes.md`, `bugs/Chat Data.md`).

Practical impact:

- Prefer deterministic integer-based formulas when possible.
- Validate all IDs and player bounds before mutating effects.
- Build defensive wrappers for dangerous APIs.
- Treat chat/log output as best-effort debug only.

## 3) Recommended spell runtime architecture

### 3.1 Core model

Represent each active spell instance as an entry in parallel arrays:

- `spellCaster[i]`
- `spellTarget[i]`
- `spellType[i]`
- `spellStartTime[i]`
- `spellDuration[i]`
- `spellTickInterval[i]`
- `spellLastTick[i]`
- `spellMagnitude[i]`
- `spellState[i]` (pending, active, ended)

Rationale: XS arrays are global and stable. This avoids dynamic object complexity and fits rule-driven updates.

### 3.2 Rule groups

Use separate rule groups:

- `SpellInput` (cast requests / trigger variables)
- `SpellUpdate` (tick processing)
- `SpellCleanup` (expiration/removal)

This keeps logic testable and lets you disable sections quickly via `xsDisableRuleGroup`.

### 3.3 Cast lifecycle

1. Validate request (cooldown, mana/resource, target validity).
2. Reserve cost (resource/charge update).
3. Create spell instance row in arrays.
4. On each update tick, evaluate effect by type.
5. Stop when duration ends or target invalid.
6. Cleanup arrays and optional visual/task effects.

## 4) Safe wrappers you should use before designing many spells

Create utility wrappers once and always call through them:

- `safeEffectAmount(effectId, objectOrTechId, attrOrOp, value, player)`
  - Reject invalid player/object/tech ranges.
  - Normalize values for known edge-cases.
- `safeSetUnitHitpoints(unitId, hp)`
  - Guard for non-existing unit.
- `safeGetUnitPosition(unitId)`
  - Return `cInvalidVector` when unit missing.
- `safeChat(msg)`
  - Avoid `%` in raw strings unless intentional formatting.

This prevents common crash paths documented in bug pages.

## 5) Spell pattern cookbook

### 5.1 Instant direct damage

- Resolve target unit ID.
- Read current HP with `xsGetUnitHitpoints`.
- Apply `xsSetUnitHitpoints(target, hp - damage)`.
- Enforce floor >= 0.

### 5.2 Damage over time (DoT)

- Store duration, tick interval, damage per tick.
- In update rule, if `now - lastTick >= tickInterval`, apply one tick.
- End when `now >= start + duration`.

### 5.3 Buff/debuff

- Apply `xsEffectAmount(cAddAttribute|cSetAttribute|cMulAttribute, ...)` at start.
- Revert with inverse operation at end (or track original value in arrays and restore).
- Prefer set/restore for deterministic behavior.

### 5.4 Aura-based spell

- Reuse task/aura technique from `tricks.md` with strict validation.
- Keep a cleanup path that always removes aura task and restores combat ability bits.

### 5.5 Charge-based spells

- Use unit charge APIs (`xsGetUnitCharge`, `xsSetUnitCharge`) and constants (`cMaxCharge`, `cRechargeRate`) for charge systems.

## 6) Minimum test protocol for each new spell

For every spell implementation, test:

1. Valid cast on valid target
2. Invalid target rejection
3. Target dies mid-effect
4. Caster dies mid-effect
5. Duration expiration cleanup
6. Double-cast same frame
7. Max player count and low player count
8. Multiplayer host/client behavior (if relevant)

Add one regression case per known bug that your spell could touch.

## 7) What to avoid in first RPG iteration

- Complex tech-mutation spells depending on obsolete effect commands
- Heavy string-based state
- Deep recursion
- Fancy float-heavy formulas where integer alternatives exist

Start with deterministic, array-driven, rule-driven effects.

## 8) Ready state checklist

You are ready to design spell content when all are true:

- Source pages are captured (`SOURCE_PAGE_INDEX.md` count matches expectations).
- You have wrapper utilities for unsafe APIs.
- You have a generic spell instance table + update loop.
- You have one validated spell in each major pattern (instant, DoT, buff, aura).
- You have a regression script covering critical crash bugs.

At that point, spell design becomes content work (numbers/behavior), not engine-risk work.
