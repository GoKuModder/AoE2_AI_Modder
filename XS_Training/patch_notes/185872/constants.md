# XS Constants Reference: Update 185872

This addendum records constants used by the XS APIs and scenario features introduced or documented in Update 185872. It supplements the current captured UGC constants page at XS_Training/ugc.aoe2.rocks/general/xs/constants/index.md.

## Sources

- Official release notes: https://www.ageofempires.com/news/age-of-empires-ii-definitive-edition-update-185872/
- Current UGC constants page: https://ugc.aoe2.rocks/general/xs/constants/constants/ (captured in the repository on 2026-09-23).
- Machine-readable UGC constants source: https://raw.githubusercontent.com/Divy1211/AoE2DE_UGC_Guide/main/docs/general/xs/constants/constants.json (1,160 rows when fetched on 2026-09-23); Markdown source: https://raw.githubusercontent.com/Divy1211/AoE2DE_UGC_Guide/main/docs/general/xs/constants/constants.md.
- Installed game reference: resources/_common/xs/Constants.xs, checked on 2026-09-23. The matching installed game executable reports file version 101.103.54800.0.
- The release notes identify the Tech Attribute, Map Tile Attribute, and Unit Property sections and enumerate object attributes 167–221. The live UGC page supplies the current full constants reference. Runtime identifiers and values below were reconciled against the installed Constants.xs; source disagreements and UGC naming errors are listed at the end.

## Tech Attribute Constants

Used by xsGetTechAttribute.

~~~xs
extern const int cTechState = 0;
extern const int cTechCost = 1;
extern const int cTechResearchTime = 2;
extern const int cTechResearchLocation = 3;
extern const int cTechButtonLocation = 4;
extern const int cTechHotkeyId = 5;
extern const int cTechIconId = 6;
extern const int cTechEffectId = 7;
extern const int cTechCurrentResearchLocation = 8;
extern const int cTechTimesResearched = 9;
extern const int cTechTimesQueued = 10;
extern const int cTechStackingAllowed = 11;
extern const int cTechStackingEnabled = 12;
extern const int cTechStackingCap = 13;
extern const int cTechNumResearchLocations = 14;
extern const int cTechCostType = 15;
extern const int cTechCostDeductFlag = 16;
~~~

The live UGC page names attribute 16 cTechDeductFlag. The installed game file declares cTechCostDeductFlag = 16; the catalogs retain both spellings and mark the UGC spelling as an alias rather than claiming it is declared by this installed build.

## Map Tile Attribute Constants

Used by xsGetMapTileAttribute. The installed Constants.xs places the cTile... declarations after a generic Unit Property Constants comment; the release notes identify this group as Map Tile Attribute constants.

~~~xs
extern const int cTileTerrainId = 0;
extern const int cTileElevation = 1;
extern const int cTileMaskId = 2;
extern const int cTileLayerId = 3;
~~~

## Unit Property Constants

The first group is marked “Get or Set - int/float”; the second group is marked “Get only - int” in Constants.xs. These values are used by xsGetUnitProperty and xsSetUnitProperty.

~~~xs
extern const int cUnitHitpoints = 0;
extern const int cUnitBuildpoints = 1;
extern const int cUnitCharge = 2;
extern const int cUnitCaptionStringId = 3;
extern const int cUnitAttributeHeld = 4;
extern const int cUnitGarrisonedInId = 5;
extern const int cUnitCaptureFlag = 6;
extern const int cUnitDeletable = 7;
extern const int cUnitTargetable = 8;
extern const int cUnitAttackable = 9;
extern const int cUnitSelectable = 10;
extern const int cUnitStance = 11;
extern const int cUnitVisibility = 12;
extern const int cUnitColorId = 13;
extern const int cUnitLocked = 14; // for gates
extern const int cUnitFacet = 15;
extern const int cUnitGroupId = 10000;
extern const int cUnitObjectId = 10001;
extern const int cUnitCopyId = 10002;
extern const int cUnitClassType = 10003;
extern const int cUnitObjectType = 10004;
extern const int cUnitAttributeTypesHeld = 10005;
extern const int cUnitGarrisonedUnitIds = 10006;
extern const int cUnitTargetId = 10007;
extern const int cUnitTarget2Id = 10008;
extern const int cUnitActionId = 10009;
extern const int cUnitOrderId = 10010;
~~~

