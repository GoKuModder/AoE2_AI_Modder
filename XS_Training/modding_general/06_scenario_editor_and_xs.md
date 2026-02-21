# Modding - Scenario Editor and XS Scripting

## Scenario Editor

- Added new elevation height options up to `16` (from `7`).
- Fixed a crash when using Modify Attribute trigger effect with Graphics ID attributes originally set to `-1`.
- Added Item ID field to Research Technology trigger effect.
- Script Filename field now accepts file names with up to `100` characters.

## XS Scripting

- Added `float xsGetObjectAttribute(int32_t playerId, int32_t objectId, int32_t attribute)` function which returns the unit attribute value of the specific player's object ID.
- Added `bool xsSetUnitPosition(int unitId, vector position, bool checkCollision = true)` to move/teleport a unit to a target position.
- Added `int xsGetWorldPlayerId(int scenarioPlayerId)`.
- Added `int xsGetGarrisonedInUnitId(int unitId)`.
- Added `int xsGetGarrisonedUnitIds(int unitId)` which returns an int array.
- Added `int xsGetPlayerType(int playerId)`. Refer to Player Type constants.
- Added `bool xsRemoveUnit(int unitId)`.
- Added `int xsGetDiplomacy(int sourcePlayerId, int targetPlayerId)`. Refer to Diplomacy constants.
- Added `bool xsSetDiplomacy(int sourcePlayerId, int targetPlayerId, int diploState, bool mirror = false)`.
- Added `int xsGetColorMood()`. Refer to Color Mood constants.
- Added `bool xsSetColorMood(int colorMood, int interval)`.
- Added `int xsGetDifficulty()`. Refer to Difficulty constants.
- Added `int xsCreateUnit(int objectId, int playerId, vector location, bool foundation = false, bool playCreatedSound = true, bool checkCollision = true)` (returns created unit ID).
- Added `int xsGetObjectTaskCount(int objectId, int playerId)`.
- Added `int xsGetUnitTaskCount(int unitId)`.
- Added `bool xsObjectTaskAmount(int objectId, int playerId, int taskId)`.
- Added `bool xsUnitTaskAmount(int unitId, int taskId)`.
- Added `float xsGetTaskAmount(int taskFieldId)`.
- Added `bool xsModifyObjectTasks(int objectOrClassId, int playerId, int taskId, bool edit = false)`.
- Added `bool xsModifyUnitTasks(int unitId, int taskId, bool edit = false)`.
- Task edits: positive task index inserts, `edit = true` modifies existing task, and negative index removes (`-1` removes task `0`, `-2` removes task `1`, etc.).
- New task fields for `xsTaskAmount`: `cTaskAttrTaskType = 28`, `cTaskAttrObjectId = 29`, `cTaskAttrObjectClass = 30`.
- `xsModifyObjectTasks`/`xsModifyUnitTasks` should be preferred over `xsTask` for task insertion/editing.
