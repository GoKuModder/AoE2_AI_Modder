# Age of Empires II: Definitive Edition Update 177723 XS Scripting Notes

Source: https://www.ageofempires.com/news/age-of-empires-ii-definitive-edition-update-177723/

## XS Functions Added In Update 177723

Update 177723 added several XS functions for locale/string lookup, data introspection, local display/chat workflows, scenario-effect-like UI actions, and math helpers.

New locale, string, and data functions:

- `int xsGetLocale()`
- `string xsGetString(int stringId, bool localized = false)`
- `string xsGetPlayerAttributeName(int resourceId, bool localized = false)`
- `string xsGetObjectAttributeName(int attributeId, bool localized = false)`
- `string xsGetDamageClassName(int damageClassId, bool localized = false)`
- `bool xsIsObjectValid(int objectId, int playerId)`
- `int xsGetPlayerNumberOfObjects(int playerId)`
- `int xsGetLocalPlayerId()`
- `string xsGetPlayerColorTag(int playerId)`
- `int xsGetMapSeed()`
- `int xsGetTechAttribute(int playerId, int techId, int techAttribute, int indexOrCostType)`

`xsGetLocale` returns one of the values from the Language Constants section of `Constants.xs`. `xsGetPlayerColorTag` returns a player color tag such as `<RED>` and works with player colors changed in the Scenario Editor Players menu. `xsGetTechAttribute` uses values from the Tech Attribute Constants section of `Constants.xs`.

## Trigger-Analogue XS Functions

The following XS functions work similarly to their Scenario Editor trigger effect analogues:

- `bool xsPlaySound(string eventOrSoundFileName, int playerId, vector position, float angle, int objectId, bool global = false)`
- `bool xsDisplayInstructions(string msg, int time, int sourcePlayer, int iconObjectId, int panelPosition, bool useTagColorForIcon, bool playSound, string soundFilename, int playerId = -1)`
- `bool xsClearInstructions(int panelPosition, int playerId = -1)`
- `bool xsDisplayTimer(int timerId, string msg, int time, int timeUnit, bool resetTimer, int playerId = -1)`
- `bool xsClearTimer(int timerId, int playerId = -1)`
- `float xsGetTimerTimeRemaining(int timerId, int timeUnit, int playerId = -1)`
- `bool xsSendChat(string msg, int playerId = -1, bool silent = false)`
- `void xsDeclareVictory(int playerId, bool victory = true)`

For these functions, passing `-1` to `playerId` applies the action to all players.

For `xsDisplayInstructions`, `sourcePlayer` corresponds to the Scenario Editor "Source Player" option. `playerId` controls which player receives the instruction. `useTagColorForIcon` controls whether the instruction icon uses the text tag color.

## xsGetLocalPlayerId Caveat

`xsGetLocalPlayerId()` is intended for display and chat-oriented logic only. It returns the local world player id, not a stable lobby slot or network player id.

In coop situations, multiple network players can share one world player id. For example, if players in lobby slots 2 and 4 choose the same color, they share world player 2; later lobby slots can then differ from their world-player ordering. XS currently has no functions that operate on network players, so it cannot distinguish specific humans inside a coop team.

Do not use `xsGetLocalPlayerId()` for synced gameplay decisions. Using it outside local-only display or chat behavior can cause desyncs.

## Math Functions Added In Update 177723

- `float ln(float x)`
- `float log2(float x)`
- `float log10(float x)`
- `float round(float x)`
- `float radians(float x)`
- `float degrees(float x)`
- `float dist(vector v1, vector v2)`
- `int bitAnd(int v1, int v2)`
- `int bitOr(int v1, int v2)`
- `int bitNot(int v1)`
- `int bitXor(int v1, int v2)`

Update 177723 also fixed the XS `main` function not being invoked in replays.