## Object Attribute Constants

The live UGC reference and installed game file include these object attribute IDs before the 167–221 range highlighted in the release notes:

| ID | Constant | Object attribute |
|---:|---|---|
| 158 | cTrainLocationsEntryMod | Train Locations Entry Mod |
| 159 | cTrainLocationsTotalNum | Train Locations Total Num |
| 160 | cAddArmorType | Add Armor Type |
| 161 | cAddAttackType | Add Attack Type |
| 162 | cChargeTarget | Charge Target |
| 163 | cSizeClass | Size Class |
| 164 | cRemoveArmorType | Remove Armor Type |
| 165 | cRemoveAttackType | Remove Attack Type |
| 166 | cUndeadFlag | Undead Flag |

The UGC links for IDs 164 and 165 incorrectly point to Add Armor Type and Add Attack Type. The names and IDs above are checked against the installed Constants.xs.

The release notes enumerate the labels and IDs from 167 to 221. The matching c... identifiers and values below come from the installed Constants.xs.

| ID | Constant | Object attribute |
|---:|---|---|
| 167 | cBuildAndGoAway | Build And Go Away |
| 168 | cTypeFirstStorage | Type First Storage |
| 169 | cTypeSecondStorage | Type Second Storage |
| 170 | cTypeThirdStorage | Type Third Storage |
| 171 | cStoreFlagFirstStorage | Store Flag First Storage |
| 172 | cStoreFlagSecondStorage | Store Flag Second Storage |
| 173 | cStoreFlagThirdStorage | Store Flag Third Storage |
| 174 | cAmountFirstCost | Amount First Cost |
| 175 | cAmountSecondCost | Amount Second Cost |
| 176 | cAmountThirdCost | Amount Third Cost |
| 177 | cTypeFirstCost | Type First Cost |
| 178 | cTypeSecondCost | Type Second Cost |
| 179 | cTypeThirdCost | Type Third Cost |
| 180 | cDeductFlagFirstCost | Deduct Flag First Cost |
| 181 | cDeductFlagSecondCost | Deduct Flag Second Cost |
| 182 | cDeductFlagThirdCost | Deduct Flag Third Cost |
| 183 | cSpawningGraphic | Spawning Graphic |
| 184 | cUpgradeGraphic | Upgrade Graphic |
| 185 | cFlyMode | Fly Mode |
| 186 | cCanBeGathered | Can Be Gathered |
| 187 | cHillMode | Hill Mode |
| 188 | cDoppelganger | Doppelganger |
| 189 | cGatherGroup | Gather Group |
| 190 | cTaskSwapGroup | Task Swap Group |
| 191 | cPlacementTerrain1 | Placement Terrain 1 |
| 192 | cPlacementTerrain2 | Placement Terrain 2 |
| 193 | cPlacementCenterTerrain1 | Placement Center Terrain 1 |
| 194 | cPlacementCenterTerrain2 | Placement Center Terrain 2 |
| 195 | cInitiatedTechId | Initiated Tech ID |
| 196 | cMinSizeMultiplier | Min Size Multiplier |
| 197 | cSelectionOutlineSizeX | Selection Outline Size X |
| 198 | cSelectionOutlineSizeY | Selection Outline Size Y |
| 199 | cSelectionOutlineSizeZ | Selection Outline Size Z |
| 200 | cClearanceSizeX | Clearance Size X |
| 201 | cClearanceSizeY | Clearance Size Y |
| 202 | cStackUnit | Stack Unit |
| 203 | cHeadUnit | Head Unit |
| 204 | cTransformUnit | Transform Unit |
| 205 | cPileUnit | Pile Unit |
| 206 | cAnnexUnit1 | Annex Unit 1 |
| 207 | cAnnexUnit2 | Annex Unit 2 |
| 208 | cAnnexUnit3 | Annex Unit 3 |
| 209 | cAnnexUnit4 | Annex Unit 4 |
| 210 | cAnnexUnit1OffsetX | Annex Unit 1 Offset X |
| 211 | cAnnexUnit1OffsetY | Annex Unit 1 Offset Y |
| 212 | cAnnexUnit2OffsetX | Annex Unit 2 Offset X |
| 213 | cAnnexUnit2OffsetY | Annex Unit 2 Offset Y |
| 214 | cAnnexUnit3OffsetX | Annex Unit 3 Offset X |
| 215 | cAnnexUnit3OffsetY | Annex Unit 3 Offset Y |
| 216 | cAnnexUnit4OffsetX | Annex Unit 4 Offset X |
| 217 | cAnnexUnit4OffsetY | Annex Unit 4 Offset Y |
| 218 | cMoveAlgorithm | Move Algorithm |
| 219 | cSpacingModifier | Spacing Modifier |
| 220 | cCanBurn | Can Burn |
| 221 | cGatherFlag | Gather Flag |

