# Age of Empires II: Definitive Edition Update 185872 XS Scripting Notes

Source: https://www.ageofempires.com/news/age-of-empires-ii-definitive-edition-update-185872/

## New functions corresponding to Scenario Editor trigger effects

- bool xsSetTechDescription(int techId, int playerId, string description)
- bool xsInitiateResearch(int buildingUnitId, int techId)
- bool xsHasResearchedLocalTechnology(int unitId, int localTechId)
- bool xsResearchLocalTechnology(int buildingUnitId, int localTechId)
- int xsGetAiSignal(int signalId, bool useLegacyAi)
- void xsSetAiSignal(int signalId, int value, bool useLegacyAi)
- int xsGetMapTileAttribute(int x, int y, int attributeId)
- bool xsTrainObject(int buildingUnitId, int objectId, int count)
- bool xsSetUnitGatherPoint(int buildingUnitId, vector position, int targetUnitId)
- vector xsGetUnitGatherPoint(int buildingUnitId)
- string xsGetUnitCaption(int unitId)
- bool xsSetUnitCaption(int unitId, string caption)
- bool xsSetUnitName(int unitId, string name)
- string xsGetUnitCivName(int unitId, bool localized)
- bool xsSetUnitCivName(int unitId, string name)
- string xsGetUnitPlayerName(int unitId)
- bool xsSetUnitPlayerName(int unitId, string name)
- bool xsSetObjectDescription(int playerId, int objectId, string description)
- float xsGetUnitProperty(int unitId, int property, int typeOrPlayer)
- bool xsSetUnitProperty(int unitId, int property, float value, int typeOrForce)
- bool xsSetUnitOwner(int unitId, int32 playerId, bool flashUnit = true)
- bool xsFlashUnit(int unitId, int playerId)
- bool xsStopUnit(int unitId)
- bool xsGetAiScriptGoal(int goalId)
- bool xsSetAiScriptGoal(int goalId, bool value)
- string xsGetCivName(int civId, bool localized)
- string xsGetPlayerCivName(int playerId, bool localized)
- bool xsSetPlayerCivName(int playerId, string name)
- bool xsSetPlayerName(int playerId, string name)
- bool xsSetPlayerColor(int playerId, int colorId)
- bool xsSetViewPosition(int playerId, vector position, int duration)
- bool xsSetZoom(int playerId, float zoom, float duration)
- bool xsBuildUnit(int unitIds, int objectId, vector location1, vector location2, bool isShiftQueue, bool isFormationCommand)
- void xsTaskUnits(int unitIds, int actionType, vector location, int locationObjectId, bool isShiftQueue, bool isFormationCommand, bool shouldPlayUnloadSound, int patrolPoints)
- void xsSetChatToPlayer(int playerId, bool enabled)

## Local-only and interface functions

- float xsUnsyncGetZoom(int playerId = -1)
- vector xsUnsyncGetViewPosition(int playerId = -1)
- int xsUnsyncGetPlayerSelectedUnitIds(int arrayId = -1, int playerId = -1)
- bool xsUnsyncIsUnitVisible(int unitId, bool allowInFog, int playerId = -1)

The optional playerId parameters on these unsynchronized functions are local-player scoped. The selected-unit function returns an array ID; it reuses arrayId when supplied, otherwise it creates an array. When a gather point targets a unit, xsGetUnitGatherPoint returns that unit ID in the vector's Z coordinate.

## Renamed functions

- int xsUnsyncGetLocalPlayerId()
- float xsUnsyncGetTimerTimeRemaining(int timerId, int timeUnit, int playerId = -1)

The old names xsGetLocalPlayerId and xsGetTimerTimeRemaining were renamed because their results are not synchronized across players. xsUnsyncGetLocalPlayerId returns a local world player ID, not a stable lobby/network slot; keep it to local display/chat logic to avoid desyncs.

## String manipulation functions

- int ord(string character)
- string chr(int code)
- int strLen(string str)
- string strCharAt(string str, int index)
- string strSubstring(string str, int start, int end)
- bool strContains(string str, string substring)
- bool strStartsWith(string str, string prefix)
- bool strEndsWith(string str, string suffix)
- string strRemovePrefix(string str, string prefix)
- string strRemoveSuffix(string str, string suffix)
- int strIndexOf(string str, string substring, int fromIndex)
- int strLastIndexOf(string str, string substring, int fromIndex)
- string strReplace(string str, string target, string replacement, int max)
- string strInsert(string str, int index, string target)
- string strRemove(string str, int index, int length)
- int strSplit(string str, string delimiter, int max)
- string strJoin(int arrayId, string delimiter)
- string strTrim(string str)
- string strTrimStart(string str)
- string strTrimEnd(string str)
- string strToUpper(string str)
- string strToLower(string str)
- string strReverse(string str)
- int strToInt(string str, int base, int defaultValue)
- float strToFloat(string str, float defaultValue)
- int hex(string str, int defaultValue)
- int bin(string str, int defaultValue)
- string fstr(string str)

The fstr function substitutes in-scope variable names in braces; expressions are not evaluated, and double braces escape braces. XS string literals also accept \n, \r, \t, \b, \f, \v, \\, and \" escape sequences.

## Existing function updates

- xsEffectAmount accepts an optional sixth int parameter for selecting a Train Location Entry Mod when changing unit or technology train-location attributes. Set its fifth playerNumber parameter to -1 explicitly to apply the effect to all players.
- The final parameter of xsGetUnitAttribute (third) and xsGetObjectAttribute (fourth) can select a Train Location Entry Mod for train-location attributes. If unspecified, the unit's own mod is used.
- New technology attributes are available through xsGetTechAttribute. The update notes refer to the Tech Attribute Constants section in Constants.xs.
- xsGetMapTileAttribute uses the Map Tile Attribute constants; xsGetUnitProperty and xsSetUnitProperty use Unit Property constants.
