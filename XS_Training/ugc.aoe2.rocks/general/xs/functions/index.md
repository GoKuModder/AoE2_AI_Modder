---
source_url: https://ugc.aoe2.rocks/general/xs/functions/
fetched_at: 2026-02-08T19:30:24+00:00
---

Functions Reference - AoE2DE UGC Guide






[Skip to content](#1-rules)

AoE2DE UGC Guide

Functions Reference



Initializing search

[AoE2DE\_UGC\_Guide](https://github.com/Divy1211/AoE2DE_UGC_Guide "Go to repository")

* [AoE2DE UGC Guide](../../..)
* [Game Mechanics](../../)
* [Custom Scenarios](../../../scenarios/)
* [XS Scripting](../)
* [Mods](../../../mods/)
* [RMS](../../../rms/)
* [AI](../../../ai/)
* [Audio](../../../audio/)



AoE2DE UGC Guide

[AoE2DE\_UGC\_Guide](https://github.com/Divy1211/AoE2DE_UGC_Guide "Go to repository")

* [AoE2DE UGC Guide](../../..)
* [Game Mechanics](../../)

  Game Mechanics
  + [Damage Calculation](../../damage_calculation/)
  + [Attributes](../../attributes/attributes/)
  + [Resources](../../resources/resources/)
  + [Hotkeys](../../hotkeys/hotkeys/)
* [Custom Scenarios](../../../scenarios/)

  Custom Scenarios
  + [Triggers](../../../scenarios/triggers/)

    Triggers
    - [Effects](../../../scenarios/triggers/effects/effects/)
  + Useful Tools




    Useful Tools
    - [AoE2ScenarioParser](../../../scenarios/useful_tools/parser/)

      AoE2ScenarioParser
* [XS Scripting](../)

  XS Scripting
  + [For Beginners](../beginner/)
  + [For Programmers](../programmer/)
  + [Tricks](../tricks/)
  + Functions Reference

    [Functions Reference](./)



    Table of contents
    - [1. Rules](#1-rules)

      * [1.1. xsDisableRule](#11-xsdisablerule)
      * [1.2. xsDisableRuleGroup](#12-xsdisablerulegroup)
      * [1.3. xsDisableSelf](#13-xsdisableself)
      * [1.4. xsEnableRule](#14-xsenablerule)
      * [1.5. xsEnableRuleGroup](#15-xsenablerulegroup)
      * [1.6. xsIsRuleEnabled](#16-xsisruleenabled)
      * [1.7. xsIsRuleGroupEnabled](#17-xsisrulegroupenabled)
      * [1.8. xsSetRuleMaxInterval](#18-xssetrulemaxinterval)
      * [1.9. xsSetRuleMaxIntervalSelf](#19-xssetrulemaxintervalself)
      * [1.10. xsSetRuleMinInterval](#110-xssetrulemininterval)
      * [1.11. xsSetRuleMinIntervalSelf](#111-xssetruleminintervalself)
      * [1.12. xsSetRulePriority](#112-xssetrulepriority)
      * [1.13. xsSetRulePrioritySelf](#113-xssetrulepriorityself)
    - [2. Vectors](#2-vectors)

      * [2.1. xsVectorGetX](#21-xsvectorgetx)
      * [2.2. xsVectorGetY](#22-xsvectorgety)
      * [2.3. xsVectorGetZ](#23-xsvectorgetz)
      * [2.4. xsVectorLength](#24-xsvectorlength)
      * [2.5. xsVectorNormalize](#25-xsvectornormalize)
      * [2.6. xsVectorSet](#26-xsvectorset)
      * [2.7. xsVectorSetX](#27-xsvectorsetx)
      * [2.8. xsVectorSetY](#28-xsvectorsety)
      * [2.9. xsVectorSetZ](#29-xsvectorsetz)
    - [3. Arrays](#3-arrays)

      * [3.1. xsArrayCreateBool](#31-xsarraycreatebool)
      * [3.2. xsArrayCreateFloat](#32-xsarraycreatefloat)
      * [3.3. xsArrayCreateInt](#33-xsarraycreateint)
      * [3.4. xsArrayCreateString](#34-xsarraycreatestring)
      * [3.5. xsArrayCreateVector](#35-xsarraycreatevector)
      * [3.6. xsArrayGetBool](#36-xsarraygetbool)
      * [3.7. xsArrayGetFloat](#37-xsarraygetfloat)
      * [3.8. xsArrayGetInt](#38-xsarraygetint)
      * [3.9. xsArrayGetSize](#39-xsarraygetsize)
      * [3.10. xsArrayGetString](#310-xsarraygetstring)
      * [3.11. xsArrayGetVector](#311-xsarraygetvector)
      * [3.12. xsArrayResizeBool](#312-xsarrayresizebool)
      * [3.13. xsArrayResizeFloat](#313-xsarrayresizefloat)
      * [3.14. xsArrayResizeInt](#314-xsarrayresizeint)
      * [3.15. xsArrayResizeString](#315-xsarrayresizestring)
      * [3.16. xsArrayResizeVector](#316-xsarrayresizevector)
      * [3.17. xsArraySetBool](#317-xsarraysetbool)
      * [3.18. xsArraySetFloat](#318-xsarraysetfloat)
      * [3.19. xsArraySetInt](#319-xsarraysetint)
      * [3.20. xsArraySetString](#320-xsarraysetstring)
      * [3.21. xsArraySetVector](#321-xsarraysetvector)
    - [4. Maths](#4-maths)

      * [4.1. abs](#41-abs)
      * [4.2. acos](#42-acos)
      * [4.3. asin](#43-asin)
      * [4.4. atan](#44-atan)
      * [4.5. atan2](#45-atan2)
      * [4.6. atan2v](#46-atan2v)
      * [4.7. bitCastToFloat](#47-bitcasttofloat)
      * [4.8. bitCastToInt](#48-bitcasttoint)
      * [4.9. ceil](#49-ceil)
      * [4.10. cos](#410-cos)
      * [4.11. exp](#411-exp)
      * [4.12. floor](#412-floor)
      * [4.13. pow](#413-pow)
      * [4.14. sin](#414-sin)
      * [4.15. sqrt](#415-sqrt)
      * [4.16. tan](#416-tan)
      * [4.17. xsCeilToInt](#417-xsceiltoint)
    - [5. General](#5-general)

      * [5.1. xsChatData](#51-xschatdata)
      * [5.2. xsDoesUnitExist](#52-xsdoesunitexist)
      * [5.3. xsEffectAmount](#53-xseffectamount)
      * [5.4. xsGetGameTime](#54-xsgetgametime)
      * [5.5. xsGetGroupMoveTarget](#55-xsgetgroupmovetarget)
      * [5.6. xsGetMapHeight](#56-xsgetmapheight)
      * [5.7. xsGetMapID](#57-xsgetmapid)
      * [5.8. xsGetMapName](#58-xsgetmapname)
      * [5.9. xsGetMapWidth](#59-xsgetmapwidth)
      * [5.10. xsGetNumPlayers](#510-xsgetnumplayers)
      * [5.11. xsGetObjectAttribute](#511-xsgetobjectattribute)
      * [5.12. xsGetObjectClass](#512-xsgetobjectclass)
      * [5.13. xsGetObjectCopyId](#513-xsgetobjectcopyid)
      * [5.14. xsGetObjectCount](#514-xsgetobjectcount)
      * [5.15. xsGetObjectCountTotal](#515-xsgetobjectcounttotal)
      * [5.16. xsGetObjectName](#516-xsgetobjectname)
      * [5.17. xsGetObjectType](#517-xsgetobjecttype)
      * [5.18. xsGetPlayerCivilization](#518-xsgetplayercivilization)
      * [5.19. xsGetPlayerInGame](#519-xsgetplayeringame)
      * [5.20. xsGetPlayerName](#520-xsgetplayername)
      * [5.21. xsGetPlayerNumberOfTechs](#521-xsgetplayernumberoftechs)
      * [5.22. xsGetPlayerUnitIds](#522-xsgetplayerunitids)
      * [5.23. xsGetRandomNumber](#523-xsgetrandomnumber)
      * [5.24. xsGetRandomNumberLH](#524-xsgetrandomnumberlh)
      * [5.25. xsGetRandomNumberMax](#525-xsgetrandomnumbermax)
      * [5.26. xsGetTechName](#526-xsgettechname)
      * [5.27. xsGetTechState](#527-xsgettechstate)
      * [5.28. xsGetTime](#528-xsgettime)
      * [5.29. xsGetTurn](#529-xsgetturn)
      * [5.30. xsGetUnitAttribute](#530-xsgetunitattribute)
      * [5.31. xsGetUnitAttributeHeld](#531-xsgetunitattributeheld)
      * [5.32. xsGetUnitAttributeTypesHeld](#532-xsgetunitattributetypesheld)
      * [5.33. xsGetUnitBuildPoints](#533-xsgetunitbuildpoints)
      * [5.34. xsGetUnitCharge](#534-xsgetunitcharge)
      * [5.35. xsGetUnitClass](#535-xsgetunitclass)
      * [5.36. xsGetUnitCopyId](#536-xsgetunitcopyid)
      * [5.37. xsGetUnitGroupId](#537-xsgetunitgroupid)
      * [5.38. xsGetUnitHitpoints](#538-xsgetunithitpoints)
      * [5.39. xsGetUnitMoveTarget](#539-xsgetunitmovetarget)
      * [5.40. xsGetUnitName](#540-xsgetunitname)
      * [5.41. xsGetUnitObjectId](#541-xsgetunitobjectid)
      * [5.42. xsGetUnitOwner](#542-xsgetunitowner)
      * [5.43. xsGetUnitPosition](#543-xsgetunitposition)
      * [5.44. xsGetUnitTargetUnitId](#544-xsgetunittargetunitid)
      * [5.45. xsGetUnitType](#545-xsgetunittype)
      * [5.46. xsGetVictoryCondition](#546-xsgetvictorycondition)
      * [5.47. xsGetVictoryConditionForSecondaryGameMode](#547-xsgetvictoryconditionforsecondarygamemode)
      * [5.48. xsGetVictoryPlayer](#548-xsgetvictoryplayer)
      * [5.49. xsGetVictoryPlayerForSecondaryGameMode](#549-xsgetvictoryplayerforsecondarygamemode)
      * [5.50. xsGetVictoryTime](#550-xsgetvictorytime)
      * [5.51. xsGetVictoryTimeForSecondaryGameMode](#551-xsgetvictorytimeforsecondarygamemode)
      * [5.52. xsGetVictoryType](#552-xsgetvictorytype)
      * [5.53. xsIsObjectAvailable](#553-xsisobjectavailable)
      * [5.54. xsObjectHasAction](#554-xsobjecthasaction)
      * [5.55. xsPlayerAttribute](#555-xsplayerattribute)
      * [5.56. xsRemoveTask](#556-xsremovetask)
      * [5.57. xsResearchTechnology](#557-xsresearchtechnology)
      * [5.58. xsResetTaskAmount](#558-xsresettaskamount)
      * [5.59. xsSetPlayerAttribute](#559-xssetplayerattribute)
      * [5.60. xsSetTriggerVariable](#560-xssettriggervariable)
      * [5.61. xsSetUnitAttributeHeld](#561-xssetunitattributeheld)
      * [5.62. xsSetUnitBuildPoints](#562-xssetunitbuildpoints)
      * [5.63. xsSetUnitCharge](#563-xssetunitcharge)
      * [5.64. xsSetUnitHitpoints](#564-xssetunithitpoints)
      * [5.65. xsTask](#565-xstask)
      * [5.66. xsTaskAmount](#566-xstaskamount)
      * [5.67. xsTriggerVariable](#567-xstriggervariable)
    - [6. Read/Write](#6-readwrite)

      * [6.1. xsCloseFile](#61-xsclosefile)
      * [6.2. xsCreateFile](#62-xscreatefile)
      * [6.3. xsGetDataTypeSize](#63-xsgetdatatypesize)
      * [6.4. xsGetFilePosition](#64-xsgetfileposition)
      * [6.5. xsGetFileSize](#65-xsgetfilesize)
      * [6.6. xsOffsetFilePosition](#66-xsoffsetfileposition)
      * [6.7. xsOpenFile](#67-xsopenfile)
      * [6.8. xsReadFloat](#68-xsreadfloat)
      * [6.9. xsReadInt](#69-xsreadint)
      * [6.10. xsReadString](#610-xsreadstring)
      * [6.11. xsReadVector](#611-xsreadvector)
      * [6.12. xsSetFilePosition](#612-xssetfileposition)
      * [6.13. xsWriteFloat](#613-xswritefloat)
      * [6.14. xsWriteInt](#614-xswriteint)
      * [6.15. xsWriteString](#615-xswritestring)
      * [6.16. xsWriteVector](#616-xswritevector)
    - [7. Ai Scripting](#7-ai-scripting)

      * [7.1. xsGetGoal](#71-xsgetgoal)
      * [7.2. xsGetStrategicNumber](#72-xsgetstrategicnumber)
      * [7.3. xsSetGoal](#73-xssetgoal)
      * [7.4. xsSetStrategicNumber](#74-xssetstrategicnumber)
    - [8. Functions With Seemingly No Practical Use](#8-functions-with-seemingly-no-practical-use)

      * [8.1. xsAddRuntimeEvent](#81-xsaddruntimeevent)
      * [8.2. xsBreakPoint](#82-xsbreakpoint)
      * [8.3. xsDumpArrays](#83-xsdumparrays)
      * [8.4. xsGetContextPlayer](#84-xsgetcontextplayer)
      * [8.5. xsGetFunctionID](#85-xsgetfunctionid)
      * [8.6. xsSetContextPlayer](#86-xssetcontextplayer)
  + [Constant Reference](../constants/)
  + [Useful Resources](../useful/)
  + [Known Bugs](../bugs/)

    Known Bugs
    - [Chat Data](../bugs/Chat%20Data/)
    - [Crashes](../bugs/Crashes/)
    - [Editor](../bugs/Editor/)
    - [Effect Amount](../bugs/Effect%20Amount/)
    - [Important](../bugs/Important/)
    - [Language Syntax](../bugs/Language%20Syntax/)
    - [Task](../bugs/Task/)
    - [Task](../bugs/Individual%20Tech%20Modifiers/)
* [Mods](../../../mods/)

  Mods
* [RMS](../../../rms/)

  RMS
* [AI](../../../ai/)

  AI
* [Audio](../../../audio/)

  Audio

Table of contents

* [1. Rules](#1-rules)

  + [1.1. xsDisableRule](#11-xsdisablerule)
  + [1.2. xsDisableRuleGroup](#12-xsdisablerulegroup)
  + [1.3. xsDisableSelf](#13-xsdisableself)
  + [1.4. xsEnableRule](#14-xsenablerule)
  + [1.5. xsEnableRuleGroup](#15-xsenablerulegroup)
  + [1.6. xsIsRuleEnabled](#16-xsisruleenabled)
  + [1.7. xsIsRuleGroupEnabled](#17-xsisrulegroupenabled)
  + [1.8. xsSetRuleMaxInterval](#18-xssetrulemaxinterval)
  + [1.9. xsSetRuleMaxIntervalSelf](#19-xssetrulemaxintervalself)
  + [1.10. xsSetRuleMinInterval](#110-xssetrulemininterval)
  + [1.11. xsSetRuleMinIntervalSelf](#111-xssetruleminintervalself)
  + [1.12. xsSetRulePriority](#112-xssetrulepriority)
  + [1.13. xsSetRulePrioritySelf](#113-xssetrulepriorityself)
* [2. Vectors](#2-vectors)

  + [2.1. xsVectorGetX](#21-xsvectorgetx)
  + [2.2. xsVectorGetY](#22-xsvectorgety)
  + [2.3. xsVectorGetZ](#23-xsvectorgetz)
  + [2.4. xsVectorLength](#24-xsvectorlength)
  + [2.5. xsVectorNormalize](#25-xsvectornormalize)
  + [2.6. xsVectorSet](#26-xsvectorset)
  + [2.7. xsVectorSetX](#27-xsvectorsetx)
  + [2.8. xsVectorSetY](#28-xsvectorsety)
  + [2.9. xsVectorSetZ](#29-xsvectorsetz)
* [3. Arrays](#3-arrays)

  + [3.1. xsArrayCreateBool](#31-xsarraycreatebool)
  + [3.2. xsArrayCreateFloat](#32-xsarraycreatefloat)
  + [3.3. xsArrayCreateInt](#33-xsarraycreateint)
  + [3.4. xsArrayCreateString](#34-xsarraycreatestring)
  + [3.5. xsArrayCreateVector](#35-xsarraycreatevector)
  + [3.6. xsArrayGetBool](#36-xsarraygetbool)
  + [3.7. xsArrayGetFloat](#37-xsarraygetfloat)
  + [3.8. xsArrayGetInt](#38-xsarraygetint)
  + [3.9. xsArrayGetSize](#39-xsarraygetsize)
  + [3.10. xsArrayGetString](#310-xsarraygetstring)
  + [3.11. xsArrayGetVector](#311-xsarraygetvector)
  + [3.12. xsArrayResizeBool](#312-xsarrayresizebool)
  + [3.13. xsArrayResizeFloat](#313-xsarrayresizefloat)
  + [3.14. xsArrayResizeInt](#314-xsarrayresizeint)
  + [3.15. xsArrayResizeString](#315-xsarrayresizestring)
  + [3.16. xsArrayResizeVector](#316-xsarrayresizevector)
  + [3.17. xsArraySetBool](#317-xsarraysetbool)
  + [3.18. xsArraySetFloat](#318-xsarraysetfloat)
  + [3.19. xsArraySetInt](#319-xsarraysetint)
  + [3.20. xsArraySetString](#320-xsarraysetstring)
  + [3.21. xsArraySetVector](#321-xsarraysetvector)
* [4. Maths](#4-maths)

  + [4.1. abs](#41-abs)
  + [4.2. acos](#42-acos)
  + [4.3. asin](#43-asin)
  + [4.4. atan](#44-atan)
  + [4.5. atan2](#45-atan2)
  + [4.6. atan2v](#46-atan2v)
  + [4.7. bitCastToFloat](#47-bitcasttofloat)
  + [4.8. bitCastToInt](#48-bitcasttoint)
  + [4.9. ceil](#49-ceil)
  + [4.10. cos](#410-cos)
  + [4.11. exp](#411-exp)
  + [4.12. floor](#412-floor)
  + [4.13. pow](#413-pow)
  + [4.14. sin](#414-sin)
  + [4.15. sqrt](#415-sqrt)
  + [4.16. tan](#416-tan)
  + [4.17. xsCeilToInt](#417-xsceiltoint)
* [5. General](#5-general)

  + [5.1. xsChatData](#51-xschatdata)
  + [5.2. xsDoesUnitExist](#52-xsdoesunitexist)
  + [5.3. xsEffectAmount](#53-xseffectamount)
  + [5.4. xsGetGameTime](#54-xsgetgametime)
  + [5.5. xsGetGroupMoveTarget](#55-xsgetgroupmovetarget)
  + [5.6. xsGetMapHeight](#56-xsgetmapheight)
  + [5.7. xsGetMapID](#57-xsgetmapid)
  + [5.8. xsGetMapName](#58-xsgetmapname)
  + [5.9. xsGetMapWidth](#59-xsgetmapwidth)
  + [5.10. xsGetNumPlayers](#510-xsgetnumplayers)
  + [5.11. xsGetObjectAttribute](#511-xsgetobjectattribute)
  + [5.12. xsGetObjectClass](#512-xsgetobjectclass)
  + [5.13. xsGetObjectCopyId](#513-xsgetobjectcopyid)
  + [5.14. xsGetObjectCount](#514-xsgetobjectcount)
  + [5.15. xsGetObjectCountTotal](#515-xsgetobjectcounttotal)
  + [5.16. xsGetObjectName](#516-xsgetobjectname)
  + [5.17. xsGetObjectType](#517-xsgetobjecttype)
  + [5.18. xsGetPlayerCivilization](#518-xsgetplayercivilization)
  + [5.19. xsGetPlayerInGame](#519-xsgetplayeringame)
  + [5.20. xsGetPlayerName](#520-xsgetplayername)
  + [5.21. xsGetPlayerNumberOfTechs](#521-xsgetplayernumberoftechs)
  + [5.22. xsGetPlayerUnitIds](#522-xsgetplayerunitids)
  + [5.23. xsGetRandomNumber](#523-xsgetrandomnumber)
  + [5.24. xsGetRandomNumberLH](#524-xsgetrandomnumberlh)
  + [5.25. xsGetRandomNumberMax](#525-xsgetrandomnumbermax)
  + [5.26. xsGetTechName](#526-xsgettechname)
  + [5.27. xsGetTechState](#527-xsgettechstate)
  + [5.28. xsGetTime](#528-xsgettime)
  + [5.29. xsGetTurn](#529-xsgetturn)
  + [5.30. xsGetUnitAttribute](#530-xsgetunitattribute)
  + [5.31. xsGetUnitAttributeHeld](#531-xsgetunitattributeheld)
  + [5.32. xsGetUnitAttributeTypesHeld](#532-xsgetunitattributetypesheld)
  + [5.33. xsGetUnitBuildPoints](#533-xsgetunitbuildpoints)
  + [5.34. xsGetUnitCharge](#534-xsgetunitcharge)
  + [5.35. xsGetUnitClass](#535-xsgetunitclass)
  + [5.36. xsGetUnitCopyId](#536-xsgetunitcopyid)
  + [5.37. xsGetUnitGroupId](#537-xsgetunitgroupid)
  + [5.38. xsGetUnitHitpoints](#538-xsgetunithitpoints)
  + [5.39. xsGetUnitMoveTarget](#539-xsgetunitmovetarget)
  + [5.40. xsGetUnitName](#540-xsgetunitname)
  + [5.41. xsGetUnitObjectId](#541-xsgetunitobjectid)
  + [5.42. xsGetUnitOwner](#542-xsgetunitowner)
  + [5.43. xsGetUnitPosition](#543-xsgetunitposition)
  + [5.44. xsGetUnitTargetUnitId](#544-xsgetunittargetunitid)
  + [5.45. xsGetUnitType](#545-xsgetunittype)
  + [5.46. xsGetVictoryCondition](#546-xsgetvictorycondition)
  + [5.47. xsGetVictoryConditionForSecondaryGameMode](#547-xsgetvictoryconditionforsecondarygamemode)
  + [5.48. xsGetVictoryPlayer](#548-xsgetvictoryplayer)
  + [5.49. xsGetVictoryPlayerForSecondaryGameMode](#549-xsgetvictoryplayerforsecondarygamemode)
  + [5.50. xsGetVictoryTime](#550-xsgetvictorytime)
  + [5.51. xsGetVictoryTimeForSecondaryGameMode](#551-xsgetvictorytimeforsecondarygamemode)
  + [5.52. xsGetVictoryType](#552-xsgetvictorytype)
  + [5.53. xsIsObjectAvailable](#553-xsisobjectavailable)
  + [5.54. xsObjectHasAction](#554-xsobjecthasaction)
  + [5.55. xsPlayerAttribute](#555-xsplayerattribute)
  + [5.56. xsRemoveTask](#556-xsremovetask)
  + [5.57. xsResearchTechnology](#557-xsresearchtechnology)
  + [5.58. xsResetTaskAmount](#558-xsresettaskamount)
  + [5.59. xsSetPlayerAttribute](#559-xssetplayerattribute)
  + [5.60. xsSetTriggerVariable](#560-xssettriggervariable)
  + [5.61. xsSetUnitAttributeHeld](#561-xssetunitattributeheld)
  + [5.62. xsSetUnitBuildPoints](#562-xssetunitbuildpoints)
  + [5.63. xsSetUnitCharge](#563-xssetunitcharge)
  + [5.64. xsSetUnitHitpoints](#564-xssetunithitpoints)
  + [5.65. xsTask](#565-xstask)
  + [5.66. xsTaskAmount](#566-xstaskamount)
  + [5.67. xsTriggerVariable](#567-xstriggervariable)
* [6. Read/Write](#6-readwrite)

  + [6.1. xsCloseFile](#61-xsclosefile)
  + [6.2. xsCreateFile](#62-xscreatefile)
  + [6.3. xsGetDataTypeSize](#63-xsgetdatatypesize)
  + [6.4. xsGetFilePosition](#64-xsgetfileposition)
  + [6.5. xsGetFileSize](#65-xsgetfilesize)
  + [6.6. xsOffsetFilePosition](#66-xsoffsetfileposition)
  + [6.7. xsOpenFile](#67-xsopenfile)
  + [6.8. xsReadFloat](#68-xsreadfloat)
  + [6.9. xsReadInt](#69-xsreadint)
  + [6.10. xsReadString](#610-xsreadstring)
  + [6.11. xsReadVector](#611-xsreadvector)
  + [6.12. xsSetFilePosition](#612-xssetfileposition)
  + [6.13. xsWriteFloat](#613-xswritefloat)
  + [6.14. xsWriteInt](#614-xswriteint)
  + [6.15. xsWriteString](#615-xswritestring)
  + [6.16. xsWriteVector](#616-xswritevector)
* [7. Ai Scripting](#7-ai-scripting)

  + [7.1. xsGetGoal](#71-xsgetgoal)
  + [7.2. xsGetStrategicNumber](#72-xsgetstrategicnumber)
  + [7.3. xsSetGoal](#73-xssetgoal)
  + [7.4. xsSetStrategicNumber](#74-xssetstrategicnumber)
* [8. Functions With Seemingly No Practical Use](#8-functions-with-seemingly-no-practical-use)

  + [8.1. xsAddRuntimeEvent](#81-xsaddruntimeevent)
  + [8.2. xsBreakPoint](#82-xsbreakpoint)
  + [8.3. xsDumpArrays](#83-xsdumparrays)
  + [8.4. xsGetContextPlayer](#84-xsgetcontextplayer)
  + [8.5. xsGetFunctionID](#85-xsgetfunctionid)
  + [8.6. xsSetContextPlayer](#86-xssetcontextplayer)

# Functions Reference

*Written by: Alian713, Kramb*

---

## 1. Rules[¶](#1-rules "Permanent link")

### 1.1. xsDisableRule[¶](#11-xsdisablerule "Permanent link")

Returning Type: `void`

Prototype: `void xsDisableRule(string ruleName)`

Parameters:

1. `string ruleName`: The name of the rule to disable

Disables the given rule.

### 1.2. xsDisableRuleGroup[¶](#12-xsdisablerulegroup "Permanent link")

Returning Type: `void`

Prototype: `void xsDisableRuleGroup(string ruleGroupName)`

Parameters:

1. `string ruleGroupName`: The name of the rule group to disable

Disables all the rules in the given rule group

### 1.3. xsDisableSelf[¶](#13-xsdisableself "Permanent link")

Returning Type: `void`

Prototype: `void xsDisableSelf()`

Disables the rule this function is called inside. Cannot be used outside of a rule's body!

### 1.4. xsEnableRule[¶](#14-xsenablerule "Permanent link")

Returning Type: `void`

Prototype: `void xsEnableRule(string ruleName)`

Parameters:

1. `string ruleName`: The name of the rule to enable

Enables the given rule.

### 1.5. xsEnableRuleGroup[¶](#15-xsenablerulegroup "Permanent link")

Returning Type: `void`

Prototype: `void xsEnableRuleGroup(string ruleGroupName)`

Parameters:

1. `string ruleGroupName`: The name of the rule group to enable

Enables all the rules in the given rule group

### 1.6. xsIsRuleEnabled[¶](#16-xsisruleenabled "Permanent link")

Returning Type: `bool`

Prototype: `bool xsIsRuleEnabled(string ruleName)`

Parameters:

1. `string ruleName`: The name of the rule to check

Returns true if the rule is enabled, else returns false.

### 1.7. xsIsRuleGroupEnabled[¶](#17-xsisrulegroupenabled "Permanent link")

Returning Type: `bool`

Prototype: `bool xsIsRuleGroupEnabled(string ruleGroupName)`

Parameters:

1. `string ruleGroupName`: The name of the rule group to check

Returns true, if all the rules in the given rule group are enabled

### 1.8. xsSetRuleMaxInterval[¶](#18-xssetrulemaxinterval "Permanent link")

Returning Type: `void`

Prototype: `void xsSetRuleMaxInterval(string ruleName, int interval)`

Parameters:

1. `string ruleName`: The name of the rule to set the max interval of
2. `int interval`: The new max interval of the rule

Sets the max interval of the given rule.

### 1.9. xsSetRuleMaxIntervalSelf[¶](#19-xssetrulemaxintervalself "Permanent link")

Returning Type: `void`

Prototype: `void xsSetRuleMaxIntervalSelf(int interval)`

Parameters:

1. `int interval`: The new max interval of the rule

Sets the max interval of the rule this function is called inside. Cannot be used outside of a rule's body!

### 1.10. xsSetRuleMinInterval[¶](#110-xssetrulemininterval "Permanent link")

Returning Type: `void`

Prototype: `void xsSetRuleMinInterval(string ruleName, int interval)`

Parameters:

1. `string ruleName`: The name of the rule to set the min interval of
2. `int interval`: The new min interval of the rule

Sets the min interval of the given rule.

### 1.11. xsSetRuleMinIntervalSelf[¶](#111-xssetruleminintervalself "Permanent link")

Returning Type: `void`

Prototype: `void xsSetRuleMinIntervalSelf(int interval)`

Parameters:

1. `int interval`: The new min interval of the rule

Sets the min interval of the rule this function is called inside. Cannot be used outside of a rule's body!

### 1.12. xsSetRulePriority[¶](#112-xssetrulepriority "Permanent link")

Returning Type: `void`

Prototype: `void xsSetRulePriority(string ruleName, int rulePriority)`

Parameters:

1. `string ruleName`: The name of the rule to set the priority of
2. `int rulePriority`: The new priority of the rule

Sets the priority of the given rule.

### 1.13. xsSetRulePrioritySelf[¶](#113-xssetrulepriorityself "Permanent link")

Returning Type: `void`

Prototype: `void xsSetRulePrioritySelf(int rulePriority)`

Parameters:

1. `int rulePriority`: The new priority of the rule

Sets the priority of the rule this function is called inside. Cannot be used outside of a rule's body!

## 2. Vectors[¶](#2-vectors "Permanent link")

### 2.1. xsVectorGetX[¶](#21-xsvectorgetx "Permanent link")

Returning Type: `float`

Prototype: `float xsVectorGetX(vector v)`

Parameters:

1. `vector v`: The vector to get the X coordinate of

The X coordinate of the vector given.

### 2.2. xsVectorGetY[¶](#22-xsvectorgety "Permanent link")

Returning Type: `float`

Prototype: `float xsVectorGetY(vector v)`

Parameters:

1. `vector v`: The vector to get the Y coordinate of

The Y coordinate of the vector given.

### 2.3. xsVectorGetZ[¶](#23-xsvectorgetz "Permanent link")

Returning Type: `float`

Prototype: `float xsVectorGetZ(vector v)`

Parameters:

1. `vector v`: The vector to get the Z coordinate of

The Z coordinate of the vector given.

### 2.4. xsVectorLength[¶](#24-xsvectorlength "Permanent link")

Returning Type: `float`

Prototype: `float xsVectorLength(vector v)`

Parameters:

1. `vector v`: The vector to calculate the length of

Returns the length of the given vector.

### 2.5. xsVectorNormalize[¶](#25-xsvectornormalize "Permanent link")

Returning Type: `vector`

Prototype: `vector xsVectorNormalize(vector v)`

Parameters:

1. `vector v`: The vector to normalise

Returns the normalised vector in the direction of the given vector.

### 2.6. xsVectorSet[¶](#26-xsvectorset "Permanent link")

Returning Type: `vector`

Prototype: `vector xsVectorSet(float x, float y, float z)`

Parameters:

1. `float x`: The value to set the X coordinate to
2. `float y`: The value to set the Y coordinate to
3. `float z`: The value to set the Z coordinate to

Returns a vector with the given X, Y and Z components.

### 2.7. xsVectorSetX[¶](#27-xsvectorsetx "Permanent link")

Returning Type: `vector`

Prototype: `vector xsVectorSetX(vector v, float x)`

Parameters:

1. `vector v`: The vector to modify the X coordinate of
2. `float x`: The value to set the X coordinate to

Returns a new vector with the X component of the given vector changed to the given value. Note: This function DOES NOT modify the vector given as the parameter!

### 2.8. xsVectorSetY[¶](#28-xsvectorsety "Permanent link")

Returning Type: `vector`

Prototype: `vector xsVectorSetY(vector v, float y)`

Parameters:

1. `vector v`: The vector to modify the Y coordinate of
2. `float y`: The value to set the Y coordinate to

Returns a new vector with the Y component of the given vector changed to the given value. Note: This function DOES NOT modify the vector given as the parameter!

### 2.9. xsVectorSetZ[¶](#29-xsvectorsetz "Permanent link")

Returning Type: `vector`

Prototype: `vector xsVectorSetZ(vector v, float z)`

Parameters:

1. `vector v`: The vector to modify the Z coordinate of
2. `float z`: The value to set the Z coordinate to

Returns a new vector with the Z component of the given vector changed to the given value. Note: This function DOES NOT modify the vector given as the parameter!

## 3. Arrays[¶](#3-arrays "Permanent link")

### 3.1. xsArrayCreateBool[¶](#31-xsarraycreatebool "Permanent link")

Returning Type: `int`

Prototype: `int xsArrayCreateBool(int size, bool defaultValue, string uniqueName)`

Parameters:

1. `int size`: The length of the array to create
2. (Optional) `bool defaultValue`: The default value to initialise all the values in the array to. If not set all array values will be false
3. (Optional) `string uniqueName`: A unique name of the created array. Note that when set, this name cannot be reused, and subsequent array creation attempts with the same name will fail (e.g. in loops)

Creates an array of type bool and returns its ID. Created arrays never go out of scope so be careful when creating them inside repeated code patterns as that can introduce memory leaks.

### 3.2. xsArrayCreateFloat[¶](#32-xsarraycreatefloat "Permanent link")

Returning Type: `int`

Prototype: `int xsArrayCreateFloat(int size, float defaultValue, string uniqueName)`

Parameters:

1. `int size`: The length of the array to create
2. (Optional) `float defaultValue`: The default value to initialise all the values in the array to. If not set all array values will be 0.0
3. (Optional) `string uniqueName`: A unique name of the created array. Note that when set, this name cannot be reused, and subsequent array creation attempts with the same name will fail (e.g. in loops)

Creates an array of type float and returns its ID. Created arrays never go out of scope so be careful when creating them inside repeated code patterns as that can introduce memory leaks.

### 3.3. xsArrayCreateInt[¶](#33-xsarraycreateint "Permanent link")

Returning Type: `int`

Prototype: `int xsArrayCreateInt(int size, int defaultValue, string uniqueName)`

Parameters:

1. `int size`: The length of the array to create
2. (Optional) `int defaultValue`: The default value to initialise all the values in the array to. If not set all array values will be 0
3. (Optional) `string uniqueName`: A unique name of the created array. Note that when set, this name cannot be reused, and subsequent array creation attempts with the same name will fail (e.g. in loops)

Creates an array of type int and returns its ID. Created arrays never go out of scope so be careful when creating them inside repeated code patterns as that can introduce memory leaks.

### 3.4. xsArrayCreateString[¶](#34-xsarraycreatestring "Permanent link")

Returning Type: `int`

Prototype: `int xsArrayCreateString(int size, string defaultValue, string uniqueName)`

Parameters:

1. `int size`: The length of the array to create
2. (Optional) `string defaultValue`: The default value to initialise all the values in the array to. If not set all array values will be ""
3. (Optional) `string uniqueName`: A unique name of the created array. Note that when set, this name cannot be reused, and subsequent array creation attempts with the same name will fail (e.g. in loops)

Creates an array of type String and returns its ID. Created arrays never go out of scope so be careful when creating them inside repeated code patterns as that can introduce memory leaks.

### 3.5. xsArrayCreateVector[¶](#35-xsarraycreatevector "Permanent link")

Returning Type: `int`

Prototype: `int xsArrayCreateVector(int size, vector defaultValue, string uniqueName)`

Parameters:

1. `int size`: The length of the array to create
2. (Optional) `vector defaultValue`: The default value to initialise all the values in the array to. If not set all array values will be vector(-1.0, -1.0, -1.0)
3. (Optional) `string uniqueName`: A unique name of the created array. Note that when set, this name cannot be reused, and subsequent array creation attempts with the same name will fail (e.g. in loops)

Creates an array of type Vector and returns its ID. Created arrays never go out of scope so be careful when creating them inside repeated code patterns as that can introduce memory leaks.

### 3.6. xsArrayGetBool[¶](#36-xsarraygetbool "Permanent link")

Returning Type: `bool`

Prototype: `bool xsArrayGetBool(int arrayId, int index)`

Parameters:

1. `int arrayId`: The ID of the array to get the value from
2. `int index`: The index to get the value of

Gets and returns the value of the given bool array at the specified index.

### 3.7. xsArrayGetFloat[¶](#37-xsarraygetfloat "Permanent link")

Returning Type: `float`

Prototype: `float xsArrayGetFloat(int arrayId, int index)`

Parameters:

1. `int arrayId`: The ID of the array to get the value from
2. `int index`: The index to get the value of

Gets and returns the value of the given float array at the specified index.

### 3.8. xsArrayGetInt[¶](#38-xsarraygetint "Permanent link")

Returning Type: `int`

Prototype: `int xsArrayGetInt(int arrayId, int index)`

Parameters:

1. `int arrayId`: The ID of the array to get the value from
2. `int index`: The index to get the value of

Gets and returns the value of the given int array at the specified index.

### 3.9. xsArrayGetSize[¶](#39-xsarraygetsize "Permanent link")

Returning Type: `int`

Prototype: `int xsArrayGetSize(int arrayId)`

Parameters:

1. `int arrayId`: The ID of the array to get the length of

Returns the length of the given array.

### 3.10. xsArrayGetString[¶](#310-xsarraygetstring "Permanent link")

Returning Type: `string`

Prototype: `string xsArrayGetString(int arrayId, int index)`

Parameters:

1. `int arrayId`: The ID of the array to get the value from
2. `int index`: The index to get the value of

Gets and returns the value of the given string array at the specified index.

### 3.11. xsArrayGetVector[¶](#311-xsarraygetvector "Permanent link")

Returning Type: `vector`

Prototype: `vector xsArrayGetVector(int arrayId, int index)`

Parameters:

1. `int arrayId`: The ID of the array to get the value from
2. `int index`: The index to get the value of

Gets and returns the value of the given vector array at the specified index.

### 3.12. xsArrayResizeBool[¶](#312-xsarrayresizebool "Permanent link")

Returning Type: `int`

Prototype: `int xsArrayResizeBool(int arrayId, int newSize)`

Parameters:

1. `int arrayId`: The ID of the array to resize
2. `int newSize`: The new size of the array

Resizes the the given bool array to the specified size and returns 1.

### 3.13. xsArrayResizeFloat[¶](#313-xsarrayresizefloat "Permanent link")

Returning Type: `int`

Prototype: `int xsArrayResizeFloat(int arrayId, int newSize)`

Parameters:

1. `int arrayId`: The ID of the array to resize
2. `int newSize`: The new size of the array

Resizes the the given float array to the specified size and returns 1.

### 3.14. xsArrayResizeInt[¶](#314-xsarrayresizeint "Permanent link")

Returning Type: `int`

Prototype: `int xsArrayResizeInt(int arrayId, int newSize)`

Parameters:

1. `int arrayId`: The ID of the array to resize
2. `int newSize`: The new size of the array

Resizes the the given int array to the specified size and returns 1.

### 3.15. xsArrayResizeString[¶](#315-xsarrayresizestring "Permanent link")

Returning Type: `int`

Prototype: `int xsArrayResizeString(int arrayId, int newSize)`

Parameters:

1. `int arrayId`: The ID of the array to resize
2. `int newSize`: The new size of the array

Resizes the the given string array to the specified size and returns 1.

### 3.16. xsArrayResizeVector[¶](#316-xsarrayresizevector "Permanent link")

Returning Type: `int`

Prototype: `int xsArrayResizeVector(int arrayId, int newSize)`

Parameters:

1. `int arrayId`: The ID of the array to resize
2. `int newSize`: The new size of the array

Resizes the the given vector array to the specified size and returns 1.

### 3.17. xsArraySetBool[¶](#317-xsarraysetbool "Permanent link")

Returning Type: `int`

Prototype: `int xsArraySetBool(int arrayId, int index, bool value)`

Parameters:

1. `int arrayId`: The ID of the array to set the value in
2. `int index`: The index to set the value of
3. `bool value`: The new value to set

Sets the value at the specified index of the given bool array to the provided value and returns 1.

### 3.18. xsArraySetFloat[¶](#318-xsarraysetfloat "Permanent link")

Returning Type: `int`

Prototype: `int xsArraySetFloat(int arrayId, int index, float value)`

Parameters:

1. `int arrayId`: The ID of the array to set the value in
2. `int index`: The index to set the value of
3. `float value`: The new value to set

Sets the value at the specified index of the given float array to the provided value and returns 1.

### 3.19. xsArraySetInt[¶](#319-xsarraysetint "Permanent link")

Returning Type: `int`

Prototype: `int xsArraySetInt(int arrayId, int index, int value)`

Parameters:

1. `int arrayId`: The ID of the array to set the value in
2. `int index`: The index to set the value of
3. `int value`: The new value to set

Sets the value at the specified index of the given int array to the provided value and returns 1.

### 3.20. xsArraySetString[¶](#320-xsarraysetstring "Permanent link")

Returning Type: `int`

Prototype: `int xsArraySetString(int arrayId, int index, string value)`

Parameters:

1. `int arrayId`: The ID of the array to set the value in
2. `int index`: The index to set the value of
3. `string value`: The new value to set

Sets the value at the specified index of the given string array to the provided value and returns 1.

### 3.21. xsArraySetVector[¶](#321-xsarraysetvector "Permanent link")

Returning Type: `int`

Prototype: `int xsArraySetVector(int arrayId, int index, vector value)`

Parameters:

1. `int arrayId`: The ID of the array to set the value in
2. `int index`: The index to set the value of
3. `vector value`: The new value to set

Sets the value at the specified index of the given vector array to the provided value and returns 1.

## 4. Maths[¶](#4-maths "Permanent link")

### 4.1. abs[¶](#41-abs "Permanent link")

Returning Type: `float`

Prototype: `float abs(float x)`

Parameters:

1. `float x`: The number to find the absolute value of

Returns the absolute value (magnitude) of the given number.

### 4.2. acos[¶](#42-acos "Permanent link")

Returning Type: `float`

Prototype: `float acos(float x)`

Parameters:

1. `float x`: The value to find the inverse cosine of

Returns the inverse cosine (arccos) of the given value

### 4.3. asin[¶](#43-asin "Permanent link")

Returning Type: `float`

Prototype: `float asin(float x)`

Parameters:

1. `float x`: The value to find the inverse sine of

Returns the inverse sine (arcsin) of the given value

### 4.4. atan[¶](#44-atan "Permanent link")

Returning Type: `float`

Prototype: `float atan(float x)`

Parameters:

1. `float x`: The value to find the inverse tangent of

Returns the inverse tangent (arctan) of the given value

### 4.5. atan2[¶](#45-atan2 "Permanent link")

Returning Type: `float`

Prototype: `float atan2(float y, float x)`

Parameters:

1. `float y`: The Y coordinate of the point to find the X+ angle of
2. `float x`: The X coordinate of the point to find the X+ angle of

Returns the angle of the given point (x, y) made from the X+ axis, in the range \([-\pi, \pi]\)

### 4.6. atan2v[¶](#46-atan2v "Permanent link")

Returning Type: `float`

Prototype: `float atan2v(vector v)`

Parameters:

1. `vector v`: The vector to get the atan2 from

Returns the angle of the given vector from the X+ axis, in the range \([-\pi, \pi]\). Ignores the Z component

### 4.7. bitCastToFloat[¶](#47-bitcasttofloat "Permanent link")

Returning Type: `float`

Prototype: `float bitCastToFloat(int number)`

Parameters:

1. `int number`: The value to `reinterpret/bit_cast` to `float`

Reinterprets/Bit casts the given `int` value to `float`. Equivalent to `std::mem::transmute::<i32, f32>(number)`

### 4.8. bitCastToInt[¶](#48-bitcasttoint "Permanent link")

Returning Type: `int`

Prototype: `int bitCastToInt(float number)`

Parameters:

1. `float number`: The value to `reinterpret/bit_cast` to `int`

Reinterprets/Bit casts the given `float` value to `int`. Equivalent to `std::mem::transmute::<f32, i32>(number)`

### 4.9. ceil[¶](#49-ceil "Permanent link")

Returning Type: `float`

Prototype: `float ceil(float x)`

Parameters:

1. `float x`: The value to find the ceil of

Returns \(\left \lceil{x}\right \rceil\)

### 4.10. cos[¶](#410-cos "Permanent link")

Returning Type: `float`

Prototype: `float cos(float x)`

Parameters:

1. `float x`: The angle (in radians) to find the cosine of

Returns the cosine of the angle in radians

### 4.11. exp[¶](#411-exp "Permanent link")

Returning Type: `float`

Prototype: `float exp(float x)`

Parameters:

1. `float x`: The value to find the exp of

Returns \(e^x\)

### 4.12. floor[¶](#412-floor "Permanent link")

Returning Type: `float`

Prototype: `float floor(float x)`

Parameters:

1. `float x`: The value to find the floor of

Returns \(\left \lfloor{x}\right \rfloor\)

### 4.13. pow[¶](#413-pow "Permanent link")

Returning Type: `float`

Prototype: `float pow(float x, float y)`

Parameters:

1. `float x`: The base value
2. `float y`: The exponent to raise the base value to

Returns x raised to the power y (x\*\*y).

### 4.14. sin[¶](#414-sin "Permanent link")

Returning Type: `float`

Prototype: `float sin(float x)`

Parameters:

1. `float x`: The angle (in radians) to find the sine of

Returns the sine of the angle in radians.

### 4.15. sqrt[¶](#415-sqrt "Permanent link")

Returning Type: `float`

Prototype: `float sqrt(float x)`

Parameters:

1. `float x`: The number to find the square root of

Returns the square root of the given number.

### 4.16. tan[¶](#416-tan "Permanent link")

Returning Type: `float`

Prototype: `float tan(float x)`

Parameters:

1. `float x`: The angle (in radians) to find the tangent of

Returns the tangent of the angle in radians

### 4.17. xsCeilToInt[¶](#417-xsceiltoint "Permanent link")

Returning Type: `int`

Prototype: `int xsCeilToInt(float value)`

Parameters:

1. `float value`: The value to determine the ceil of

Rounds the number **up** to the next integer

## 5. General[¶](#5-general "Permanent link")

### 5.1. xsChatData[¶](#51-xschatdata "Permanent link")

Returning Type: `void`

Prototype: `void xsChatData(string message, int value)`

Parameters:

1. `string message`: The message to display in chat
2. (Optional) `int value`: This value is inserted in place of any `%d` used in the message of the function

Shows the given message in the game chat

### 5.2. xsDoesUnitExist[¶](#52-xsdoesunitexist "Permanent link")

Returning Type: `bool`

Prototype: `bool xsDoesUnitExist(int unitId)`

Parameters:

1. `int unitId`: The unit ID to check

Returns true if a unit with the given ID exists on the map.

### 5.3. xsEffectAmount[¶](#53-xseffectamount "Permanent link")

Returning Type: `void`

Prototype: `void xsEffectAmount(int effectId, int objectOrTechnologyId, int attributeOrOperation, float value, int playerNumber)`

Parameters:

1. `int effectId`: The ID of the effect to use
2. `int objectOrTechnologyId`: The ID of the object or technology to effect
3. `int attributeOrOperation`: The attribute to modify or the operation to perform
4. `float value`: The value of the effect
5. (Optional) `int playerNumber`: The player to apply the effect to. If unspecified, applies to all players except Gaia.

Change the specified attribute of the specified object or technology by the value for the specified player. For more information on this, check the UserPatch section of the guide

### 5.4. xsGetGameTime[¶](#54-xsgetgametime "Permanent link")

Returning Type: `int`

Prototype: `int xsGetGameTime()`

Returns the current game time in seconds

### 5.5. xsGetGroupMoveTarget[¶](#55-xsgetgroupmovetarget "Permanent link")

Returning Type: `vector`

Prototype: `vector xsGetGroupMoveTarget(int groupId)`

Parameters:

1. `int groupId`: The group (formation) to get the movement target for

Returns the location this group (formation) is currently moving to

### 5.6. xsGetMapHeight[¶](#56-xsgetmapheight "Permanent link")

Returning Type: `int`

Prototype: `int xsGetMapHeight()`

Returns the Height of the map.

### 5.7. xsGetMapID[¶](#57-xsgetmapid "Permanent link")

Returning Type: `int`

Prototype: `int xsGetMapID()`

Returns the AI map type.

### 5.8. xsGetMapName[¶](#58-xsgetmapname "Permanent link")

Returning Type: `string`

Prototype: `string xsGetMapName(bool showFileExtension)`

Parameters:

1. `bool showFileExtension`: If this is set to true, then the returned name also contains the file extension

Returns the name of the map currently being played.

### 5.9. xsGetMapWidth[¶](#59-xsgetmapwidth "Permanent link")

Returning Type: `int`

Prototype: `int xsGetMapWidth()`

Returns the Width of the map.

### 5.10. xsGetNumPlayers[¶](#510-xsgetnumplayers "Permanent link")

Returning Type: `int`

Prototype: `int xsGetNumPlayers()`

Returns the number of players in the game

### 5.11. xsGetObjectAttribute[¶](#511-xsgetobjectattribute "Permanent link")

Returning Type: `float`

Prototype: `float xsGetObjectAttribute(int playerId, int objectId, int attribute, int damageClass)`

Parameters:

1. `int playerId`: The player whose object to get the attribute for
2. `int objectId`: The object to get the attribute for
3. `int attribute`: The attribute to get
4. `int damageClass`: For use with armor/attack attributes - specifies which armor/attack class to get

Returns the attribute value for an object

### 5.12. xsGetObjectClass[¶](#512-xsgetobjectclass "Permanent link")

Returning Type: `int`

Prototype: `int xsGetObjectClass(int playerId, int objectId)`

Parameters:

1. `int playerId`: The player to get the object's class for
2. `int objectId`: The object to get the class for

Returns the given object's class for the specified player. See [cClass constants](../constants/#10-object-class "Jump To: XS > Constant Reference > EffectAmount Object Class")

### 5.13. xsGetObjectCopyId[¶](#513-xsgetobjectcopyid "Permanent link")

Returning Type: `int`

Prototype: `int xsGetObjectCopyId(int playerId, int objectId)`

Parameters:

1. `int playerId`: The player to get the object's copy ID for
2. `int objectId`: The object to get the copy ID for

Returns the given object's copy ID in data for the specified player

### 5.14. xsGetObjectCount[¶](#514-xsgetobjectcount "Permanent link")

Returning Type: `int`

Prototype: `int xsGetObjectCount(int playerId, int objectOrClassId)`

Parameters:

1. `int playerId`: The player to get the object count for
2. `int objectOrClassId`: The ID of the object or class to get the count for

Returns the number of currently alive objects with the given ID of the specified player

### 5.15. xsGetObjectCountTotal[¶](#515-xsgetobjectcounttotal "Permanent link")

Returning Type: `int`

Prototype: `int xsGetObjectCountTotal(int playerId, int objectOrClassId)`

Parameters:

1. `int playerId`: The player to get the object count for
2. `int objectOrClassId`: The ID of the object or class to get the count for

Returns the number of currently alive/standing + queued/foundation objects with the given ID of the specified player

### 5.16. xsGetObjectName[¶](#516-xsgetobjectname "Permanent link")

Returning Type: `string`

Prototype: `string xsGetObjectName(int objectId, int playerId, bool internalName)`

Parameters:

1. `int objectId`: The object to get the name for
2. `int playerId`: The player to get the object's name for
3. (Optional) `bool internalName`: Returns the internal name of the object if set. `!#xs false` by default.

Returns the current name of the given object for the specified player.

### 5.17. xsGetObjectType[¶](#517-xsgetobjecttype "Permanent link")

Returning Type: `int`

Prototype: `int xsGetObjectType(int playerId, int objectId)`

Parameters:

1. `int playerId`: The player to get the object's type for
2. `int objectId`: The object to get the type for

Returns the given object's type for the specified player. See [cObjectType constants](../constants/#16-object-type "Jump To: XS > Constant Reference > Object Type")

### 5.18. xsGetPlayerCivilization[¶](#518-xsgetplayercivilization "Permanent link")

Returning Type: `int`

Prototype: `int xsGetPlayerCivilization(int playerNumber)`

Parameters:

1. `int playerNumber`: The player to get the civilization of

Returns the civilization ID of the given player. Refer to the [Constant Reference](../constants/#3-civs "Jump to: XS Scripting > Constant Reference > #3. Civs") for all the different civ IDs

### 5.19. xsGetPlayerInGame[¶](#519-xsgetplayeringame "Permanent link")

Returning Type: `bool`

Prototype: `bool xsGetPlayerInGame(int playerNumber)`

Parameters:

1. `int playerNumber`: Check if this player is still alive

Returns true if the player given is still alive, and false otherwise.

### 5.20. xsGetPlayerName[¶](#520-xsgetplayername "Permanent link")

Returning Type: `string`

Prototype: `string xsGetPlayerName(int playerId)`

Parameters:

1. `int playerId`: The lobby index of the player

Returns the given player's name.

### 5.21. xsGetPlayerNumberOfTechs[¶](#521-xsgetplayernumberoftechs "Permanent link")

Returning Type: `int`

Prototype: `int xsGetPlayerNumberOfTechs(int playerNumber)`

Parameters:

1. `int playerNumber`: The player whose technology count is being requested.

Returns the number of technologies available to the player in the entire game.

### 5.22. xsGetPlayerUnitIds[¶](#522-xsgetplayerunitids "Permanent link")

Returning Type: `int`

Prototype: `int xsGetPlayerUnitIds(int playerId, int objectOrClassId, int arrayId)`

Parameters:

1. `int playerId`: The player to get the unit IDs for
2. `int objectOrClassId`: The ID of the object or class to get the unit reference IDs for
3. (Optional) `int arrayId`: Reuse an existing array to save memory

Returns an array of unit IDs on the map for the given player and the specified object ID or class. The IDs here are the same as the `reference_id` used by the scenario editor

### 5.23. xsGetRandomNumber[¶](#523-xsgetrandomnumber "Permanent link")

Returning Type: `int`

Prototype: `int xsGetRandomNumber()`

Returns a random number between 0 and 32767.

### 5.24. xsGetRandomNumberLH[¶](#524-xsgetrandomnumberlh "Permanent link")

Returning Type: `int`

Prototype: `int xsGetRandomNumberLH(int low, int high)`

Parameters:

1. `int low`: The lower bound for the range for the random number returned (included)
2. `int high`: The upper bound for the range for the random number returned (excluded)

Returns a random number between `low` and `high`

### 5.25. xsGetRandomNumberMax[¶](#525-xsgetrandomnumbermax "Permanent link")

Returning Type: `int`

Prototype: `int xsGetRandomNumberMax(int max)`

Parameters:

1. `int max`: The upper bound for the range for the random number returned (excluded)

Returns a random number between 0 and `max`.

### 5.26. xsGetTechName[¶](#526-xsgettechname "Permanent link")

Returning Type: `string`

Prototype: `string xsGetTechName(int techId, int playerId, bool internalName)`

Parameters:

1. `int techId`: The tech to get the name for
2. `int playerId`: The player to get the tech's name for
3. (Optional) `bool internalName`: Returns the internal name of the tech if set. `!#xs false` by default.

Returns the current name of the given tech for the specified player.

### 5.27. xsGetTechState[¶](#527-xsgettechstate "Permanent link")

Returning Type: `int`

Prototype: `int xsGetTechState(int techId, int playerId)`

Parameters:

1. `int techId`: The tech to get the state for
2. `int playerId`: The player to get the tech's state for

Returns one of the [cTechState constants](../constants/#15-techstate "Jump To: XS > Constant Reference > Tech State Constants") based on the tech's status

### 5.28. xsGetTime[¶](#528-xsgettime "Permanent link")

Returning Type: `int`

Prototype: `int xsGetTime()`

Returns the current game time - 1 in seconds

### 5.29. xsGetTurn[¶](#529-xsgetturn "Permanent link")

Returning Type: `int`

Prototype: `int xsGetTurn()`

Returns the current game tick (called turn).

### 5.30. xsGetUnitAttribute[¶](#530-xsgetunitattribute "Permanent link")

Returning Type: `float`

Prototype: `float xsGetUnitAttribute(int unitId, int attribute, int damageClass)`

Parameters:

1. `int unitId`: The unit to get the attribute for.
2. `int attribute`: The attribute to get
3. `int damageClass`: For use with armor/attack attributes - specifies which armor/attack class to get

Returns the attribute value for a specific unit on the map.

### 5.31. xsGetUnitAttributeHeld[¶](#531-xsgetunitattributeheld "Permanent link")

Returning Type: `float`

Prototype: `float xsGetUnitAttributeHeld(int unitId, int attributeId)`

Parameters:

1. `int unitId`: The unit to get the resource held for
2. (Optional) `int attributeId`: The ID of the resource to get. If unspecified, return the first resource which the unit holds

Returns the given unit's amount of the specified resource held.

### 5.32. xsGetUnitAttributeTypesHeld[¶](#532-xsgetunitattributetypesheld "Permanent link")

Returning Type: `int`

Prototype: `int xsGetUnitAttributeTypesHeld(int unitId)`

Parameters:

1. `int unitId`: The unit to get the held resource types for

Returns the given unit's type of resources held as an array of ints. The only unit that this currently returns multiple values for is the trade cart/cog.

### 5.33. xsGetUnitBuildPoints[¶](#533-xsgetunitbuildpoints "Permanent link")

Returning Type: `float`

Prototype: `float xsGetUnitBuildPoints(int unitId)`

Parameters:

1. `int unitId`: The unit to get the Build Points for

Returns the given unit's Built Points

### 5.34. xsGetUnitCharge[¶](#534-xsgetunitcharge "Permanent link")

Returning Type: `float`

Prototype: `float xsGetUnitCharge(int unitId)`

Parameters:

1. `int unitId`: The unit to get the charge for

Returns the given unit's charge

### 5.35. xsGetUnitClass[¶](#535-xsgetunitclass "Permanent link")

Returning Type: `int`

Prototype: `int xsGetUnitClass(int unitId)`

Parameters:

1. `int unitId`: The unit to get the class for

Returns the given unit's class See [cClass constants](../constants/#10-effectamount-object-class "Jump To: XS > Constant Reference > EffectAmount Object Class")

### 5.36. xsGetUnitCopyId[¶](#536-xsgetunitcopyid "Permanent link")

Returning Type: `int`

Prototype: `int xsGetUnitCopyId(int unitId)`

Parameters:

1. `int unitId`: The unit to get the copy ID for

Returns the given unit's copy ID in data

### 5.37. xsGetUnitGroupId[¶](#537-xsgetunitgroupid "Permanent link")

Returning Type: `int`

Prototype: `int xsGetUnitGroupId(int unitId)`

Parameters:

1. `int unitId`: The unit to get the group ID (formation) for

Returns the ID of the group (formation) for this unit

### 5.38. xsGetUnitHitpoints[¶](#538-xsgetunithitpoints "Permanent link")

Returning Type: `float`

Prototype: `float xsGetUnitHitpoints(int unitId)`

Parameters:

1. `int unitId`: The unit to get the HP for

Returns the given unit's HP

### 5.39. xsGetUnitMoveTarget[¶](#539-xsgetunitmovetarget "Permanent link")

Returning Type: `vector`

Prototype: `vector xsGetUnitMoveTarget(int unitId)`

Parameters:

1. `int unitId`: The unit to get the movement target for

Returns the location this unit is currently moving to

### 5.40. xsGetUnitName[¶](#540-xsgetunitname "Permanent link")

Returning Type: `string`

Prototype: `string xsGetUnitName(int unitId, bool internalName)`

Parameters:

1. `int unitId`: The unit ID to check
2. (Optional) `bool internalName`: Returns the internal name of the unit if set. `!#xs false` by default.

Returns the current name of a given unit

### 5.41. xsGetUnitObjectId[¶](#541-xsgetunitobjectid "Permanent link")

Returning Type: `int`

Prototype: `int xsGetUnitObjectId(int unitId)`

Parameters:

1. `int unitId`: The unit to get the object ID for

Returns the given unit's ID in data

### 5.42. xsGetUnitOwner[¶](#542-xsgetunitowner "Permanent link")

Returning Type: `int`

Prototype: `int xsGetUnitOwner(int unitId)`

Parameters:

1. `int unitId`: The unit to get the owner ID for

Returns the lobby index of the player owning this unit.

### 5.43. xsGetUnitPosition[¶](#543-xsgetunitposition "Permanent link")

Returning Type: `vector`

Prototype: `vector xsGetUnitPosition(int unitId)`

Parameters:

1. `int unitId`: The unit to get the position for

Returns the current position of a unit.

### 5.44. xsGetUnitTargetUnitId[¶](#544-xsgetunittargetunitid "Permanent link")

Returning Type: `int`

Prototype: `int xsGetUnitTargetUnitId(int unitId)`

Parameters:

1. `int unitId`: The unit to get the target for

Returns the ID of the currently targeted unit for this unit

### 5.45. xsGetUnitType[¶](#545-xsgetunittype "Permanent link")

Returning Type: `int`

Prototype: `int xsGetUnitType(int unitId)`

Parameters:

1. `int unitId`: The unit to get the type for

Returns the given unit's type. See [cObjectType constants](../constants/#16-object-type "Jump To: XS > Constant Reference > Object Type")

### 5.46. xsGetVictoryCondition[¶](#546-xsgetvictorycondition "Permanent link")

Returning Type: `int`

Prototype: `int xsGetVictoryCondition()`

Returns one of these constants: `cStandardVictory` `cWonderVictory` `cRelicVictory` `cKingOfTheHillVictory`

### 5.47. xsGetVictoryConditionForSecondaryGameMode[¶](#547-xsgetvictoryconditionforsecondarygamemode "Permanent link")

Returning Type: `int`

Prototype: `int xsGetVictoryConditionForSecondaryGameMode()`

Returns one of these constants: `cStandardVictory` `cWonderVictory` `cRelicVictory` `cKingOfTheHillVictory`

### 5.48. xsGetVictoryPlayer[¶](#548-xsgetvictoryplayer "Permanent link")

Returning Type: `int`

Prototype: `int xsGetVictoryPlayer()`

Returns the number of the player with the highest score in a normal game. Returns the number of the player who owns 5 relics or has a wonder if standard victory is enabled. In a game like KoTH, returns the number of the player who owns the monument.

### 5.49. xsGetVictoryPlayerForSecondaryGameMode[¶](#549-xsgetvictoryplayerforsecondarygamemode "Permanent link")

Returning Type: `int`

Prototype: `int xsGetVictoryPlayerForSecondaryGameMode()`

Returns `1` when no secondary game mode is set. Returns the number of the player who owns the monument in game modes like KotH

### 5.50. xsGetVictoryTime[¶](#550-xsgetvictorytime "Permanent link")

Returning Type: `int`

Prototype: `int xsGetVictoryTime()`

For game modes like KoTH and other game modes where there is a timer on the screen, it returns the amount of time left in half seconds. meaning if the value returned is 799, it means there are 399.5s remaining. Returns `-1` otherwise

### 5.51. xsGetVictoryTimeForSecondaryGameMode[¶](#551-xsgetvictorytimeforsecondarygamemode "Permanent link")

Returning Type: `int`

Prototype: `int xsGetVictoryTimeForSecondaryGameMode()`

For game modes like KoTH and other game modes where there is a timer on the screen, it returns the amount of time left in half seconds. meaning if the value returned is 799, it means there are 399.5s remaining. Returns `-1` otherwise

### 5.52. xsGetVictoryType[¶](#552-xsgetvictorytype "Permanent link")

Returning Type: `int`

Prototype: `int xsGetVictoryType()`

Returns an integer corresponding to different victory settings in game. These are:

0: Standard

1: Conquest

2: Time Limit

3: Score

4: Custom (scenarios only).

Last Man Standing returns 0 as well.

### 5.53. xsIsObjectAvailable[¶](#553-xsisobjectavailable "Permanent link")

Returning Type: `bool`

Prototype: `bool xsIsObjectAvailable(int objectId, int playerId)`

Parameters:

1. `int objectId`: The object to check the availability for
2. `int playerId`: The player to get the object's availability for

Returns true if this object can currently be trained or built.

### 5.54. xsObjectHasAction[¶](#554-xsobjecthasaction "Permanent link")

Returning Type: `bool`

Prototype: `bool xsObjectHasAction(int playerId, int objectOrClassId, int actionId, int targetPlayerId, int targetType, int targetUnitLevel)`

Parameters:

1. `int playerId`: The player to check unit actions for
2. `int objectOrClassId`: The ID of the object or class to check actions for
3. `int actionId`: The type of action to check for
4. (Optional) `int targetPlayerId`: Check if the action is being performed on a unit (eg. attacking) of this player. Can use -1 to ignore this filter.
5. (Optional) `int targetType`: Check if the action is being performed on a unit of this type. Values 9xx refer to classes. Can use -1 to ignore this filter.
6. (Optional) `int targetUnitLevel`: Check if the action is being performed on a unit with this `Interface Kind` (look in the A.G.E.), eg: 3 - villagers, 4 - most military units. Can be used as an alternative to `targetType`. If both are used, will pick units that match either. Can use -1 to ignore this filter.

Checks and returns if any unit matching the set filters of the given player has the specified action.

### 5.55. xsPlayerAttribute[¶](#555-xsplayerattribute "Permanent link")

Returning Type: `float`

Prototype: `float xsPlayerAttribute(int playerNumber, int resourceId)`

Parameters:

1. `int playerNumber`: The player to get the resource of (0 for Gaia)
2. `int resourceId`: The ID of the resource to get the amount of

Returns the amount the specified resource of the given player.

### 5.56. xsRemoveTask[¶](#556-xsremovetask "Permanent link")

Returning Type: `void`

Prototype: `void xsRemoveTask(int objectOrClassId, int actionType, int targetObjectOrClassId, int playerId)`

Parameters:

1. `int objectOrClassId`: The object or class ID to remove the task from.
2. `int actionType`: Task type. Refer to [cTaskType constants](../constants/#14-task-type "Jump To: XS > Constant Reference > Task Type Constants")
3. (Optional) `int targetObjectOrClassId`: Target object or class ID for the task to filter by.
4. (Optional) `int playerId`: The player from whose objects the task will be removed. If unspecified or -1, applies to all players except Gaia.

Removes a task from a object if the specified `actionType`, `objectId`, and `Search Wait Time` (set by [xsTaskAmount](./#564-xstaskamount)) match an existing task in a object. No other fields are used for filtering (same as when [xsTask](./#563-xstask) edits instead of adding a new task)

### 5.57. xsResearchTechnology[¶](#557-xsresearchtechnology "Permanent link")

Returning Type: `bool`

Prototype: `bool xsResearchTechnology(int techId, bool force, bool techAvailable, int playerNumber)`

Parameters:

1. `int techId`: The technology ID to research.
2. `bool force`: Force researching the tech even if it is not enabled. To force an unavailable tech, the argument `techAvailable` must be set to false
3. `bool techAvailable`: This flag determines if it is required to check if a tech is available before researching it
4. `int playerNumber`: The player to research the technology for

Returns a boolean based on whether the technology was researched or not.

### 5.58. xsResetTaskAmount[¶](#558-xsresettaskamount "Permanent link")

Returning Type: `void`

Prototype: `void xsResetTaskAmount()`

Resets all the values of the global XS task struct to their defaults. See also [xsTask](./#563-xstask).

### 5.59. xsSetPlayerAttribute[¶](#559-xssetplayerattribute "Permanent link")

Returning Type: `void`

Prototype: `void xsSetPlayerAttribute(int playerNumber, int resourceId, float value)`

Parameters:

1. `int playerNumber`: The player to set the resource of (0 for Gaia)
2. `int resourceId`: The ID of the resource to set the amount of
3. `float value`: The amount to set the resource to

Sets the amount of the specified resource of the given player to the provided value.

### 5.60. xsSetTriggerVariable[¶](#560-xssettriggervariable "Permanent link")

Returning Type: `void`

Prototype: `void xsSetTriggerVariable(int variableId, int value)`

Parameters:

1. `int variableId`: The ID of the variable to set the value of
2. `int value`: The value to set the variable to

Sets the value of the variable of the given variable ID to the provided value.

### 5.61. xsSetUnitAttributeHeld[¶](#561-xssetunitattributeheld "Permanent link")

Returning Type: `bool`

Prototype: `bool xsSetUnitAttributeHeld(int unitId, float value, int attributeId)`

Parameters:

1. `int unitId`: The unit to set the resource held for
2. `float value`: The amount to set the held resource to
3. (Optional) `int attributeId`: The ID of the resource to set. If unspecified, sets the first resource which the unit holds

Sets the given unit's amount of the specified resource. The only unit this can currently add extra resources to is the trade cart/cog.

### 5.62. xsSetUnitBuildPoints[¶](#562-xssetunitbuildpoints "Permanent link")

Returning Type: `bool`

Prototype: `bool xsSetUnitBuildPoints(int unitId, float value)`

Parameters:

1. `int unitId`: The unit to set the build points for
2. `float value`: The value to set the build points to

Sets the given unit's Build Points

### 5.63. xsSetUnitCharge[¶](#563-xssetunitcharge "Permanent link")

Returning Type: `bool`

Prototype: `bool xsSetUnitCharge(int unitId, float value)`

Parameters:

1. `int unitId`: The unit to set the charge for
2. `float value`: The value to set the charge to

Sets the given unit's charge

### 5.64. xsSetUnitHitpoints[¶](#564-xssetunithitpoints "Permanent link")

Returning Type: `bool`

Prototype: `bool xsSetUnitHitpoints(int unitId, float value)`

Parameters:

1. `int unitId`: The unit to set the HP for
2. `float value`: The value to set the HP to

Sets the given unit's HP

### 5.65. xsTask[¶](#565-xstask "Permanent link")

Returning Type: `void`

Prototype: `void xsTask(int objectOrClassId, int actionType, int targetObjectOrClassId, int playerId)`

Parameters:

1. `int objectOrClassId`: The object or class ID to add the task to
2. `int actionType`: Task type. Refer to [cTaskType constants](../constants/#14-task-type "Jump To: XS > Constant Reference > Task Type Constants")
3. (Optional) `int targetObjectOrClassId`: Target object or class ID for the task to filter by.
4. (Optional) `int playerId`: The player to whose objects the task will be inserted. If unspecified or -1, applies to all players except Gaia.

Adds a new (or edits an existing) task with the fields previously defined by calls to [xsTaskAmount](./#564-xstaskamount) for the specified object at the end of the task list (see A.G.E.). If a task with the specified `actionType`, `objectId`, and `Search Wait Time` (set by `xsTaskAmount`) already exists, it is edited instead of a new one being added.

Note that `xsTaskAmount` modifies a global task struct which is re-used every time `xsTask` is called (For non programmers, this is similar to filling out a form once (the calls to [xsTaskAmount](./#564-xstaskamount)) and then submitting multiple copies of it for different people)

### 5.66. xsTaskAmount[¶](#566-xstaskamount "Permanent link")

Returning Type: `void`

Prototype: `void xsTaskAmount(int taskFieldId, float value)`

Parameters:

1. `int taskFieldId`: Specifies which property of the task to change. Refer to [cTaskAttr constants](../constants/#13-task-attribute "Jump To: XS > Constant Reference > Task Type Constants")
2. `float value`: The value to set the task field to

Sets the value of the given field of the global XS task struct to the provided value. See also [xsTask](./#563-xstask). It is recommended to always set all values before inserting or updating a task otherwise the insert/update might fail.

### 5.67. xsTriggerVariable[¶](#567-xstriggervariable "Permanent link")

Returning Type: `int`

Prototype: `int xsTriggerVariable(int variableId)`

Parameters:

1. `int variableId`: The ID of the variable to get the value of

Returns the value of the variable of the given variable ID.

## 6. Read/Write[¶](#6-readwrite "Permanent link")

### 6.1. xsCloseFile[¶](#61-xsclosefile "Permanent link")

Returning Type: `bool`

Prototype: `bool xsCloseFile()`

Close the currently opened or created file. Returns `true` if the file was successfully closed

### 6.2. xsCreateFile[¶](#62-xscreatefile "Permanent link")

Returning Type: `bool`

Prototype: `bool xsCreateFile(bool append)`

Parameters:

1. (Optional) `bool append`: Default: `true`. If set to `false`, this will overwrite any existing file with the same name.

Creates a new (or appends to an existing) `.xsdat` file with the same name as the RMS/scenario being played. After invoking this function, the writing functions can be used to write data to the file. Returns `true` if the file was successfully created. In a multiplayer game a file is created for each player, and subsequent writes will be duplicated to each player.

### 6.3. xsGetDataTypeSize[¶](#63-xsgetdatatypesize "Permanent link")

Returning Type: `int`

Prototype: `int xsGetDataTypeSize(int type)`

Parameters:

1. `int type`: One of the `cOffsetXXX` constants may be used as a parameter

Returns the number of bytes used to store a given type value.

### 6.4. xsGetFilePosition[¶](#64-xsgetfileposition "Permanent link")

Returning Type: `int`

Prototype: `int xsGetFilePosition()`

Gets the byte (0-indexed) of the file that the next read function will start reading from.

### 6.5. xsGetFileSize[¶](#65-xsgetfilesize "Permanent link")

Returning Type: `int`

Prototype: `int xsGetFileSize()`

Gets the size (in bytes) of the currently open file

### 6.6. xsOffsetFilePosition[¶](#66-xsoffsetfileposition "Permanent link")

Returning Type: `bool`

Prototype: `bool xsOffsetFilePosition(int dataType, bool forward)`

Parameters:

1. `int dataType`: The [cOffset constants](../constants/#1-readwrite "Jump To: XS > Constant Reference > Read/Write Constants") can be used to specify the datatype used for the offset. Integers and floats are 4 bytes long, vectors are 12 bytes long and strings can be of variable length (specified by the 32 bit int preceding the chars of the string)
2. (Optional) `bool forward`: Default: `true`. Setting this to `false` will make the file position move back

Moves the file position forward (or backward) relative to the current file position, and by an amount of bytes equivalent to reading the given data type

### 6.7. xsOpenFile[¶](#67-xsopenfile "Permanent link")

Returning Type: `bool`

Prototype: `bool xsOpenFile(string filename)`

Parameters:

1. `string filename`: The name of the file to open, without the `.xsdat` extension

Opens an existing `.xsdat`file in read only mode. After invoking this function, the reading functions can be used to read data from the file. Returns `true` if the file was successfully opened. In a multiplayer game, the file being read must exist for all players and contain the same data to avoid an out of sync error

### 6.8. xsReadFloat[¶](#68-xsreadfloat "Permanent link")

Returning Type: `float`

Prototype: `float xsReadFloat()`

Reads and returns a float from the previously opened `.xsdat` file. Note that this function does not check if the value being read is actually meant to be a float, which means the value being read is bit casted into a float regardless of what it originally was. This function also moves the file position forward by 4 bytes

### 6.9. xsReadInt[¶](#69-xsreadint "Permanent link")

Returning Type: `int`

Prototype: `int xsReadInt()`

Reads and returns an integer from the previously opened `.xsdat` file. Note that this function does not check if the value being read is actually meant to be an integer, which means the value being read is bit casted into an integer regardless of what it originally was. This function also moves the file position forward by 4 bytes

### 6.10. xsReadString[¶](#610-xsreadstring "Permanent link")

Returning Type: `string`

Prototype: `string xsReadString()`

Reads and returns a string from the previously opened `.xsdat` file. Note that this function does not check if the value being read is actually meant to be a string, which means the value being read is bit casted into a string regardless of what it originally was. This function also moves the file position forward by 4 bytes + the amount of bytes in the length of the string

### 6.11. xsReadVector[¶](#611-xsreadvector "Permanent link")

Returning Type: `vector`

Prototype: `vector xsReadVector()`

Reads and returns a vector from the previously opened `.xsdat` file. Note that this function does not check if the value being read is actually meant to be a vector, which means the value being read is bit casted into a vector regardless of what it originally was. This function also moves the file position forward by 12 bytes

### 6.12. xsSetFilePosition[¶](#612-xssetfileposition "Permanent link")

Returning Type: `bool`

Prototype: `bool xsSetFilePosition(int byteOffset)`

Parameters:

1. `int byteOffset`: 0 indexed byte offset to determine which byte to read and return from the file

Sets the byte (0-indexed) of the file that the next read function will start reading from.

### 6.13. xsWriteFloat[¶](#613-xswritefloat "Permanent link")

Returning Type: `bool`

Prototype: `bool xsWriteFloat(float data)`

Parameters:

1. `float data`: The float value to write

Writes a floating point number to the previously created `.xsdat` file. Causes an error if a file hasn't been opened before using. Returns `true` if the floating point number was successfully written. Floats are written in the 32 bit IEEE 754 format

### 6.14. xsWriteInt[¶](#614-xswriteint "Permanent link")

Returning Type: `bool`

Prototype: `bool xsWriteInt(int data)`

Parameters:

1. `int data`: The integer to write

Writes an integer to the previously created `.xsdat` file. Causes an error if a file hasn't been opened before using. Returns `true` if the integer was successfully written. Integers are written as signed 32 bit numbers

### 6.15. xsWriteString[¶](#615-xswritestring "Permanent link")

Returning Type: `bool`

Prototype: `bool xsWriteString(string data)`

Parameters:

1. `string data`: The string to write

Writes a string to the previously created `.xsdat` file. Causes an error if a file hasn't been opened before using. Returns `true` if the string was successfully written. A string is written to the file in two parts, an unsigned 32 bit integer (indicates the length of the string) followed by that many bytes making up the actual characters of the string

### 6.16. xsWriteVector[¶](#616-xswritevector "Permanent link")

Returning Type: `bool`

Prototype: `bool xsWriteVector(vector data)`

Parameters:

1. `vector data`: The vector to write

Writes a vector to the previously created `.xsdat` file. Causes an error if a file hasn't been opened before using. Returns `true` if the vector was successfully written. Vectors are written as 3 consecutive floating point numbers, one for each coordinate.

## 7. Ai Scripting[¶](#7-ai-scripting "Permanent link")

### 7.1. xsGetGoal[¶](#71-xsgetgoal "Permanent link")

Returning Type: `int`

Prototype: `int xsGetGoal(int id)`

Parameters:

1. `int id`: The goal id/number to get for the current AI

Gets the goal id/number of the current AI

### 7.2. xsGetStrategicNumber[¶](#72-xsgetstrategicnumber "Permanent link")

Returning Type: `int`

Prototype: `int xsGetStrategicNumber(int id)`

Parameters:

1. `int id`: The SN to get for the current AI

Gets the SN of the current AI

### 7.3. xsSetGoal[¶](#73-xssetgoal "Permanent link")

Returning Type: `int`

Prototype: `int xsSetGoal(int id, int value)`

Parameters:

1. `int id`: The goal id/number to get for the current AI
2. `int value`: The value to set the goal id/number to

Sets the goal id/number of the current AI

### 7.4. xsSetStrategicNumber[¶](#74-xssetstrategicnumber "Permanent link")

Returning Type: `int`

Prototype: `int xsSetStrategicNumber(int id, int value)`

Parameters:

1. `int id`: The SN to get for the current AI
2. `int value`: The value to set the SN to

Sets the SN of the current AI

## 8. Functions With Seemingly No Practical Use[¶](#8-functions-with-seemingly-no-practical-use "Permanent link")

### 8.1. xsAddRuntimeEvent[¶](#81-xsaddruntimeevent "Permanent link")

Returning Type: `bool`

Prototype: `bool xsAddRuntimeEvent(string runtimeName, string functionName, int functionArgument)`

Parameters:

1. `string runtimeName`: This is the name of the runtime to create the event in. This should be `"Random Map"` for RMS and `"Scenario Triggers"` for scenarios. Find which one to use in a general script by using the `xsGetMapName(true)` [function](./#56-xsgetmapname "Jump To: Function Reference > xsGetMapName") and checking the extension. To use with an AI, set the runtime name to "Expert" and pass the player number as the arg
2. `string functionName`: This is the name of a user defined function that takes a single integer argument
3. `int functionArgument`: This is an integer argument that is passed to the function given to the argument `functionName` when this event runs.

A runtime event is called after all the XS code has finished executing but before rules start executing. It calls the function `functionName` given to it with the `functionArgument` passed to it as a parameter. For programmers familiar with the terminology, this is basically a way to set a callback. It also returns true if the function name given to it exists, otherwise it returns false. Does not work with built-ins

### 8.2. xsBreakPoint[¶](#82-xsbreakpoint "Permanent link")

Returning Type: `void`

Prototype: `void xsBreakPoint()`

This function is meant to add a break point to the execution of XS code for debugging. This used to cause a crash in crash earlier versions of DE.

### 8.3. xsDumpArrays[¶](#83-xsdumparrays "Permanent link")

Returning Type: `void`

Prototype: `void xsDumpArrays()`

This function is supposed to blogs out all XS arrays. Currently, it does absolutely nothing.

### 8.4. xsGetContextPlayer[¶](#84-xsgetcontextplayer "Permanent link")

Returning Type: `int`

Prototype: `int xsGetContextPlayer()`

Returns the current context player ID.

### 8.5. xsGetFunctionID[¶](#85-xsgetfunctionid "Permanent link")

Returning Type: `int`

Prototype: `int xsGetFunctionID(string functionName)`

Parameters:

1. `string functionName`: The name of the function to get the hash of

Returns the hash of a given function. This function has no practical application and is probably for internal usage only.

### 8.6. xsSetContextPlayer[¶](#86-xssetcontextplayer "Permanent link")

Returning Type: `void`

Prototype: `void xsSetContextPlayer(int playerNumber)`

Parameters:

1. `int playerNumber`: The player to set the context player to

In other functions involving a `playerNumber` argument, the value of the context player is used if `-1` is passed as `playerNumber` to them. `xsEffectAmount` will use the value of the context player as its player if `-2` is passed to it as the player argument.

Was this page helpful?

Thanks for your feedback!

Thanks for your feedback! Help us improve this page by using our [feedback form](...).

Back to top


Made with
[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