### Undead Flag Values

These flags are used with object attribute 166, cUndeadFlag.

~~~xs
extern const int cUndeadFlagShowUndeadGraphic = 1;
extern const int cUndeadFlagIgnoreInKillStats = 2;
extern const int cUndeadFlagGarrisonInvincibility = 4;
~~~

## Scenario Unit State Values

The update adds the Capture Flag and Unit State options to the scenario editor. These exact enumerators are present in the installed Constants.xs; capture flags are also described in the update notes.

The UGC reference documents the capture behavior: cCaptureFlagNever prevents conversion; cCaptureFlagOnce allows one conversion and is the default for Gaia units; cCaptureFlagMultipleTimes allows repeated conversion (for example, sheep and monuments); and cCaptureFlagNeverGaiaAggressive prevents conversion while making Gaia units aggressive toward player units.

~~~xs
extern const int cCaptureFlagNever = 0;
extern const int cCaptureFlagOnce = 1;
extern const int cCaptureFlagMultipleTimes = 2;
extern const int cCaptureFlagNeverGaiaAggressive = 3;
extern const int cStanceAggressive = 0;
extern const int cStanceDefensive = 1;
extern const int cStanceStandGround = 2;
extern const int cStanceNoAttack = 3;
~~~

## Full UGC Catalog Audit

The catalog mirrors now include all verified entries from the 1,160-row live UGC JSON source, plus installed-game constants that the page omits. Two malformed Unit Task/Action names in the UGC source, cctionTypeUnload and cctionTypeGatherPoint, are represented under the actual installed names cActionTypeUnload = 9 and cActionTypeGatherPoint = 10. The UGC-only cTechDeductFlag = 16 spelling is retained beside the installed cTechCostDeductFlag = 16 name. The installed-only cUnitFacet = 15 remains in the catalog.

For conflicting values, the installed Constants.xs wins for this build:

| Constant | Live UGC value | Installed Constants.xs value | Catalog value |
|---|---:|---:|---:|
| cNumCivs | 63 | 62 | 62 |
| cAttributeResearch | 2 | 3 | 3 |
| cSentinelEndClass | 965 | 968 | 968 |

The live UGC source also lists cAttributeTriggerSharedLOS = 217, but the installed Constants.xs does not declare it; its catalog description marks that availability gap. Language-provided values cActivationTime, cOriginVector, and cInvalidVector are also absent from Constants.xs declarations and remain documented as XS language constants.
