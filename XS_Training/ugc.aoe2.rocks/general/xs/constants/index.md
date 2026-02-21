---
source_url: https://ugc.aoe2.rocks/general/xs/constants/
fetched_at: 2026-02-08T19:30:26+00:00
---

Constant Reference - AoE2DE UGC Guide






[Skip to content](#1-readwrite)

AoE2DE UGC Guide

Constant Reference



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
  + [Functions Reference](../functions/)
  + Constant Reference

    [Constant Reference](./)



    Table of contents
    - [1. Read/Write](#1-readwrite)

      * [1.1. cOffsetString](#11-coffsetstring)
      * [1.2. cOffsetInteger](#12-coffsetinteger)
      * [1.3. cOffsetFloat](#13-coffsetfloat)
      * [1.4. cOffsetVector](#14-coffsetvector)
    - [2. Age](#2-age)

      * [2.1. cDarkAge](#21-cdarkage)
      * [2.2. cFeudalAge](#22-cfeudalage)
      * [2.3. cCastleAge](#23-ccastleage)
      * [2.4. cImperialAge](#24-cimperialage)
      * [2.5. cStoneAge](#25-cstoneage)
      * [2.6. cToolAge](#26-ctoolage)
      * [2.7. cBronzeAge](#27-cbronzeage)
      * [2.8. cIronAge](#28-cironage)
    - [3. Value](#3-value)

      * [3.1. cActivationTime](#31-cactivationtime)
      * [3.2. cOriginVector](#32-coriginvector)
      * [3.3. cInvalidVector](#33-cinvalidvector)
    - [4. Victory Conditions](#4-victory-conditions)

      * [4.1. cStandardVictory](#41-cstandardvictory)
      * [4.2. cWonderVictory](#42-cwondervictory)
      * [4.3. cRelicVictory](#43-crelicvictory)
      * [4.4. cKingOfTheHillVictory](#44-ckingofthehillvictory)
    - [5. Civilization](#5-civilization)

      * [5.1. cGaia](#51-cgaia)
      * [5.2. cBritons](#52-cbritons)
      * [5.3. cFranks](#53-cfranks)
      * [5.4. cGoths](#54-cgoths)
      * [5.5. cTeutons](#55-cteutons)
      * [5.6. cJapanese](#56-cjapanese)
      * [5.7. cChinese](#57-cchinese)
      * [5.8. cByzantines](#58-cbyzantines)
      * [5.9. cPersians](#59-cpersians)
      * [5.10. cSaracens](#510-csaracens)
      * [5.11. cTurks](#511-cturks)
      * [5.12. cVikings](#512-cvikings)
      * [5.13. cMongols](#513-cmongols)
      * [5.14. cCelts](#514-ccelts)
      * [5.15. cSpanish](#515-cspanish)
      * [5.16. cAztecs](#516-caztecs)
      * [5.17. cMayans](#517-cmayans)
      * [5.18. cHuns](#518-chuns)
      * [5.19. cKoreans](#519-ckoreans)
      * [5.20. cItalians](#520-citalians)
      * [5.21. cIndians](#521-cindians)
      * [5.22. cIncas](#522-cincas)
      * [5.23. cMagyars](#523-cmagyars)
      * [5.24. cSlavs](#524-cslavs)
      * [5.25. cPortuguese](#525-cportuguese)
      * [5.26. cEthiopians](#526-cethiopians)
      * [5.27. cMalians](#527-cmalians)
      * [5.28. cBerbers](#528-cberbers)
      * [5.29. cKhmer](#529-ckhmer)
      * [5.30. cMalay](#530-cmalay)
      * [5.31. cBurmese](#531-cburmese)
      * [5.32. cVietnamese](#532-cvietnamese)
      * [5.33. cBulgarians](#533-cbulgarians)
      * [5.34. cTatars](#534-ctatars)
      * [5.35. cCumans](#535-ccumans)
      * [5.36. cLithuanians](#536-clithuanians)
      * [5.37. cBurgundians](#537-cburgundians)
      * [5.38. cSicilians](#538-csicilians)
      * [5.39. cPoles](#539-cpoles)
      * [5.40. cBohemians](#540-cbohemians)
      * [5.41. cDravidians](#541-cdravidians)
      * [5.42. cBengalis](#542-cbengalis)
      * [5.43. cGurjaras](#543-cgurjaras)
      * [5.44. cRomans](#544-cromans)
      * [5.45. cArmenians](#545-carmenians)
      * [5.46. cGeorgians](#546-cgeorgians)
      * [5.47. cAchaemenids](#547-cachaemenids)
      * [5.48. cAthenians](#548-cathenians)
      * [5.49. cSpartans](#549-cspartans)
      * [5.50. cShu](#550-cshu)
      * [5.51. cWu](#551-cwu)
      * [5.52. cWei](#552-cwei)
      * [5.53. cJurchens](#553-cjurchens)
      * [5.54. cKhitans](#554-ckhitans)
      * [5.55. cAoeEgyptians](#555-caoeegyptians)
      * [5.56. cAoeGreeks](#556-caoegreeks)
      * [5.57. cAoeBabylonians](#557-caoebabylonians)
      * [5.58. cAoeAssyrians](#558-caoeassyrians)
      * [5.59. cAoeMinoans](#559-caoeminoans)
      * [5.60. cAoeHittites](#560-caoehittites)
      * [5.61. cAoePhoenicians](#561-caoephoenicians)
      * [5.62. cAoeSumerians](#562-caoesumerians)
      * [5.63. cAoePersians](#563-caoepersians)
      * [5.64. cAoeShang](#564-caoeshang)
      * [5.65. cAoeYamato](#565-caoeyamato)
      * [5.66. cAoeChoson](#566-caoechoson)
      * [5.67. cAoeRomans](#567-caoeromans)
      * [5.68. cAoeCarthaginians](#568-caoecarthaginians)
      * [5.69. cAoePalmyrans](#569-caoepalmyrans)
      * [5.70. cAoeMacedonians](#570-caoemacedonians)
      * [5.71. cAoeLacViet](#571-caoelacviet)
    - [6. EffectAmount Effect Type](#6-effectamount-effect-type)

      * [6.1. cSetAttribute](#61-csetattribute)
      * [6.2. cModResource](#62-cmodresource)
      * [6.3. cEnableObject](#63-cenableobject)
      * [6.4. cUpgradeUnit](#64-cupgradeunit)
      * [6.5. cAddAttribute](#65-caddattribute)
      * [6.6. cMulAttribute](#66-cmulattribute)
      * [6.7. cMulResource](#67-cmulresource)
      * [6.8. cSpawnUnit](#68-cspawnunit)
      * [6.9. cModifyTech](#69-cmodifytech)
      * [6.10. cSetPlayerData](#610-csetplayerdata)
      * [6.11. cSetTechCost](#611-csettechcost)
      * [6.12. cAddTechCost](#612-caddtechcost)
      * [6.13. cDisableTech](#613-cdisabletech)
      * [6.14. cModTechTime](#614-cmodtechtime)
      * [6.15. cGaiaSetAttribute](#615-cgaiasetattribute)
      * [6.16. cGaiaModResource](#616-cgaiamodresource)
      * [6.17. cGaiaEnableObject](#617-cgaiaenableobject)
      * [6.18. cGaiaUpgradeUnit](#618-cgaiaupgradeunit)
      * [6.19. cGaiaAddAttribute](#619-cgaiaaddattribute)
      * [6.20. cGaiaMulAttribute](#620-cgaiamulattribute)
      * [6.21. cGaiaMulResource](#621-cgaiamulresource)
      * [6.22. cGaiaSpawnUnit](#622-cgaiaspawnunit)
      * [6.23. cGaiaModifyTech](#623-cgaiamodifytech)
      * [6.24. cGaiaSetPlayerData](#624-cgaiasetplayerdata)
      * [6.25. cGaiaSetTechCost](#625-cgaiasettechcost)
      * [6.26. cGaiaAddTechCost](#626-cgaiaaddtechcost)
      * [6.27. cGaiaDisableTech](#627-cgaiadisabletech)
      * [6.28. cGaiaModTechTime](#628-cgaiamodtechtime)
    - [7. EffectAmount Effect Operations](#7-effectamount-effect-operations)

      * [7.1. cAttributeDisable](#71-cattributedisable)
      * [7.2. cAttributeEnable](#72-cattributeenable)
      * [7.3. cAttributeForce](#73-cattributeforce)
      * [7.4. cAttributeResearch](#74-cattributeresearch)
      * [7.5. cAttributeSet](#75-cattributeset)
      * [7.6. cAttributeAdd](#76-cattributeadd)
    - [8. EffectAmount Technology Attribute](#8-effectamount-technology-attribute)

      * [8.1. cAttrSetTime](#81-cattrsettime)
      * [8.2. cAttrAddTime](#82-cattraddtime)
      * [8.3. cAttrMulTime](#83-cattrmultime)
      * [8.4. cAttrSetFoodCost](#84-cattrsetfoodcost)
      * [8.5. cAttrSetWoodCost](#85-cattrsetwoodcost)
      * [8.6. cAttrSetStoneCost](#86-cattrsetstonecost)
      * [8.7. cAttrSetGoldCost](#87-cattrsetgoldcost)
      * [8.8. cAttrAddFoodCost](#88-cattraddfoodcost)
      * [8.9. cAttrAddWoodCost](#89-cattraddwoodcost)
      * [8.10. cAttrAddStoneCost](#810-cattraddstonecost)
      * [8.11. cAttrAddGoldCost](#811-cattraddgoldcost)
      * [8.12. cAttrMulFoodCost](#812-cattrmulfoodcost)
      * [8.13. cAttrMulWoodCost](#813-cattrmulwoodcost)
      * [8.14. cAttrMulStoneCost](#814-cattrmulstonecost)
      * [8.15. cAttrMulGoldCost](#815-cattrmulgoldcost)
      * [8.16. cAttrMulAllCosts](#816-cattrmulallcosts)
      * [8.17. cAttrSetEffect](#817-cattrseteffect)
      * [8.18. cAttrSetLocation](#818-cattrsetlocation)
      * [8.19. cAttrSetButton](#819-cattrsetbutton)
      * [8.20. cAttrSetIcon](#820-cattrseticon)
      * [8.21. cAttrSetName](#821-cattrsetname)
      * [8.22. cAttrSetDescription](#822-cattrsetdescription)
      * [8.23. cAttrSetStacking](#823-cattrsetstacking)
      * [8.24. cAttrSetStackingResearchCap](#824-cattrsetstackingresearchcap)
      * [8.25. cAttrSetHotkey](#825-cattrsethotkey)
      * [8.26. cAttrSetState](#826-cattrsetstate)
    - [9. EffectAmount Unit Attribute](#9-effectamount-unit-attribute)

      * [9.1. cHitpoints](#91-chitpoints)
      * [9.2. cLineOfSight](#92-clineofsight)
      * [9.3. cGarrisonCapacity](#93-cgarrisoncapacity)
      * [9.4. cUnitSizeX](#94-cunitsizex)
      * [9.5. cUnitSizeY](#95-cunitsizey)
      * [9.6. cMovementSpeed](#96-cmovementspeed)
      * [9.7. cRotationSpeed](#97-crotationspeed)
      * [9.8. cArmor](#98-carmor)
      * [9.9. cAttack](#99-cattack)
      * [9.10. cAttackReloadTime](#910-cattackreloadtime)
      * [9.11. cAccuracyPercent](#911-caccuracypercent)
      * [9.12. cMaxRange](#912-cmaxrange)
      * [9.13. cWorkRate](#913-cworkrate)
      * [9.14. cCarryCapacity](#914-ccarrycapacity)
      * [9.15. cBaseArmor](#915-cbasearmor)
      * [9.16. cProjectileUnit](#916-cprojectileunit)
      * [9.17. cIconGraphicsAngle](#917-cicongraphicsangle)
      * [9.18. cTerrainDefenseBonus](#918-cterraindefensebonus)
      * [9.19. cEnableSmartProjectile](#919-cenablesmartprojectile)
      * [9.20. cMinimumRange](#920-cminimumrange)
      * [9.21. cAmountFirstStorage](#921-camountfirststorage)
      * [9.22. cBlastWidth](#922-cblastwidth)
      * [9.23. cSearchRadius](#923-csearchradius)
      * [9.24. cBonusResistance](#924-cbonusresistance)
      * [9.25. cIconId](#925-ciconid)
      * [9.26. cAmountSecondStorage](#926-camountsecondstorage)
      * [9.27. cAmountThirdStorage](#927-camountthirdstorage)
      * [9.28. cFogFlag](#928-cfogflag)
      * [9.29. cOcclusionMode](#929-cocclusionmode)
      * [9.30. cGarrisonType](#930-cgarrisontype)
      * [9.31. cUnitSizeZ](#931-cunitsizez)
      * [9.32. cCanBeBuiltOn](#932-ccanbebuilton)
      * [9.33. cFoundationTerrain](#933-cfoundationterrain)
      * [9.34. cHeroStatus](#934-cherostatus)
      * [9.35. cAttackDelay](#935-cattackdelay)
      * [9.36. cTrainLocation](#936-ctrainlocation)
      * [9.37. cTrainButton](#937-ctrainbutton)
      * [9.38. cBlastAttackLevel](#938-cblastattacklevel)
      * [9.39. cBlastDefenseLevel](#939-cblastdefenselevel)
      * [9.40. cShownAttack](#940-cshownattack)
      * [9.41. cShownRange](#941-cshownrange)
      * [9.42. cShownMeleeArmor](#942-cshownmeleearmor)
      * [9.43. cShownPierceArmor](#943-cshownpiercearmor)
      * [9.44. cNameId](#944-cnameid)
      * [9.45. cDescriptionId](#945-cdescriptionid)
      * [9.46. cTerrainTable](#946-cterraintable)
      * [9.47. cTraits](#947-ctraits)
      * [9.48. cTraitPiece](#948-ctraitpiece)
      * [9.49. cDeadUnitId](#949-cdeadunitid)
      * [9.50. cHotkeyId](#950-chotkeyid)
      * [9.51. cMaxCharge](#951-cmaxcharge)
      * [9.52. cRechargeRate](#952-crechargerate)
      * [9.53. cChargeEvent](#953-cchargeevent)
      * [9.54. cChargeType](#954-cchargetype)
      * [9.55. cCombatAbility](#955-ccombatability)
      * [9.56. cAttackDispersion](#956-cattackdispersion)
      * [9.57. cSecondaryProjectileUnit](#957-csecondaryprojectileunit)
      * [9.58. cBloodUnitId](#958-cbloodunitid)
      * [9.59. cHitMode](#959-chitmode)
      * [9.60. cVanishMode](#960-cvanishmode)
      * [9.61. cProjectileArc](#961-cprojectilearc)
      * [9.62. cAttackGraphic](#962-cattackgraphic)
      * [9.63. cStandingGraphic](#963-cstandinggraphic)
      * [9.64. cStanding2Graphic](#964-cstanding2graphic)
      * [9.65. cDyingGraphic](#965-cdyinggraphic)
      * [9.66. cUndeadGraphic](#966-cundeadgraphic)
      * [9.67. cWalkingGraphic](#967-cwalkinggraphic)
      * [9.68. cRunningGraphic](#968-crunninggraphic)
      * [9.69. cSpecialGraphic](#969-cspecialgraphic)
      * [9.70. cObstructionType](#970-cobstructiontype)
      * [9.71. cBlockageClass](#971-cblockageclass)
      * [9.72. cSelectionEffect](#972-cselectioneffect)
      * [9.73. cSpecialAbility](#973-cspecialability)
      * [9.74. cIdleAttackGraphic](#974-cidleattackgraphic)
      * [9.75. cHeroGlowGraphic](#975-cheroglowgraphic)
      * [9.76. cGarrisonGraphic](#976-cgarrisongraphic)
      * [9.77. cConstructionGraphic](#977-cconstructiongraphic)
      * [9.78. cSnowGraphic](#978-csnowgraphic)
      * [9.79. cDestructionGraphic](#979-cdestructiongraphic)
      * [9.80. cDestructionRubbleGraphic](#980-cdestructionrubblegraphic)
      * [9.81. cResearchingGraphic](#981-cresearchinggraphic)
      * [9.82. cResearchCompletedGraphic](#982-cresearchcompletedgraphic)
      * [9.83. cDamageGraphic](#983-cdamagegraphic)
      * [9.84. cSelectionSound](#984-cselectionsound)
      * [9.85. cSelectionSoundEvent](#985-cselectionsoundevent)
      * [9.86. cDyingSound](#986-cdyingsound)
      * [9.87. cDyingSoundEvent](#987-cdyingsoundevent)
      * [9.88. cTrainSound](#988-ctrainsound)
      * [9.89. cTrainSoundEvent](#989-ctrainsoundevent)
      * [9.90. cDamageSound](#990-cdamagesound)
      * [9.91. cDamageSoundEvent](#991-cdamagesoundevent)
      * [9.92. cResourceCost](#992-cresourcecost)
      * [9.93. cTrainTime](#993-ctraintime)
      * [9.94. cTotalProjectiles](#994-ctotalprojectiles)
      * [9.95. cFoodCost](#995-cfoodcost)
      * [9.96. cWoodCost](#996-cwoodcost)
      * [9.97. cGoldCost](#997-cgoldcost)
      * [9.98. cStoneCost](#998-cstonecost)
      * [9.99. cMaxTotalProjectiles](#999-cmaxtotalprojectiles)
      * [9.100. cGarrisonHealRate](#9100-cgarrisonhealrate)
      * [9.101. cRegenerationRate](#9101-cregenerationrate)
      * [9.102. cPopulation](#9102-cpopulation)
      * [9.103. cMinConversionTimeMod](#9103-cminconversiontimemod)
      * [9.104. cMaxConversionTimeMod](#9104-cmaxconversiontimemod)
      * [9.105. cConversionChanceMod](#9105-cconversionchancemod)
      * [9.106. cFormationCategory](#9106-cformationcategory)
      * [9.107. cAreaDamage](#9107-careadamage)
      * [9.108. cDamageReflection](#9108-cdamagereflection)
      * [9.109. cFriendlyFireDamage](#9109-cfriendlyfiredamage)
      * [9.110. cRegenerationHpPercent](#9110-cregenerationhppercent)
      * [9.111. cButtonIconId](#9111-cbuttoniconid)
      * [9.112. cShortTooltipId](#9112-cshorttooltipid)
      * [9.113. cExtendedTooltipId](#9113-cextendedtooltipid)
      * [9.114. cHotkeyAction](#9114-chotkeyaction)
      * [9.115. cChargeProjectileUnit](#9115-cchargeprojectileunit)
      * [9.116. cAvailableFlag](#9116-cavailableflag)
      * [9.117. cDisabledFlag](#9117-cdisabledflag)
      * [9.118. cAttackPriority](#9118-cattackpriority)
      * [9.119. cInvulnerabilityLevel](#9119-cinvulnerabilitylevel)
      * [9.120. cGarrisonFirepower](#9120-cgarrisonfirepower)
      * [9.121. cAttack2Graphic](#9121-cattack2graphic)
      * [9.122. cCommandSound](#9122-ccommandsound)
      * [9.123. cCommandSoundEvent](#9123-ccommandsoundevent)
      * [9.124. cMoveSound](#9124-cmovesound)
      * [9.125. cMoveSoundEvent](#9125-cmovesoundevent)
      * [9.126. cConstructionSound](#9126-cconstructionsound)
      * [9.127. cConstructionSoundEvent](#9127-cconstructionsoundevent)
      * [9.128. cTransformSound](#9128-ctransformsound)
      * [9.129. cTransformSoundEvent](#9129-ctransformsoundevent)
      * [9.130. cRunPattern](#9130-crunpattern)
      * [9.131. cInterfaceKind](#9131-cinterfacekind)
      * [9.132. cCombatLevel](#9132-ccombatlevel)
      * [9.133. cInteractionMode](#9133-cinteractionmode)
      * [9.134. cMinimapMode](#9134-cminimapmode)
      * [9.135. cTrailingUnit](#9135-ctrailingunit)
      * [9.136. cTrailMode](#9136-ctrailmode)
      * [9.137. cTrailDensity](#9137-ctraildensity)
      * [9.138. cProjectileGraphicDisplacementX](#9138-cprojectilegraphicdisplacementx)
      * [9.139. cProjectileGraphicDisplacementY](#9139-cprojectilegraphicdisplacementy)
      * [9.140. cProjectileGraphicDisplacementZ](#9140-cprojectilegraphicdisplacementz)
      * [9.141. cProjectileSpawningAreaWidth](#9141-cprojectilespawningareawidth)
      * [9.142. cProjectileSpawningAreaLength](#9142-cprojectilespawningarealength)
      * [9.143. cProjectileSpawningAreaRandomness](#9143-cprojectilespawningarearandomness)
      * [9.144. cDamageGraphicsEntryMod](#9144-cdamagegraphicsentrymod)
      * [9.145. cDamageGraphicsTotalNum](#9145-cdamagegraphicstotalnum)
      * [9.146. cDamageGraphicPercent](#9146-cdamagegraphicpercent)
      * [9.147. cDamageGraphicApplyMode](#9147-cdamagegraphicapplymode)
    - [10. EffectAmount Object Class](#10-effectamount-object-class)

      * [10.1. cArcherClass](#101-carcherclass)
      * [10.2. cArtifactClass](#102-cartifactclass)
      * [10.3. cTradeBoatClass](#103-ctradeboatclass)
      * [10.4. cBuildingClass](#104-cbuildingclass)
      * [10.5. cVillagerClass](#105-cvillagerclass)
      * [10.6. cSeaFishClass](#106-cseafishclass)
      * [10.7. cInfantryClass](#107-cinfantryclass)
      * [10.8. cForageBushClass](#108-cforagebushclass)
      * [10.9. cStoneMineClass](#109-cstonemineclass)
      * [10.10. cPreyAnimalClass](#1010-cpreyanimalclass)
      * [10.11. cPredatorAnimalClass](#1011-cpredatoranimalclass)
      * [10.12. cMiscellaneousClass](#1012-cmiscellaneousclass)
      * [10.13. cCavalryClass](#1013-ccavalryclass)
      * [10.14. cSiegeWeaponClass](#1014-csiegeweaponclass)
      * [10.15. cTerrainClass](#1015-cterrainclass)
      * [10.16. cTreeClass](#1016-ctreeclass)
      * [10.17. cTreeStumpClass](#1017-ctreestumpclass)
      * [10.18. cHealerClass](#1018-chealerclass)
      * [10.19. cMonkClass](#1019-cmonkclass)
      * [10.20. cTradeCartClass](#1020-ctradecartclass)
      * [10.21. cTransportShipClass](#1021-ctransportshipclass)
      * [10.22. cFishingBoatClass](#1022-cfishingboatclass)
      * [10.23. cWarshipClass](#1023-cwarshipclass)
      * [10.24. cConquistadorClass](#1024-cconquistadorclass)
      * [10.25. cWarElephantClass](#1025-cwarelephantclass)
      * [10.26. cHeroClass](#1026-cheroclass)
      * [10.27. cElephantArcherClass](#1027-celephantarcherclass)
      * [10.28. cWallClass](#1028-cwallclass)
      * [10.29. cPhalanxClass](#1029-cphalanxclass)
      * [10.30. cDomesticAnimalClass](#1030-cdomesticanimalclass)
      * [10.31. cFlagClass](#1031-cflagclass)
      * [10.32. cDeepSeaFishClass](#1032-cdeepseafishclass)
      * [10.33. cGoldMine](#1033-cgoldmine)
      * [10.34. cShoreFish](#1034-cshorefish)
      * [10.35. cCliffClass](#1035-ccliffclass)
      * [10.36. cPetardClass](#1036-cpetardclass)
      * [10.37. cCavalryArcherClass](#1037-ccavalryarcherclass)
      * [10.38. cDoppelgangerClass](#1038-cdoppelgangerclass)
      * [10.39. cBirdClass](#1039-cbirdclass)
      * [10.40. cGateClass](#1040-cgateclass)
      * [10.41. cSalvagePileClass](#1041-csalvagepileclass)
      * [10.42. cResourcePileClass](#1042-cresourcepileclass)
      * [10.43. cRelicClass](#1043-crelicclass)
      * [10.44. cMonkWithRelicClass](#1044-cmonkwithrelicclass)
      * [10.45. cHandCannoneerClass](#1045-chandcannoneerclass)
      * [10.46. cTwoHandedSwordsmanClass](#1046-ctwohandedswordsmanclass)
      * [10.47. cPikemanClass](#1047-cpikemanclass)
      * [10.48. cScoutCavalryClass](#1048-cscoutcavalryclass)
      * [10.49. cOreMineClass](#1049-coremineclass)
      * [10.50. cFarmClass](#1050-cfarmclass)
      * [10.51. cSpearmanClass](#1051-cspearmanclass)
      * [10.52. cPackedUnitClass](#1052-cpackedunitclass)
      * [10.53. cTowerClass](#1053-ctowerclass)
      * [10.54. cBoardingShipClass](#1054-cboardingshipclass)
      * [10.55. cUnpackedSiegeUnitClass](#1055-cunpackedsiegeunitclass)
      * [10.56. cScorpionClass](#1056-cscorpionclass)
      * [10.57. cRaiderClass](#1057-craiderclass)
      * [10.58. cCavalryRaiderClass](#1058-ccavalryraiderclass)
      * [10.59. cLivestockClass](#1059-clivestockclass)
      * [10.60. cKingClass](#1060-ckingclass)
      * [10.61. cMiscBuildingClass](#1061-cmiscbuildingclass)
      * [10.62. cControlledAnimalClass](#1062-ccontrolledanimalclass)
      * [10.63. cGoldFishClass](#1063-cgoldfishclass)
      * [10.64. cLandMineClass](#1064-clandmineclass)
    - [11. Resource](#11-resource)

      * [11.1. cAttributeFood](#111-cattributefood)
      * [11.2. cAttributeWood](#112-cattributewood)
      * [11.3. cAttributeStone](#113-cattributestone)
      * [11.4. cAttributeGold](#114-cattributegold)
      * [11.5. cAttributePopulationCap](#115-cattributepopulationcap)
      * [11.6. cAttributeReligion](#116-cattributereligion)
      * [11.7. cAttributeCurrentAge](#117-cattributecurrentage)
      * [11.8. cAttributeRelics](#118-cattributerelics)
      * [11.9. cAttributeTrageBonus](#119-cattributetragebonus)
      * [11.10. cAttributeTradeGoods](#1110-cattributetradegoods)
      * [11.11. cAttributeTradeProducation](#1111-cattributetradeproducation)
      * [11.12. cAttributePopulation](#1112-cattributepopulation)
      * [11.13. cAttributeDecay](#1113-cattributedecay)
      * [11.14. cAttributeDiscovery](#1114-cattributediscovery)
      * [11.15. cAttributeRuins](#1115-cattributeruins)
      * [11.16. cAttributeMeat](#1116-cattributemeat)
      * [11.17. cAttributeBerries](#1117-cattributeberries)
      * [11.18. cAttributeFish](#1118-cattributefish)
      * [11.19. cAttributeKills](#1119-cattributekills)
      * [11.20. cAttributeResearchCount](#1120-cattributeresearchcount)
      * [11.21. cAttributeExploration](#1121-cattributeexploration)
      * [11.22. cAttributeConvertPriest](#1122-cattributeconvertpriest)
      * [11.23. cAttributeConvertBuilding](#1123-cattributeconvertbuilding)
      * [11.24. cAttributeBuildingLimit](#1124-cattributebuildinglimit)
      * [11.25. cAttributeFoodLimit](#1125-cattributefoodlimit)
      * [11.26. cAttributeUnitLimit](#1126-cattributeunitlimit)
      * [11.27. cAttributeMaintenance](#1127-cattributemaintenance)
      * [11.28. cAttributeFaith](#1128-cattributefaith)
      * [11.29. cAttributeFaithRechargeRate](#1129-cattributefaithrechargerate)
      * [11.30. cAttributeFarmFood](#1130-cattributefarmfood)
      * [11.31. cAttributeCivilianPopulation](#1131-cattributecivilianpopulation)
      * [11.32. cAttributeAllTechsAchieved](#1132-cattributealltechsachieved)
      * [11.33. cAttributeMilitaryPopulation](#1133-cattributemilitarypopulation)
      * [11.34. cAttributeConversions](#1134-cattributeconversions)
      * [11.35. cAttributeWonder](#1135-cattributewonder)
      * [11.36. cAttributeRazings](#1136-cattributerazings)
      * [11.37. cAttributeKillRatio](#1137-cattributekillratio)
      * [11.38. cAttributePlayerKilled](#1138-cattributeplayerkilled)
      * [11.39. cAttributeTributeInefficency](#1139-cattributetributeinefficency)
      * [11.40. cAttributeGoldBonus](#1140-cattributegoldbonus)
      * [11.41. cAttributeTownCenterUnavailable](#1141-cattributetowncenterunavailable)
      * [11.42. cAttributeGoldCounter](#1142-cattributegoldcounter)
      * [11.43. cAttributeWriting](#1143-cattributewriting)
      * [11.44. cAttributeMonasteries](#1144-cattributemonasteries)
      * [11.45. cAttributeTribute](#1145-cattributetribute)
      * [11.46. cAttributeHoldRuins](#1146-cattributeholdruins)
      * [11.47. cAttributeHoldRelics](#1147-cattributeholdrelics)
      * [11.48. cAttributeOre](#1148-cattributeore)
      * [11.49. cAttributeCapturedUnit](#1149-cattributecapturedunit)
      * [11.50. cAttributeTradeGoodQuality](#1150-cattributetradegoodquality)
      * [11.51. cAttributeTradeMarketLevel](#1151-cattributetrademarketlevel)
      * [11.52. cAttributeFormations](#1152-cattributeformations)
      * [11.53. cAttributeBuildingHouseRate](#1153-cattributebuildinghouserate)
      * [11.54. cAttributeGatherTaxRate](#1154-cattributegathertaxrate)
      * [11.55. cAttributeGatherAccumalation](#1155-cattributegatheraccumalation)
      * [11.56. cAttributeSalvageDecayRate](#1156-cattributesalvagedecayrate)
      * [11.57. cAttributeAllowFormations](#1157-cattributeallowformations)
      * [11.58. cAttributeCanConvert](#1158-cattributecanconvert)
      * [11.59. cAttributeConvertResistance](#1159-cattributeconvertresistance)
      * [11.60. cAttributeTradeVigRate](#1160-cattributetradevigrate)
      * [11.61. cAttributeStoneBonus](#1161-cattributestonebonus)
      * [11.62. cAttributeQueuedCount](#1162-cattributequeuedcount)
      * [11.63. cAttributeTrainingCount](#1163-cattributetrainingcount)
      * [11.64. cAttributeRaider](#1164-cattributeraider)
      * [11.65. cAttributeBoardingRechargeRate](#1165-cattributeboardingrechargerate)
      * [11.66. cAttributeStartingVillagers](#1166-cattributestartingvillagers)
      * [11.67. cAttributeResearchCostMod](#1167-cattributeresearchcostmod)
      * [11.68. cAttributeResearchTimeMod](#1168-cattributeresearchtimemod)
      * [11.69. cAttributeConvertBoats](#1169-cattributeconvertboats)
      * [11.70. cAttributeFishTrapFood](#1170-cattributefishtrapfood)
      * [11.71. cAttributeHealRateModifer](#1171-cattributehealratemodifer)
      * [11.72. cAttributeHealRange](#1172-cattributehealrange)
      * [11.73. cAttributeStartingFood](#1173-cattributestartingfood)
      * [11.74. cAttributeStartingWood](#1174-cattributestartingwood)
      * [11.75. cAttributeStartingStone](#1175-cattributestartingstone)
      * [11.76. cAttributeStartingGold](#1176-cattributestartinggold)
      * [11.77. cAttributeRaiderAbility](#1177-cattributeraiderability)
      * [11.78. cAttributeNoDropsiteFarmers](#1178-cattributenodropsitefarmers)
      * [11.79. cAttributeDominantSheepControl](#1179-cattributedominantsheepcontrol)
      * [11.80. cAttributeObjectCostSummation](#1180-cattributeobjectcostsummation)
      * [11.81. cAttributeResearchCostSummation](#1181-cattributeresearchcostsummation)
      * [11.82. cAttributeRelicIncomeSummation](#1182-cattributerelicincomesummation)
      * [11.83. cAttributeTradeIncomeSummation](#1183-cattributetradeincomesummation)
      * [11.84. cAttributeCastle](#1184-cattributecastle)
      * [11.85. cAttributeHitPointRazings](#1185-cattributehitpointrazings)
      * [11.86. cAttributeValueKilledByOthers](#1186-cattributevaluekilledbyothers)
      * [11.87. cAttributeValueRazedByOthers](#1187-cattributevaluerazedbyothers)
      * [11.88. cAttributeKilledByOthers](#1188-cattributekilledbyothers)
      * [11.89. cAttributeRazedByOthers](#1189-cattributerazedbyothers)
      * [11.90. cAttributeValueCurrentUnits](#1190-cattributevaluecurrentunits)
      * [11.91. cAttributeValueCurrentBuildings](#1191-cattributevaluecurrentbuildings)
      * [11.92. cAttributeFoodTotal](#1192-cattributefoodtotal)
      * [11.93. cAttributeWoodTotal](#1193-cattributewoodtotal)
      * [11.94. cAttributeStoneTotal](#1194-cattributestonetotal)
      * [11.95. cAttributeGoldTotal](#1195-cattributegoldtotal)
      * [11.96. cAttributeTotalValueOfKills](#1196-cattributetotalvalueofkills)
      * [11.97. cAttributeTotalTributeReceived](#1197-cattributetotaltributereceived)
      * [11.98. cAttributeTotalValueOfRazings](#1198-cattributetotalvalueofrazings)
      * [11.99. cAttributeTotalCastlesBuilt](#1199-cattributetotalcastlesbuilt)
      * [11.100. cAttributeTotalWondersBuilt](#11100-cattributetotalwondersbuilt)
      * [11.101. cAttributeTributeScore](#11101-cattributetributescore)
      * [11.102. cAttributeConvertMinAdj](#11102-cattributeconvertminadj)
      * [11.103. cAttributeConvertMaxAdj](#11103-cattributeconvertmaxadj)
      * [11.104. cAttributeConvertResistMinAdj](#11104-cattributeconvertresistminadj)
      * [11.105. cAttributeConvertResistMaxAdj](#11105-cattributeconvertresistmaxadj)
      * [11.106. cAttributeConvertBuildingMin](#11106-cattributeconvertbuildingmin)
      * [11.107. cAttributeConvertBuildingMax](#11107-cattributeconvertbuildingmax)
      * [11.108. cAttributeConvertBuildingChance](#11108-cattributeconvertbuildingchance)
      * [11.109. cAttributeSpies](#11109-cattributespies)
      * [11.110. cAttributeValueWondersCastles](#11110-cattributevaluewonderscastles)
      * [11.111. cAttributeFoodScore](#11111-cattributefoodscore)
      * [11.112. cAttributeWoodScore](#11112-cattributewoodscore)
      * [11.113. cAttributeStoneScore](#11113-cattributestonescore)
      * [11.114. cAttributeGoldScore](#11114-cattributegoldscore)
      * [11.115. cAttributeWoodBonus](#11115-cattributewoodbonus)
      * [11.116. cAttributeFoodBonus](#11116-cattributefoodbonus)
      * [11.117. cAttributeRelicRate](#11117-cattributerelicrate)
      * [11.118. cAttributeHeresy](#11118-cattributeheresy)
      * [11.119. cAttributeTheocracy](#11119-cattributetheocracy)
      * [11.120. cAttributeCrenellations](#11120-cattributecrenellations)
      * [11.121. cAttributeConstructionRateMod](#11121-cattributeconstructionratemod)
      * [11.122. cAttributeHunWonderBonus](#11122-cattributehunwonderbonus)
      * [11.123. cAttributeSpiesDiscount](#11123-cattributespiesdiscount)
      * [11.124. cAttributeTemporaryMapReveal](#11124-cattributetemporarymapreveal)
      * [11.125. cAttributeRevealInitialType](#11125-cattributerevealinitialtype)
      * [11.126. cAttributeElevationBonusHigher](#11126-cattributeelevationbonushigher)
      * [11.127. cAttributeElevationBonusLower](#11127-cattributeelevationbonuslower)
      * [11.128. cAttributeTriggerSharedLOS](#11128-cattributetriggersharedlos)
      * [11.129. cAttributeFeudalTownCenterLimit](#11129-cattributefeudaltowncenterlimit)
      * [11.130. cAttributeFishingProductivity](#11130-cattributefishingproductivity)
      * [11.131. cAttributeUnused220](#11131-cattributeunused220)
      * [11.132. cAttributeMonumentFoodTrickle](#11132-cattributemonumentfoodtrickle)
      * [11.133. cAttributeMonumentWoodTrickle](#11133-cattributemonumentwoodtrickle)
      * [11.134. cAttributeMonumentStoneTrickle](#11134-cattributemonumentstonetrickle)
      * [11.135. cAttributeMonumentGoldTrickle](#11135-cattributemonumentgoldtrickle)
      * [11.136. cAttributeRelicFoodRate](#11136-cattributerelicfoodrate)
      * [11.137. cAttributeVillagersKilledByGaia](#11137-cattributevillagerskilledbygaia)
      * [11.138. cAttributeVillgaersKilledByAnimal](#11138-cattributevillgaerskilledbyanimal)
      * [11.139. cAttributeVillagersKilledByAIPlayer](#11139-cattributevillagerskilledbyaiplayer)
      * [11.140. cAttributeVillagersKilledByHumanPlayer](#11140-cattributevillagerskilledbyhumanplayer)
      * [11.141. cAttributeFoodGeneration](#11141-cattributefoodgeneration)
      * [11.142. cAttributeWoodGeneration](#11142-cattributewoodgeneration)
      * [11.143. cAttributeStoneGeneration](#11143-cattributestonegeneration)
      * [11.144. cAttributeGoldGeneration](#11144-cattributegoldgeneration)
      * [11.145. cAttributeSpawnCap](#11145-cattributespawncap)
      * [11.146. cAttributeFlemishMilitiaPop](#11146-cattributeflemishmilitiapop)
      * [11.147. cAttributeGoldFarmingProductivity](#11147-cattributegoldfarmingproductivity)
      * [11.148. cAttributeFolwarkCollectionAmount](#11148-cattributefolwarkcollectionamount)
      * [11.149. cAttributeFolwarkCollectionType](#11149-cattributefolwarkcollectiontype)
      * [11.150. cAttributeBuildingId](#11150-cattributebuildingid)
      * [11.151. cAttributeUnitsConverted](#11151-cattributeunitsconverted)
      * [11.152. cAttributeStoneGoldMiningProductivity](#11152-cattributestonegoldminingproductivity)
      * [11.153. cAttributeWorkshopFoodTrickle](#11153-cattributeworkshopfoodtrickle)
      * [11.154. cAttributeWorkshopWoodTrickle](#11154-cattributeworkshopwoodtrickle)
      * [11.155. cAttributeWorkshopStoneTrickle](#11155-cattributeworkshopstonetrickle)
      * [11.156. cAttributeWorkshopGoldTrickle](#11156-cattributeworkshopgoldtrickle)
      * [11.157. cAttributeUnitsValueTotal](#11157-cattributeunitsvaluetotal)
      * [11.158. cAttributeBuildingsValueTotal](#11158-cattributebuildingsvaluetotal)
      * [11.159. cAttributeVillagersCreatedTotal](#11159-cattributevillagerscreatedtotal)
      * [11.160. cAttributeVillagersIdlePeriodsTotal](#11160-cattributevillagersidleperiodstotal)
      * [11.161. cAttributeVillagersIdleSecondsTotal](#11161-cattributevillagersidlesecondstotal)
      * [11.162. cAttributeTradeFoodPercent](#11162-cattributetradefoodpercent)
      * [11.163. cAttributeTradeWoodPercent](#11163-cattributetradewoodpercent)
      * [11.164. cAttributeTradeStonePercent](#11164-cattributetradestonepercent)
      * [11.165. cAttributeLivestockFoodProductivity](#11165-cattributelivestockfoodproductivity)
      * [11.166. cAttributeSpeedUpBuildingType](#11166-cattributespeedupbuildingtype)
      * [11.167. cAttributeSpeedUpBuildingRange](#11167-cattributespeedupbuildingrange)
      * [11.168. cAttributeSpeedUpPercentage](#11168-cattributespeeduppercentage)
      * [11.169. cAttributeSpeedUpObjectType](#11169-cattributespeedupobjecttype)
      * [11.170. cAttributeSpeedUpEffectType](#11170-cattributespeedupeffecttype)
      * [11.171. cAttributeSpeedUpSecondaryEffectType](#11171-cattributespeedupsecondaryeffecttype)
      * [11.172. cAttributeSpeedUpSecondaryPercentage](#11172-cattributespeedupsecondarypercentage)
      * [11.173. cAttributeCivNameOverride](#11173-cattributecivnameoverride)
      * [11.174. cAttributeStartingScoutID](#11174-cattributestartingscoutid)
      * [11.175. cAttributeRelicWoodRate](#11175-cattributerelicwoodrate)
      * [11.176. cAttributeRelicStoneRate](#11176-cattributerelicstonerate)
      * [11.177. cAttributeChoppingGoldProductivity](#11177-cattributechoppinggoldproductivity)
      * [11.178. cAttributeForagingWoodProductivity](#11178-cattributeforagingwoodproductivity)
      * [11.179. cAttributeHuntingProductivity](#11179-cattributehuntingproductivity)
      * [11.180. cAttributeTechnologyRewardEffect](#11180-cattributetechnologyrewardeffect)
      * [11.181. cAttributeUnitRepairCost](#11181-cattributeunitrepaircost)
      * [11.182. cAttributeBuildingRepairCost](#11182-cattributebuildingrepaircost)
      * [11.183. cAttributeElevationDamageHigher](#11183-cattributeelevationdamagehigher)
      * [11.184. cAttributeElevationDamageLower](#11184-cattributeelevationdamagelower)
      * [11.185. cAttributeInfantryKillReward](#11185-cattributeinfantrykillreward)
      * [11.186. cAttributeMilitaryCanConvert](#11186-cattributemilitarycanconvert)
      * [11.187. cAttributeMilitaryConversionRangeAdj](#11187-cattributemilitaryconversionrangeadj)
      * [11.188. cAttributeMilitaryConversionChance](#11188-cattributemilitaryconversionchance)
      * [11.189. cAttributeMilitaryConversionRechargeRate](#11189-cattributemilitaryconversionrechargerate)
      * [11.190. cAttributeSpawnStayInside](#11190-cattributespawnstayinside)
      * [11.191. cAttributeCavalryKillReward](#11191-cattributecavalrykillreward)
      * [11.192. cAttributeTriggerSharedVisibility](#11192-cattributetriggersharedvisibility)
      * [11.193. cAttributeTriggerSharedExploration](#11193-cattributetriggersharedexploration)
      * [11.194. cAttributeMilitaryFoodTrickle](#11194-cattributemilitaryfoodtrickle)
      * [11.195. cAttributePastureFoodAmount](#11195-cattributepasturefoodamount)
      * [11.196. cAttributePastureAnimalCount](#11196-cattributepastureanimalcount)
      * [11.197. cAttributePastureHerderCount](#11197-cattributepastureherdercount)
      * [11.198. cAttributeDisableAnimalDecay](#11198-cattributedisableanimaldecay)
      * [11.199. cAttributeHerdingFoodProductivity](#11199-cattributeherdingfoodproductivity)
      * [11.200. cAttributeShepherdingFoodProductivity](#11200-cattributeshepherdingfoodproductivity)
      * [11.201. cAttributeGaiaKills](#11201-cattributegaiakills)
      * [11.202. cAttributePlayer1Kills](#11202-cattributeplayer1kills)
      * [11.203. cAttributePlayer2Kills](#11203-cattributeplayer2kills)
      * [11.204. cAttributePlayer3Kills](#11204-cattributeplayer3kills)
      * [11.205. cAttributePlayer4Kills](#11205-cattributeplayer4kills)
      * [11.206. cAttributePlayer5Kills](#11206-cattributeplayer5kills)
      * [11.207. cAttributePlayer6Kills](#11207-cattributeplayer6kills)
      * [11.208. cAttributePlayer7Kills](#11208-cattributeplayer7kills)
      * [11.209. cAttributePlayer8Kills](#11209-cattributeplayer8kills)
      * [11.210. cAttributeKillsByGaia](#11210-cattributekillsbygaia)
      * [11.211. cAttributeKillsByPlayer1](#11211-cattributekillsbyplayer1)
      * [11.212. cAttributeKillsByPlayer2](#11212-cattributekillsbyplayer2)
      * [11.213. cAttributeKillsByPlayer3](#11213-cattributekillsbyplayer3)
      * [11.214. cAttributeKillsByPlayer4](#11214-cattributekillsbyplayer4)
      * [11.215. cAttributeKillsByPlayer5](#11215-cattributekillsbyplayer5)
      * [11.216. cAttributeKillsByPlayer6](#11216-cattributekillsbyplayer6)
      * [11.217. cAttributeKillsByPlayer7](#11217-cattributekillsbyplayer7)
      * [11.218. cAttributeKillsByPlayer8](#11218-cattributekillsbyplayer8)
      * [11.219. cAttributeGaiaRazings](#11219-cattributegaiarazings)
      * [11.220. cAttributePlayer1Razings](#11220-cattributeplayer1razings)
      * [11.221. cAttributePlayer2Razings](#11221-cattributeplayer2razings)
      * [11.222. cAttributePlayer3Razings](#11222-cattributeplayer3razings)
      * [11.223. cAttributePlayer4Razings](#11223-cattributeplayer4razings)
      * [11.224. cAttributePlayer5Razings](#11224-cattributeplayer5razings)
      * [11.225. cAttributePlayer6Razings](#11225-cattributeplayer6razings)
      * [11.226. cAttributePlayer7Razings](#11226-cattributeplayer7razings)
      * [11.227. cAttributePlayer8Razings](#11227-cattributeplayer8razings)
      * [11.228. cAttributeRazingsByGaia](#11228-cattributerazingsbygaia)
      * [11.229. cAttributeRazingsByPlayer1](#11229-cattributerazingsbyplayer1)
      * [11.230. cAttributeRazingsByPlayer2](#11230-cattributerazingsbyplayer2)
      * [11.231. cAttributeRazingsByPlayer3](#11231-cattributerazingsbyplayer3)
      * [11.232. cAttributeRazingsByPlayer4](#11232-cattributerazingsbyplayer4)
      * [11.233. cAttributeRazingsByPlayer5](#11233-cattributerazingsbyplayer5)
      * [11.234. cAttributeRazingsByPlayer6](#11234-cattributerazingsbyplayer6)
      * [11.235. cAttributeRazingsByPlayer7](#11235-cattributerazingsbyplayer7)
      * [11.236. cAttributeRazingsByPlayer8](#11236-cattributerazingsbyplayer8)
      * [11.237. cAttributeGaiaKillValue](#11237-cattributegaiakillvalue)
      * [11.238. cAttributePlayer1KillValue](#11238-cattributeplayer1killvalue)
      * [11.239. cAttributePlayer2KillValue](#11239-cattributeplayer2killvalue)
      * [11.240. cAttributePlayer3KillValue](#11240-cattributeplayer3killvalue)
      * [11.241. cAttributePlayer4KillValue](#11241-cattributeplayer4killvalue)
      * [11.242. cAttributePlayer5KillValue](#11242-cattributeplayer5killvalue)
      * [11.243. cAttributePlayer6KillValue](#11243-cattributeplayer6killvalue)
      * [11.244. cAttributePlayer7KillValue](#11244-cattributeplayer7killvalue)
      * [11.245. cAttributePlayer8KillValue](#11245-cattributeplayer8killvalue)
      * [11.246. cAttributeGaiaRazingValue](#11246-cattributegaiarazingvalue)
      * [11.247. cAttributePlayer1RazingValue](#11247-cattributeplayer1razingvalue)
      * [11.248. cAttributePlayer2RazingValue](#11248-cattributeplayer2razingvalue)
      * [11.249. cAttributePlayer3RazingValue](#11249-cattributeplayer3razingvalue)
      * [11.250. cAttributePlayer4RazingValue](#11250-cattributeplayer4razingvalue)
      * [11.251. cAttributePlayer5RazingValue](#11251-cattributeplayer5razingvalue)
      * [11.252. cAttributePlayer6RazingValue](#11252-cattributeplayer6razingvalue)
      * [11.253. cAttributePlayer7RazingValue](#11253-cattributeplayer7razingvalue)
      * [11.254. cAttributePlayer8RazingValue](#11254-cattributeplayer8razingvalue)
      * [11.255. cAttributeGaiaTribute](#11255-cattributegaiatribute)
      * [11.256. cAttributePlayer1Tribute](#11256-cattributeplayer1tribute)
      * [11.257. cAttributePlayer2Tribute](#11257-cattributeplayer2tribute)
      * [11.258. cAttributePlayer3Tribute](#11258-cattributeplayer3tribute)
      * [11.259. cAttributePlayer4Tribute](#11259-cattributeplayer4tribute)
      * [11.260. cAttributePlayer5Tribute](#11260-cattributeplayer5tribute)
      * [11.261. cAttributePlayer6Tribute](#11261-cattributeplayer6tribute)
      * [11.262. cAttributePlayer7Tribute](#11262-cattributeplayer7tribute)
      * [11.263. cAttributePlayer8Tribute](#11263-cattributeplayer8tribute)
      * [11.264. cAttributeTributeFromGaia](#11264-cattributetributefromgaia)
      * [11.265. cAttributeTributeFromPlayer1](#11265-cattributetributefromplayer1)
      * [11.266. cAttributeTributeFromPlayer2](#11266-cattributetributefromplayer2)
      * [11.267. cAttributeTributeFromPlayer3](#11267-cattributetributefromplayer3)
      * [11.268. cAttributeTributeFromPlayer4](#11268-cattributetributefromplayer4)
      * [11.269. cAttributeTributeFromPlayer5](#11269-cattributetributefromplayer5)
      * [11.270. cAttributeTributeFromPlayer6](#11270-cattributetributefromplayer6)
      * [11.271. cAttributeTributeFromPlayer7](#11271-cattributetributefromplayer7)
      * [11.272. cAttributeTributeFromPlayer8](#11272-cattributetributefromplayer8)
      * [11.273. cAttributeChoppingFoodProductivity](#11273-cattributechoppingfoodproductivity)
    - [12. Damage Class](#12-damage-class)

      * [12.1. cDamageClassInfantry](#121-cdamageclassinfantry)
      * [12.2. cDamageClassCapitalShips](#122-cdamageclasscapitalships)
      * [12.3. cDamageClassPierce](#123-cdamageclasspierce)
      * [12.4. cDamageClassMelee](#124-cdamageclassmelee)
      * [12.5. cDamageClassElephantUnits](#125-cdamageclasselephantunits)
      * [12.6. cDamageClassCavalry](#126-cdamageclasscavalry)
      * [12.7. cDamageClassAllBuildings](#127-cdamageclassallbuildings)
      * [12.8. cDamageClassStoneDefense](#128-cdamageclassstonedefense)
      * [12.9. cDamageClassPredatorAnimals](#129-cdamageclasspredatoranimals)
      * [12.10. cDamageClassArchers](#1210-cdamageclassarchers)
      * [12.11. cDamageClassShips](#1211-cdamageclassships)
      * [12.12. cDamageClassRams](#1212-cdamageclassrams)
      * [12.13. cDamageClassTrees](#1213-cdamageclasstrees)
      * [12.14. cDamageClassUniqueUnits](#1214-cdamageclassuniqueunits)
      * [12.15. cDamageClassSiegeWeapons](#1215-cdamageclasssiegeweapons)
      * [12.16. cDamageClassStandardBuildings](#1216-cdamageclassstandardbuildings)
      * [12.17. cDamageClassWallsAndGates](#1217-cdamageclasswallsandgates)
      * [12.18. cDamageClassGunpowderUnits](#1218-cdamageclassgunpowderunits)
      * [12.19. cDamageClassBoars](#1219-cdamageclassboars)
      * [12.20. cDamageClassMonks](#1220-cdamageclassmonks)
      * [12.21. cDamageClassCastles](#1221-cdamageclasscastles)
      * [12.22. cDamageClassSpearmen](#1222-cdamageclassspearmen)
      * [12.23. cDamageClassCavalryArchers](#1223-cdamageclasscavalryarchers)
      * [12.24. cDamageClassShockInfantry](#1224-cdamageclassshockinfantry)
      * [12.25. cDamageClassCamelUnits](#1225-cdamageclasscamelunits)
      * [12.26. cDamageClassCondottieri](#1226-cdamageclasscondottieri)
      * [12.27. cDamageClassFishingShips](#1227-cdamageclassfishingships)
      * [12.28. cDamageClassMamelukes](#1228-cdamageclassmamelukes)
      * [12.29. cDamageClassHeroesAndKings](#1229-cdamageclassheroesandkings)
      * [12.30. cDamageClassHeavySiege](#1230-cdamageclassheavysiege)
      * [12.31. cDamageClassSkirmishers](#1231-cdamageclassskirmishers)
      * [12.32. cDamageClassRoyalHeirs](#1232-cdamageclassroyalheirs)
    - [13. Task Attribute](#13-task-attribute)

      * [13.1. cTaskAttrWorkValue1](#131-ctaskattrworkvalue1)
      * [13.2. cTaskAttrWorkValue2](#132-ctaskattrworkvalue2)
      * [13.3. cTaskAttrWorkRange](#133-ctaskattrworkrange)
      * [13.4. cTaskAttrWorkFlag2](#134-ctaskattrworkflag2)
      * [13.5. cTaskAttrSearchWaitTime](#135-ctaskattrsearchwaittime)
      * [13.6. cTaskAttrCombatLevelFlag](#136-ctaskattrcombatlevelflag)
      * [13.7. cTaskAttrOwnerType](#137-ctaskattrownertype)
      * [13.8. cTaskAttrTerrain](#138-ctaskattrterrain)
      * [13.9. cTaskAttrResourceIn](#139-ctaskattrresourcein)
      * [13.10. cTaskAttrProductivityResource](#1310-ctaskattrproductivityresource)
      * [13.11. cTaskAttrResourceOut](#1311-ctaskattrresourceout)
      * [13.12. cTaskAttrUnusedResource](#1312-ctaskattrunusedresource)
      * [13.13. cTaskAttrMovingGraphic](#1313-ctaskattrmovinggraphic)
      * [13.14. cTaskAttrProceedingGraphic](#1314-ctaskattrproceedinggraphic)
      * [13.15. cTaskAttrWorkingGraphic](#1315-ctaskattrworkinggraphic)
      * [13.16. cTaskAttrCarryingGraphic](#1316-ctaskattrcarryinggraphic)
      * [13.17. cTaskAttrGatheringSound](#1317-ctaskattrgatheringsound)
      * [13.18. cTaskAttrGatheringSoundEvent](#1318-ctaskattrgatheringsoundevent)
      * [13.19. cTaskAttrGatheringSoundInt32](#1319-ctaskattrgatheringsoundint32)
      * [13.20. cTaskAttrDepositSound](#1320-ctaskattrdepositsound)
      * [13.21. cTaskAttrDepositSoundEvent](#1321-ctaskattrdepositsoundevent)
      * [13.22. cTaskAttrDepositSoundInt32](#1322-ctaskattrdepositsoundint32)
      * [13.23. cTaskAttrAutoSearch](#1323-ctaskattrautosearch)
      * [13.24. cTaskAttrCarryCheck](#1324-ctaskattrcarrycheck)
      * [13.25. cTaskAttrBuildingPick](#1325-ctaskattrbuildingpick)
      * [13.26. cTaskAttrGatherType](#1326-ctaskattrgathertype)
      * [13.27. cTaskAttrEnableTargeting](#1327-ctaskattrenabletargeting)
      * [13.28. cTaskAttrEnabled](#1328-ctaskattrenabled)
    - [14. Task Type](#14-task-type)

      * [14.1. cTaskTypeMoveTo](#141-ctasktypemoveto)
      * [14.2. cTaskTypeFollow](#142-ctasktypefollow)
      * [14.3. cTaskTypeGarrison](#143-ctasktypegarrison)
      * [14.4. cTaskTypeExplore](#144-ctasktypeexplore)
      * [14.5. cTaskTypeGatherRebuild](#145-ctasktypegatherrebuild)
      * [14.6. cTaskTypeGraze](#146-ctasktypegraze)
      * [14.7. cTaskTypeCombat](#147-ctasktypecombat)
      * [14.8. cTaskTypeShoot](#148-ctasktypeshoot)
      * [14.9. cTaskTypeAttack](#149-ctasktypeattack)
      * [14.10. cTaskTypeFly](#1410-ctasktypefly)
      * [14.11. cTaskTypeUnloadBoatLike](#1411-ctasktypeunloadboatlike)
      * [14.12. cTaskTypeGuard](#1412-ctasktypeguard)
      * [14.13. cTaskTypeUnloadOverWall](#1413-ctasktypeunloadoverwall)
      * [14.14. cTaskTypeMake](#1414-ctasktypemake)
      * [14.15. cTaskTypeBuild](#1415-ctasktypebuild)
      * [14.16. cTaskTypeMakeUnit](#1416-ctasktypemakeunit)
      * [14.17. cTaskTypeMakeTech](#1417-ctasktypemaketech)
      * [14.18. cTaskTypeConvert](#1418-ctasktypeconvert)
      * [14.19. cTaskTypeHeal](#1419-ctasktypeheal)
      * [14.20. cTaskTypeRepair](#1420-ctasktyperepair)
      * [14.21. cTaskTypeGetAutoConverted](#1421-ctasktypegetautoconverted)
      * [14.22. cTaskTypeDiscoveryArtifact](#1422-ctasktypediscoveryartifact)
      * [14.23. cTaskTypeHunt](#1423-ctasktypehunt)
      * [14.24. cTaskTypeTrade](#1424-ctasktypetrade)
      * [14.25. cTaskTypeGenerateWonderVictory](#1425-ctasktypegeneratewondervictory)
      * [14.26. cTaskTypeDeselectWhenTasked](#1426-ctasktypedeselectwhentasked)
      * [14.27. cTaskTypeLootGather](#1427-ctasktypelootgather)
      * [14.28. cTaskTypeHousing](#1428-ctasktypehousing)
      * [14.29. cTaskTypePack](#1429-ctasktypepack)
      * [14.30. cTaskTypeUnpackAndAttack](#1430-ctasktypeunpackandattack)
      * [14.31. cTaskTypeOffMapTrade](#1431-ctasktypeoffmaptrade)
      * [14.32. cTaskTypePickupUnit](#1432-ctasktypepickupunit)
      * [14.33. cTaskTypeChargeAttack](#1433-ctasktypechargeattack)
      * [14.34. cTaskTypeTransformUnit](#1434-ctasktypetransformunit)
      * [14.35. cTaskTypeKidnapUnit](#1435-ctasktypekidnapunit)
      * [14.36. cTaskTypeDepositUnit](#1436-ctasktypedepositunit)
      * [14.37. cTaskTypeShear](#1437-ctasktypeshear)
      * [14.38. cTaskTypeGenerateResources](#1438-ctasktypegenerateresources)
      * [14.39. cTaskTypeMovementDamage](#1439-ctasktypemovementdamage)
      * [14.40. cTaskTypeMovableDropsite](#1440-ctasktypemovabledropsite)
      * [14.41. cTaskTypeLoot](#1441-ctasktypeloot)
      * [14.42. cTaskTypeAura](#1442-ctasktypeaura)
      * [14.43. cTaskTypeExtraSpawn](#1443-ctasktypeextraspawn)
      * [14.44. cTaskTypeStinger](#1444-ctasktypestinger)
      * [14.45. cTaskTypeHPTransform](#1445-ctasktypehptransform)
      * [14.46. cTaskTypeHPModifier](#1446-ctasktypehpmodifier)
    - [15. Tech State](#15-tech-state)

      * [15.1. cTechStateNotReady](#151-ctechstatenotready)
      * [15.2. cTechStateReady](#152-ctechstateready)
      * [15.3. cTechStateQueued](#153-ctechstatequeued)
      * [15.4. cTechStateResearching](#154-ctechstateresearching)
      * [15.5. cTechStateDone](#155-ctechstatedone)
      * [15.6. cTechStateDisabled](#156-ctechstatedisabled)
      * [15.7. cTechStateInvalid](#157-ctechstateinvalid)
    - [16. Object Type](#16-object-type)

      * [16.1. cObjectTypeEyeCandy](#161-cobjecttypeeyecandy)
      * [16.2. cObjectTypeTrees](#162-cobjecttypetrees)
      * [16.3. cObjectTypeAnimated](#163-cobjecttypeanimated)
      * [16.4. cObjectTypeDoppleganger](#164-cobjecttypedoppleganger)
      * [16.5. cObjectTypeMoving](#165-cobjecttypemoving)
      * [16.6. cObjectTypeActing](#166-cobjecttypeacting)
      * [16.7. cObjectTypeCombat](#167-cobjecttypecombat)
      * [16.8. cObjectTypeProjectile](#168-cobjecttypeprojectile)
      * [16.9. cObjectTypeCreatable](#169-cobjecttypecreatable)
      * [16.10. cObjectTypeBuilding](#1610-cobjecttypebuilding)
      * [16.11. cObjectTypeLegacyTree](#1611-cobjecttypelegacytree)
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

* [1. Read/Write](#1-readwrite)

  + [1.1. cOffsetString](#11-coffsetstring)
  + [1.2. cOffsetInteger](#12-coffsetinteger)
  + [1.3. cOffsetFloat](#13-coffsetfloat)
  + [1.4. cOffsetVector](#14-coffsetvector)
* [2. Age](#2-age)

  + [2.1. cDarkAge](#21-cdarkage)
  + [2.2. cFeudalAge](#22-cfeudalage)
  + [2.3. cCastleAge](#23-ccastleage)
  + [2.4. cImperialAge](#24-cimperialage)
  + [2.5. cStoneAge](#25-cstoneage)
  + [2.6. cToolAge](#26-ctoolage)
  + [2.7. cBronzeAge](#27-cbronzeage)
  + [2.8. cIronAge](#28-cironage)
* [3. Value](#3-value)

  + [3.1. cActivationTime](#31-cactivationtime)
  + [3.2. cOriginVector](#32-coriginvector)
  + [3.3. cInvalidVector](#33-cinvalidvector)
* [4. Victory Conditions](#4-victory-conditions)

  + [4.1. cStandardVictory](#41-cstandardvictory)
  + [4.2. cWonderVictory](#42-cwondervictory)
  + [4.3. cRelicVictory](#43-crelicvictory)
  + [4.4. cKingOfTheHillVictory](#44-ckingofthehillvictory)
* [5. Civilization](#5-civilization)

  + [5.1. cGaia](#51-cgaia)
  + [5.2. cBritons](#52-cbritons)
  + [5.3. cFranks](#53-cfranks)
  + [5.4. cGoths](#54-cgoths)
  + [5.5. cTeutons](#55-cteutons)
  + [5.6. cJapanese](#56-cjapanese)
  + [5.7. cChinese](#57-cchinese)
  + [5.8. cByzantines](#58-cbyzantines)
  + [5.9. cPersians](#59-cpersians)
  + [5.10. cSaracens](#510-csaracens)
  + [5.11. cTurks](#511-cturks)
  + [5.12. cVikings](#512-cvikings)
  + [5.13. cMongols](#513-cmongols)
  + [5.14. cCelts](#514-ccelts)
  + [5.15. cSpanish](#515-cspanish)
  + [5.16. cAztecs](#516-caztecs)
  + [5.17. cMayans](#517-cmayans)
  + [5.18. cHuns](#518-chuns)
  + [5.19. cKoreans](#519-ckoreans)
  + [5.20. cItalians](#520-citalians)
  + [5.21. cIndians](#521-cindians)
  + [5.22. cIncas](#522-cincas)
  + [5.23. cMagyars](#523-cmagyars)
  + [5.24. cSlavs](#524-cslavs)
  + [5.25. cPortuguese](#525-cportuguese)
  + [5.26. cEthiopians](#526-cethiopians)
  + [5.27. cMalians](#527-cmalians)
  + [5.28. cBerbers](#528-cberbers)
  + [5.29. cKhmer](#529-ckhmer)
  + [5.30. cMalay](#530-cmalay)
  + [5.31. cBurmese](#531-cburmese)
  + [5.32. cVietnamese](#532-cvietnamese)
  + [5.33. cBulgarians](#533-cbulgarians)
  + [5.34. cTatars](#534-ctatars)
  + [5.35. cCumans](#535-ccumans)
  + [5.36. cLithuanians](#536-clithuanians)
  + [5.37. cBurgundians](#537-cburgundians)
  + [5.38. cSicilians](#538-csicilians)
  + [5.39. cPoles](#539-cpoles)
  + [5.40. cBohemians](#540-cbohemians)
  + [5.41. cDravidians](#541-cdravidians)
  + [5.42. cBengalis](#542-cbengalis)
  + [5.43. cGurjaras](#543-cgurjaras)
  + [5.44. cRomans](#544-cromans)
  + [5.45. cArmenians](#545-carmenians)
  + [5.46. cGeorgians](#546-cgeorgians)
  + [5.47. cAchaemenids](#547-cachaemenids)
  + [5.48. cAthenians](#548-cathenians)
  + [5.49. cSpartans](#549-cspartans)
  + [5.50. cShu](#550-cshu)
  + [5.51. cWu](#551-cwu)
  + [5.52. cWei](#552-cwei)
  + [5.53. cJurchens](#553-cjurchens)
  + [5.54. cKhitans](#554-ckhitans)
  + [5.55. cAoeEgyptians](#555-caoeegyptians)
  + [5.56. cAoeGreeks](#556-caoegreeks)
  + [5.57. cAoeBabylonians](#557-caoebabylonians)
  + [5.58. cAoeAssyrians](#558-caoeassyrians)
  + [5.59. cAoeMinoans](#559-caoeminoans)
  + [5.60. cAoeHittites](#560-caoehittites)
  + [5.61. cAoePhoenicians](#561-caoephoenicians)
  + [5.62. cAoeSumerians](#562-caoesumerians)
  + [5.63. cAoePersians](#563-caoepersians)
  + [5.64. cAoeShang](#564-caoeshang)
  + [5.65. cAoeYamato](#565-caoeyamato)
  + [5.66. cAoeChoson](#566-caoechoson)
  + [5.67. cAoeRomans](#567-caoeromans)
  + [5.68. cAoeCarthaginians](#568-caoecarthaginians)
  + [5.69. cAoePalmyrans](#569-caoepalmyrans)
  + [5.70. cAoeMacedonians](#570-caoemacedonians)
  + [5.71. cAoeLacViet](#571-caoelacviet)
* [6. EffectAmount Effect Type](#6-effectamount-effect-type)

  + [6.1. cSetAttribute](#61-csetattribute)
  + [6.2. cModResource](#62-cmodresource)
  + [6.3. cEnableObject](#63-cenableobject)
  + [6.4. cUpgradeUnit](#64-cupgradeunit)
  + [6.5. cAddAttribute](#65-caddattribute)
  + [6.6. cMulAttribute](#66-cmulattribute)
  + [6.7. cMulResource](#67-cmulresource)
  + [6.8. cSpawnUnit](#68-cspawnunit)
  + [6.9. cModifyTech](#69-cmodifytech)
  + [6.10. cSetPlayerData](#610-csetplayerdata)
  + [6.11. cSetTechCost](#611-csettechcost)
  + [6.12. cAddTechCost](#612-caddtechcost)
  + [6.13. cDisableTech](#613-cdisabletech)
  + [6.14. cModTechTime](#614-cmodtechtime)
  + [6.15. cGaiaSetAttribute](#615-cgaiasetattribute)
  + [6.16. cGaiaModResource](#616-cgaiamodresource)
  + [6.17. cGaiaEnableObject](#617-cgaiaenableobject)
  + [6.18. cGaiaUpgradeUnit](#618-cgaiaupgradeunit)
  + [6.19. cGaiaAddAttribute](#619-cgaiaaddattribute)
  + [6.20. cGaiaMulAttribute](#620-cgaiamulattribute)
  + [6.21. cGaiaMulResource](#621-cgaiamulresource)
  + [6.22. cGaiaSpawnUnit](#622-cgaiaspawnunit)
  + [6.23. cGaiaModifyTech](#623-cgaiamodifytech)
  + [6.24. cGaiaSetPlayerData](#624-cgaiasetplayerdata)
  + [6.25. cGaiaSetTechCost](#625-cgaiasettechcost)
  + [6.26. cGaiaAddTechCost](#626-cgaiaaddtechcost)
  + [6.27. cGaiaDisableTech](#627-cgaiadisabletech)
  + [6.28. cGaiaModTechTime](#628-cgaiamodtechtime)
* [7. EffectAmount Effect Operations](#7-effectamount-effect-operations)

  + [7.1. cAttributeDisable](#71-cattributedisable)
  + [7.2. cAttributeEnable](#72-cattributeenable)
  + [7.3. cAttributeForce](#73-cattributeforce)
  + [7.4. cAttributeResearch](#74-cattributeresearch)
  + [7.5. cAttributeSet](#75-cattributeset)
  + [7.6. cAttributeAdd](#76-cattributeadd)
* [8. EffectAmount Technology Attribute](#8-effectamount-technology-attribute)

  + [8.1. cAttrSetTime](#81-cattrsettime)
  + [8.2. cAttrAddTime](#82-cattraddtime)
  + [8.3. cAttrMulTime](#83-cattrmultime)
  + [8.4. cAttrSetFoodCost](#84-cattrsetfoodcost)
  + [8.5. cAttrSetWoodCost](#85-cattrsetwoodcost)
  + [8.6. cAttrSetStoneCost](#86-cattrsetstonecost)
  + [8.7. cAttrSetGoldCost](#87-cattrsetgoldcost)
  + [8.8. cAttrAddFoodCost](#88-cattraddfoodcost)
  + [8.9. cAttrAddWoodCost](#89-cattraddwoodcost)
  + [8.10. cAttrAddStoneCost](#810-cattraddstonecost)
  + [8.11. cAttrAddGoldCost](#811-cattraddgoldcost)
  + [8.12. cAttrMulFoodCost](#812-cattrmulfoodcost)
  + [8.13. cAttrMulWoodCost](#813-cattrmulwoodcost)
  + [8.14. cAttrMulStoneCost](#814-cattrmulstonecost)
  + [8.15. cAttrMulGoldCost](#815-cattrmulgoldcost)
  + [8.16. cAttrMulAllCosts](#816-cattrmulallcosts)
  + [8.17. cAttrSetEffect](#817-cattrseteffect)
  + [8.18. cAttrSetLocation](#818-cattrsetlocation)
  + [8.19. cAttrSetButton](#819-cattrsetbutton)
  + [8.20. cAttrSetIcon](#820-cattrseticon)
  + [8.21. cAttrSetName](#821-cattrsetname)
  + [8.22. cAttrSetDescription](#822-cattrsetdescription)
  + [8.23. cAttrSetStacking](#823-cattrsetstacking)
  + [8.24. cAttrSetStackingResearchCap](#824-cattrsetstackingresearchcap)
  + [8.25. cAttrSetHotkey](#825-cattrsethotkey)
  + [8.26. cAttrSetState](#826-cattrsetstate)
* [9. EffectAmount Unit Attribute](#9-effectamount-unit-attribute)

  + [9.1. cHitpoints](#91-chitpoints)
  + [9.2. cLineOfSight](#92-clineofsight)
  + [9.3. cGarrisonCapacity](#93-cgarrisoncapacity)
  + [9.4. cUnitSizeX](#94-cunitsizex)
  + [9.5. cUnitSizeY](#95-cunitsizey)
  + [9.6. cMovementSpeed](#96-cmovementspeed)
  + [9.7. cRotationSpeed](#97-crotationspeed)
  + [9.8. cArmor](#98-carmor)
  + [9.9. cAttack](#99-cattack)
  + [9.10. cAttackReloadTime](#910-cattackreloadtime)
  + [9.11. cAccuracyPercent](#911-caccuracypercent)
  + [9.12. cMaxRange](#912-cmaxrange)
  + [9.13. cWorkRate](#913-cworkrate)
  + [9.14. cCarryCapacity](#914-ccarrycapacity)
  + [9.15. cBaseArmor](#915-cbasearmor)
  + [9.16. cProjectileUnit](#916-cprojectileunit)
  + [9.17. cIconGraphicsAngle](#917-cicongraphicsangle)
  + [9.18. cTerrainDefenseBonus](#918-cterraindefensebonus)
  + [9.19. cEnableSmartProjectile](#919-cenablesmartprojectile)
  + [9.20. cMinimumRange](#920-cminimumrange)
  + [9.21. cAmountFirstStorage](#921-camountfirststorage)
  + [9.22. cBlastWidth](#922-cblastwidth)
  + [9.23. cSearchRadius](#923-csearchradius)
  + [9.24. cBonusResistance](#924-cbonusresistance)
  + [9.25. cIconId](#925-ciconid)
  + [9.26. cAmountSecondStorage](#926-camountsecondstorage)
  + [9.27. cAmountThirdStorage](#927-camountthirdstorage)
  + [9.28. cFogFlag](#928-cfogflag)
  + [9.29. cOcclusionMode](#929-cocclusionmode)
  + [9.30. cGarrisonType](#930-cgarrisontype)
  + [9.31. cUnitSizeZ](#931-cunitsizez)
  + [9.32. cCanBeBuiltOn](#932-ccanbebuilton)
  + [9.33. cFoundationTerrain](#933-cfoundationterrain)
  + [9.34. cHeroStatus](#934-cherostatus)
  + [9.35. cAttackDelay](#935-cattackdelay)
  + [9.36. cTrainLocation](#936-ctrainlocation)
  + [9.37. cTrainButton](#937-ctrainbutton)
  + [9.38. cBlastAttackLevel](#938-cblastattacklevel)
  + [9.39. cBlastDefenseLevel](#939-cblastdefenselevel)
  + [9.40. cShownAttack](#940-cshownattack)
  + [9.41. cShownRange](#941-cshownrange)
  + [9.42. cShownMeleeArmor](#942-cshownmeleearmor)
  + [9.43. cShownPierceArmor](#943-cshownpiercearmor)
  + [9.44. cNameId](#944-cnameid)
  + [9.45. cDescriptionId](#945-cdescriptionid)
  + [9.46. cTerrainTable](#946-cterraintable)
  + [9.47. cTraits](#947-ctraits)
  + [9.48. cTraitPiece](#948-ctraitpiece)
  + [9.49. cDeadUnitId](#949-cdeadunitid)
  + [9.50. cHotkeyId](#950-chotkeyid)
  + [9.51. cMaxCharge](#951-cmaxcharge)
  + [9.52. cRechargeRate](#952-crechargerate)
  + [9.53. cChargeEvent](#953-cchargeevent)
  + [9.54. cChargeType](#954-cchargetype)
  + [9.55. cCombatAbility](#955-ccombatability)
  + [9.56. cAttackDispersion](#956-cattackdispersion)
  + [9.57. cSecondaryProjectileUnit](#957-csecondaryprojectileunit)
  + [9.58. cBloodUnitId](#958-cbloodunitid)
  + [9.59. cHitMode](#959-chitmode)
  + [9.60. cVanishMode](#960-cvanishmode)
  + [9.61. cProjectileArc](#961-cprojectilearc)
  + [9.62. cAttackGraphic](#962-cattackgraphic)
  + [9.63. cStandingGraphic](#963-cstandinggraphic)
  + [9.64. cStanding2Graphic](#964-cstanding2graphic)
  + [9.65. cDyingGraphic](#965-cdyinggraphic)
  + [9.66. cUndeadGraphic](#966-cundeadgraphic)
  + [9.67. cWalkingGraphic](#967-cwalkinggraphic)
  + [9.68. cRunningGraphic](#968-crunninggraphic)
  + [9.69. cSpecialGraphic](#969-cspecialgraphic)
  + [9.70. cObstructionType](#970-cobstructiontype)
  + [9.71. cBlockageClass](#971-cblockageclass)
  + [9.72. cSelectionEffect](#972-cselectioneffect)
  + [9.73. cSpecialAbility](#973-cspecialability)
  + [9.74. cIdleAttackGraphic](#974-cidleattackgraphic)
  + [9.75. cHeroGlowGraphic](#975-cheroglowgraphic)
  + [9.76. cGarrisonGraphic](#976-cgarrisongraphic)
  + [9.77. cConstructionGraphic](#977-cconstructiongraphic)
  + [9.78. cSnowGraphic](#978-csnowgraphic)
  + [9.79. cDestructionGraphic](#979-cdestructiongraphic)
  + [9.80. cDestructionRubbleGraphic](#980-cdestructionrubblegraphic)
  + [9.81. cResearchingGraphic](#981-cresearchinggraphic)
  + [9.82. cResearchCompletedGraphic](#982-cresearchcompletedgraphic)
  + [9.83. cDamageGraphic](#983-cdamagegraphic)
  + [9.84. cSelectionSound](#984-cselectionsound)
  + [9.85. cSelectionSoundEvent](#985-cselectionsoundevent)
  + [9.86. cDyingSound](#986-cdyingsound)
  + [9.87. cDyingSoundEvent](#987-cdyingsoundevent)
  + [9.88. cTrainSound](#988-ctrainsound)
  + [9.89. cTrainSoundEvent](#989-ctrainsoundevent)
  + [9.90. cDamageSound](#990-cdamagesound)
  + [9.91. cDamageSoundEvent](#991-cdamagesoundevent)
  + [9.92. cResourceCost](#992-cresourcecost)
  + [9.93. cTrainTime](#993-ctraintime)
  + [9.94. cTotalProjectiles](#994-ctotalprojectiles)
  + [9.95. cFoodCost](#995-cfoodcost)
  + [9.96. cWoodCost](#996-cwoodcost)
  + [9.97. cGoldCost](#997-cgoldcost)
  + [9.98. cStoneCost](#998-cstonecost)
  + [9.99. cMaxTotalProjectiles](#999-cmaxtotalprojectiles)
  + [9.100. cGarrisonHealRate](#9100-cgarrisonhealrate)
  + [9.101. cRegenerationRate](#9101-cregenerationrate)
  + [9.102. cPopulation](#9102-cpopulation)
  + [9.103. cMinConversionTimeMod](#9103-cminconversiontimemod)
  + [9.104. cMaxConversionTimeMod](#9104-cmaxconversiontimemod)
  + [9.105. cConversionChanceMod](#9105-cconversionchancemod)
  + [9.106. cFormationCategory](#9106-cformationcategory)
  + [9.107. cAreaDamage](#9107-careadamage)
  + [9.108. cDamageReflection](#9108-cdamagereflection)
  + [9.109. cFriendlyFireDamage](#9109-cfriendlyfiredamage)
  + [9.110. cRegenerationHpPercent](#9110-cregenerationhppercent)
  + [9.111. cButtonIconId](#9111-cbuttoniconid)
  + [9.112. cShortTooltipId](#9112-cshorttooltipid)
  + [9.113. cExtendedTooltipId](#9113-cextendedtooltipid)
  + [9.114. cHotkeyAction](#9114-chotkeyaction)
  + [9.115. cChargeProjectileUnit](#9115-cchargeprojectileunit)
  + [9.116. cAvailableFlag](#9116-cavailableflag)
  + [9.117. cDisabledFlag](#9117-cdisabledflag)
  + [9.118. cAttackPriority](#9118-cattackpriority)
  + [9.119. cInvulnerabilityLevel](#9119-cinvulnerabilitylevel)
  + [9.120. cGarrisonFirepower](#9120-cgarrisonfirepower)
  + [9.121. cAttack2Graphic](#9121-cattack2graphic)
  + [9.122. cCommandSound](#9122-ccommandsound)
  + [9.123. cCommandSoundEvent](#9123-ccommandsoundevent)
  + [9.124. cMoveSound](#9124-cmovesound)
  + [9.125. cMoveSoundEvent](#9125-cmovesoundevent)
  + [9.126. cConstructionSound](#9126-cconstructionsound)
  + [9.127. cConstructionSoundEvent](#9127-cconstructionsoundevent)
  + [9.128. cTransformSound](#9128-ctransformsound)
  + [9.129. cTransformSoundEvent](#9129-ctransformsoundevent)
  + [9.130. cRunPattern](#9130-crunpattern)
  + [9.131. cInterfaceKind](#9131-cinterfacekind)
  + [9.132. cCombatLevel](#9132-ccombatlevel)
  + [9.133. cInteractionMode](#9133-cinteractionmode)
  + [9.134. cMinimapMode](#9134-cminimapmode)
  + [9.135. cTrailingUnit](#9135-ctrailingunit)
  + [9.136. cTrailMode](#9136-ctrailmode)
  + [9.137. cTrailDensity](#9137-ctraildensity)
  + [9.138. cProjectileGraphicDisplacementX](#9138-cprojectilegraphicdisplacementx)
  + [9.139. cProjectileGraphicDisplacementY](#9139-cprojectilegraphicdisplacementy)
  + [9.140. cProjectileGraphicDisplacementZ](#9140-cprojectilegraphicdisplacementz)
  + [9.141. cProjectileSpawningAreaWidth](#9141-cprojectilespawningareawidth)
  + [9.142. cProjectileSpawningAreaLength](#9142-cprojectilespawningarealength)
  + [9.143. cProjectileSpawningAreaRandomness](#9143-cprojectilespawningarearandomness)
  + [9.144. cDamageGraphicsEntryMod](#9144-cdamagegraphicsentrymod)
  + [9.145. cDamageGraphicsTotalNum](#9145-cdamagegraphicstotalnum)
  + [9.146. cDamageGraphicPercent](#9146-cdamagegraphicpercent)
  + [9.147. cDamageGraphicApplyMode](#9147-cdamagegraphicapplymode)
* [10. EffectAmount Object Class](#10-effectamount-object-class)

  + [10.1. cArcherClass](#101-carcherclass)
  + [10.2. cArtifactClass](#102-cartifactclass)
  + [10.3. cTradeBoatClass](#103-ctradeboatclass)
  + [10.4. cBuildingClass](#104-cbuildingclass)
  + [10.5. cVillagerClass](#105-cvillagerclass)
  + [10.6. cSeaFishClass](#106-cseafishclass)
  + [10.7. cInfantryClass](#107-cinfantryclass)
  + [10.8. cForageBushClass](#108-cforagebushclass)
  + [10.9. cStoneMineClass](#109-cstonemineclass)
  + [10.10. cPreyAnimalClass](#1010-cpreyanimalclass)
  + [10.11. cPredatorAnimalClass](#1011-cpredatoranimalclass)
  + [10.12. cMiscellaneousClass](#1012-cmiscellaneousclass)
  + [10.13. cCavalryClass](#1013-ccavalryclass)
  + [10.14. cSiegeWeaponClass](#1014-csiegeweaponclass)
  + [10.15. cTerrainClass](#1015-cterrainclass)
  + [10.16. cTreeClass](#1016-ctreeclass)
  + [10.17. cTreeStumpClass](#1017-ctreestumpclass)
  + [10.18. cHealerClass](#1018-chealerclass)
  + [10.19. cMonkClass](#1019-cmonkclass)
  + [10.20. cTradeCartClass](#1020-ctradecartclass)
  + [10.21. cTransportShipClass](#1021-ctransportshipclass)
  + [10.22. cFishingBoatClass](#1022-cfishingboatclass)
  + [10.23. cWarshipClass](#1023-cwarshipclass)
  + [10.24. cConquistadorClass](#1024-cconquistadorclass)
  + [10.25. cWarElephantClass](#1025-cwarelephantclass)
  + [10.26. cHeroClass](#1026-cheroclass)
  + [10.27. cElephantArcherClass](#1027-celephantarcherclass)
  + [10.28. cWallClass](#1028-cwallclass)
  + [10.29. cPhalanxClass](#1029-cphalanxclass)
  + [10.30. cDomesticAnimalClass](#1030-cdomesticanimalclass)
  + [10.31. cFlagClass](#1031-cflagclass)
  + [10.32. cDeepSeaFishClass](#1032-cdeepseafishclass)
  + [10.33. cGoldMine](#1033-cgoldmine)
  + [10.34. cShoreFish](#1034-cshorefish)
  + [10.35. cCliffClass](#1035-ccliffclass)
  + [10.36. cPetardClass](#1036-cpetardclass)
  + [10.37. cCavalryArcherClass](#1037-ccavalryarcherclass)
  + [10.38. cDoppelgangerClass](#1038-cdoppelgangerclass)
  + [10.39. cBirdClass](#1039-cbirdclass)
  + [10.40. cGateClass](#1040-cgateclass)
  + [10.41. cSalvagePileClass](#1041-csalvagepileclass)
  + [10.42. cResourcePileClass](#1042-cresourcepileclass)
  + [10.43. cRelicClass](#1043-crelicclass)
  + [10.44. cMonkWithRelicClass](#1044-cmonkwithrelicclass)
  + [10.45. cHandCannoneerClass](#1045-chandcannoneerclass)
  + [10.46. cTwoHandedSwordsmanClass](#1046-ctwohandedswordsmanclass)
  + [10.47. cPikemanClass](#1047-cpikemanclass)
  + [10.48. cScoutCavalryClass](#1048-cscoutcavalryclass)
  + [10.49. cOreMineClass](#1049-coremineclass)
  + [10.50. cFarmClass](#1050-cfarmclass)
  + [10.51. cSpearmanClass](#1051-cspearmanclass)
  + [10.52. cPackedUnitClass](#1052-cpackedunitclass)
  + [10.53. cTowerClass](#1053-ctowerclass)
  + [10.54. cBoardingShipClass](#1054-cboardingshipclass)
  + [10.55. cUnpackedSiegeUnitClass](#1055-cunpackedsiegeunitclass)
  + [10.56. cScorpionClass](#1056-cscorpionclass)
  + [10.57. cRaiderClass](#1057-craiderclass)
  + [10.58. cCavalryRaiderClass](#1058-ccavalryraiderclass)
  + [10.59. cLivestockClass](#1059-clivestockclass)
  + [10.60. cKingClass](#1060-ckingclass)
  + [10.61. cMiscBuildingClass](#1061-cmiscbuildingclass)
  + [10.62. cControlledAnimalClass](#1062-ccontrolledanimalclass)
  + [10.63. cGoldFishClass](#1063-cgoldfishclass)
  + [10.64. cLandMineClass](#1064-clandmineclass)
* [11. Resource](#11-resource)

  + [11.1. cAttributeFood](#111-cattributefood)
  + [11.2. cAttributeWood](#112-cattributewood)
  + [11.3. cAttributeStone](#113-cattributestone)
  + [11.4. cAttributeGold](#114-cattributegold)
  + [11.5. cAttributePopulationCap](#115-cattributepopulationcap)
  + [11.6. cAttributeReligion](#116-cattributereligion)
  + [11.7. cAttributeCurrentAge](#117-cattributecurrentage)
  + [11.8. cAttributeRelics](#118-cattributerelics)
  + [11.9. cAttributeTrageBonus](#119-cattributetragebonus)
  + [11.10. cAttributeTradeGoods](#1110-cattributetradegoods)
  + [11.11. cAttributeTradeProducation](#1111-cattributetradeproducation)
  + [11.12. cAttributePopulation](#1112-cattributepopulation)
  + [11.13. cAttributeDecay](#1113-cattributedecay)
  + [11.14. cAttributeDiscovery](#1114-cattributediscovery)
  + [11.15. cAttributeRuins](#1115-cattributeruins)
  + [11.16. cAttributeMeat](#1116-cattributemeat)
  + [11.17. cAttributeBerries](#1117-cattributeberries)
  + [11.18. cAttributeFish](#1118-cattributefish)
  + [11.19. cAttributeKills](#1119-cattributekills)
  + [11.20. cAttributeResearchCount](#1120-cattributeresearchcount)
  + [11.21. cAttributeExploration](#1121-cattributeexploration)
  + [11.22. cAttributeConvertPriest](#1122-cattributeconvertpriest)
  + [11.23. cAttributeConvertBuilding](#1123-cattributeconvertbuilding)
  + [11.24. cAttributeBuildingLimit](#1124-cattributebuildinglimit)
  + [11.25. cAttributeFoodLimit](#1125-cattributefoodlimit)
  + [11.26. cAttributeUnitLimit](#1126-cattributeunitlimit)
  + [11.27. cAttributeMaintenance](#1127-cattributemaintenance)
  + [11.28. cAttributeFaith](#1128-cattributefaith)
  + [11.29. cAttributeFaithRechargeRate](#1129-cattributefaithrechargerate)
  + [11.30. cAttributeFarmFood](#1130-cattributefarmfood)
  + [11.31. cAttributeCivilianPopulation](#1131-cattributecivilianpopulation)
  + [11.32. cAttributeAllTechsAchieved](#1132-cattributealltechsachieved)
  + [11.33. cAttributeMilitaryPopulation](#1133-cattributemilitarypopulation)
  + [11.34. cAttributeConversions](#1134-cattributeconversions)
  + [11.35. cAttributeWonder](#1135-cattributewonder)
  + [11.36. cAttributeRazings](#1136-cattributerazings)
  + [11.37. cAttributeKillRatio](#1137-cattributekillratio)
  + [11.38. cAttributePlayerKilled](#1138-cattributeplayerkilled)
  + [11.39. cAttributeTributeInefficency](#1139-cattributetributeinefficency)
  + [11.40. cAttributeGoldBonus](#1140-cattributegoldbonus)
  + [11.41. cAttributeTownCenterUnavailable](#1141-cattributetowncenterunavailable)
  + [11.42. cAttributeGoldCounter](#1142-cattributegoldcounter)
  + [11.43. cAttributeWriting](#1143-cattributewriting)
  + [11.44. cAttributeMonasteries](#1144-cattributemonasteries)
  + [11.45. cAttributeTribute](#1145-cattributetribute)
  + [11.46. cAttributeHoldRuins](#1146-cattributeholdruins)
  + [11.47. cAttributeHoldRelics](#1147-cattributeholdrelics)
  + [11.48. cAttributeOre](#1148-cattributeore)
  + [11.49. cAttributeCapturedUnit](#1149-cattributecapturedunit)
  + [11.50. cAttributeTradeGoodQuality](#1150-cattributetradegoodquality)
  + [11.51. cAttributeTradeMarketLevel](#1151-cattributetrademarketlevel)
  + [11.52. cAttributeFormations](#1152-cattributeformations)
  + [11.53. cAttributeBuildingHouseRate](#1153-cattributebuildinghouserate)
  + [11.54. cAttributeGatherTaxRate](#1154-cattributegathertaxrate)
  + [11.55. cAttributeGatherAccumalation](#1155-cattributegatheraccumalation)
  + [11.56. cAttributeSalvageDecayRate](#1156-cattributesalvagedecayrate)
  + [11.57. cAttributeAllowFormations](#1157-cattributeallowformations)
  + [11.58. cAttributeCanConvert](#1158-cattributecanconvert)
  + [11.59. cAttributeConvertResistance](#1159-cattributeconvertresistance)
  + [11.60. cAttributeTradeVigRate](#1160-cattributetradevigrate)
  + [11.61. cAttributeStoneBonus](#1161-cattributestonebonus)
  + [11.62. cAttributeQueuedCount](#1162-cattributequeuedcount)
  + [11.63. cAttributeTrainingCount](#1163-cattributetrainingcount)
  + [11.64. cAttributeRaider](#1164-cattributeraider)
  + [11.65. cAttributeBoardingRechargeRate](#1165-cattributeboardingrechargerate)
  + [11.66. cAttributeStartingVillagers](#1166-cattributestartingvillagers)
  + [11.67. cAttributeResearchCostMod](#1167-cattributeresearchcostmod)
  + [11.68. cAttributeResearchTimeMod](#1168-cattributeresearchtimemod)
  + [11.69. cAttributeConvertBoats](#1169-cattributeconvertboats)
  + [11.70. cAttributeFishTrapFood](#1170-cattributefishtrapfood)
  + [11.71. cAttributeHealRateModifer](#1171-cattributehealratemodifer)
  + [11.72. cAttributeHealRange](#1172-cattributehealrange)
  + [11.73. cAttributeStartingFood](#1173-cattributestartingfood)
  + [11.74. cAttributeStartingWood](#1174-cattributestartingwood)
  + [11.75. cAttributeStartingStone](#1175-cattributestartingstone)
  + [11.76. cAttributeStartingGold](#1176-cattributestartinggold)
  + [11.77. cAttributeRaiderAbility](#1177-cattributeraiderability)
  + [11.78. cAttributeNoDropsiteFarmers](#1178-cattributenodropsitefarmers)
  + [11.79. cAttributeDominantSheepControl](#1179-cattributedominantsheepcontrol)
  + [11.80. cAttributeObjectCostSummation](#1180-cattributeobjectcostsummation)
  + [11.81. cAttributeResearchCostSummation](#1181-cattributeresearchcostsummation)
  + [11.82. cAttributeRelicIncomeSummation](#1182-cattributerelicincomesummation)
  + [11.83. cAttributeTradeIncomeSummation](#1183-cattributetradeincomesummation)
  + [11.84. cAttributeCastle](#1184-cattributecastle)
  + [11.85. cAttributeHitPointRazings](#1185-cattributehitpointrazings)
  + [11.86. cAttributeValueKilledByOthers](#1186-cattributevaluekilledbyothers)
  + [11.87. cAttributeValueRazedByOthers](#1187-cattributevaluerazedbyothers)
  + [11.88. cAttributeKilledByOthers](#1188-cattributekilledbyothers)
  + [11.89. cAttributeRazedByOthers](#1189-cattributerazedbyothers)
  + [11.90. cAttributeValueCurrentUnits](#1190-cattributevaluecurrentunits)
  + [11.91. cAttributeValueCurrentBuildings](#1191-cattributevaluecurrentbuildings)
  + [11.92. cAttributeFoodTotal](#1192-cattributefoodtotal)
  + [11.93. cAttributeWoodTotal](#1193-cattributewoodtotal)
  + [11.94. cAttributeStoneTotal](#1194-cattributestonetotal)
  + [11.95. cAttributeGoldTotal](#1195-cattributegoldtotal)
  + [11.96. cAttributeTotalValueOfKills](#1196-cattributetotalvalueofkills)
  + [11.97. cAttributeTotalTributeReceived](#1197-cattributetotaltributereceived)
  + [11.98. cAttributeTotalValueOfRazings](#1198-cattributetotalvalueofrazings)
  + [11.99. cAttributeTotalCastlesBuilt](#1199-cattributetotalcastlesbuilt)
  + [11.100. cAttributeTotalWondersBuilt](#11100-cattributetotalwondersbuilt)
  + [11.101. cAttributeTributeScore](#11101-cattributetributescore)
  + [11.102. cAttributeConvertMinAdj](#11102-cattributeconvertminadj)
  + [11.103. cAttributeConvertMaxAdj](#11103-cattributeconvertmaxadj)
  + [11.104. cAttributeConvertResistMinAdj](#11104-cattributeconvertresistminadj)
  + [11.105. cAttributeConvertResistMaxAdj](#11105-cattributeconvertresistmaxadj)
  + [11.106. cAttributeConvertBuildingMin](#11106-cattributeconvertbuildingmin)
  + [11.107. cAttributeConvertBuildingMax](#11107-cattributeconvertbuildingmax)
  + [11.108. cAttributeConvertBuildingChance](#11108-cattributeconvertbuildingchance)
  + [11.109. cAttributeSpies](#11109-cattributespies)
  + [11.110. cAttributeValueWondersCastles](#11110-cattributevaluewonderscastles)
  + [11.111. cAttributeFoodScore](#11111-cattributefoodscore)
  + [11.112. cAttributeWoodScore](#11112-cattributewoodscore)
  + [11.113. cAttributeStoneScore](#11113-cattributestonescore)
  + [11.114. cAttributeGoldScore](#11114-cattributegoldscore)
  + [11.115. cAttributeWoodBonus](#11115-cattributewoodbonus)
  + [11.116. cAttributeFoodBonus](#11116-cattributefoodbonus)
  + [11.117. cAttributeRelicRate](#11117-cattributerelicrate)
  + [11.118. cAttributeHeresy](#11118-cattributeheresy)
  + [11.119. cAttributeTheocracy](#11119-cattributetheocracy)
  + [11.120. cAttributeCrenellations](#11120-cattributecrenellations)
  + [11.121. cAttributeConstructionRateMod](#11121-cattributeconstructionratemod)
  + [11.122. cAttributeHunWonderBonus](#11122-cattributehunwonderbonus)
  + [11.123. cAttributeSpiesDiscount](#11123-cattributespiesdiscount)
  + [11.124. cAttributeTemporaryMapReveal](#11124-cattributetemporarymapreveal)
  + [11.125. cAttributeRevealInitialType](#11125-cattributerevealinitialtype)
  + [11.126. cAttributeElevationBonusHigher](#11126-cattributeelevationbonushigher)
  + [11.127. cAttributeElevationBonusLower](#11127-cattributeelevationbonuslower)
  + [11.128. cAttributeTriggerSharedLOS](#11128-cattributetriggersharedlos)
  + [11.129. cAttributeFeudalTownCenterLimit](#11129-cattributefeudaltowncenterlimit)
  + [11.130. cAttributeFishingProductivity](#11130-cattributefishingproductivity)
  + [11.131. cAttributeUnused220](#11131-cattributeunused220)
  + [11.132. cAttributeMonumentFoodTrickle](#11132-cattributemonumentfoodtrickle)
  + [11.133. cAttributeMonumentWoodTrickle](#11133-cattributemonumentwoodtrickle)
  + [11.134. cAttributeMonumentStoneTrickle](#11134-cattributemonumentstonetrickle)
  + [11.135. cAttributeMonumentGoldTrickle](#11135-cattributemonumentgoldtrickle)
  + [11.136. cAttributeRelicFoodRate](#11136-cattributerelicfoodrate)
  + [11.137. cAttributeVillagersKilledByGaia](#11137-cattributevillagerskilledbygaia)
  + [11.138. cAttributeVillgaersKilledByAnimal](#11138-cattributevillgaerskilledbyanimal)
  + [11.139. cAttributeVillagersKilledByAIPlayer](#11139-cattributevillagerskilledbyaiplayer)
  + [11.140. cAttributeVillagersKilledByHumanPlayer](#11140-cattributevillagerskilledbyhumanplayer)
  + [11.141. cAttributeFoodGeneration](#11141-cattributefoodgeneration)
  + [11.142. cAttributeWoodGeneration](#11142-cattributewoodgeneration)
  + [11.143. cAttributeStoneGeneration](#11143-cattributestonegeneration)
  + [11.144. cAttributeGoldGeneration](#11144-cattributegoldgeneration)
  + [11.145. cAttributeSpawnCap](#11145-cattributespawncap)
  + [11.146. cAttributeFlemishMilitiaPop](#11146-cattributeflemishmilitiapop)
  + [11.147. cAttributeGoldFarmingProductivity](#11147-cattributegoldfarmingproductivity)
  + [11.148. cAttributeFolwarkCollectionAmount](#11148-cattributefolwarkcollectionamount)
  + [11.149. cAttributeFolwarkCollectionType](#11149-cattributefolwarkcollectiontype)
  + [11.150. cAttributeBuildingId](#11150-cattributebuildingid)
  + [11.151. cAttributeUnitsConverted](#11151-cattributeunitsconverted)
  + [11.152. cAttributeStoneGoldMiningProductivity](#11152-cattributestonegoldminingproductivity)
  + [11.153. cAttributeWorkshopFoodTrickle](#11153-cattributeworkshopfoodtrickle)
  + [11.154. cAttributeWorkshopWoodTrickle](#11154-cattributeworkshopwoodtrickle)
  + [11.155. cAttributeWorkshopStoneTrickle](#11155-cattributeworkshopstonetrickle)
  + [11.156. cAttributeWorkshopGoldTrickle](#11156-cattributeworkshopgoldtrickle)
  + [11.157. cAttributeUnitsValueTotal](#11157-cattributeunitsvaluetotal)
  + [11.158. cAttributeBuildingsValueTotal](#11158-cattributebuildingsvaluetotal)
  + [11.159. cAttributeVillagersCreatedTotal](#11159-cattributevillagerscreatedtotal)
  + [11.160. cAttributeVillagersIdlePeriodsTotal](#11160-cattributevillagersidleperiodstotal)
  + [11.161. cAttributeVillagersIdleSecondsTotal](#11161-cattributevillagersidlesecondstotal)
  + [11.162. cAttributeTradeFoodPercent](#11162-cattributetradefoodpercent)
  + [11.163. cAttributeTradeWoodPercent](#11163-cattributetradewoodpercent)
  + [11.164. cAttributeTradeStonePercent](#11164-cattributetradestonepercent)
  + [11.165. cAttributeLivestockFoodProductivity](#11165-cattributelivestockfoodproductivity)
  + [11.166. cAttributeSpeedUpBuildingType](#11166-cattributespeedupbuildingtype)
  + [11.167. cAttributeSpeedUpBuildingRange](#11167-cattributespeedupbuildingrange)
  + [11.168. cAttributeSpeedUpPercentage](#11168-cattributespeeduppercentage)
  + [11.169. cAttributeSpeedUpObjectType](#11169-cattributespeedupobjecttype)
  + [11.170. cAttributeSpeedUpEffectType](#11170-cattributespeedupeffecttype)
  + [11.171. cAttributeSpeedUpSecondaryEffectType](#11171-cattributespeedupsecondaryeffecttype)
  + [11.172. cAttributeSpeedUpSecondaryPercentage](#11172-cattributespeedupsecondarypercentage)
  + [11.173. cAttributeCivNameOverride](#11173-cattributecivnameoverride)
  + [11.174. cAttributeStartingScoutID](#11174-cattributestartingscoutid)
  + [11.175. cAttributeRelicWoodRate](#11175-cattributerelicwoodrate)
  + [11.176. cAttributeRelicStoneRate](#11176-cattributerelicstonerate)
  + [11.177. cAttributeChoppingGoldProductivity](#11177-cattributechoppinggoldproductivity)
  + [11.178. cAttributeForagingWoodProductivity](#11178-cattributeforagingwoodproductivity)
  + [11.179. cAttributeHuntingProductivity](#11179-cattributehuntingproductivity)
  + [11.180. cAttributeTechnologyRewardEffect](#11180-cattributetechnologyrewardeffect)
  + [11.181. cAttributeUnitRepairCost](#11181-cattributeunitrepaircost)
  + [11.182. cAttributeBuildingRepairCost](#11182-cattributebuildingrepaircost)
  + [11.183. cAttributeElevationDamageHigher](#11183-cattributeelevationdamagehigher)
  + [11.184. cAttributeElevationDamageLower](#11184-cattributeelevationdamagelower)
  + [11.185. cAttributeInfantryKillReward](#11185-cattributeinfantrykillreward)
  + [11.186. cAttributeMilitaryCanConvert](#11186-cattributemilitarycanconvert)
  + [11.187. cAttributeMilitaryConversionRangeAdj](#11187-cattributemilitaryconversionrangeadj)
  + [11.188. cAttributeMilitaryConversionChance](#11188-cattributemilitaryconversionchance)
  + [11.189. cAttributeMilitaryConversionRechargeRate](#11189-cattributemilitaryconversionrechargerate)
  + [11.190. cAttributeSpawnStayInside](#11190-cattributespawnstayinside)
  + [11.191. cAttributeCavalryKillReward](#11191-cattributecavalrykillreward)
  + [11.192. cAttributeTriggerSharedVisibility](#11192-cattributetriggersharedvisibility)
  + [11.193. cAttributeTriggerSharedExploration](#11193-cattributetriggersharedexploration)
  + [11.194. cAttributeMilitaryFoodTrickle](#11194-cattributemilitaryfoodtrickle)
  + [11.195. cAttributePastureFoodAmount](#11195-cattributepasturefoodamount)
  + [11.196. cAttributePastureAnimalCount](#11196-cattributepastureanimalcount)
  + [11.197. cAttributePastureHerderCount](#11197-cattributepastureherdercount)
  + [11.198. cAttributeDisableAnimalDecay](#11198-cattributedisableanimaldecay)
  + [11.199. cAttributeHerdingFoodProductivity](#11199-cattributeherdingfoodproductivity)
  + [11.200. cAttributeShepherdingFoodProductivity](#11200-cattributeshepherdingfoodproductivity)
  + [11.201. cAttributeGaiaKills](#11201-cattributegaiakills)
  + [11.202. cAttributePlayer1Kills](#11202-cattributeplayer1kills)
  + [11.203. cAttributePlayer2Kills](#11203-cattributeplayer2kills)
  + [11.204. cAttributePlayer3Kills](#11204-cattributeplayer3kills)
  + [11.205. cAttributePlayer4Kills](#11205-cattributeplayer4kills)
  + [11.206. cAttributePlayer5Kills](#11206-cattributeplayer5kills)
  + [11.207. cAttributePlayer6Kills](#11207-cattributeplayer6kills)
  + [11.208. cAttributePlayer7Kills](#11208-cattributeplayer7kills)
  + [11.209. cAttributePlayer8Kills](#11209-cattributeplayer8kills)
  + [11.210. cAttributeKillsByGaia](#11210-cattributekillsbygaia)
  + [11.211. cAttributeKillsByPlayer1](#11211-cattributekillsbyplayer1)
  + [11.212. cAttributeKillsByPlayer2](#11212-cattributekillsbyplayer2)
  + [11.213. cAttributeKillsByPlayer3](#11213-cattributekillsbyplayer3)
  + [11.214. cAttributeKillsByPlayer4](#11214-cattributekillsbyplayer4)
  + [11.215. cAttributeKillsByPlayer5](#11215-cattributekillsbyplayer5)
  + [11.216. cAttributeKillsByPlayer6](#11216-cattributekillsbyplayer6)
  + [11.217. cAttributeKillsByPlayer7](#11217-cattributekillsbyplayer7)
  + [11.218. cAttributeKillsByPlayer8](#11218-cattributekillsbyplayer8)
  + [11.219. cAttributeGaiaRazings](#11219-cattributegaiarazings)
  + [11.220. cAttributePlayer1Razings](#11220-cattributeplayer1razings)
  + [11.221. cAttributePlayer2Razings](#11221-cattributeplayer2razings)
  + [11.222. cAttributePlayer3Razings](#11222-cattributeplayer3razings)
  + [11.223. cAttributePlayer4Razings](#11223-cattributeplayer4razings)
  + [11.224. cAttributePlayer5Razings](#11224-cattributeplayer5razings)
  + [11.225. cAttributePlayer6Razings](#11225-cattributeplayer6razings)
  + [11.226. cAttributePlayer7Razings](#11226-cattributeplayer7razings)
  + [11.227. cAttributePlayer8Razings](#11227-cattributeplayer8razings)
  + [11.228. cAttributeRazingsByGaia](#11228-cattributerazingsbygaia)
  + [11.229. cAttributeRazingsByPlayer1](#11229-cattributerazingsbyplayer1)
  + [11.230. cAttributeRazingsByPlayer2](#11230-cattributerazingsbyplayer2)
  + [11.231. cAttributeRazingsByPlayer3](#11231-cattributerazingsbyplayer3)
  + [11.232. cAttributeRazingsByPlayer4](#11232-cattributerazingsbyplayer4)
  + [11.233. cAttributeRazingsByPlayer5](#11233-cattributerazingsbyplayer5)
  + [11.234. cAttributeRazingsByPlayer6](#11234-cattributerazingsbyplayer6)
  + [11.235. cAttributeRazingsByPlayer7](#11235-cattributerazingsbyplayer7)
  + [11.236. cAttributeRazingsByPlayer8](#11236-cattributerazingsbyplayer8)
  + [11.237. cAttributeGaiaKillValue](#11237-cattributegaiakillvalue)
  + [11.238. cAttributePlayer1KillValue](#11238-cattributeplayer1killvalue)
  + [11.239. cAttributePlayer2KillValue](#11239-cattributeplayer2killvalue)
  + [11.240. cAttributePlayer3KillValue](#11240-cattributeplayer3killvalue)
  + [11.241. cAttributePlayer4KillValue](#11241-cattributeplayer4killvalue)
  + [11.242. cAttributePlayer5KillValue](#11242-cattributeplayer5killvalue)
  + [11.243. cAttributePlayer6KillValue](#11243-cattributeplayer6killvalue)
  + [11.244. cAttributePlayer7KillValue](#11244-cattributeplayer7killvalue)
  + [11.245. cAttributePlayer8KillValue](#11245-cattributeplayer8killvalue)
  + [11.246. cAttributeGaiaRazingValue](#11246-cattributegaiarazingvalue)
  + [11.247. cAttributePlayer1RazingValue](#11247-cattributeplayer1razingvalue)
  + [11.248. cAttributePlayer2RazingValue](#11248-cattributeplayer2razingvalue)
  + [11.249. cAttributePlayer3RazingValue](#11249-cattributeplayer3razingvalue)
  + [11.250. cAttributePlayer4RazingValue](#11250-cattributeplayer4razingvalue)
  + [11.251. cAttributePlayer5RazingValue](#11251-cattributeplayer5razingvalue)
  + [11.252. cAttributePlayer6RazingValue](#11252-cattributeplayer6razingvalue)
  + [11.253. cAttributePlayer7RazingValue](#11253-cattributeplayer7razingvalue)
  + [11.254. cAttributePlayer8RazingValue](#11254-cattributeplayer8razingvalue)
  + [11.255. cAttributeGaiaTribute](#11255-cattributegaiatribute)
  + [11.256. cAttributePlayer1Tribute](#11256-cattributeplayer1tribute)
  + [11.257. cAttributePlayer2Tribute](#11257-cattributeplayer2tribute)
  + [11.258. cAttributePlayer3Tribute](#11258-cattributeplayer3tribute)
  + [11.259. cAttributePlayer4Tribute](#11259-cattributeplayer4tribute)
  + [11.260. cAttributePlayer5Tribute](#11260-cattributeplayer5tribute)
  + [11.261. cAttributePlayer6Tribute](#11261-cattributeplayer6tribute)
  + [11.262. cAttributePlayer7Tribute](#11262-cattributeplayer7tribute)
  + [11.263. cAttributePlayer8Tribute](#11263-cattributeplayer8tribute)
  + [11.264. cAttributeTributeFromGaia](#11264-cattributetributefromgaia)
  + [11.265. cAttributeTributeFromPlayer1](#11265-cattributetributefromplayer1)
  + [11.266. cAttributeTributeFromPlayer2](#11266-cattributetributefromplayer2)
  + [11.267. cAttributeTributeFromPlayer3](#11267-cattributetributefromplayer3)
  + [11.268. cAttributeTributeFromPlayer4](#11268-cattributetributefromplayer4)
  + [11.269. cAttributeTributeFromPlayer5](#11269-cattributetributefromplayer5)
  + [11.270. cAttributeTributeFromPlayer6](#11270-cattributetributefromplayer6)
  + [11.271. cAttributeTributeFromPlayer7](#11271-cattributetributefromplayer7)
  + [11.272. cAttributeTributeFromPlayer8](#11272-cattributetributefromplayer8)
  + [11.273. cAttributeChoppingFoodProductivity](#11273-cattributechoppingfoodproductivity)
* [12. Damage Class](#12-damage-class)

  + [12.1. cDamageClassInfantry](#121-cdamageclassinfantry)
  + [12.2. cDamageClassCapitalShips](#122-cdamageclasscapitalships)
  + [12.3. cDamageClassPierce](#123-cdamageclasspierce)
  + [12.4. cDamageClassMelee](#124-cdamageclassmelee)
  + [12.5. cDamageClassElephantUnits](#125-cdamageclasselephantunits)
  + [12.6. cDamageClassCavalry](#126-cdamageclasscavalry)
  + [12.7. cDamageClassAllBuildings](#127-cdamageclassallbuildings)
  + [12.8. cDamageClassStoneDefense](#128-cdamageclassstonedefense)
  + [12.9. cDamageClassPredatorAnimals](#129-cdamageclasspredatoranimals)
  + [12.10. cDamageClassArchers](#1210-cdamageclassarchers)
  + [12.11. cDamageClassShips](#1211-cdamageclassships)
  + [12.12. cDamageClassRams](#1212-cdamageclassrams)
  + [12.13. cDamageClassTrees](#1213-cdamageclasstrees)
  + [12.14. cDamageClassUniqueUnits](#1214-cdamageclassuniqueunits)
  + [12.15. cDamageClassSiegeWeapons](#1215-cdamageclasssiegeweapons)
  + [12.16. cDamageClassStandardBuildings](#1216-cdamageclassstandardbuildings)
  + [12.17. cDamageClassWallsAndGates](#1217-cdamageclasswallsandgates)
  + [12.18. cDamageClassGunpowderUnits](#1218-cdamageclassgunpowderunits)
  + [12.19. cDamageClassBoars](#1219-cdamageclassboars)
  + [12.20. cDamageClassMonks](#1220-cdamageclassmonks)
  + [12.21. cDamageClassCastles](#1221-cdamageclasscastles)
  + [12.22. cDamageClassSpearmen](#1222-cdamageclassspearmen)
  + [12.23. cDamageClassCavalryArchers](#1223-cdamageclasscavalryarchers)
  + [12.24. cDamageClassShockInfantry](#1224-cdamageclassshockinfantry)
  + [12.25. cDamageClassCamelUnits](#1225-cdamageclasscamelunits)
  + [12.26. cDamageClassCondottieri](#1226-cdamageclasscondottieri)
  + [12.27. cDamageClassFishingShips](#1227-cdamageclassfishingships)
  + [12.28. cDamageClassMamelukes](#1228-cdamageclassmamelukes)
  + [12.29. cDamageClassHeroesAndKings](#1229-cdamageclassheroesandkings)
  + [12.30. cDamageClassHeavySiege](#1230-cdamageclassheavysiege)
  + [12.31. cDamageClassSkirmishers](#1231-cdamageclassskirmishers)
  + [12.32. cDamageClassRoyalHeirs](#1232-cdamageclassroyalheirs)
* [13. Task Attribute](#13-task-attribute)

  + [13.1. cTaskAttrWorkValue1](#131-ctaskattrworkvalue1)
  + [13.2. cTaskAttrWorkValue2](#132-ctaskattrworkvalue2)
  + [13.3. cTaskAttrWorkRange](#133-ctaskattrworkrange)
  + [13.4. cTaskAttrWorkFlag2](#134-ctaskattrworkflag2)
  + [13.5. cTaskAttrSearchWaitTime](#135-ctaskattrsearchwaittime)
  + [13.6. cTaskAttrCombatLevelFlag](#136-ctaskattrcombatlevelflag)
  + [13.7. cTaskAttrOwnerType](#137-ctaskattrownertype)
  + [13.8. cTaskAttrTerrain](#138-ctaskattrterrain)
  + [13.9. cTaskAttrResourceIn](#139-ctaskattrresourcein)
  + [13.10. cTaskAttrProductivityResource](#1310-ctaskattrproductivityresource)
  + [13.11. cTaskAttrResourceOut](#1311-ctaskattrresourceout)
  + [13.12. cTaskAttrUnusedResource](#1312-ctaskattrunusedresource)
  + [13.13. cTaskAttrMovingGraphic](#1313-ctaskattrmovinggraphic)
  + [13.14. cTaskAttrProceedingGraphic](#1314-ctaskattrproceedinggraphic)
  + [13.15. cTaskAttrWorkingGraphic](#1315-ctaskattrworkinggraphic)
  + [13.16. cTaskAttrCarryingGraphic](#1316-ctaskattrcarryinggraphic)
  + [13.17. cTaskAttrGatheringSound](#1317-ctaskattrgatheringsound)
  + [13.18. cTaskAttrGatheringSoundEvent](#1318-ctaskattrgatheringsoundevent)
  + [13.19. cTaskAttrGatheringSoundInt32](#1319-ctaskattrgatheringsoundint32)
  + [13.20. cTaskAttrDepositSound](#1320-ctaskattrdepositsound)
  + [13.21. cTaskAttrDepositSoundEvent](#1321-ctaskattrdepositsoundevent)
  + [13.22. cTaskAttrDepositSoundInt32](#1322-ctaskattrdepositsoundint32)
  + [13.23. cTaskAttrAutoSearch](#1323-ctaskattrautosearch)
  + [13.24. cTaskAttrCarryCheck](#1324-ctaskattrcarrycheck)
  + [13.25. cTaskAttrBuildingPick](#1325-ctaskattrbuildingpick)
  + [13.26. cTaskAttrGatherType](#1326-ctaskattrgathertype)
  + [13.27. cTaskAttrEnableTargeting](#1327-ctaskattrenabletargeting)
  + [13.28. cTaskAttrEnabled](#1328-ctaskattrenabled)
* [14. Task Type](#14-task-type)

  + [14.1. cTaskTypeMoveTo](#141-ctasktypemoveto)
  + [14.2. cTaskTypeFollow](#142-ctasktypefollow)
  + [14.3. cTaskTypeGarrison](#143-ctasktypegarrison)
  + [14.4. cTaskTypeExplore](#144-ctasktypeexplore)
  + [14.5. cTaskTypeGatherRebuild](#145-ctasktypegatherrebuild)
  + [14.6. cTaskTypeGraze](#146-ctasktypegraze)
  + [14.7. cTaskTypeCombat](#147-ctasktypecombat)
  + [14.8. cTaskTypeShoot](#148-ctasktypeshoot)
  + [14.9. cTaskTypeAttack](#149-ctasktypeattack)
  + [14.10. cTaskTypeFly](#1410-ctasktypefly)
  + [14.11. cTaskTypeUnloadBoatLike](#1411-ctasktypeunloadboatlike)
  + [14.12. cTaskTypeGuard](#1412-ctasktypeguard)
  + [14.13. cTaskTypeUnloadOverWall](#1413-ctasktypeunloadoverwall)
  + [14.14. cTaskTypeMake](#1414-ctasktypemake)
  + [14.15. cTaskTypeBuild](#1415-ctasktypebuild)
  + [14.16. cTaskTypeMakeUnit](#1416-ctasktypemakeunit)
  + [14.17. cTaskTypeMakeTech](#1417-ctasktypemaketech)
  + [14.18. cTaskTypeConvert](#1418-ctasktypeconvert)
  + [14.19. cTaskTypeHeal](#1419-ctasktypeheal)
  + [14.20. cTaskTypeRepair](#1420-ctasktyperepair)
  + [14.21. cTaskTypeGetAutoConverted](#1421-ctasktypegetautoconverted)
  + [14.22. cTaskTypeDiscoveryArtifact](#1422-ctasktypediscoveryartifact)
  + [14.23. cTaskTypeHunt](#1423-ctasktypehunt)
  + [14.24. cTaskTypeTrade](#1424-ctasktypetrade)
  + [14.25. cTaskTypeGenerateWonderVictory](#1425-ctasktypegeneratewondervictory)
  + [14.26. cTaskTypeDeselectWhenTasked](#1426-ctasktypedeselectwhentasked)
  + [14.27. cTaskTypeLootGather](#1427-ctasktypelootgather)
  + [14.28. cTaskTypeHousing](#1428-ctasktypehousing)
  + [14.29. cTaskTypePack](#1429-ctasktypepack)
  + [14.30. cTaskTypeUnpackAndAttack](#1430-ctasktypeunpackandattack)
  + [14.31. cTaskTypeOffMapTrade](#1431-ctasktypeoffmaptrade)
  + [14.32. cTaskTypePickupUnit](#1432-ctasktypepickupunit)
  + [14.33. cTaskTypeChargeAttack](#1433-ctasktypechargeattack)
  + [14.34. cTaskTypeTransformUnit](#1434-ctasktypetransformunit)
  + [14.35. cTaskTypeKidnapUnit](#1435-ctasktypekidnapunit)
  + [14.36. cTaskTypeDepositUnit](#1436-ctasktypedepositunit)
  + [14.37. cTaskTypeShear](#1437-ctasktypeshear)
  + [14.38. cTaskTypeGenerateResources](#1438-ctasktypegenerateresources)
  + [14.39. cTaskTypeMovementDamage](#1439-ctasktypemovementdamage)
  + [14.40. cTaskTypeMovableDropsite](#1440-ctasktypemovabledropsite)
  + [14.41. cTaskTypeLoot](#1441-ctasktypeloot)
  + [14.42. cTaskTypeAura](#1442-ctasktypeaura)
  + [14.43. cTaskTypeExtraSpawn](#1443-ctasktypeextraspawn)
  + [14.44. cTaskTypeStinger](#1444-ctasktypestinger)
  + [14.45. cTaskTypeHPTransform](#1445-ctasktypehptransform)
  + [14.46. cTaskTypeHPModifier](#1446-ctasktypehpmodifier)
* [15. Tech State](#15-tech-state)

  + [15.1. cTechStateNotReady](#151-ctechstatenotready)
  + [15.2. cTechStateReady](#152-ctechstateready)
  + [15.3. cTechStateQueued](#153-ctechstatequeued)
  + [15.4. cTechStateResearching](#154-ctechstateresearching)
  + [15.5. cTechStateDone](#155-ctechstatedone)
  + [15.6. cTechStateDisabled](#156-ctechstatedisabled)
  + [15.7. cTechStateInvalid](#157-ctechstateinvalid)
* [16. Object Type](#16-object-type)

  + [16.1. cObjectTypeEyeCandy](#161-cobjecttypeeyecandy)
  + [16.2. cObjectTypeTrees](#162-cobjecttypetrees)
  + [16.3. cObjectTypeAnimated](#163-cobjecttypeanimated)
  + [16.4. cObjectTypeDoppleganger](#164-cobjecttypedoppleganger)
  + [16.5. cObjectTypeMoving](#165-cobjecttypemoving)
  + [16.6. cObjectTypeActing](#166-cobjecttypeacting)
  + [16.7. cObjectTypeCombat](#167-cobjecttypecombat)
  + [16.8. cObjectTypeProjectile](#168-cobjecttypeprojectile)
  + [16.9. cObjectTypeCreatable](#169-cobjecttypecreatable)
  + [16.10. cObjectTypeBuilding](#1610-cobjecttypebuilding)
  + [16.11. cObjectTypeLegacyTree](#1611-cobjecttypelegacytree)

# Constant Reference

*Written by: Alian713*

---

## 1. Read/Write[¶](#1-readwrite "Permanent link")

### 1.1. cOffsetString[¶](#11-coffsetstring "Permanent link")

Value: `int 0`

Used with the [xsOffsetFilePosition](../functions/#66-xsoffsetfileposition "Jump To: XS > Function Reference > xsOffsetFilePosition"). Makes the offset function move the file position by the number of bytes it takes to store a string (4 bytes + a number of bytes that is determined by the integer that the first 4 bytes represent)

### 1.2. cOffsetInteger[¶](#12-coffsetinteger "Permanent link")

Value: `int 1`

Used with the [xsOffsetFilePosition](../functions/#66-xsoffsetfileposition "Jump To: XS > Function Reference > xsOffsetFilePosition"). Makes the offset function move the file position by the number of bytes it takes to store an integer (4 bytes)

### 1.3. cOffsetFloat[¶](#13-coffsetfloat "Permanent link")

Value: `int 2`

Used with the [xsOffsetFilePosition](../functions/#66-xsoffsetfileposition "Jump To: XS > Function Reference > xsOffsetFilePosition"). Makes the offset function move the file position by the number of bytes it takes to store a float (4 bytes)

### 1.4. cOffsetVector[¶](#14-coffsetvector "Permanent link")

Value: `int 3`

Used with the [xsOffsetFilePosition](../functions/#66-xsoffsetfileposition "Jump To: XS > Function Reference > xsOffsetFilePosition"). Makes the offset function move the file position by the number of bytes it takes to store a vector (12 bytes)

## 2. Age[¶](#2-age "Permanent link")

### 2.1. cDarkAge[¶](#21-cdarkage "Permanent link")

Value: `int 0`

Value of the [Current Age](../../resources/resources/#6-current-age "Jump to: Game Mechanics > Resources > #7. Current Age") resource when a player is in the Dark Age

### 2.2. cFeudalAge[¶](#22-cfeudalage "Permanent link")

Value: `int 1`

Value of the [Current Age](../../resources/resources/#6-current-age "Jump to: Game Mechanics > Resources > #7. Current Age") resource when a player is in the Feudal Age

### 2.3. cCastleAge[¶](#23-ccastleage "Permanent link")

Value: `int 2`

Value of the [Current Age](../../resources/resources/#6-current-age "Jump to: Game Mechanics > Resources > #7. Current Age") resource when a player is in the Castle Age

### 2.4. cImperialAge[¶](#24-cimperialage "Permanent link")

Value: `int 3`

Value of the [Current Age](../../resources/resources/#6-current-age "Jump to: Game Mechanics > Resources > #7. Current Age") resource when a player is in the Imperial Age

### 2.5. cStoneAge[¶](#25-cstoneage "Permanent link")

Value: `int 0`

Value of the [Current Age](../../resources/resources/#6-current-age "Jump to: Game Mechanics > Resources > #7. Current Age") resource when a player is in the Dark Age

### 2.6. cToolAge[¶](#26-ctoolage "Permanent link")

Value: `int 1`

Value of the [Current Age](../../resources/resources/#6-current-age "Jump to: Game Mechanics > Resources > #7. Current Age") resource when a player is in the Feudal Age

### 2.7. cBronzeAge[¶](#27-cbronzeage "Permanent link")

Value: `int 2`

Value of the [Current Age](../../resources/resources/#6-current-age "Jump to: Game Mechanics > Resources > #7. Current Age") resource when a player is in the Castle Age

### 2.8. cIronAge[¶](#28-cironage "Permanent link")

Value: `int 3`

Value of the [Current Age](../../resources/resources/#6-current-age "Jump to: Game Mechanics > Resources > #7. Current Age") resource when a player is in the Imperial Age

## 3. Value[¶](#3-value "Permanent link")

### 3.1. cActivationTime[¶](#31-cactivationtime "Permanent link")

Value: `int -1`

This value is only defined inside the body of a rule. It holds the time of initial activation of that rule

### 3.2. cOriginVector[¶](#32-coriginvector "Permanent link")

Value: `vector (0, 0, 0)`

The Origin Vector

### 3.3. cInvalidVector[¶](#33-cinvalidvector "Permanent link")

Value: `vector (-1, -1, -1)`

The Invalid Vector

## 4. Victory Conditions[¶](#4-victory-conditions "Permanent link")

### 4.1. cStandardVictory[¶](#41-cstandardvictory "Permanent link")

Value: `int 100`

one of the values returned by the `xsGetVictoryCondition[ForSecondaryGameMode]` functions

### 4.2. cWonderVictory[¶](#42-cwondervictory "Permanent link")

Value: `int 101`

one of the values returned by the `xsGetVictoryCondition[ForSecondaryGameMode]` functions

### 4.3. cRelicVictory[¶](#43-crelicvictory "Permanent link")

Value: `int 102`

one of the values returned by the `xsGetVictoryCondition[ForSecondaryGameMode]` functions

### 4.4. cKingOfTheHillVictory[¶](#44-ckingofthehillvictory "Permanent link")

Value: `int 103`

one of the values returned by the `xsGetVictoryCondition[ForSecondaryGameMode]` functions

## 5. Civilization[¶](#5-civilization "Permanent link")

### 5.1. cGaia[¶](#51-cgaia "Permanent link")

Value: `int 0`

This is the civilization ID of Gaia

### 5.2. cBritons[¶](#52-cbritons "Permanent link")

Value: `int 1`

This is the civilization ID of Britons

### 5.3. cFranks[¶](#53-cfranks "Permanent link")

Value: `int 2`

This is the civilization ID of Franks

### 5.4. cGoths[¶](#54-cgoths "Permanent link")

Value: `int 3`

This is the civilization ID of Goths

### 5.5. cTeutons[¶](#55-cteutons "Permanent link")

Value: `int 4`

This is the civilization ID of Teutons

### 5.6. cJapanese[¶](#56-cjapanese "Permanent link")

Value: `int 5`

This is the civilization ID of Japanese

### 5.7. cChinese[¶](#57-cchinese "Permanent link")

Value: `int 6`

This is the civilization ID of Chinese

### 5.8. cByzantines[¶](#58-cbyzantines "Permanent link")

Value: `int 7`

This is the civilization ID of Byzantines

### 5.9. cPersians[¶](#59-cpersians "Permanent link")

Value: `int 8`

This is the civilization ID of Persians

### 5.10. cSaracens[¶](#510-csaracens "Permanent link")

Value: `int 9`

This is the civilization ID of Saracens

### 5.11. cTurks[¶](#511-cturks "Permanent link")

Value: `int 10`

This is the civilization ID of Turks

### 5.12. cVikings[¶](#512-cvikings "Permanent link")

Value: `int 11`

This is the civilization ID of Vikings

### 5.13. cMongols[¶](#513-cmongols "Permanent link")

Value: `int 12`

This is the civilization ID of Mongols

### 5.14. cCelts[¶](#514-ccelts "Permanent link")

Value: `int 13`

This is the civilization ID of Celts

### 5.15. cSpanish[¶](#515-cspanish "Permanent link")

Value: `int 14`

This is the civilization ID of Spanish

### 5.16. cAztecs[¶](#516-caztecs "Permanent link")

Value: `int 15`

This is the civilization ID of Aztecs

### 5.17. cMayans[¶](#517-cmayans "Permanent link")

Value: `int 16`

This is the civilization ID of Mayans

### 5.18. cHuns[¶](#518-chuns "Permanent link")

Value: `int 17`

This is the civilization ID of Huns

### 5.19. cKoreans[¶](#519-ckoreans "Permanent link")

Value: `int 18`

This is the civilization ID of Koreans

### 5.20. cItalians[¶](#520-citalians "Permanent link")

Value: `int 19`

This is the civilization ID of Italians

### 5.21. cIndians[¶](#521-cindians "Permanent link")

Value: `int 20`

This is the civilization ID of Indians

### 5.22. cIncas[¶](#522-cincas "Permanent link")

Value: `int 21`

This is the civilization ID of Incas

### 5.23. cMagyars[¶](#523-cmagyars "Permanent link")

Value: `int 22`

This is the civilization ID of Magyars

### 5.24. cSlavs[¶](#524-cslavs "Permanent link")

Value: `int 23`

This is the civilization ID of Slavs

### 5.25. cPortuguese[¶](#525-cportuguese "Permanent link")

Value: `int 24`

This is the civilization ID of Portuguese

### 5.26. cEthiopians[¶](#526-cethiopians "Permanent link")

Value: `int 25`

This is the civilization ID of Ethiopians

### 5.27. cMalians[¶](#527-cmalians "Permanent link")

Value: `int 26`

This is the civilization ID of Malians

### 5.28. cBerbers[¶](#528-cberbers "Permanent link")

Value: `int 27`

This is the civilization ID of Berbers

### 5.29. cKhmer[¶](#529-ckhmer "Permanent link")

Value: `int 28`

This is the civilization ID of Khmer

### 5.30. cMalay[¶](#530-cmalay "Permanent link")

Value: `int 29`

This is the civilization ID of Malay

### 5.31. cBurmese[¶](#531-cburmese "Permanent link")

Value: `int 30`

This is the civilization ID of Burmese

### 5.32. cVietnamese[¶](#532-cvietnamese "Permanent link")

Value: `int 31`

This is the civilization ID of Vietnamese

### 5.33. cBulgarians[¶](#533-cbulgarians "Permanent link")

Value: `int 32`

This is the civilization ID of Bulgarians

### 5.34. cTatars[¶](#534-ctatars "Permanent link")

Value: `int 33`

This is the civilization ID of Tatars

### 5.35. cCumans[¶](#535-ccumans "Permanent link")

Value: `int 34`

This is the civilization ID of Cumans

### 5.36. cLithuanians[¶](#536-clithuanians "Permanent link")

Value: `int 35`

This is the civilization ID of Lithuanians

### 5.37. cBurgundians[¶](#537-cburgundians "Permanent link")

Value: `int 36`

This is the civilization ID of Burgundians

### 5.38. cSicilians[¶](#538-csicilians "Permanent link")

Value: `int 37`

This is the civilization ID of Sicilians

### 5.39. cPoles[¶](#539-cpoles "Permanent link")

Value: `int 38`

This is the civilization ID of Poles

### 5.40. cBohemians[¶](#540-cbohemians "Permanent link")

Value: `int 39`

This is the civilization ID of Bohemians

### 5.41. cDravidians[¶](#541-cdravidians "Permanent link")

Value: `int 40`

This is the civilization ID of Dravidians

### 5.42. cBengalis[¶](#542-cbengalis "Permanent link")

Value: `int 41`

This is the civilization ID of Bengalis

### 5.43. cGurjaras[¶](#543-cgurjaras "Permanent link")

Value: `int 42`

This is the civilization ID of Gurjaras

### 5.44. cRomans[¶](#544-cromans "Permanent link")

Value: `int 43`

This is the civilization ID of Romans

### 5.45. cArmenians[¶](#545-carmenians "Permanent link")

Value: `int 44`

This is the civilization ID of Armenians

### 5.46. cGeorgians[¶](#546-cgeorgians "Permanent link")

Value: `int 45`

This is the civilization ID of Georgians

### 5.47. cAchaemenids[¶](#547-cachaemenids "Permanent link")

Value: `int 46`

This is the civilization ID of Achaemenids

### 5.48. cAthenians[¶](#548-cathenians "Permanent link")

Value: `int 47`

This is the civilization ID of Athenians

### 5.49. cSpartans[¶](#549-cspartans "Permanent link")

Value: `int 48`

This is the civilization ID of Spartans

### 5.50. cShu[¶](#550-cshu "Permanent link")

Value: `int 49`

This is the civilization ID of Shu

### 5.51. cWu[¶](#551-cwu "Permanent link")

Value: `int 50`

This is the civilization ID of Wu

### 5.52. cWei[¶](#552-cwei "Permanent link")

Value: `int 51`

This is the civilization ID of Wei

### 5.53. cJurchens[¶](#553-cjurchens "Permanent link")

Value: `int 52`

This is the civilization ID of Jurchens

### 5.54. cKhitans[¶](#554-ckhitans "Permanent link")

Value: `int 53`

This is the civilization ID of Khitans

### 5.55. cAoeEgyptians[¶](#555-caoeegyptians "Permanent link")

Value: `int 1`

This is the civilization ID of Aoe Egyptians

### 5.56. cAoeGreeks[¶](#556-caoegreeks "Permanent link")

Value: `int 2`

This is the civilization ID of Aoe Greeks

### 5.57. cAoeBabylonians[¶](#557-caoebabylonians "Permanent link")

Value: `int 3`

This is the civilization ID of Aoe Babylonians

### 5.58. cAoeAssyrians[¶](#558-caoeassyrians "Permanent link")

Value: `int 4`

This is the civilization ID of Aoe Assyrians

### 5.59. cAoeMinoans[¶](#559-caoeminoans "Permanent link")

Value: `int 5`

This is the civilization ID of Aoe Minoans

### 5.60. cAoeHittites[¶](#560-caoehittites "Permanent link")

Value: `int 6`

This is the civilization ID of Aoe Hittites

### 5.61. cAoePhoenicians[¶](#561-caoephoenicians "Permanent link")

Value: `int 7`

This is the civilization ID of Aoe Phoenicians

### 5.62. cAoeSumerians[¶](#562-caoesumerians "Permanent link")

Value: `int 8`

This is the civilization ID of Aoe Sumerians

### 5.63. cAoePersians[¶](#563-caoepersians "Permanent link")

Value: `int 9`

This is the civilization ID of Aoe Persians

### 5.64. cAoeShang[¶](#564-caoeshang "Permanent link")

Value: `int 10`

This is the civilization ID of Aoe Shang

### 5.65. cAoeYamato[¶](#565-caoeyamato "Permanent link")

Value: `int 11`

This is the civilization ID of Aoe Yamato

### 5.66. cAoeChoson[¶](#566-caoechoson "Permanent link")

Value: `int 12`

This is the civilization ID of Aoe Choson

### 5.67. cAoeRomans[¶](#567-caoeromans "Permanent link")

Value: `int 13`

This is the civilization ID of Aoe Romans

### 5.68. cAoeCarthaginians[¶](#568-caoecarthaginians "Permanent link")

Value: `int 14`

This is the civilization ID of Aoe Carthaginians

### 5.69. cAoePalmyrans[¶](#569-caoepalmyrans "Permanent link")

Value: `int 15`

This is the civilization ID of Aoe Palmyrans

### 5.70. cAoeMacedonians[¶](#570-caoemacedonians "Permanent link")

Value: `int 16`

This is the civilization ID of Aoe Macedonians

### 5.71. cAoeLacViet[¶](#571-caoelacviet "Permanent link")

Value: `int 17`

This is the civilization ID of Aoe Lac Viet

## 6. EffectAmount Effect Type[¶](#6-effectamount-effect-type "Permanent link")

### 6.1. cSetAttribute[¶](#61-csetattribute "Permanent link")

Value: `int 0`

This is the ID of the `Set Attribute` effect of the xsEffectAmount function

Syntax:

|  |  |
| --- | --- |
| ``` 1 ``` | ```  xsEffectAmount(cSetAttribute, unitID, attributeID, value) ``` |

Example:

|  |  |
| --- | --- |
| ``` 1 ``` | ```  xsEffectAmount(cSetAttribute, 74, cHitpoints, 100) ``` |

This sets the HP of unit 74 (militia) to 100 (the value). Alternatively, any of the [Unit Attribute Constants](./#7-effectamount-unit-attribute "Jump to: Unit Attribute Constants") may be used to modify the corresponding unit property

### 6.2. cModResource[¶](#62-cmodresource "Permanent link")

Value: `int 1`

This is the ID of the `Modify Resource` effect for the xsEffectAmount function

Syntax:

|  |  |
| --- | --- |
| ``` 1 ``` | ```  xsEffectAmount(cModResource, resourceID, operation, value) ``` |

Example:

|  |  |
| --- | --- |
| ``` 1 ``` | ```  xsEffectAmount(cModResource, cAttributeFood, cAttributeAdd, 100) ``` |

This adds 100 to the current food amount. Alternatively, `cAttributeSet` may be used to set the food amount to 100. Also, see the [Resource](./#9-resource "Jump to: Constant Reference > Resource")

### 6.3. cEnableObject[¶](#63-cenableobject "Permanent link")

Value: `int 2`

This is the ID of the `Enable (or disable) Object` effect for the xsEffectAmount function

Syntax:

|  |  |
| --- | --- |
| ``` 1 ``` | ```  xsEffectAmount(cEnableObject, unitID, enableOrDisable, 0) ``` |

Example:

|  |  |
| --- | --- |
| ``` 1 ``` | ```  xsEffectAmount(cEnableObject, 74, cAttributeDisable, 0) ``` |

This disables the unit 74 (militia). Alternatively, `cAttributeEnable` may be used to enable an object instead

### 6.4. cUpgradeUnit[¶](#64-cupgradeunit "Permanent link")

Value: `int 3`

This is the ID of the `Upgrade Unit` effect for the xsEffectAmount function

Syntax:

|  |  |
| --- | --- |
| ``` 1 ``` | ```  xsEffectAmount(cUpgradeUnit, oldUnitID, newUnitID, 0) ``` |

Example:

|  |  |
| --- | --- |
| ``` 1 ``` | ```  xsEffectAmount(cUpgradeUnit, 74, 75, 0) ``` |

This copies all units attributes except ID and available from unit 75 (man at arms) to 74 (militia)

### 6.5. cAddAttribute[¶](#65-caddattribute "Permanent link")

Value: `int 4`

This is the ID of the `Add Attribute` effect for the xsEffectAmount function

Syntax:

|  |  |
| --- | --- |
| ``` 1 ``` | ```  xsEffectAmount(cAddAttribute, unitID, attributeID, value) ``` |

Example:

|  |  |
| --- | --- |
| ``` 1 ``` | ```  xsEffectAmount(cAddAttribute, 74, 0, 100) ``` |

This adds 100 (the value) to the attribute 0 (HP) of unit 74 (militia)

### 6.6. cMulAttribute[¶](#66-cmulattribute "Permanent link")

Value: `int 5`

This is the ID of the `Multiply Attribute` effect for the xsEffectAmount function

Syntax:

|  |  |
| --- | --- |
| ``` 1 ``` | ```  xsEffectAmount(cMulAttribute, unitID, attributeID, value) ``` |

Example:

|  |  |
| --- | --- |
| ``` 1 ``` | ```  xsEffectAmount(cMulAttribute, 74, 0, 100) ``` |

This multiplies the attribute 0 (HP) of unit 74 (militia) by 100 (the value)

### 6.7. cMulResource[¶](#67-cmulresource "Permanent link")

Value: `int 6`

This is the ID of the `Multiply Resource` effect for the xsEffectAmount function

Syntax:

|  |  |
| --- | --- |
| ``` 1 ``` | ```  xsEffectAmount(cMulResource, resourceID, 0, value) ``` |

Example:

|  |  |
| --- | --- |
| ``` 1 ``` | ```  xsEffectAmount(cMulResource, cAttributeFood, 0, 10) ``` |

This multiplies the food amount by 10 (the value)

### 6.8. cSpawnUnit[¶](#68-cspawnunit "Permanent link")

Value: `int 7`

This is the ID of the `Spawn Unit` effect for the xsEffectAmount function

Syntax:

|  |  |
| --- | --- |
| ``` 1 2 ``` | ```  xsEffectAmount(cModResource, cAttributeSpawnCap, cAttributeSet, numBuildings);  xsEffectAmount(cSpawnUnit, unitID, buildingID, numUnits) ``` |

Example:

|  |  |
| --- | --- |
| ``` 1 2 ``` | ```  xsEffectAmount(cModResource, cAttributeSpawnCap, cAttributeSet, 2);  xsEffectAmount(cSpawnUnit, 83, 109, 5) ``` |

This will spawn 5 villagers (83) from each town centre (109), for a maximum of 2 town centres. Note that setting the `cAttributeCap` resource to a non 0 value is required for using this effect. If you prefer spawning the units garrisoned set resource `cAttributeSpawnStayInside` to 1.

### 6.9. cModifyTech[¶](#69-cmodifytech "Permanent link")

Value: `int 8`

This is the ID of the `Modify Technology` effect for the xsEffectAmount function

Syntax:

|  |  |
| --- | --- |
| ``` 1 ``` | ```  xsEffectAmount(cModifyTech, techID, techAttribute, value) ``` |

Example:

|  |  |
| --- | --- |
| ``` 1 ``` | ```  xsEffectAmount(cModifyTech, 22, cAttrSetTime, 10) ``` |

This sets the research time of tech 22 (loom) to 10s (the value). Alternatively, any of the [Tech Attribute Constants](./#6-effectamount-technology-attribute "Jump to: Tech Attribute Constants") may be used to modify the corresponding tech property

### 6.10. cSetPlayerData[¶](#610-csetplayerdata "Permanent link")

Value: `int 9`

This is the ID of the `Set Player Data` effect for the xsEffectAmount function

Syntax:

|  |  |
| --- | --- |
| ``` 1 ``` | ```  xsEffectAmount(cSetPlayerData, 0, cAttributeSet, value) ``` |

Example:

|  |  |
| --- | --- |
| ``` 1 ``` | ```  xsEffectAmount(cSetPlayerData, 0, cAttributeSet, 10230) ``` |

This sets the player data 0 (Civilization Name ID) to 10230 (the value)

### 6.11. cSetTechCost[¶](#611-csettechcost "Permanent link")

Value: `int 100`

This is the ID of the `Set Technology Cost` effect for the xsEffectAmount function. No Longer works, use `cModifyTech` instead

Syntax:

|  |  |
| --- | --- |
| ``` 1 ``` | ```  xsEffectAmount(cSetTechCost, techID, resourceID, value) ``` |

Example:

|  |  |
| --- | --- |
| ``` 1 ``` | ```  xsEffectAmount(cSetTechCost, 22, cAttributeFood, 10) ``` |

This sets the food cost of tech 22 (loom) to 10 (the value)

### 6.12. cAddTechCost[¶](#612-caddtechcost "Permanent link")

Value: `int 101`

This is the ID of the `Add Technology Cost` effect for the xsEffectAmount function. No Longer works, use `cModifyTech` instead

Syntax:

|  |  |
| --- | --- |
| ``` 1 ``` | ```  xsEffectAmount(cAddTechCost, techID, resourceID, value) ``` |

Example:

|  |  |
| --- | --- |
| ``` 1 ``` | ```  xsEffectAmount(cAddTechCost, 22, cAttributeFood, 10) ``` |

This adds 10 (the) to the current food cost of tech 22 (loom)

### 6.13. cDisableTech[¶](#613-cdisabletech "Permanent link")

Value: `int 102`

This is the ID of the `Disable Tech` effect for the xsEffectAmount function

Syntax:

|  |  |
| --- | --- |
| ``` 1 ``` | ```  xsEffectAmount(cDisableTech, techID, 0, 0) ``` |

Example:

|  |  |
| --- | --- |
| ``` 1 ``` | ```  xsEffectAmount(cDisableTech, 22, 0, 0) ``` |

This disables the tech 22 (loom)

### 6.14. cModTechTime[¶](#614-cmodtechtime "Permanent link")

Value: `int 103`

This is the ID of the `Modify Technology Time` effect for the xsEffectAmount function. No Longer works, use `cModifyTech` instead

Syntax:

|  |  |
| --- | --- |
| ``` 1 ``` | ```  xsEffectAmount(cModTechTime, techID, operation, value) ``` |

Example:

|  |  |
| --- | --- |
| ``` 1 ``` | ```  xsEffectAmount(cModTechTime, 22, cAttributeSet, 10) ``` |

This sets the research time of tech 22 (loom) to 10s (the value). Alternatively, `cAttributeAdd` may be used to add to the current research time of the technology

### 6.15. cGaiaSetAttribute[¶](#615-cgaiasetattribute "Permanent link")

Value: `int -1`

This is the ID of the `Gaia Set Attribute` effect of the xsEffectAmount function

Syntax:

|  |  |
| --- | --- |
| ``` 1 ``` | ```  xsEffectAmount(cGaiaSetAttribute, unitID, attributeID, value) ``` |

Example:

|  |  |
| --- | --- |
| ``` 1 ``` | ```  xsEffectAmount(cGaiaSetAttribute, 74, 0, 100) ``` |

This sets the attribute 0 (HP) of unit 74 (militia) to 100 (the value)

### 6.16. cGaiaModResource[¶](#616-cgaiamodresource "Permanent link")

Value: `int -2`

This is the ID of the `Gaia Modify Resource` effect for the xsEffectAmount function

Syntax:

|  |  |
| --- | --- |
| ``` 1 ``` | ```  xsEffectAmount(cGaiaModResource, resourceID, operation, value) ``` |

Example:

|  |  |
| --- | --- |
| ``` 1 ``` | ```  xsEffectAmount(cGaiaModResource, cAttributeFood, cAttributeAdd, 100) ``` |

This adds 100 to the current food amount. Alternatively, `cAttributeSet` may be used to set the food amount to 100

### 6.17. cGaiaEnableObject[¶](#617-cgaiaenableobject "Permanent link")

Value: `int -3`

This is the ID of the `Gaia Enable (or disable) Object` effect for the xsEffectAmount function

Syntax:

|  |  |
| --- | --- |
| ``` 1 ``` | ```  xsEffectAmount(cGaiaEnableObject, unitID, enableOrDisable, 0) ``` |

Example:

|  |  |
| --- | --- |
| ``` 1 ``` | ```  xsEffectAmount(cGaiaEnableObject, 74, cAttributeDisable, 0) ``` |

This disables the unit 74 (militia). Alternatively, `cAttributeEnable` may be used to enable an object instead

### 6.18. cGaiaUpgradeUnit[¶](#618-cgaiaupgradeunit "Permanent link")

Value: `int -4`

This is the ID of the `Gaia Upgrade Unit` effect for the xsEffectAmount function

Syntax:

|  |  |
| --- | --- |
| ``` 1 ``` | ```  xsEffectAmount(cGaiaUpgradeUnit, oldUnitID, newUnitID, 0) ``` |

Example:

|  |  |
| --- | --- |
| ``` 1 ``` | ```  xsEffectAmount(cGaiaUpgradeUnit, 74, 75, 0) ``` |

This replaces all units 74 (militia) with 75 (man at arms) on the map and also disables unit 74 and enables unit 75

### 6.19. cGaiaAddAttribute[¶](#619-cgaiaaddattribute "Permanent link")

Value: `int -5`

This is the ID of the `Gaia Add Attribute` effect for the xsEffectAmount function

Syntax:

|  |  |
| --- | --- |
| ``` 1 ``` | ```  xsEffectAmount(cGaiaAddAttribute, unitID, attributeID, value) ``` |

Example:

|  |  |
| --- | --- |
| ``` 1 ``` | ```  xsEffectAmount(cGaiaAddAttribute, 74, 0, 100) ``` |

This adds 100 (the value) to the attribute 0 (HP) of unit 74 (militia)

### 6.20. cGaiaMulAttribute[¶](#620-cgaiamulattribute "Permanent link")

Value: `int -6`

This is the ID of the `Gaia Multiply Attribute` effect for the xsEffectAmount function

Syntax:

|  |  |
| --- | --- |
| ``` 1 ``` | ```  xsEffectAmount(cGaiaMulAttribute, unitID, attributeID, value) ``` |

Example:

|  |  |
| --- | --- |
| ``` 1 ``` | ```  xsEffectAmount(cGaiaMulAttribute, 74, 0, 100) ``` |

This multiplies the attribute 0 (HP) of unit 74 (militia) by 100 (the value)

### 6.21. cGaiaMulResource[¶](#621-cgaiamulresource "Permanent link")

Value: `int -7`

This is the ID of the `Gaia Multiply Resource` effect for the xsEffectAmount function

Syntax:

|  |  |
| --- | --- |
| ``` 1 ``` | ```  xsEffectAmount(cGaiaMulResource, resourceID, 0, value) ``` |

Example:

|  |  |
| --- | --- |
| ``` 1 ``` | ```  xsEffectAmount(cGaiaMulResource, cAttributeFood, 0, 10) ``` |

This multiplies the food amount by 10 (the value)

### 6.22. cGaiaSpawnUnit[¶](#622-cgaiaspawnunit "Permanent link")

Value: `int -8`

This is the ID of the `Gaia Spawn Unit` effect for the xsEffectAmount function

Syntax:

|  |  |
| --- | --- |
| ``` 1 2 ``` | ```  xsEffectAmount(cGaiaModResource, cAttributeSpawnCap, cAttributeSet, numBuildings);  xsEffectAmount(cGaiaSpawnUnit, unitID, buildingID, numUnits) ``` |

Example:

|  |  |
| --- | --- |
| ``` 1 2 ``` | ```  xsEffectAmount(cGaiaModResource, cAttributeSpawnCap, cAttributeSet, 2);  xsEffectAmount(cGaiaSpawnUnit, 83, 109, 5) ``` |

This will spawn 5 villagers (83) from each town centre (109), for a maximum of 2 town centres. Note that setting the `cAttributeCap` resource to a non 0 value is required for using this effect. If you prefer spawning the units garrisoned set resource `cAttributeSpawnStayInside` to 1.

### 6.23. cGaiaModifyTech[¶](#623-cgaiamodifytech "Permanent link")

Value: `int -9`

This is the ID of the `Gaia Modify Technology` effect for the xsEffectAmount function

Syntax:

|  |  |
| --- | --- |
| ``` 1 ``` | ```  xsEffectAmount(cGaiaModifyTech, techID, techAttribute, value) ``` |

Example:

|  |  |
| --- | --- |
| ``` 1 ``` | ```  xsEffectAmount(cGaiaModifyTech, 22, cAttrSetTime, 10) ``` |

This sets the research time of tech 22 (loom) to 10s (the value). Alternatively, any of the [Tech Attribute Constants](./6-effectamount-technology-attribute "Jump to: Tech Attribute Constants") may be used to modify the corresponding tech property

### 6.24. cGaiaSetPlayerData[¶](#624-cgaiasetplayerdata "Permanent link")

Value: `int -10`

This is the ID of the `Gaia Set Player Data` effect for the xsEffectAmount function

Syntax:

|  |  |
| --- | --- |
| ``` 1 ``` | ```  xsEffectAmount(cGaiaSetPlayerData, 0, cAttributeSet, value) ``` |

Example:

|  |  |
| --- | --- |
| ``` 1 ``` | ```  xsEffectAmount(cGaiaSetPlayerData, 0, cAttributeSet, 10230) ``` |

This sets the player data 0 (Civilization Name ID) to 10230 (the value)

### 6.25. cGaiaSetTechCost[¶](#625-cgaiasettechcost "Permanent link")

Value: `int -101`

This is the ID of the `Gaia Set Technology Cost` effect for the xsEffectAmount function. No Longer works, use `cModifyTech` instead

Syntax:

|  |  |
| --- | --- |
| ``` 1 ``` | ```  xsEffectAmount(cGaiaSetTechCost, techID, resourceID, value) ``` |

Example:

|  |  |
| --- | --- |
| ``` 1 ``` | ```  xsEffectAmount(cGaiaSetTechCost, 22, cAttributeFood, 10) ``` |

This sets the food cost of tech 22 (loom) to 10 (the value)

### 6.26. cGaiaAddTechCost[¶](#626-cgaiaaddtechcost "Permanent link")

Value: `int -102`

This is the ID of the `Gaia Add Technology Cost` effect for the xsEffectAmount function. No Longer works, use `cModifyTech` instead

Syntax:

|  |  |
| --- | --- |
| ``` 1 ``` | ```  xsEffectAmount(cGaiaAddTechCost, techID, resourceID, value) ``` |

Example:

|  |  |
| --- | --- |
| ``` 1 ``` | ```  xsEffectAmount(cGaiaAddTechCost, 22, cAttributeFood, 10) ``` |

This adds 10 (the) to the current food cost of tech 22 (loom)

### 6.27. cGaiaDisableTech[¶](#627-cgaiadisabletech "Permanent link")

Value: `int -103`

This is the ID of the `Gaia Disable Tech` effect for the xsEffectAmount function

Syntax:

|  |  |
| --- | --- |
| ``` 1 ``` | ```  xsEffectAmount(cGaiaDisableTech, techID, 0, 0) ``` |

Example:

|  |  |
| --- | --- |
| ``` 1 ``` | ```  xsEffectAmount(cGaiaDisableTech, 22, 0, 0) ``` |

This disables the tech 22 (loom)

### 6.28. cGaiaModTechTime[¶](#628-cgaiamodtechtime "Permanent link")

Value: `int -104`

This is the ID of the `Gaia Modify Technology Time` effect for the xsEffectAmount function. No Longer works, use `cModifyTech` instead

Syntax:

|  |  |
| --- | --- |
| ``` 1 ``` | ```  xsEffectAmount(cGaiaModTechTime, techID, operation, value) ``` |

Example:

|  |  |
| --- | --- |
| ``` 1 ``` | ```  xsEffectAmount(cGaiaModTechTime, 22, cAttributeSet, 10) ``` |

This sets the research time of tech 22 (loom) to 10s (the value). Alternatively, `cAttributeAdd` may be used to add to the current research time of the technology

## 7. EffectAmount Effect Operations[¶](#7-effectamount-effect-operations "Permanent link")

### 7.1. cAttributeDisable[¶](#71-cattributedisable "Permanent link")

Value: `int 0`

This is the ID of the `Attribute Disbale` modifier for the xsEffectAmount function

### 7.2. cAttributeEnable[¶](#72-cattributeenable "Permanent link")

Value: `int 1`

This is the ID of the `Attribute Enable` modifier for the xsEffectAmount function

### 7.3. cAttributeForce[¶](#73-cattributeforce "Permanent link")

Value: `int 2`

This is the ID of the `Attribute Force` modifier for the xsEffectAmount function

### 7.4. cAttributeResearch[¶](#74-cattributeresearch "Permanent link")

Value: `int 2`

This is the ID of the `Attribute Research` modifier for the xsEffectAmount function

### 7.5. cAttributeSet[¶](#75-cattributeset "Permanent link")

Value: `int 0`

This is the ID of the `Attribute Set` modifier for the xsEffectAmount function

### 7.6. cAttributeAdd[¶](#76-cattributeadd "Permanent link")

Value: `int 1`

This is the ID of the `Attribute Add` modifier for the xsEffectAmount function

## 8. EffectAmount Technology Attribute[¶](#8-effectamount-technology-attribute "Permanent link")

### 8.1. cAttrSetTime[¶](#81-cattrsettime "Permanent link")

Value: `int -1`

This is the ID of the `Attribute Set Time` modifier for the xsEffectAmount function

### 8.2. cAttrAddTime[¶](#82-cattraddtime "Permanent link")

Value: `int -2`

This is the ID of the `Attribute Add Time` modifier for the xsEffectAmount function

### 8.3. cAttrMulTime[¶](#83-cattrmultime "Permanent link")

Value: `int -3`

This is the ID of the `Attribute Multiply Time` modifier for the xsEffectAmount function

### 8.4. cAttrSetFoodCost[¶](#84-cattrsetfoodcost "Permanent link")

Value: `int 0`

This is the ID of the `Attribute Set Food Cost` modifier for the xsEffectAmount function

### 8.5. cAttrSetWoodCost[¶](#85-cattrsetwoodcost "Permanent link")

Value: `int 1`

This is the ID of the `Attribute Set Wood Cost` modifier for the xsEffectAmount function

### 8.6. cAttrSetStoneCost[¶](#86-cattrsetstonecost "Permanent link")

Value: `int 2`

This is the ID of the `Attribute Set Stone Cost` modifier for the xsEffectAmount function

### 8.7. cAttrSetGoldCost[¶](#87-cattrsetgoldcost "Permanent link")

Value: `int 3`

This is the ID of the `Attribute Set Gold Cost` modifier for the xsEffectAmount function

### 8.8. cAttrAddFoodCost[¶](#88-cattraddfoodcost "Permanent link")

Value: `int 16384`

This is the ID of the `Attribute Add Food Cost` modifier for the xsEffectAmount function

### 8.9. cAttrAddWoodCost[¶](#89-cattraddwoodcost "Permanent link")

Value: `int 16385`

This is the ID of the `Attribute Add Wood Cost` modifier for the xsEffectAmount function

### 8.10. cAttrAddStoneCost[¶](#810-cattraddstonecost "Permanent link")

Value: `int 16386`

This is the ID of the `Attribute Add Stone Cost` modifier for the xsEffectAmount function

### 8.11. cAttrAddGoldCost[¶](#811-cattraddgoldcost "Permanent link")

Value: `int 16387`

This is the ID of the `Attribute Add Gold Cost` modifier for the xsEffectAmount function

### 8.12. cAttrMulFoodCost[¶](#812-cattrmulfoodcost "Permanent link")

Value: `int 13`

This is the ID of the `Attribute Multiply Food Cost` modifier for the xsEffectAmount function

### 8.13. cAttrMulWoodCost[¶](#813-cattrmulwoodcost "Permanent link")

Value: `int 14`

This is the ID of the `Attribute Multiply Wood Cost` modifier for the xsEffectAmount function

### 8.14. cAttrMulStoneCost[¶](#814-cattrmulstonecost "Permanent link")

Value: `int 15`

This is the ID of the `Attribute Multiply Stone Cost` modifier for the xsEffectAmount function

### 8.15. cAttrMulGoldCost[¶](#815-cattrmulgoldcost "Permanent link")

Value: `int 16`

This is the ID of the `Attribute Multiply Gold Cost` modifier for the xsEffectAmount function

### 8.16. cAttrMulAllCosts[¶](#816-cattrmulallcosts "Permanent link")

Value: `int 17`

This is the ID of the `Attribute Multiply All Costs` modifier for the xsEffectAmount function

### 8.17. cAttrSetEffect[¶](#817-cattrseteffect "Permanent link")

Value: `int 18`

This is the ID of the `Attribute Set Effect` modifier for the xsEffectAmount function

### 8.18. cAttrSetLocation[¶](#818-cattrsetlocation "Permanent link")

Value: `int 4`

This is the ID of the `Attribute Set Tech Location` modifier for the xsEffectAmount function

### 8.19. cAttrSetButton[¶](#819-cattrsetbutton "Permanent link")

Value: `int 5`

This is the ID of the `Attribute Set Tech Button` modifier for the xsEffectAmount function

### 8.20. cAttrSetIcon[¶](#820-cattrseticon "Permanent link")

Value: `int 6`

This is the ID of the `Attribute Set Tech Icon` modifier for the xsEffectAmount function

### 8.21. cAttrSetName[¶](#821-cattrsetname "Permanent link")

Value: `int 7`

This is the ID of the `Attribute Set Tech Name` modifier for the xsEffectAmount function

### 8.22. cAttrSetDescription[¶](#822-cattrsetdescription "Permanent link")

Value: `int 8`

This is the ID of the `Attribute Set Tech Description` modifier for the xsEffectAmount function

### 8.23. cAttrSetStacking[¶](#823-cattrsetstacking "Permanent link")

Value: `int 9`

This is the ID of the `Attribute Set Tech Stacking` modifier for the xsEffectAmount function

### 8.24. cAttrSetStackingResearchCap[¶](#824-cattrsetstackingresearchcap "Permanent link")

Value: `int 10`

This is the ID of the `Attribute Set Stacking Research Cap` modifier for the xsEffectAmount function

### 8.25. cAttrSetHotkey[¶](#825-cattrsethotkey "Permanent link")

Value: `int 11`

This is the ID of the `Attribute Set Hotkey` modifier for the xsEffectAmount function

### 8.26. cAttrSetState[¶](#826-cattrsetstate "Permanent link")

Value: `int 12`

This is the ID of the `Attribute Set State` modifier for the xsEffectAmount function

## 9. EffectAmount Unit Attribute[¶](#9-effectamount-unit-attribute "Permanent link")

### 9.1. cHitpoints[¶](#91-chitpoints "Permanent link")

Value: `int 0`

This is the attribute [Hit Points](./../../attributes/attributes/#0-hit-points)

### 9.2. cLineOfSight[¶](#92-clineofsight "Permanent link")

Value: `int 1`

This is the attribute [Line of Sight](./../../attributes/attributes/#1-line-of-sight)

### 9.3. cGarrisonCapacity[¶](#93-cgarrisoncapacity "Permanent link")

Value: `int 2`

This is the attribute [Garrison Capacity](./../../attributes/attributes/#2-garrison-capacity)

### 9.4. cUnitSizeX[¶](#94-cunitsizex "Permanent link")

Value: `int 3`

This is the attribute [Unit Size X](./../../attributes/attributes/#3-unit-size-x)

### 9.5. cUnitSizeY[¶](#95-cunitsizey "Permanent link")

Value: `int 4`

This is the attribute [Unit Size Y](./../../attributes/attributes/#4-unit-size-y)

### 9.6. cMovementSpeed[¶](#96-cmovementspeed "Permanent link")

Value: `int 5`

This is the attribute [Movement Speed](./../../attributes/attributes/#5-movement-speed)

### 9.7. cRotationSpeed[¶](#97-crotationspeed "Permanent link")

Value: `int 6`

This is the attribute [Rotation Speed](./../../attributes/attributes/#6-rotation-speed)

### 9.8. cArmor[¶](#98-carmor "Permanent link")

Value: `int 8`

This is the attribute [Armor](./../../attributes/attributes/#8-armor)

### 9.9. cAttack[¶](#99-cattack "Permanent link")

Value: `int 9`

This is the attribute [Attack](./../../attributes/attributes/#9-attack)

### 9.10. cAttackReloadTime[¶](#910-cattackreloadtime "Permanent link")

Value: `int 10`

This is the attribute [Attack Reload Time](./../../attributes/attributes/#10-attack-reload-time)

### 9.11. cAccuracyPercent[¶](#911-caccuracypercent "Permanent link")

Value: `int 11`

This is the attribute [Accuracy Percent](./../../attributes/attributes/#11-accuracy-percent)

### 9.12. cMaxRange[¶](#912-cmaxrange "Permanent link")

Value: `int 12`

This is the attribute [Max Range](./../../attributes/attributes/#12-max-range)

### 9.13. cWorkRate[¶](#913-cworkrate "Permanent link")

Value: `int 13`

This is the attribute [Work Rate](./../../attributes/attributes/#13-work-rate)

### 9.14. cCarryCapacity[¶](#914-ccarrycapacity "Permanent link")

Value: `int 14`

This is the attribute [Carry Capacity](./../../attributes/attributes/#14-carry-capacity)

### 9.15. cBaseArmor[¶](#915-cbasearmor "Permanent link")

Value: `int 15`

This is the attribute [Base Armor](./../../attributes/attributes/#15-base-armor)

### 9.16. cProjectileUnit[¶](#916-cprojectileunit "Permanent link")

Value: `int 16`

This is the attribute [Projectile Unit](./../../attributes/attributes/#16-projectile-unit)

### 9.17. cIconGraphicsAngle[¶](#917-cicongraphicsangle "Permanent link")

Value: `int 17`

This is the attribute [Building Icon Override](./../../attributes/attributes/#17-building-icon-override)

### 9.18. cTerrainDefenseBonus[¶](#918-cterraindefensebonus "Permanent link")

Value: `int 18`

This is the attribute [Terrain Defense Bonus](./../../attributes/attributes/#18-terrain-defense-bonus)

### 9.19. cEnableSmartProjectile[¶](#919-cenablesmartprojectile "Permanent link")

Value: `int 19`

This is the attribute [Projectile Smart Mode](./../../attributes/attributes/#19-projectile-smart-mode)

### 9.20. cMinimumRange[¶](#920-cminimumrange "Permanent link")

Value: `int 20`

This is the attribute [Minimum Range](./../../attributes/attributes/#20-minimum-range)

### 9.21. cAmountFirstStorage[¶](#921-camountfirststorage "Permanent link")

Value: `int 21`

This is the attribute [Amount of 1st Resource Storage](./../../attributes/attributes/#21-amount-of-1st-resource-storage)

### 9.22. cBlastWidth[¶](#922-cblastwidth "Permanent link")

Value: `int 22`

This is the attribute [Blast Width](./../../attributes/attributes/#22-blast-width)

### 9.23. cSearchRadius[¶](#923-csearchradius "Permanent link")

Value: `int 23`

This is the attribute [Search Radius](./../../attributes/attributes/#23-search-radius)

### 9.24. cBonusResistance[¶](#924-cbonusresistance "Permanent link")

Value: `int 24`

This is the attribute [Bonus Damage Resistance](./../../attributes/attributes/#24-bonus-damage-resistance)

### 9.25. cIconId[¶](#925-ciconid "Permanent link")

Value: `int 25`

This is the attribute [Icon ID](./../../attributes/attributes/#25-icon-id)

### 9.26. cAmountSecondStorage[¶](#926-camountsecondstorage "Permanent link")

Value: `int 26`

This is the attribute [Amount of 2nd Resource Storage](./../../attributes/attributes/#26-amount-of-2nd-resource-storage)

### 9.27. cAmountThirdStorage[¶](#927-camountthirdstorage "Permanent link")

Value: `int 27`

This is the attribute [Amount of 3rd Resource Storage](./../../attributes/attributes/#27-amount-of-3rd-resource-storage)

### 9.28. cFogFlag[¶](#928-cfogflag "Permanent link")

Value: `int 28`

This is the attribute [Fog Visibility](./../../attributes/attributes/#28-fog-visibility)

### 9.29. cOcclusionMode[¶](#929-cocclusionmode "Permanent link")

Value: `int 29`

This is the attribute [Occlusion Mode](./../../attributes/attributes/#29-occlusion-mode)

### 9.30. cGarrisonType[¶](#930-cgarrisontype "Permanent link")

Value: `int 30`

This is the attribute [Garrison Type](./../../attributes/attributes/#30-garrison-type)

### 9.31. cUnitSizeZ[¶](#931-cunitsizez "Permanent link")

Value: `int 32`

This is the attribute [Unit Size Z](./../../attributes/attributes/#32-unit-size-z)

### 9.32. cCanBeBuiltOn[¶](#932-ccanbebuilton "Permanent link")

Value: `int 33`

This is the attribute [Can Be Built On](./../../attributes/attributes/#33-can-be-built-on)

### 9.33. cFoundationTerrain[¶](#933-cfoundationterrain "Permanent link")

Value: `int 34`

This is the attribute [Foundation Terrain](./../../attributes/attributes/#34-foundation-terrain)

### 9.34. cHeroStatus[¶](#934-cherostatus "Permanent link")

Value: `int 40`

This is the attribute [Hero Status](./../../attributes/attributes/#40-hero-status)

### 9.35. cAttackDelay[¶](#935-cattackdelay "Permanent link")

Value: `int 41`

This is the attribute [Frame Delay](./../../attributes/attributes/#41-frame-delay)

### 9.36. cTrainLocation[¶](#936-ctrainlocation "Permanent link")

Value: `int 42`

This is the attribute [Train Location](./../../attributes/attributes/#42-train-location)

### 9.37. cTrainButton[¶](#937-ctrainbutton "Permanent link")

Value: `int 43`

This is the attribute [Train Button](./../../attributes/attributes/#43-train-button)

### 9.38. cBlastAttackLevel[¶](#938-cblastattacklevel "Permanent link")

Value: `int 44`

This is the attribute [Blast Attack Level](./../../attributes/attributes/#44-blast-attack-level)

### 9.39. cBlastDefenseLevel[¶](#939-cblastdefenselevel "Permanent link")

Value: `int 45`

This is the attribute [Blast Defense Level](./../../attributes/attributes/#45-blast-defense-level)

### 9.40. cShownAttack[¶](#940-cshownattack "Permanent link")

Value: `int 46`

This is the attribute [Shown Attack](./../../attributes/attributes/#46-shown-attack)

### 9.41. cShownRange[¶](#941-cshownrange "Permanent link")

Value: `int 47`

This is the attribute [Shown Range](./../../attributes/attributes/#47-shown-range)

### 9.42. cShownMeleeArmor[¶](#942-cshownmeleearmor "Permanent link")

Value: `int 48`

This is the attribute [Shown Melee Armor](./../../attributes/attributes/#48-shown-melee-armor)

### 9.43. cShownPierceArmor[¶](#943-cshownpiercearmor "Permanent link")

Value: `int 49`

This is the attribute [Shown Pierce Armor](./../../attributes/attributes/#49-shown-pierce-armor)

### 9.44. cNameId[¶](#944-cnameid "Permanent link")

Value: `int 50`

This is the attribute [Object Name ID](./../../attributes/attributes/#50-object-name-id)

### 9.45. cDescriptionId[¶](#945-cdescriptionid "Permanent link")

Value: `int 51`

This is the attribute [Short Description ID](./../../attributes/attributes/#51-short-description-id)

### 9.46. cTerrainTable[¶](#946-cterraintable "Permanent link")

Value: `int 53`

This is the attribute [Terrain Restriction ID](./../../attributes/attributes/#53-terrain-restriction-id)

### 9.47. cTraits[¶](#947-ctraits "Permanent link")

Value: `int 54`

This is the attribute [Unit Trait](./../../attributes/attributes/#54-unit-trait)

### 9.48. cTraitPiece[¶](#948-ctraitpiece "Permanent link")

Value: `int 56`

This is the attribute [Trait Piece](./../../attributes/attributes/#56-trait-piece)

### 9.49. cDeadUnitId[¶](#949-cdeadunitid "Permanent link")

Value: `int 57`

This is the attribute [Dead Unit ID](./../../attributes/attributes/#57-dead-unit-id)

### 9.50. cHotkeyId[¶](#950-chotkeyid "Permanent link")

Value: `int 58`

This is the attribute [Hotkey ID](./../../attributes/attributes/#58-hotkey-id)

### 9.51. cMaxCharge[¶](#951-cmaxcharge "Permanent link")

Value: `int 59`

This is the attribute [Maximum Charge](./../../attributes/attributes/#59-maximum-charge)

### 9.52. cRechargeRate[¶](#952-crechargerate "Permanent link")

Value: `int 60`

This is the attribute [Recharge Rate](./../../attributes/attributes/#60-recharge-rate)

### 9.53. cChargeEvent[¶](#953-cchargeevent "Permanent link")

Value: `int 61`

This is the attribute [Charge Event](./../../attributes/attributes/#61-charge-event)

### 9.54. cChargeType[¶](#954-cchargetype "Permanent link")

Value: `int 62`

This is the attribute [Charge Type](./../../attributes/attributes/#62-charge-type)

### 9.55. cCombatAbility[¶](#955-ccombatability "Permanent link")

Value: `int 63`

This is the attribute [Combat Ability](./../../attributes/attributes/#63-combat-ability)

### 9.56. cAttackDispersion[¶](#956-cattackdispersion "Permanent link")

Value: `int 64`

This is the attribute [Attack Dispersion](./../../attributes/attributes/#64-attack-dispersion)

### 9.57. cSecondaryProjectileUnit[¶](#957-csecondaryprojectileunit "Permanent link")

Value: `int 65`

This is the attribute [Secondary Projectile Unit](./../../attributes/attributes/#65-secondary-projectile-unit)

### 9.58. cBloodUnitId[¶](#958-cbloodunitid "Permanent link")

Value: `int 66`

This is the attribute [Blood Unit](./../../attributes/attributes/#66-blood-unit)

### 9.59. cHitMode[¶](#959-chitmode "Permanent link")

Value: `int 67`

This is the attribute [Projectile Hit Mode](./../../attributes/attributes/#67-projectile-hit-mode)

### 9.60. cVanishMode[¶](#960-cvanishmode "Permanent link")

Value: `int 68`

This is the attribute [Projectile Vanish Mode](./../../attributes/attributes/#68-projectile-vanish-mode)

### 9.61. cProjectileArc[¶](#961-cprojectilearc "Permanent link")

Value: `int 69`

This is the attribute [Projectile Arc](./../../attributes/attributes/#69-projectile-arc)

### 9.62. cAttackGraphic[¶](#962-cattackgraphic "Permanent link")

Value: `int 70`

This is the attribute [Attack Graphic](./../../attributes/attributes/#70-attack-graphic)

### 9.63. cStandingGraphic[¶](#963-cstandinggraphic "Permanent link")

Value: `int 71`

This is the attribute [Standing Graphic](./../../attributes/attributes/#71-standing-graphic)

### 9.64. cStanding2Graphic[¶](#964-cstanding2graphic "Permanent link")

Value: `int 72`

This is the attribute [Standing Graphic 2](./../../attributes/attributes/#72-standing-graphic-2)

### 9.65. cDyingGraphic[¶](#965-cdyinggraphic "Permanent link")

Value: `int 73`

This is the attribute [Dying Graphic](./../../attributes/attributes/#73-dying-graphic)

### 9.66. cUndeadGraphic[¶](#966-cundeadgraphic "Permanent link")

Value: `int 74`

This is the attribute [Undead Graphic](./../../attributes/attributes/#74-undead-graphic)

### 9.67. cWalkingGraphic[¶](#967-cwalkinggraphic "Permanent link")

Value: `int 75`

This is the attribute [Walking Graphic](./../../attributes/attributes/#75-walking-graphic)

### 9.68. cRunningGraphic[¶](#968-crunninggraphic "Permanent link")

Value: `int 76`

This is the attribute [Running Graphic](./../../attributes/attributes/#76-running-graphic)

### 9.69. cSpecialGraphic[¶](#969-cspecialgraphic "Permanent link")

Value: `int 77`

This is the attribute [Special Graphic](./../../attributes/attributes/#77-special-graphic)

### 9.70. cObstructionType[¶](#970-cobstructiontype "Permanent link")

Value: `int 78`

This is the attribute [Obstruction Type](./../../attributes/attributes/#78-obstruction-type)

### 9.71. cBlockageClass[¶](#971-cblockageclass "Permanent link")

Value: `int 79`

This is the attribute [Blockage Class](./../../attributes/attributes/#79-blockage-class)

### 9.72. cSelectionEffect[¶](#972-cselectioneffect "Permanent link")

Value: `int 80`

This is the attribute [Selection Effect](./../../attributes/attributes/#80-selection-effect)

### 9.73. cSpecialAbility[¶](#973-cspecialability "Permanent link")

Value: `int 81`

This is the attribute [Special Ability](./../../attributes/attributes/#81-special-ability)

### 9.74. cIdleAttackGraphic[¶](#974-cidleattackgraphic "Permanent link")

Value: `int 82`

This is the attribute [Idle Attack Graphic](./../../attributes/attributes/#82-idle-attack-graphic)

### 9.75. cHeroGlowGraphic[¶](#975-cheroglowgraphic "Permanent link")

Value: `int 83`

This is the attribute [Hero Glow Graphic](./../../attributes/attributes/#83-hero-glow-graphic)

### 9.76. cGarrisonGraphic[¶](#976-cgarrisongraphic "Permanent link")

Value: `int 84`

This is the attribute [Garrison Graphic](./../../attributes/attributes/#84-garrison-graphic)

### 9.77. cConstructionGraphic[¶](#977-cconstructiongraphic "Permanent link")

Value: `int 85`

This is the attribute [Construction Graphic](./../../attributes/attributes/#85-construction-graphic)

### 9.78. cSnowGraphic[¶](#978-csnowgraphic "Permanent link")

Value: `int 86`

This is the attribute [Snow Graphic](./../../attributes/attributes/#86-snow-graphic)

### 9.79. cDestructionGraphic[¶](#979-cdestructiongraphic "Permanent link")

Value: `int 87`

This is the attribute [Destruction Graphic](./../../attributes/attributes/#87-destruction-graphic)

### 9.80. cDestructionRubbleGraphic[¶](#980-cdestructionrubblegraphic "Permanent link")

Value: `int 88`

This is the attribute [Destruction Rubble Graphic](./../../attributes/attributes/#88-destruction-rubble-graphic)

### 9.81. cResearchingGraphic[¶](#981-cresearchinggraphic "Permanent link")

Value: `int 89`

This is the attribute [Researching Graphic](./../../attributes/attributes/#89-researching-graphic)

### 9.82. cResearchCompletedGraphic[¶](#982-cresearchcompletedgraphic "Permanent link")

Value: `int 90`

This is the attribute [Research Completed Graphic](./../../attributes/attributes/#90-research-completed-graphic)

### 9.83. cDamageGraphic[¶](#983-cdamagegraphic "Permanent link")

Value: `int 91`

This is the attribute [Damage Graphic](./../../attributes/attributes/#91-damage-graphic)

### 9.84. cSelectionSound[¶](#984-cselectionsound "Permanent link")

Value: `int 92`

This is the attribute [Selection Sound](./../../attributes/attributes/#92-selection-sound)

### 9.85. cSelectionSoundEvent[¶](#985-cselectionsoundevent "Permanent link")

Value: `int 93`

This is the attribute [Selection Sound Event](./../../attributes/attributes/#93-selection-sound-event)

### 9.86. cDyingSound[¶](#986-cdyingsound "Permanent link")

Value: `int 94`

This is the attribute [Dying Sound](./../../attributes/attributes/#94-dying-sound)

### 9.87. cDyingSoundEvent[¶](#987-cdyingsoundevent "Permanent link")

Value: `int 95`

This is the attribute [Dying Sound Event](./../../attributes/attributes/#95-dying-sound-event)

### 9.88. cTrainSound[¶](#988-ctrainsound "Permanent link")

Value: `int 96`

This is the attribute [Train Sound](./../../attributes/attributes/#96-train-sound)

### 9.89. cTrainSoundEvent[¶](#989-ctrainsoundevent "Permanent link")

Value: `int 97`

This is the attribute [Train Sound Event](./../../attributes/attributes/#97-train-sound-event)

### 9.90. cDamageSound[¶](#990-cdamagesound "Permanent link")

Value: `int 98`

This is the attribute [Damage Sound](./../../attributes/attributes/#98-damage-sound)

### 9.91. cDamageSoundEvent[¶](#991-cdamagesoundevent "Permanent link")

Value: `int 99`

This is the attribute [Damage Sound Event](./../../attributes/attributes/#99-damage-sound-event)

### 9.92. cResourceCost[¶](#992-cresourcecost "Permanent link")

Value: `int 100`

This is the attribute [Resource Costs](./../../attributes/attributes/#100-resource-costs)

### 9.93. cTrainTime[¶](#993-ctraintime "Permanent link")

Value: `int 101`

This is the attribute [Train Time](./../../attributes/attributes/#101-train-time)

### 9.94. cTotalProjectiles[¶](#994-ctotalprojectiles "Permanent link")

Value: `int 102`

This is the attribute [Total Missiles](./../../attributes/attributes/#102-total-missiles)

### 9.95. cFoodCost[¶](#995-cfoodcost "Permanent link")

Value: `int 103`

This is the attribute [Food Costs](./../../attributes/attributes/#103-food-costs)

### 9.96. cWoodCost[¶](#996-cwoodcost "Permanent link")

Value: `int 104`

This is the attribute [Wood Costs](./../../attributes/attributes/#104-wood-costs)

### 9.97. cGoldCost[¶](#997-cgoldcost "Permanent link")

Value: `int 105`

This is the attribute [Gold Costs](./../../attributes/attributes/#105-gold-costs)

### 9.98. cStoneCost[¶](#998-cstonecost "Permanent link")

Value: `int 106`

This is the attribute [Stone Costs](./../../attributes/attributes/#106-stone-costs)

### 9.99. cMaxTotalProjectiles[¶](#999-cmaxtotalprojectiles "Permanent link")

Value: `int 107`

This is the attribute [Max Total Missiles](./../../attributes/attributes/#107-max-total-missiles)

### 9.100. cGarrisonHealRate[¶](#9100-cgarrisonhealrate "Permanent link")

Value: `int 108`

This is the attribute [Garrison Heal Rate](./../../attributes/attributes/#108-garrison-heal-rate)

### 9.101. cRegenerationRate[¶](#9101-cregenerationrate "Permanent link")

Value: `int 109`

This is the attribute [Regeneration Rate](./../../attributes/attributes/#109-regeneration-rate)

### 9.102. cPopulation[¶](#9102-cpopulation "Permanent link")

Value: `int 110`

This is the attribute [Population](./../../attributes/attributes/#110-population)

### 9.103. cMinConversionTimeMod[¶](#9103-cminconversiontimemod "Permanent link")

Value: `int 111`

This is the attribute [Minimum Conversion Time Modifier](./../../attributes/attributes/#111-minimum-conversion-time-modifier)

### 9.104. cMaxConversionTimeMod[¶](#9104-cmaxconversiontimemod "Permanent link")

Value: `int 112`

This is the attribute [Maximum Conversion Time Modifier](./../../attributes/attributes/#112-maximum-conversion-time-modifier)

### 9.105. cConversionChanceMod[¶](#9105-cconversionchancemod "Permanent link")

Value: `int 113`

This is the attribute [Conversion Chance Modifier](./../../attributes/attributes/#113-conversion-chance-modifier)

### 9.106. cFormationCategory[¶](#9106-cformationcategory "Permanent link")

Value: `int 114`

This is the attribute [Formation Category](./../../attributes/attributes/#114-formation-category)

### 9.107. cAreaDamage[¶](#9107-careadamage "Permanent link")

Value: `int 115`

This is the attribute [Area Damage](./../../attributes/attributes/#115-area-damage)

### 9.108. cDamageReflection[¶](#9108-cdamagereflection "Permanent link")

Value: `int 118`

This is the attribute [Damage Reflection](./../../attributes/attributes/#118-damage-reflection)

### 9.109. cFriendlyFireDamage[¶](#9109-cfriendlyfiredamage "Permanent link")

Value: `int 119`

This is the attribute [Friendly Fire Damage](./../../attributes/attributes/#119-friendly-fire-damage)

### 9.110. cRegenerationHpPercent[¶](#9110-cregenerationhppercent "Permanent link")

Value: `int 120`

This is the attribute [Regeneration Hp Percent](./../../attributes/attributes/#120-regeneration-hp-percent)

### 9.111. cButtonIconId[¶](#9111-cbuttoniconid "Permanent link")

Value: `int 121`

This is the attribute [Button Icon Id](./../../attributes/attributes/#121-button-icon-id)

### 9.112. cShortTooltipId[¶](#9112-cshorttooltipid "Permanent link")

Value: `int 122`

This is the attribute [Short Tooltip Id](./../../attributes/attributes/#122-short-tooltip-id)

### 9.113. cExtendedTooltipId[¶](#9113-cextendedtooltipid "Permanent link")

Value: `int 123`

This is the attribute [Extended Tooltip Id](./../../attributes/attributes/#123-extended-tooltip-id)

### 9.114. cHotkeyAction[¶](#9114-chotkeyaction "Permanent link")

Value: `int 124`

This is the attribute [Hotkey Action](./../../attributes/attributes/#124-hotkey-action)

### 9.115. cChargeProjectileUnit[¶](#9115-cchargeprojectileunit "Permanent link")

Value: `int 125`

This is the attribute [Charge Projectile Unit](./../../attributes/attributes/#125-charge-projectile-unit)

### 9.116. cAvailableFlag[¶](#9116-cavailableflag "Permanent link")

Value: `int 126`

This is the attribute [Available Flag](./../../attributes/attributes/#126-available-flag)

### 9.117. cDisabledFlag[¶](#9117-cdisabledflag "Permanent link")

Value: `int 127`

This is the attribute [Disabled Flag](./../../attributes/attributes/#127-disabled-flag)

### 9.118. cAttackPriority[¶](#9118-cattackpriority "Permanent link")

Value: `int 128`

This is the attribute [Attack Priority](./../../attributes/attributes/#128-attack-priority)

### 9.119. cInvulnerabilityLevel[¶](#9119-cinvulnerabilitylevel "Permanent link")

Value: `int 129`

This is the attribute [Invulnerability Level](./../../attributes/attributes/#129-invulnerability-level)

### 9.120. cGarrisonFirepower[¶](#9120-cgarrisonfirepower "Permanent link")

Value: `int 130`

This is the attribute [Garrison Firepower](./../../attributes/attributes/#130-garrison-firepower)

### 9.121. cAttack2Graphic[¶](#9121-cattack2graphic "Permanent link")

Value: `int 131`

This is the attribute [Attack Graphic 2](./../../attributes/attributes/#131-attack-graphic-2).

### 9.122. cCommandSound[¶](#9122-ccommandsound "Permanent link")

Value: `int 132`

This is the attribute [Command Sound](./../../attributes/attributes/#132-command-sound).

### 9.123. cCommandSoundEvent[¶](#9123-ccommandsoundevent "Permanent link")

Value: `int 133`

This is the attribute [Command Sound Event](./../../attributes/attributes/#133-command-sound-event).

### 9.124. cMoveSound[¶](#9124-cmovesound "Permanent link")

Value: `int 134`

This is the attribute [Move Sound](./../../attributes/attributes/#134-move-sound).

### 9.125. cMoveSoundEvent[¶](#9125-cmovesoundevent "Permanent link")

Value: `int 135`

This is the attribute [Move Sound Event](./../../attributes/attributes/#135-move-sound-event).

### 9.126. cConstructionSound[¶](#9126-cconstructionsound "Permanent link")

Value: `int 136`

This is the attribute [Construction Sound](./../../attributes/attributes/#136-construction-sound).

### 9.127. cConstructionSoundEvent[¶](#9127-cconstructionsoundevent "Permanent link")

Value: `int 137`

This is the attribute [Construction Sound Event](./../../attributes/attributes/#137-construction-sound-event).

### 9.128. cTransformSound[¶](#9128-ctransformsound "Permanent link")

Value: `int 138`

This is the attribute [Transform Sound](./../../attributes/attributes/#138-transform-sound).

### 9.129. cTransformSoundEvent[¶](#9129-ctransformsoundevent "Permanent link")

Value: `int 139`

This is the attribute [Transform Sound Event](./../../attributes/attributes/#139-transform-sound-event).

### 9.130. cRunPattern[¶](#9130-crunpattern "Permanent link")

Value: `int 140`

This is the attribute [Run Pattern](./../../attributes/attributes/#140-run-pattern).

### 9.131. cInterfaceKind[¶](#9131-cinterfacekind "Permanent link")

Value: `int 141`

This is the attribute [Interface Kind](./../../attributes/attributes/#141-interface-kind).

### 9.132. cCombatLevel[¶](#9132-ccombatlevel "Permanent link")

Value: `int 142`

This is the attribute [Combat Level](./../../attributes/attributes/#142-combat-level).

### 9.133. cInteractionMode[¶](#9133-cinteractionmode "Permanent link")

Value: `int 143`

This is the attribute [Interaction Mode](./../../attributes/attributes/#143-interaction-mode).

### 9.134. cMinimapMode[¶](#9134-cminimapmode "Permanent link")

Value: `int 144`

This is the attribute [Minimap Mode](./../../attributes/attributes/#144-minimap-mode).

### 9.135. cTrailingUnit[¶](#9135-ctrailingunit "Permanent link")

Value: `int 145`

This is the attribute [Trailing Unit](./../../attributes/attributes/#145-trailing-unit).

### 9.136. cTrailMode[¶](#9136-ctrailmode "Permanent link")

Value: `int 146`

This is the attribute [Trail Mode](./../../attributes/attributes/#146-trail-mode).

### 9.137. cTrailDensity[¶](#9137-ctraildensity "Permanent link")

Value: `int 147`

This is the attribute [Trail Density](./../../attributes/attributes/#147-trail-density).

### 9.138. cProjectileGraphicDisplacementX[¶](#9138-cprojectilegraphicdisplacementx "Permanent link")

Value: `int 148`

This is the attribute [Projectile Graphic Displacement X](./../../attributes/attributes/#148-projectile-graphic-displacement-x).

### 9.139. cProjectileGraphicDisplacementY[¶](#9139-cprojectilegraphicdisplacementy "Permanent link")

Value: `int 149`

This is the attribute [Projectile Graphic Displacement Y](./../../attributes/attributes/#149-projectile-graphic-displacement-y).

### 9.140. cProjectileGraphicDisplacementZ[¶](#9140-cprojectilegraphicdisplacementz "Permanent link")

Value: `int 150`

This is the attribute [Projectile Graphic Displacement Z](./../../attributes/attributes/#150-projectile-graphic-displacement-z).

### 9.141. cProjectileSpawningAreaWidth[¶](#9141-cprojectilespawningareawidth "Permanent link")

Value: `int 151`

This is the attribute [Projectile Spawning Area Width](./../../attributes/attributes/#151-projectile-spawning-area-width).

### 9.142. cProjectileSpawningAreaLength[¶](#9142-cprojectilespawningarealength "Permanent link")

Value: `int 152`

This is the attribute [Projectile Spawning Area Length](./../../attributes/attributes/#152-projectile-spawning-area-length).

### 9.143. cProjectileSpawningAreaRandomness[¶](#9143-cprojectilespawningarearandomness "Permanent link")

Value: `int 153`

This is the attribute [Projectile Spawning Area Randomness](./../../attributes/attributes/#153-projectile-spawning-area-randomness).

### 9.144. cDamageGraphicsEntryMod[¶](#9144-cdamagegraphicsentrymod "Permanent link")

Value: `int 154`

This is the attribute [Damage Graphics Entry Mod](./../../attributes/attributes/#154-damage-graphics-entry-mod).

### 9.145. cDamageGraphicsTotalNum[¶](#9145-cdamagegraphicstotalnum "Permanent link")

Value: `int 155`

This is the attribute [Damage Graphics Total Num](./../../attributes/attributes/#155-damage-graphics-total-num).

### 9.146. cDamageGraphicPercent[¶](#9146-cdamagegraphicpercent "Permanent link")

Value: `int 156`

This is the attribute [Damage Graphic Percent](./../../attributes/attributes/#156-damage-graphic-percent).

### 9.147. cDamageGraphicApplyMode[¶](#9147-cdamagegraphicapplymode "Permanent link")

Value: `int 157`

This is the attribute [Damage Graphic Apply Mode](./../../attributes/attributes/#157-damage-graphic-apply-mode).

## 10. EffectAmount Object Class[¶](#10-effectamount-object-class "Permanent link")

### 10.1. cArcherClass[¶](#101-carcherclass "Permanent link")

Value: `int 900`

This is the ID used to target the Archer Class

### 10.2. cArtifactClass[¶](#102-cartifactclass "Permanent link")

Value: `int 901`

This is the ID used to target the Artifact Class

### 10.3. cTradeBoatClass[¶](#103-ctradeboatclass "Permanent link")

Value: `int 902`

This is the ID used to target the Trade Boat Class

### 10.4. cBuildingClass[¶](#104-cbuildingclass "Permanent link")

Value: `int 903`

This is the ID used to target the Building Class

### 10.5. cVillagerClass[¶](#105-cvillagerclass "Permanent link")

Value: `int 904`

This is the ID used to target the Villager Class

### 10.6. cSeaFishClass[¶](#106-cseafishclass "Permanent link")

Value: `int 905`

This is the ID used to target the Sea Fish Class

### 10.7. cInfantryClass[¶](#107-cinfantryclass "Permanent link")

Value: `int 906`

This is the ID used to target the Infantry Class

### 10.8. cForageBushClass[¶](#108-cforagebushclass "Permanent link")

Value: `int 907`

This is the ID used to target the Forage Bush Class

### 10.9. cStoneMineClass[¶](#109-cstonemineclass "Permanent link")

Value: `int 908`

This is the ID used to target the Stone Mine Class

### 10.10. cPreyAnimalClass[¶](#1010-cpreyanimalclass "Permanent link")

Value: `int 909`

This is the ID used to target the Prey Animal Class

### 10.11. cPredatorAnimalClass[¶](#1011-cpredatoranimalclass "Permanent link")

Value: `int 910`

This is the ID used to target the Predator Animal Class

### 10.12. cMiscellaneousClass[¶](#1012-cmiscellaneousclass "Permanent link")

Value: `int 911`

This is the ID used to target the Miscellaneous Class

### 10.13. cCavalryClass[¶](#1013-ccavalryclass "Permanent link")

Value: `int 912`

This is the ID used to target the Cavalry Class

### 10.14. cSiegeWeaponClass[¶](#1014-csiegeweaponclass "Permanent link")

Value: `int 913`

This is the ID used to target the Siege Weapon Class

### 10.15. cTerrainClass[¶](#1015-cterrainclass "Permanent link")

Value: `int 914`

This is the ID used to target the Terrain Class

### 10.16. cTreeClass[¶](#1016-ctreeclass "Permanent link")

Value: `int 915`

This is the ID used to target the Tree Class

### 10.17. cTreeStumpClass[¶](#1017-ctreestumpclass "Permanent link")

Value: `int 916`

This is the ID used to target the Tree Stump Class

### 10.18. cHealerClass[¶](#1018-chealerclass "Permanent link")

Value: `int 917`

This is the ID used to target the Healer Class

### 10.19. cMonkClass[¶](#1019-cmonkclass "Permanent link")

Value: `int 918`

This is the ID used to target the Monk Class

### 10.20. cTradeCartClass[¶](#1020-ctradecartclass "Permanent link")

Value: `int 919`

This is the ID used to target the Trade Cart Class

### 10.21. cTransportShipClass[¶](#1021-ctransportshipclass "Permanent link")

Value: `int 920`

This is the ID used to target the Transport Ship Class

### 10.22. cFishingBoatClass[¶](#1022-cfishingboatclass "Permanent link")

Value: `int 921`

This is the ID used to target the Fishing Boat Class

### 10.23. cWarshipClass[¶](#1023-cwarshipclass "Permanent link")

Value: `int 922`

This is the ID used to target the Warship Class

### 10.24. cConquistadorClass[¶](#1024-cconquistadorclass "Permanent link")

Value: `int 923`

This is the ID used to target the Conquistador Class

### 10.25. cWarElephantClass[¶](#1025-cwarelephantclass "Permanent link")

Value: `int 924`

This is the ID used to target the War Elephant Class

### 10.26. cHeroClass[¶](#1026-cheroclass "Permanent link")

Value: `int 925`

This is the ID used to target the Hero Class

### 10.27. cElephantArcherClass[¶](#1027-celephantarcherclass "Permanent link")

Value: `int 926`

This is the ID used to target the Elephant Archer Class

### 10.28. cWallClass[¶](#1028-cwallclass "Permanent link")

Value: `int 927`

This is the ID used to target the Wall Class

### 10.29. cPhalanxClass[¶](#1029-cphalanxclass "Permanent link")

Value: `int 928`

This is the ID used to target the Phalanx Class

### 10.30. cDomesticAnimalClass[¶](#1030-cdomesticanimalclass "Permanent link")

Value: `int 929`

This is the ID used to target the Domestic Animal Class

### 10.31. cFlagClass[¶](#1031-cflagclass "Permanent link")

Value: `int 930`

This is the ID used to target the Flag Class

### 10.32. cDeepSeaFishClass[¶](#1032-cdeepseafishclass "Permanent link")

Value: `int 931`

This is the ID used to target the Deep Sea Fish Class

### 10.33. cGoldMine[¶](#1033-cgoldmine "Permanent link")

Value: `int 932`

This is the ID used to target the Gold Mine

### 10.34. cShoreFish[¶](#1034-cshorefish "Permanent link")

Value: `int 933`

This is the ID used to target the Shore Fish

### 10.35. cCliffClass[¶](#1035-ccliffclass "Permanent link")

Value: `int 934`

This is the ID used to target the Cliff Class

### 10.36. cPetardClass[¶](#1036-cpetardclass "Permanent link")

Value: `int 935`

This is the ID used to target the Petard Class

### 10.37. cCavalryArcherClass[¶](#1037-ccavalryarcherclass "Permanent link")

Value: `int 936`

This is the ID used to target the Cavalry Archer Class

### 10.38. cDoppelgangerClass[¶](#1038-cdoppelgangerclass "Permanent link")

Value: `int 937`

This is the ID used to target the Doppelganger Class

### 10.39. cBirdClass[¶](#1039-cbirdclass "Permanent link")

Value: `int 938`

This is the ID used to target the Bird Class

### 10.40. cGateClass[¶](#1040-cgateclass "Permanent link")

Value: `int 939`

This is the ID used to target the Gate Class

### 10.41. cSalvagePileClass[¶](#1041-csalvagepileclass "Permanent link")

Value: `int 940`

This is the ID used to target the Salvage Pile Class

### 10.42. cResourcePileClass[¶](#1042-cresourcepileclass "Permanent link")

Value: `int 941`

This is the ID used to target the Resource Pile Class

### 10.43. cRelicClass[¶](#1043-crelicclass "Permanent link")

Value: `int 942`

This is the ID used to target the Relic Class

### 10.44. cMonkWithRelicClass[¶](#1044-cmonkwithrelicclass "Permanent link")

Value: `int 943`

This is the ID used to target the Monk With Relic Class

### 10.45. cHandCannoneerClass[¶](#1045-chandcannoneerclass "Permanent link")

Value: `int 944`

This is the ID used to target the Hand Cannoneer Class

### 10.46. cTwoHandedSwordsmanClass[¶](#1046-ctwohandedswordsmanclass "Permanent link")

Value: `int 945`

This is the ID used to target the Two Handed Swordsman Class

### 10.47. cPikemanClass[¶](#1047-cpikemanclass "Permanent link")

Value: `int 946`

This is the ID used to target the Pikeman Class

### 10.48. cScoutCavalryClass[¶](#1048-cscoutcavalryclass "Permanent link")

Value: `int 947`

This is the ID used to target the Scout Cavalry Class

### 10.49. cOreMineClass[¶](#1049-coremineclass "Permanent link")

Value: `int 948`

This is the ID used to target the Ore Mine Class

### 10.50. cFarmClass[¶](#1050-cfarmclass "Permanent link")

Value: `int 949`

This is the ID used to target the Farm Class

### 10.51. cSpearmanClass[¶](#1051-cspearmanclass "Permanent link")

Value: `int 950`

This is the ID used to target the Spearman Class

### 10.52. cPackedUnitClass[¶](#1052-cpackedunitclass "Permanent link")

Value: `int 951`

This is the ID used to target the Packed Unit Class

### 10.53. cTowerClass[¶](#1053-ctowerclass "Permanent link")

Value: `int 952`

This is the ID used to target the Tower Class

### 10.54. cBoardingShipClass[¶](#1054-cboardingshipclass "Permanent link")

Value: `int 953`

This is the ID used to target the Boarding Ship Class

### 10.55. cUnpackedSiegeUnitClass[¶](#1055-cunpackedsiegeunitclass "Permanent link")

Value: `int 954`

This is the ID used to target the Unpacked Siege Unit Class

### 10.56. cScorpionClass[¶](#1056-cscorpionclass "Permanent link")

Value: `int 955`

This is the ID used to target the Scorpion Class

### 10.57. cRaiderClass[¶](#1057-craiderclass "Permanent link")

Value: `int 956`

This is the ID used to target the Raider Class

### 10.58. cCavalryRaiderClass[¶](#1058-ccavalryraiderclass "Permanent link")

Value: `int 957`

This is the ID used to target the Cavalry Raider Class

### 10.59. cLivestockClass[¶](#1059-clivestockclass "Permanent link")

Value: `int 958`

This is the ID used to target the Livestock Class

### 10.60. cKingClass[¶](#1060-ckingclass "Permanent link")

Value: `int 959`

This is the ID used to target the King Class

### 10.61. cMiscBuildingClass[¶](#1061-cmiscbuildingclass "Permanent link")

Value: `int 960`

This is the ID used to target the Misc Building Class

### 10.62. cControlledAnimalClass[¶](#1062-ccontrolledanimalclass "Permanent link")

Value: `int 961`

This is the ID used to target the Controlled Animal Class

### 10.63. cGoldFishClass[¶](#1063-cgoldfishclass "Permanent link")

Value: `int 963`

This is the ID used to target the Gold Fish Class

### 10.64. cLandMineClass[¶](#1064-clandmineclass "Permanent link")

Value: `int 964`

This is the ID used to target the Land Mine Class

## 11. Resource[¶](#11-resource "Permanent link")

### 11.1. cAttributeFood[¶](#111-cattributefood "Permanent link")

Value: `int 0`

ID of the player resource Food. Check [here](../../resources/resources/#0-food-storage "Jump to: Game Mecahnicsc > Resources > #0-food-storage") for more info about what this resource does.

### 11.2. cAttributeWood[¶](#112-cattributewood "Permanent link")

Value: `int 1`

ID of the player resource Wood. Check [here](../../resources/resources/#1-wood-storage "Jump to: Game Mecahnicsc > Resources > #1-wood-storage") for more info about what this resource does.

### 11.3. cAttributeStone[¶](#113-cattributestone "Permanent link")

Value: `int 2`

ID of the player resource Stone. Check [here](../../resources/resources/#2-stone-storage "Jump to: Game Mecahnicsc > Resources > #2-stone-storage") for more info about what this resource does.

### 11.4. cAttributeGold[¶](#114-cattributegold "Permanent link")

Value: `int 3`

ID of the player resource Gold. Check [here](../../resources/resources/#3-gold-storage "Jump to: Game Mecahnicsc > Resources > #3-gold-storage") for more info about what this resource does.

### 11.5. cAttributePopulationCap[¶](#115-cattributepopulationcap "Permanent link")

Value: `int 4`

ID of the player resource Population Cap. Check [here](../../resources/resources/#4-population-headroom "Jump to: Game Mecahnicsc > Resources > #4-population-headroom") for more info about what this resource does.

### 11.6. cAttributeReligion[¶](#116-cattributereligion "Permanent link")

Value: `int 5`

ID of the player resource Religion. Check [here](../../resources/resources/#5-conversion-range "Jump to: Game Mecahnicsc > Resources > #5-conversion-range") for more info about what this resource does.

### 11.7. cAttributeCurrentAge[¶](#117-cattributecurrentage "Permanent link")

Value: `int 6`

ID of the player resource Current Age. Check [here](../../resources/resources/#6-current-age "Jump to: Game Mecahnicsc > Resources > #6-current-age") for more info about what this resource does.

### 11.8. cAttributeRelics[¶](#118-cattributerelics "Permanent link")

Value: `int 7`

ID of the player resource Relics. Check [here](../../resources/resources/#7-relics-captured "Jump to: Game Mecahnicsc > Resources > #7-relics-captured") for more info about what this resource does.

### 11.9. cAttributeTrageBonus[¶](#119-cattributetragebonus "Permanent link")

Value: `int 8`

ID of the player resource Trage Bonus. Click [here](../../resources/resources/#8-unused-resource-008 "Jump to: Game Mecahnicsc > Resources > #8-unused-resource-008"). The name is mispelled in the `Constants.xs` Check so thats how it needs to be used for more info about what this resource does.

### 11.10. cAttributeTradeGoods[¶](#1110-cattributetradegoods "Permanent link")

Value: `int 9`

ID of the player resource Trade Goods. Check [here](../../resources/resources/#9-trade-goods "Jump to: Game Mecahnicsc > Resources > #9-trade-goods") for more info about what this resource does.

### 11.11. cAttributeTradeProducation[¶](#1111-cattributetradeproducation "Permanent link")

Value: `int 10`

ID of the player resource Trade Producation. Check [here](../../resources/resources/#10-unused-resource-010 "Jump to: Game Mecahnicsc > Resources > #10-unused-resource-010") for more info about what this resource does.

### 11.12. cAttributePopulation[¶](#1112-cattributepopulation "Permanent link")

Value: `int 11`

ID of the player resource Population. Check [here](../../resources/resources/#11-current-population "Jump to: Game Mecahnicsc > Resources > #11-current-population") for more info about what this resource does.

### 11.13. cAttributeDecay[¶](#1113-cattributedecay "Permanent link")

Value: `int 12`

ID of the player resource Decay. Check [here](../../resources/resources/#12-corpse-decay-time "Jump to: Game Mecahnicsc > Resources > #12-corpse-decay-time") for more info about what this resource does.

### 11.14. cAttributeDiscovery[¶](#1114-cattributediscovery "Permanent link")

Value: `int 13`

ID of the player resource Discovery. Check [here](../../resources/resources/#13-remarkable-discovery "Jump to: Game Mecahnicsc > Resources > #13-remarkable-discovery") for more info about what this resource does.

### 11.15. cAttributeRuins[¶](#1115-cattributeruins "Permanent link")

Value: `int 14`

ID of the player resource Ruins. Check [here](../../resources/resources/#14-monuments-captured "Jump to: Game Mecahnicsc > Resources > #14-monuments-captured") for more info about what this resource does.

### 11.16. cAttributeMeat[¶](#1116-cattributemeat "Permanent link")

Value: `int 15`

ID of the player resource Meat. Check [here](../../resources/resources/#15-meat-storage "Jump to: Game Mecahnicsc > Resources > #15-meat-storage") for more info about what this resource does.

### 11.17. cAttributeBerries[¶](#1117-cattributeberries "Permanent link")

Value: `int 16`

ID of the player resource Berries. Check [here](../../resources/resources/#16-berry-storage "Jump to: Game Mecahnicsc > Resources > #16-berry-storage") for more info about what this resource does.

### 11.18. cAttributeFish[¶](#1118-cattributefish "Permanent link")

Value: `int 17`

ID of the player resource Fish. Check [here](../../resources/resources/#17-fish-storage "Jump to: Game Mecahnicsc > Resources > #17-fish-storage") for more info about what this resource does.

### 11.19. cAttributeKills[¶](#1119-cattributekills "Permanent link")

Value: `int 20`

ID of the player resource Kills. Check [here](../../resources/resources/#20-units-killed "Jump to: Game Mecahnicsc > Resources > #20-units-killed") for more info about what this resource does.

### 11.20. cAttributeResearchCount[¶](#1120-cattributeresearchcount "Permanent link")

Value: `int 21`

ID of the player resource Research Count. Check [here](../../resources/resources/#21-technology-count "Jump to: Game Mecahnicsc > Resources > #21-technology-count") for more info about what this resource does.

### 11.21. cAttributeExploration[¶](#1121-cattributeexploration "Permanent link")

Value: `int 22`

ID of the player resource Exploration. Check [here](../../resources/resources/#22--map-explored "Jump to: Game Mecahnicsc > Resources > #22--map-explored") for more info about what this resource does.

### 11.22. cAttributeConvertPriest[¶](#1122-cattributeconvertpriest "Permanent link")

Value: `int 27`

ID of the player resource Convert Priest. Check [here](../../resources/resources/#27-enable-monk-conversion "Jump to: Game Mecahnicsc > Resources > #27-enable-monk-conversion") for more info about what this resource does.

### 11.23. cAttributeConvertBuilding[¶](#1123-cattributeconvertbuilding "Permanent link")

Value: `int 28`

ID of the player resource Convert Building. Check [here](../../resources/resources/#28-enable-building-conversion "Jump to: Game Mecahnicsc > Resources > #28-enable-building-conversion") for more info about what this resource does.

### 11.24. cAttributeBuildingLimit[¶](#1124-cattributebuildinglimit "Permanent link")

Value: `int 30`

ID of the player resource Building Limit. Check [here](../../resources/resources/#30-unused-resource-030 "Jump to: Game Mecahnicsc > Resources > #30-unused-resource-030") for more info about what this resource does.

### 11.25. cAttributeFoodLimit[¶](#1125-cattributefoodlimit "Permanent link")

Value: `int 31`

ID of the player resource Food Limit. Check [here](../../resources/resources/#31-unused-resource-031 "Jump to: Game Mecahnicsc > Resources > #31-unused-resource-031") for more info about what this resource does.

### 11.26. cAttributeUnitLimit[¶](#1126-cattributeunitlimit "Permanent link")

Value: `int 32`

ID of the player resource Unit Limit. Check [here](../../resources/resources/#32-bonus-population-cap "Jump to: Game Mecahnicsc > Resources > #32-bonus-population-cap") for more info about what this resource does.

### 11.27. cAttributeMaintenance[¶](#1127-cattributemaintenance "Permanent link")

Value: `int 33`

ID of the player resource Maintenance. Check [here](../../resources/resources/#33-effect-function-number "Jump to: Game Mecahnicsc > Resources > #33-effect-function-number") for more info about what this resource does.

### 11.28. cAttributeFaith[¶](#1128-cattributefaith "Permanent link")

Value: `int 34`

ID of the player resource Faith. Check [here](../../resources/resources/#34-unused-resource-34 "Jump to: Game Mecahnicsc > Resources > #34-unused-resource-34") for more info about what this resource does.

### 11.29. cAttributeFaithRechargeRate[¶](#1129-cattributefaithrechargerate "Permanent link")

Value: `int 35`

ID of the player resource Faith Recharge Rate. Check [here](../../resources/resources/#35-unused-resource-35 "Jump to: Game Mecahnicsc > Resources > #35-unused-resource-35") for more info about what this resource does.

### 11.30. cAttributeFarmFood[¶](#1130-cattributefarmfood "Permanent link")

Value: `int 36`

ID of the player resource Farm Food. Check [here](../../resources/resources/#36-farm-food-amount "Jump to: Game Mecahnicsc > Resources > #36-farm-food-amount") for more info about what this resource does.

### 11.31. cAttributeCivilianPopulation[¶](#1131-cattributecivilianpopulation "Permanent link")

Value: `int 37`

ID of the player resource Civilian Population. Check [here](../../resources/resources/#37-civilian-population "Jump to: Game Mecahnicsc > Resources > #37-civilian-population") for more info about what this resource does.

### 11.32. cAttributeAllTechsAchieved[¶](#1132-cattributealltechsachieved "Permanent link")

Value: `int 39`

ID of the player resource All Techs Achieved. Check [here](../../resources/resources/#39-all-techs-achieved "Jump to: Game Mecahnicsc > Resources > #39-all-techs-achieved") for more info about what this resource does.

### 11.33. cAttributeMilitaryPopulation[¶](#1133-cattributemilitarypopulation "Permanent link")

Value: `int 40`

ID of the player resource Military Population. Check [here](../../resources/resources/#40-military-population "Jump to: Game Mecahnicsc > Resources > #40-military-population") for more info about what this resource does.

### 11.34. cAttributeConversions[¶](#1134-cattributeconversions "Permanent link")

Value: `int 41`

ID of the player resource Conversions. Check [here](../../resources/resources/#41-conversions "Jump to: Game Mecahnicsc > Resources > #41-conversions") for more info about what this resource does.

### 11.35. cAttributeWonder[¶](#1135-cattributewonder "Permanent link")

Value: `int 42`

ID of the player resource Wonder. Check [here](../../resources/resources/#42-standing-wonders "Jump to: Game Mecahnicsc > Resources > #42-standing-wonders") for more info about what this resource does.

### 11.36. cAttributeRazings[¶](#1136-cattributerazings "Permanent link")

Value: `int 43`

ID of the player resource Razings. Check [here](../../resources/resources/#43-razings "Jump to: Game Mecahnicsc > Resources > #43-razings") for more info about what this resource does.

### 11.37. cAttributeKillRatio[¶](#1137-cattributekillratio "Permanent link")

Value: `int 44`

ID of the player resource Kill Ratio. Check [here](../../resources/resources/#44-kill-ratio "Jump to: Game Mecahnicsc > Resources > #44-kill-ratio") for more info about what this resource does.

### 11.38. cAttributePlayerKilled[¶](#1138-cattributeplayerkilled "Permanent link")

Value: `int 45`

ID of the player resource Player Killed. Check [here](../../resources/resources/#45-survival-to-finish "Jump to: Game Mecahnicsc > Resources > #45-survival-to-finish") for more info about what this resource does.

### 11.39. cAttributeTributeInefficency[¶](#1139-cattributetributeinefficency "Permanent link")

Value: `int 46`

ID of the player resource Tribute Inefficency. Check [here](../../resources/resources/#46-tribute-inefficiency "Jump to: Game Mecahnicsc > Resources > #46-tribute-inefficiency") for more info about what this resource does.

### 11.40. cAttributeGoldBonus[¶](#1140-cattributegoldbonus "Permanent link")

Value: `int 47`

ID of the player resource Gold Bonus. Check [here](../../resources/resources/#47-gold-mining-productivity "Jump to: Game Mecahnicsc > Resources > #47-gold-mining-productivity") for more info about what this resource does.

### 11.41. cAttributeTownCenterUnavailable[¶](#1141-cattributetowncenterunavailable "Permanent link")

Value: `int 48`

ID of the player resource Town Center Unavailable. Check [here](../../resources/resources/#48-town-center-unavailable "Jump to: Game Mecahnicsc > Resources > #48-town-center-unavailable") for more info about what this resource does.

### 11.42. cAttributeGoldCounter[¶](#1142-cattributegoldcounter "Permanent link")

Value: `int 49`

ID of the player resource Gold Counter. Check [here](../../resources/resources/#49-gold-counter "Jump to: Game Mecahnicsc > Resources > #49-gold-counter") for more info about what this resource does.

### 11.43. cAttributeWriting[¶](#1143-cattributewriting "Permanent link")

Value: `int 50`

ID of the player resource Writing. Check [here](../../resources/resources/#50-reveal-ally "Jump to: Game Mecahnicsc > Resources > #50-reveal-ally") for more info about what this resource does.

### 11.44. cAttributeMonasteries[¶](#1144-cattributemonasteries "Permanent link")

Value: `int 52`

ID of the player resource Monasteries. Check [here](../../resources/resources/#52-monasteries "Jump to: Game Mecahnicsc > Resources > #52-monasteries") for more info about what this resource does.

### 11.45. cAttributeTribute[¶](#1145-cattributetribute "Permanent link")

Value: `int 53`

ID of the player resource Tribute. Check [here](../../resources/resources/#53-tribute-sent "Jump to: Game Mecahnicsc > Resources > #53-tribute-sent") for more info about what this resource does.

### 11.46. cAttributeHoldRuins[¶](#1146-cattributeholdruins "Permanent link")

Value: `int 54`

ID of the player resource Hold Ruins. Check [here](../../resources/resources/#54-all-monuments-captured "Jump to: Game Mecahnicsc > Resources > #54-all-monuments-captured") for more info about what this resource does.

### 11.47. cAttributeHoldRelics[¶](#1147-cattributeholdrelics "Permanent link")

Value: `int 55`

ID of the player resource Hold Relics. Check [here](../../resources/resources/#55-all-relics-captured "Jump to: Game Mecahnicsc > Resources > #55-all-relics-captured") for more info about what this resource does.

### 11.48. cAttributeOre[¶](#1148-cattributeore "Permanent link")

Value: `int 56`

ID of the player resource Ore. Check [here](../../resources/resources/#56-ore-storage "Jump to: Game Mecahnicsc > Resources > #56-ore-storage") for more info about what this resource does.

### 11.49. cAttributeCapturedUnit[¶](#1149-cattributecapturedunit "Permanent link")

Value: `int 57`

ID of the player resource Captured Unit. Check [here](../../resources/resources/#57-kidnap-storage "Jump to: Game Mecahnicsc > Resources > #57-kidnap-storage") for more info about what this resource does.

### 11.50. cAttributeTradeGoodQuality[¶](#1150-cattributetradegoodquality "Permanent link")

Value: `int 59`

ID of the player resource Trade Good Quality. Check [here](../../resources/resources/#59-unused-resource-059 "Jump to: Game Mecahnicsc > Resources > #59-unused-resource-059") for more info about what this resource does.

### 11.51. cAttributeTradeMarketLevel[¶](#1151-cattributetrademarketlevel "Permanent link")

Value: `int 60`

ID of the player resource Trade Market Level. Check [here](../../resources/resources/#60-unused-resource-060 "Jump to: Game Mecahnicsc > Resources > #60-unused-resource-060") for more info about what this resource does.

### 11.52. cAttributeFormations[¶](#1152-cattributeformations "Permanent link")

Value: `int 61`

ID of the player resource Formations. Check [here](../../resources/resources/#61-unused-resource-061 "Jump to: Game Mecahnicsc > Resources > #61-unused-resource-061") for more info about what this resource does.

### 11.53. cAttributeBuildingHouseRate[¶](#1153-cattributebuildinghouserate "Permanent link")

Value: `int 62`

ID of the player resource Building House Rate. Check [here](../../resources/resources/#62-building-housing-rate "Jump to: Game Mecahnicsc > Resources > #62-building-housing-rate") for more info about what this resource does.

### 11.54. cAttributeGatherTaxRate[¶](#1154-cattributegathertaxrate "Permanent link")

Value: `int 63`

ID of the player resource Gather Tax Rate. Check [here](../../resources/resources/#63-tax-gather-rate "Jump to: Game Mecahnicsc > Resources > #63-tax-gather-rate") for more info about what this resource does.

### 11.55. cAttributeGatherAccumalation[¶](#1155-cattributegatheraccumalation "Permanent link")

Value: `int 64`

ID of the player resource Gather Accumalation. Check [here](../../resources/resources/#64-gather-accumulator "Jump to: Game Mecahnicsc > Resources > #64-gather-accumulator") for more info about what this resource does.

### 11.56. cAttributeSalvageDecayRate[¶](#1156-cattributesalvagedecayrate "Permanent link")

Value: `int 65`

ID of the player resource Salvage Decay Rate. Check [here](../../resources/resources/#65-salvage-decay-rate "Jump to: Game Mecahnicsc > Resources > #65-salvage-decay-rate") for more info about what this resource does.

### 11.57. cAttributeAllowFormations[¶](#1157-cattributeallowformations "Permanent link")

Value: `int 66`

ID of the player resource Allow Formations. Check [here](../../resources/resources/#66-unused-resource-066 "Jump to: Game Mecahnicsc > Resources > #66-unused-resource-066") for more info about what this resource does.

### 11.58. cAttributeCanConvert[¶](#1158-cattributecanconvert "Permanent link")

Value: `int 67`

ID of the player resource Can Convert. Check [here](../../resources/resources/#67-can-convert "Jump to: Game Mecahnicsc > Resources > #67-can-convert") for more info about what this resource does.

### 11.59. cAttributeConvertResistance[¶](#1159-cattributeconvertresistance "Permanent link")

Value: `int 77`

ID of the player resource Convert Resistance. Check [here](../../resources/resources/#77-conversion-resistance "Jump to: Game Mecahnicsc > Resources > #77-conversion-resistance") for more info about what this resource does.

### 11.60. cAttributeTradeVigRate[¶](#1160-cattributetradevigrate "Permanent link")

Value: `int 78`

ID of the player resource Trade Vig Rate. Check [here](../../resources/resources/#78-trade-vig-rate "Jump to: Game Mecahnicsc > Resources > #78-trade-vig-rate") for more info about what this resource does.

### 11.61. cAttributeStoneBonus[¶](#1161-cattributestonebonus "Permanent link")

Value: `int 79`

ID of the player resource Stone Bonus. Check [here](../../resources/resources/#79-stone-mining-productivity "Jump to: Game Mecahnicsc > Resources > #79-stone-mining-productivity") for more info about what this resource does.

### 11.62. cAttributeQueuedCount[¶](#1162-cattributequeuedcount "Permanent link")

Value: `int 80`

ID of the player resource Queued Count. Check [here](../../resources/resources/#80-queued-units "Jump to: Game Mecahnicsc > Resources > #80-queued-units") for more info about what this resource does.

### 11.63. cAttributeTrainingCount[¶](#1163-cattributetrainingcount "Permanent link")

Value: `int 81`

ID of the player resource Training Count. Check [here](../../resources/resources/#81-training-count "Jump to: Game Mecahnicsc > Resources > #81-training-count") for more info about what this resource does.

### 11.64. cAttributeRaider[¶](#1164-cattributeraider "Permanent link")

Value: `int 82`

ID of the player resource Raider. Check [here](../../resources/resources/#82-start-with-unit-444-ptwc "Jump to: Game Mecahnicsc > Resources > #82-start-with-unit-444-ptwc") for more info about what this resource does.

### 11.65. cAttributeBoardingRechargeRate[¶](#1165-cattributeboardingrechargerate "Permanent link")

Value: `int 83`

ID of the player resource Boarding Recharge Rate. Check [here](../../resources/resources/#83-unused-resource-83 "Jump to: Game Mecahnicsc > Resources > #83-unused-resource-83") for more info about what this resource does.

### 11.66. cAttributeStartingVillagers[¶](#1166-cattributestartingvillagers "Permanent link")

Value: `int 84`

ID of the player resource Starting Villagers. Check [here](../../resources/resources/#84-starting-villagers "Jump to: Game Mecahnicsc > Resources > #84-starting-villagers") for more info about what this resource does.

### 11.67. cAttributeResearchCostMod[¶](#1167-cattributeresearchcostmod "Permanent link")

Value: `int 85`

ID of the player resource Research Cost Mod. Check [here](../../resources/resources/#85-research-cost-modifier "Jump to: Game Mecahnicsc > Resources > #85-research-cost-modifier") for more info about what this resource does.

### 11.68. cAttributeResearchTimeMod[¶](#1168-cattributeresearchtimemod "Permanent link")

Value: `int 86`

ID of the player resource Research Time Mod. Check [here](../../resources/resources/#86-research-time-modifier "Jump to: Game Mecahnicsc > Resources > #86-research-time-modifier") for more info about what this resource does.

### 11.69. cAttributeConvertBoats[¶](#1169-cattributeconvertboats "Permanent link")

Value: `int 87`

ID of the player resource Convert Boats. Check [here](../../resources/resources/#87-convert-boats "Jump to: Game Mecahnicsc > Resources > #87-convert-boats") for more info about what this resource does.

### 11.70. cAttributeFishTrapFood[¶](#1170-cattributefishtrapfood "Permanent link")

Value: `int 88`

ID of the player resource Fish Trap Food. Check [here](../../resources/resources/#88-fish-trap-food-amount "Jump to: Game Mecahnicsc > Resources > #88-fish-trap-food-amount") for more info about what this resource does.

### 11.71. cAttributeHealRateModifer[¶](#1171-cattributehealratemodifer "Permanent link")

Value: `int 89`

ID of the player resource Heal Rate Modifer. Check [here](../../resources/resources/#89-heal-rate-modifier "Jump to: Game Mecahnicsc > Resources > #89-heal-rate-modifier") for more info about what this resource does.

### 11.72. cAttributeHealRange[¶](#1172-cattributehealrange "Permanent link")

Value: `int 90`

ID of the player resource Heal Range. Check [here](../../resources/resources/#90-healing-range "Jump to: Game Mecahnicsc > Resources > #90-healing-range") for more info about what this resource does.

### 11.73. cAttributeStartingFood[¶](#1173-cattributestartingfood "Permanent link")

Value: `int 91`

ID of the player resource Starting Food. Check [here](../../resources/resources/#91-starting-food "Jump to: Game Mecahnicsc > Resources > #91-starting-food") for more info about what this resource does.

### 11.74. cAttributeStartingWood[¶](#1174-cattributestartingwood "Permanent link")

Value: `int 92`

ID of the player resource Starting Wood. Check [here](../../resources/resources/#92-starting-wood "Jump to: Game Mecahnicsc > Resources > #92-starting-wood") for more info about what this resource does.

### 11.75. cAttributeStartingStone[¶](#1175-cattributestartingstone "Permanent link")

Value: `int 93`

ID of the player resource Starting Stone. Check [here](../../resources/resources/#93-starting-stone "Jump to: Game Mecahnicsc > Resources > #93-starting-stone") for more info about what this resource does.

### 11.76. cAttributeStartingGold[¶](#1176-cattributestartinggold "Permanent link")

Value: `int 94`

ID of the player resource Starting Gold. Check [here](../../resources/resources/#94-starting-gold "Jump to: Game Mecahnicsc > Resources > #94-starting-gold") for more info about what this resource does.

### 11.77. cAttributeRaiderAbility[¶](#1177-cattributeraiderability "Permanent link")

Value: `int 95`

ID of the player resource Raider Ability. Check [here](../../resources/resources/#95-enable-ptwc--kidnap--loot "Jump to: Game Mecahnicsc > Resources > #95-enable-ptwc--kidnap--loot") for more info about what this resource does.

### 11.78. cAttributeNoDropsiteFarmers[¶](#1178-cattributenodropsitefarmers "Permanent link")

Value: `int 96`

ID of the player resource No Dropsite Farmers. Check [here](../../resources/resources/#96-no-dropsite-farmers "Jump to: Game Mecahnicsc > Resources > #96-no-dropsite-farmers") for more info about what this resource does.

### 11.79. cAttributeDominantSheepControl[¶](#1179-cattributedominantsheepcontrol "Permanent link")

Value: `int 97`

ID of the player resource Dominant Sheep Control. Check [here](../../resources/resources/#97-dominant-sheep-control "Jump to: Game Mecahnicsc > Resources > #97-dominant-sheep-control") for more info about what this resource does.

### 11.80. cAttributeObjectCostSummation[¶](#1180-cattributeobjectcostsummation "Permanent link")

Value: `int 98`

ID of the player resource Object Cost Summation. Check [here](../../resources/resources/#98-building-cost-sum "Jump to: Game Mecahnicsc > Resources > #98-building-cost-sum") for more info about what this resource does.

### 11.81. cAttributeResearchCostSummation[¶](#1181-cattributeresearchcostsummation "Permanent link")

Value: `int 99`

ID of the player resource Research Cost Summation. Check [here](../../resources/resources/#99-tech-cost-sum "Jump to: Game Mecahnicsc > Resources > #99-tech-cost-sum") for more info about what this resource does.

### 11.82. cAttributeRelicIncomeSummation[¶](#1182-cattributerelicincomesummation "Permanent link")

Value: `int 100`

ID of the player resource Relic Income Summation. Check [here](../../resources/resources/#100-relic-income-sum "Jump to: Game Mecahnicsc > Resources > #100-relic-income-sum") for more info about what this resource does.

### 11.83. cAttributeTradeIncomeSummation[¶](#1183-cattributetradeincomesummation "Permanent link")

Value: `int 101`

ID of the player resource Trade Income Summation. Check [here](../../resources/resources/#101-trade-income-sum "Jump to: Game Mecahnicsc > Resources > #101-trade-income-sum") for more info about what this resource does.

### 11.84. cAttributeCastle[¶](#1184-cattributecastle "Permanent link")

Value: `int 134`

ID of the player resource Castle. Check [here](../../resources/resources/#134-standing-castles "Jump to: Game Mecahnicsc > Resources > #134-standing-castles") for more info about what this resource does.

### 11.85. cAttributeHitPointRazings[¶](#1185-cattributehitpointrazings "Permanent link")

Value: `int 135`

ID of the player resource Hit Point Razings. Check [here](../../resources/resources/#135-hit-points-razed "Jump to: Game Mecahnicsc > Resources > #135-hit-points-razed") for more info about what this resource does.

### 11.86. cAttributeValueKilledByOthers[¶](#1186-cattributevaluekilledbyothers "Permanent link")

Value: `int 152`

ID of the player resource Value Killed By Others. Check [here](../../resources/resources/#152-value-killed-by-others "Jump to: Game Mecahnicsc > Resources > #152-value-killed-by-others") for more info about what this resource does.

### 11.87. cAttributeValueRazedByOthers[¶](#1187-cattributevaluerazedbyothers "Permanent link")

Value: `int 153`

ID of the player resource Value Razed By Others. Check [here](../../resources/resources/#153-value-razed-by-others "Jump to: Game Mecahnicsc > Resources > #153-value-razed-by-others") for more info about what this resource does.

### 11.88. cAttributeKilledByOthers[¶](#1188-cattributekilledbyothers "Permanent link")

Value: `int 154`

ID of the player resource Killed By Others. Check [here](../../resources/resources/#154-killed-by-others "Jump to: Game Mecahnicsc > Resources > #154-killed-by-others") for more info about what this resource does.

### 11.89. cAttributeRazedByOthers[¶](#1189-cattributerazedbyothers "Permanent link")

Value: `int 155`

ID of the player resource Razed By Others. Check [here](../../resources/resources/#155-razed-by-others "Jump to: Game Mecahnicsc > Resources > #155-razed-by-others") for more info about what this resource does.

### 11.90. cAttributeValueCurrentUnits[¶](#1190-cattributevaluecurrentunits "Permanent link")

Value: `int 164`

ID of the player resource Value Current Units. Check [here](../../resources/resources/#164-value-current-units "Jump to: Game Mecahnicsc > Resources > #164-value-current-units") for more info about what this resource does.

### 11.91. cAttributeValueCurrentBuildings[¶](#1191-cattributevaluecurrentbuildings "Permanent link")

Value: `int 165`

ID of the player resource Value Current Buildings. Check [here](../../resources/resources/#165-value-current-buildings "Jump to: Game Mecahnicsc > Resources > #165-value-current-buildings") for more info about what this resource does.

### 11.92. cAttributeFoodTotal[¶](#1192-cattributefoodtotal "Permanent link")

Value: `int 166`

ID of the player resource Food Total. Check [here](../../resources/resources/#166-food-total "Jump to: Game Mecahnicsc > Resources > #166-food-total") for more info about what this resource does.

### 11.93. cAttributeWoodTotal[¶](#1193-cattributewoodtotal "Permanent link")

Value: `int 167`

ID of the player resource Wood Total. Check [here](../../resources/resources/#167-wood-total "Jump to: Game Mecahnicsc > Resources > #167-wood-total") for more info about what this resource does.

### 11.94. cAttributeStoneTotal[¶](#1194-cattributestonetotal "Permanent link")

Value: `int 168`

ID of the player resource Stone Total. Check [here](../../resources/resources/#168-stone-total "Jump to: Game Mecahnicsc > Resources > #168-stone-total") for more info about what this resource does.

### 11.95. cAttributeGoldTotal[¶](#1195-cattributegoldtotal "Permanent link")

Value: `int 169`

ID of the player resource Gold Total. Check [here](../../resources/resources/#169-gold-total "Jump to: Game Mecahnicsc > Resources > #169-gold-total") for more info about what this resource does.

### 11.96. cAttributeTotalValueOfKills[¶](#1196-cattributetotalvalueofkills "Permanent link")

Value: `int 170`

ID of the player resource Total Value Of Kills. Check [here](../../resources/resources/#170-total-value-of-kills "Jump to: Game Mecahnicsc > Resources > #170-total-value-of-kills") for more info about what this resource does.

### 11.97. cAttributeTotalTributeReceived[¶](#1197-cattributetotaltributereceived "Permanent link")

Value: `int 171`

ID of the player resource Total Tribute Received. Check [here](../../resources/resources/#171-total-tribute-received "Jump to: Game Mecahnicsc > Resources > #171-total-tribute-received") for more info about what this resource does.

### 11.98. cAttributeTotalValueOfRazings[¶](#1198-cattributetotalvalueofrazings "Permanent link")

Value: `int 172`

ID of the player resource Total Value Of Razings. Check [here](../../resources/resources/#172-total-value-of-razings "Jump to: Game Mecahnicsc > Resources > #172-total-value-of-razings") for more info about what this resource does.

### 11.99. cAttributeTotalCastlesBuilt[¶](#1199-cattributetotalcastlesbuilt "Permanent link")

Value: `int 173`

ID of the player resource Total Castles Built. Check [here](../../resources/resources/#173-total-castles-built "Jump to: Game Mecahnicsc > Resources > #173-total-castles-built") for more info about what this resource does.

### 11.100. cAttributeTotalWondersBuilt[¶](#11100-cattributetotalwondersbuilt "Permanent link")

Value: `int 174`

ID of the player resource Total Wonders Built. Check [here](../../resources/resources/#174-total-wonders-built "Jump to: Game Mecahnicsc > Resources > #174-total-wonders-built") for more info about what this resource does.

### 11.101. cAttributeTributeScore[¶](#11101-cattributetributescore "Permanent link")

Value: `int 175`

ID of the player resource Tribute Score. Check [here](../../resources/resources/#175-tribute-score "Jump to: Game Mecahnicsc > Resources > #175-tribute-score") for more info about what this resource does.

### 11.102. cAttributeConvertMinAdj[¶](#11102-cattributeconvertminadj "Permanent link")

Value: `int 176`

ID of the player resource Convert Min Adj. Check [here](../../resources/resources/#176-convert-min-adjustment "Jump to: Game Mecahnicsc > Resources > #176-convert-min-adjustment") for more info about what this resource does.

### 11.103. cAttributeConvertMaxAdj[¶](#11103-cattributeconvertmaxadj "Permanent link")

Value: `int 177`

ID of the player resource Convert Max Adj. Check [here](../../resources/resources/#177-convert-max-adjustment "Jump to: Game Mecahnicsc > Resources > #177-convert-max-adjustment") for more info about what this resource does.

### 11.104. cAttributeConvertResistMinAdj[¶](#11104-cattributeconvertresistminadj "Permanent link")

Value: `int 178`

ID of the player resource Convert Resist Min Adj. Check [here](../../resources/resources/#178-convert-resist-min-adjustment "Jump to: Game Mecahnicsc > Resources > #178-convert-resist-min-adjustment") for more info about what this resource does.

### 11.105. cAttributeConvertResistMaxAdj[¶](#11105-cattributeconvertresistmaxadj "Permanent link")

Value: `int 179`

ID of the player resource Convert Resist Max Adj. Check [here](../../resources/resources/#179-convert-resist-max-adjustment "Jump to: Game Mecahnicsc > Resources > #179-convert-resist-max-adjustment") for more info about what this resource does.

### 11.106. cAttributeConvertBuildingMin[¶](#11106-cattributeconvertbuildingmin "Permanent link")

Value: `int 180`

ID of the player resource Convert Building Min. Check [here](../../resources/resources/#180-convert-building-min "Jump to: Game Mecahnicsc > Resources > #180-convert-building-min") for more info about what this resource does.

### 11.107. cAttributeConvertBuildingMax[¶](#11107-cattributeconvertbuildingmax "Permanent link")

Value: `int 181`

ID of the player resource Convert Building Max. Check [here](../../resources/resources/#181-convert-building-max "Jump to: Game Mecahnicsc > Resources > #181-convert-building-max") for more info about what this resource does.

### 11.108. cAttributeConvertBuildingChance[¶](#11108-cattributeconvertbuildingchance "Permanent link")

Value: `int 182`

ID of the player resource Convert Building Chance. Check [here](../../resources/resources/#182-convert-building-chance "Jump to: Game Mecahnicsc > Resources > #182-convert-building-chance") for more info about what this resource does.

### 11.109. cAttributeSpies[¶](#11109-cattributespies "Permanent link")

Value: `int 183`

ID of the player resource Spies. Check [here](../../resources/resources/#183-reveal-enemy "Jump to: Game Mecahnicsc > Resources > #183-reveal-enemy") for more info about what this resource does.

### 11.110. cAttributeValueWondersCastles[¶](#11110-cattributevaluewonderscastles "Permanent link")

Value: `int 184`

ID of the player resource Value Wonders Castles. Check [here](../../resources/resources/#184-value-wonders-castles "Jump to: Game Mecahnicsc > Resources > #184-value-wonders-castles") for more info about what this resource does.

### 11.111. cAttributeFoodScore[¶](#11111-cattributefoodscore "Permanent link")

Value: `int 185`

ID of the player resource Food Score. Check [here](../../resources/resources/#185-food-score "Jump to: Game Mecahnicsc > Resources > #185-food-score") for more info about what this resource does.

### 11.112. cAttributeWoodScore[¶](#11112-cattributewoodscore "Permanent link")

Value: `int 186`

ID of the player resource Wood Score. Check [here](../../resources/resources/#186-wood-score "Jump to: Game Mecahnicsc > Resources > #186-wood-score") for more info about what this resource does.

### 11.113. cAttributeStoneScore[¶](#11113-cattributestonescore "Permanent link")

Value: `int 187`

ID of the player resource Stone Score. Check [here](../../resources/resources/#187-stone-score "Jump to: Game Mecahnicsc > Resources > #187-stone-score") for more info about what this resource does.

### 11.114. cAttributeGoldScore[¶](#11114-cattributegoldscore "Permanent link")

Value: `int 188`

ID of the player resource Gold Score. Check [here](../../resources/resources/#188-gold-score "Jump to: Game Mecahnicsc > Resources > #188-gold-score") for more info about what this resource does.

### 11.115. cAttributeWoodBonus[¶](#11115-cattributewoodbonus "Permanent link")

Value: `int 189`

ID of the player resource Wood Bonus. Check [here](../../resources/resources/#189-chopping-productivity "Jump to: Game Mecahnicsc > Resources > #189-chopping-productivity") for more info about what this resource does.

### 11.116. cAttributeFoodBonus[¶](#11116-cattributefoodbonus "Permanent link")

Value: `int 190`

ID of the player resource Food Bonus. Check [here](../../resources/resources/#190-food-gathering-productivity "Jump to: Game Mecahnicsc > Resources > #190-food-gathering-productivity") for more info about what this resource does.

### 11.117. cAttributeRelicRate[¶](#11117-cattributerelicrate "Permanent link")

Value: `int 191`

ID of the player resource Relic Rate. Check [here](../../resources/resources/#191-relic-gold-production-rate "Jump to: Game Mecahnicsc > Resources > #191-relic-gold-production-rate") for more info about what this resource does.

### 11.118. cAttributeHeresy[¶](#11118-cattributeheresy "Permanent link")

Value: `int 192`

ID of the player resource Heresy. Check [here](../../resources/resources/#192-converted-units-die "Jump to: Game Mecahnicsc > Resources > #192-converted-units-die") for more info about what this resource does.

### 11.119. cAttributeTheocracy[¶](#11119-cattributetheocracy "Permanent link")

Value: `int 193`

ID of the player resource Theocracy. Check [here](../../resources/resources/#193-theocracy "Jump to: Game Mecahnicsc > Resources > #193-theocracy") for more info about what this resource does.

### 11.120. cAttributeCrenellations[¶](#11120-cattributecrenellations "Permanent link")

Value: `int 194`

ID of the player resource Crenellations. Check [here](../../resources/resources/#194-unused-resource-194 "Jump to: Game Mecahnicsc > Resources > #194-unused-resource-194") for more info about what this resource does.

### 11.121. cAttributeConstructionRateMod[¶](#11121-cattributeconstructionratemod "Permanent link")

Value: `int 195`

ID of the player resource Construction Rate Mod. Check [here](../../resources/resources/#195-construction-rate-modifier "Jump to: Game Mecahnicsc > Resources > #195-construction-rate-modifier") for more info about what this resource does.

### 11.122. cAttributeHunWonderBonus[¶](#11122-cattributehunwonderbonus "Permanent link")

Value: `int 196`

ID of the player resource Hun Wonder Bonus. Check [here](../../resources/resources/#196-hun-wonder-discount "Jump to: Game Mecahnicsc > Resources > #196-hun-wonder-discount") for more info about what this resource does.

### 11.123. cAttributeSpiesDiscount[¶](#11123-cattributespiesdiscount "Permanent link")

Value: `int 197`

ID of the player resource Spies Discount. Check [here](../../resources/resources/#197-spies-discount "Jump to: Game Mecahnicsc > Resources > #197-spies-discount") for more info about what this resource does.

### 11.124. cAttributeTemporaryMapReveal[¶](#11124-cattributetemporarymapreveal "Permanent link")

Value: `int 209`

ID of the player resource Temporary Map Reveal. Check [here](../../resources/resources/#209-reveal-enemy-town-centers "Jump to: Game Mecahnicsc > Resources > #209-reveal-enemy-town-centers") for more info about what this resource does.

### 11.125. cAttributeRevealInitialType[¶](#11125-cattributerevealinitialtype "Permanent link")

Value: `int 210`

ID of the player resource Reveal Initial Type. Check [here](../../resources/resources/#210-relics-visible-on-map "Jump to: Game Mecahnicsc > Resources > #210-relics-visible-on-map") for more info about what this resource does.

### 11.126. cAttributeElevationBonusHigher[¶](#11126-cattributeelevationbonushigher "Permanent link")

Value: `int 211`

ID of the player resource Elevation Bonus Higher. Check [here](../../resources/resources/#211-elevation-higher-bonus "Jump to: Game Mecahnicsc > Resources > #211-elevation-higher-bonus") for more info about what this resource does.

### 11.127. cAttributeElevationBonusLower[¶](#11127-cattributeelevationbonuslower "Permanent link")

Value: `int 212`

ID of the player resource Elevation Bonus Lower. Check [here](../../resources/resources/#212-elevation-lower-bonus "Jump to: Game Mecahnicsc > Resources > #212-elevation-lower-bonus") for more info about what this resource does.

### 11.128. cAttributeTriggerSharedLOS[¶](#11128-cattributetriggersharedlos "Permanent link")

Value: `int 217`

ID of the player resource Trigger Shared L O S. Check [here](../../resources/resources/#217-shared-line-of-sight "Jump to: Game Mecahnicsc > Resources > #217-shared-line-of-sight") for more info about what this resource does.

### 11.129. cAttributeFeudalTownCenterLimit[¶](#11129-cattributefeudaltowncenterlimit "Permanent link")

Value: `int 218`

ID of the player resource Feudal Town Center Limit. Check [here](../../resources/resources/#218-early-town-center-limit "Jump to: Game Mecahnicsc > Resources > #218-early-town-center-limit") for more info about what this resource does.

### 11.130. cAttributeFishingProductivity[¶](#11130-cattributefishingproductivity "Permanent link")

Value: `int 219`

ID of the player resource Fishing Productivity. Check [here](../../resources/resources/#219-fishing-productivity "Jump to: Game Mecahnicsc > Resources > #219-fishing-productivity") for more info about what this resource does.

### 11.131. cAttributeUnused220[¶](#11131-cattributeunused220 "Permanent link")

Value: `int 220`

ID of the player resource Unused220. Check [here](../../resources/resources/#220-unused-resource-220 "Jump to: Game Mecahnicsc > Resources > #220-unused-resource-220") for more info about what this resource does.

### 11.132. cAttributeMonumentFoodTrickle[¶](#11132-cattributemonumentfoodtrickle "Permanent link")

Value: `int 221`

ID of the player resource Monument Food Trickle. Check [here](../../resources/resources/#221-monument-food-productivity "Jump to: Game Mecahnicsc > Resources > #221-monument-food-productivity") for more info about what this resource does.

### 11.133. cAttributeMonumentWoodTrickle[¶](#11133-cattributemonumentwoodtrickle "Permanent link")

Value: `int 222`

ID of the player resource Monument Wood Trickle. Check [here](../../resources/resources/#222-monument-wood-productivity "Jump to: Game Mecahnicsc > Resources > #222-monument-wood-productivity") for more info about what this resource does.

### 11.134. cAttributeMonumentStoneTrickle[¶](#11134-cattributemonumentstonetrickle "Permanent link")

Value: `int 223`

ID of the player resource Monument Stone Trickle. Check [here](../../resources/resources/#223-monument-stone-productivity "Jump to: Game Mecahnicsc > Resources > #223-monument-stone-productivity") for more info about what this resource does.

### 11.135. cAttributeMonumentGoldTrickle[¶](#11135-cattributemonumentgoldtrickle "Permanent link")

Value: `int 224`

ID of the player resource Monument Gold Trickle. Check [here](../../resources/resources/#224-monument-gold-productivity "Jump to: Game Mecahnicsc > Resources > #224-monument-gold-productivity") for more info about what this resource does.

### 11.136. cAttributeRelicFoodRate[¶](#11136-cattributerelicfoodrate "Permanent link")

Value: `int 225`

ID of the player resource Relic Food Rate. Check [here](../../resources/resources/#225-relic-food-production-rate "Jump to: Game Mecahnicsc > Resources > #225-relic-food-production-rate") for more info about what this resource does.

### 11.137. cAttributeVillagersKilledByGaia[¶](#11137-cattributevillagerskilledbygaia "Permanent link")

Value: `int 226`

ID of the player resource Villagers Killed By Gaia. Check [here](../../resources/resources/#226-villagers-killed-by-gaia "Jump to: Game Mecahnicsc > Resources > #226-villagers-killed-by-gaia") for more info about what this resource does.

### 11.138. cAttributeVillgaersKilledByAnimal[¶](#11138-cattributevillgaerskilledbyanimal "Permanent link")

Value: `int 227`

ID of the player resource Villgaers Killed By Animal. Check [here](../../resources/resources/#227-villagers-killed-by-animals "Jump to: Game Mecahnicsc > Resources > #227-villagers-killed-by-animals") for more info about what this resource does.

### 11.139. cAttributeVillagersKilledByAIPlayer[¶](#11139-cattributevillagerskilledbyaiplayer "Permanent link")

Value: `int 228`

ID of the player resource Villagers Killed By A I Player. Check [here](../../resources/resources/#228-villagers-killed-by-ai-player "Jump to: Game Mecahnicsc > Resources > #228-villagers-killed-by-ai-player") for more info about what this resource does.

### 11.140. cAttributeVillagersKilledByHumanPlayer[¶](#11140-cattributevillagerskilledbyhumanplayer "Permanent link")

Value: `int 229`

ID of the player resource Villagers Killed By Human Player. Check [here](../../resources/resources/#229-villagers-killed-by-human-player "Jump to: Game Mecahnicsc > Resources > #229-villagers-killed-by-human-player") for more info about what this resource does.

### 11.141. cAttributeFoodGeneration[¶](#11141-cattributefoodgeneration "Permanent link")

Value: `int 230`

ID of the player resource Food Generation. Check [here](../../resources/resources/#230-food-generation-rate "Jump to: Game Mecahnicsc > Resources > #230-food-generation-rate") for more info about what this resource does.

### 11.142. cAttributeWoodGeneration[¶](#11142-cattributewoodgeneration "Permanent link")

Value: `int 231`

ID of the player resource Wood Generation. Check [here](../../resources/resources/#231-wood-generation-rate "Jump to: Game Mecahnicsc > Resources > #231-wood-generation-rate") for more info about what this resource does.

### 11.143. cAttributeStoneGeneration[¶](#11143-cattributestonegeneration "Permanent link")

Value: `int 232`

ID of the player resource Stone Generation. Check [here](../../resources/resources/#232-stone-generation-rate "Jump to: Game Mecahnicsc > Resources > #232-stone-generation-rate") for more info about what this resource does.

### 11.144. cAttributeGoldGeneration[¶](#11144-cattributegoldgeneration "Permanent link")

Value: `int 233`

ID of the player resource Gold Generation. Check [here](../../resources/resources/#233-gold-generation-rate "Jump to: Game Mecahnicsc > Resources > #233-gold-generation-rate") for more info about what this resource does.

### 11.145. cAttributeSpawnCap[¶](#11145-cattributespawncap "Permanent link")

Value: `int 234`

ID of the player resource Spawn Cap. Check [here](../../resources/resources/#234-spawn-limit "Jump to: Game Mecahnicsc > Resources > #234-spawn-limit") for more info about what this resource does.

### 11.146. cAttributeFlemishMilitiaPop[¶](#11146-cattributeflemishmilitiapop "Permanent link")

Value: `int 235`

ID of the player resource Flemish Militia Pop. Check [here](../../resources/resources/#235-flemish-militia-population "Jump to: Game Mecahnicsc > Resources > #235-flemish-militia-population") for more info about what this resource does.

### 11.147. cAttributeGoldFarmingProductivity[¶](#11147-cattributegoldfarmingproductivity "Permanent link")

Value: `int 236`

ID of the player resource Gold Farming Productivity. Check [here](../../resources/resources/#236-farming-gold-productivity "Jump to: Game Mecahnicsc > Resources > #236-farming-gold-productivity") for more info about what this resource does.

### 11.148. cAttributeFolwarkCollectionAmount[¶](#11148-cattributefolwarkcollectionamount "Permanent link")

Value: `int 237`

ID of the player resource Folwark Collection Amount. Check [here](../../resources/resources/#237-folwark-collection-amount "Jump to: Game Mecahnicsc > Resources > #237-folwark-collection-amount") for more info about what this resource does.

### 11.149. cAttributeFolwarkCollectionType[¶](#11149-cattributefolwarkcollectiontype "Permanent link")

Value: `int 238`

ID of the player resource Folwark Collection Type. Check [here](../../resources/resources/#238-folwark-attribute-type "Jump to: Game Mecahnicsc > Resources > #238-folwark-attribute-type") for more info about what this resource does.

### 11.150. cAttributeBuildingId[¶](#11150-cattributebuildingid "Permanent link")

Value: `int 239`

ID of the player resource Building Id. Check [here](../../resources/resources/#239-folwark-building-type "Jump to: Game Mecahnicsc > Resources > #239-folwark-building-type") for more info about what this resource does.

### 11.151. cAttributeUnitsConverted[¶](#11151-cattributeunitsconverted "Permanent link")

Value: `int 240`

ID of the player resource Units Converted. Check [here](../../resources/resources/#240-units-converted "Jump to: Game Mecahnicsc > Resources > #240-units-converted") for more info about what this resource does.

### 11.152. cAttributeStoneGoldMiningProductivity[¶](#11152-cattributestonegoldminingproductivity "Permanent link")

Value: `int 241`

ID of the player resource Stone Gold Mining Productivity. Check [here](../../resources/resources/#241-stone-mining-gold-productivity "Jump to: Game Mecahnicsc > Resources > #241-stone-mining-gold-productivity") for more info about what this resource does.

### 11.153. cAttributeWorkshopFoodTrickle[¶](#11153-cattributeworkshopfoodtrickle "Permanent link")

Value: `int 242`

ID of the player resource Workshop Food Trickle. Check [here](../../resources/resources/#242-trade-workshop-food-productivity "Jump to: Game Mecahnicsc > Resources > #242-trade-workshop-food-productivity") for more info about what this resource does.

### 11.154. cAttributeWorkshopWoodTrickle[¶](#11154-cattributeworkshopwoodtrickle "Permanent link")

Value: `int 243`

ID of the player resource Workshop Wood Trickle. Check [here](../../resources/resources/#243-trade-workshop-wood-productivity "Jump to: Game Mecahnicsc > Resources > #243-trade-workshop-wood-productivity") for more info about what this resource does.

### 11.155. cAttributeWorkshopStoneTrickle[¶](#11155-cattributeworkshopstonetrickle "Permanent link")

Value: `int 244`

ID of the player resource Workshop Stone Trickle. Check [here](../../resources/resources/#244-trade-workshop-stone-productivity "Jump to: Game Mecahnicsc > Resources > #244-trade-workshop-stone-productivity") for more info about what this resource does.

### 11.156. cAttributeWorkshopGoldTrickle[¶](#11156-cattributeworkshopgoldtrickle "Permanent link")

Value: `int 245`

ID of the player resource Workshop Gold Trickle. Check [here](../../resources/resources/#245-trade-workshop-gold-productivity "Jump to: Game Mecahnicsc > Resources > #245-trade-workshop-gold-productivity") for more info about what this resource does.

### 11.157. cAttributeUnitsValueTotal[¶](#11157-cattributeunitsvaluetotal "Permanent link")

Value: `int 246`

ID of the player resource Units Value Total. Check [here](../../resources/resources/#246-units-value-total "Jump to: Game Mecahnicsc > Resources > #246-units-value-total") for more info about what this resource does.

### 11.158. cAttributeBuildingsValueTotal[¶](#11158-cattributebuildingsvaluetotal "Permanent link")

Value: `int 247`

ID of the player resource Buildings Value Total. Check [here](../../resources/resources/#247-buildings-value-total "Jump to: Game Mecahnicsc > Resources > #247-buildings-value-total") for more info about what this resource does.

### 11.159. cAttributeVillagersCreatedTotal[¶](#11159-cattributevillagerscreatedtotal "Permanent link")

Value: `int 248`

ID of the player resource Villagers Created Total. Check [here](../../resources/resources/#248-villagers-created-total "Jump to: Game Mecahnicsc > Resources > #248-villagers-created-total") for more info about what this resource does.

### 11.160. cAttributeVillagersIdlePeriodsTotal[¶](#11160-cattributevillagersidleperiodstotal "Permanent link")

Value: `int 249`

ID of the player resource Villagers Idle Periods Total. Check [here](../../resources/resources/#249-villagers-idle-periods-total "Jump to: Game Mecahnicsc > Resources > #249-villagers-idle-periods-total") for more info about what this resource does.

### 11.161. cAttributeVillagersIdleSecondsTotal[¶](#11161-cattributevillagersidlesecondstotal "Permanent link")

Value: `int 250`

ID of the player resource Villagers Idle Seconds Total. Check [here](../../resources/resources/#250-villagers-idle-seconds-total "Jump to: Game Mecahnicsc > Resources > #250-villagers-idle-seconds-total") for more info about what this resource does.

### 11.162. cAttributeTradeFoodPercent[¶](#11162-cattributetradefoodpercent "Permanent link")

Value: `int 251`

ID of the player resource Trade Food Percent. Check [here](../../resources/resources/#251-trade-food-percent "Jump to: Game Mecahnicsc > Resources > #251-trade-food-percent") for more info about what this resource does.

### 11.163. cAttributeTradeWoodPercent[¶](#11163-cattributetradewoodpercent "Permanent link")

Value: `int 252`

ID of the player resource Trade Wood Percent. Check [here](../../resources/resources/#252-trade-wood-percent "Jump to: Game Mecahnicsc > Resources > #252-trade-wood-percent") for more info about what this resource does.

### 11.164. cAttributeTradeStonePercent[¶](#11164-cattributetradestonepercent "Permanent link")

Value: `int 253`

ID of the player resource Trade Stone Percent. Check [here](../../resources/resources/#253-trade-stone-percent "Jump to: Game Mecahnicsc > Resources > #253-trade-stone-percent") for more info about what this resource does.

### 11.165. cAttributeLivestockFoodProductivity[¶](#11165-cattributelivestockfoodproductivity "Permanent link")

Value: `int 254`

ID of the player resource Livestock Food Productivity. Check [here](../../resources/resources/#254-livestock-food-productivity "Jump to: Game Mecahnicsc > Resources > #254-livestock-food-productivity") for more info about what this resource does.

### 11.166. cAttributeSpeedUpBuildingType[¶](#11166-cattributespeedupbuildingtype "Permanent link")

Value: `int 255`

ID of the player resource Speed Up Building Type. Check [here](../../resources/resources/#255-unused-resource-255 "Jump to: Game Mecahnicsc > Resources > #255-unused-resource-255") for more info about what this resource does.

### 11.167. cAttributeSpeedUpBuildingRange[¶](#11167-cattributespeedupbuildingrange "Permanent link")

Value: `int 256`

ID of the player resource Speed Up Building Range. Check [here](../../resources/resources/#256-unused-resource-256 "Jump to: Game Mecahnicsc > Resources > #256-unused-resource-256") for more info about what this resource does.

### 11.168. cAttributeSpeedUpPercentage[¶](#11168-cattributespeeduppercentage "Permanent link")

Value: `int 257`

ID of the player resource Speed Up Percentage. Check [here](../../resources/resources/#257-unused-resource-257 "Jump to: Game Mecahnicsc > Resources > #257-unused-resource-257") for more info about what this resource does.

### 11.169. cAttributeSpeedUpObjectType[¶](#11169-cattributespeedupobjecttype "Permanent link")

Value: `int 258`

ID of the player resource Speed Up. Check [here](../../resources/resources/#258-unused-resource-258 "Jump to: Game Mecahnicsc > Resources > #258-unused-resource-258") for more info about what this resource does.

### 11.170. cAttributeSpeedUpEffectType[¶](#11170-cattributespeedupeffecttype "Permanent link")

Value: `int 259`

ID of the player resource Speed Up Effect Type. Check [here](../../resources/resources/#259-unused-resource-259 "Jump to: Game Mecahnicsc > Resources > #259-unused-resource-259") for more info about what this resource does.

### 11.171. cAttributeSpeedUpSecondaryEffectType[¶](#11171-cattributespeedupsecondaryeffecttype "Permanent link")

Value: `int 260`

ID of the player resource Speed Up Secondary Effect Type. Check [here](../../resources/resources/#260-unused-resource-260 "Jump to: Game Mecahnicsc > Resources > #260-unused-resource-260") for more info about what this resource does.

### 11.172. cAttributeSpeedUpSecondaryPercentage[¶](#11172-cattributespeedupsecondarypercentage "Permanent link")

Value: `int 261`

ID of the player resource Speed Up Secondary Percentage. Check [here](../../resources/resources/#261-unused-resource-261 "Jump to: Game Mecahnicsc > Resources > #261-unused-resource-261") for more info about what this resource does.

### 11.173. cAttributeCivNameOverride[¶](#11173-cattributecivnameoverride "Permanent link")

Value: `int 262`

ID of the player resource Civ Name Override. Check [here](../../resources/resources/#262-civilization-name-override "Jump to: Game Mecahnicsc > Resources > #262-civilization-name-override") for more info about what this resource does.

### 11.174. cAttributeStartingScoutID[¶](#11174-cattributestartingscoutid "Permanent link")

Value: `int 263`

ID of the player resource Starting Scout I D. Check [here](../../resources/resources/#263-starting-scout-id "Jump to: Game Mecahnicsc > Resources > #263-starting-scout-id") for more info about what this resource does.

### 11.175. cAttributeRelicWoodRate[¶](#11175-cattributerelicwoodrate "Permanent link")

Value: `int 264`

ID of the player resource Relic Wood Rate. Check [here](../../resources/resources/#264-relic-wood-production-rate "Jump to: Game Mecahnicsc > Resources > #264-relic-wood-production-rate") for more info about what this resource does.

### 11.176. cAttributeRelicStoneRate[¶](#11176-cattributerelicstonerate "Permanent link")

Value: `int 265`

ID of the player resource Relic Stone Rate. Check [here](../../resources/resources/#265-relic-stone-production-rate "Jump to: Game Mecahnicsc > Resources > #265-relic-stone-production-rate") for more info about what this resource does.

### 11.177. cAttributeChoppingGoldProductivity[¶](#11177-cattributechoppinggoldproductivity "Permanent link")

Value: `int 266`

ID of the player resource Chopping Gold Productivity. Check [here](../../resources/resources/#266-chopping-gold-productivity "Jump to: Game Mecahnicsc > Resources > #266-chopping-gold-productivity") for more info about what this resource does.

### 11.178. cAttributeForagingWoodProductivity[¶](#11178-cattributeforagingwoodproductivity "Permanent link")

Value: `int 267`

ID of the player resource Foraging Wood Productivity. Check [here](../../resources/resources/#267-foraging-wood-productivity "Jump to: Game Mecahnicsc > Resources > #267-foraging-wood-productivity") for more info about what this resource does.

### 11.179. cAttributeHuntingProductivity[¶](#11179-cattributehuntingproductivity "Permanent link")

Value: `int 268`

ID of the player resource Hunting Productivity. Check [here](../../resources/resources/#268-hunter-productivity "Jump to: Game Mecahnicsc > Resources > #268-hunter-productivity") for more info about what this resource does.

### 11.180. cAttributeTechnologyRewardEffect[¶](#11180-cattributetechnologyrewardeffect "Permanent link")

Value: `int 269`

ID of the player resource Technology Reward Effect. Check [here](../../resources/resources/#269-technology-reward-effect "Jump to: Game Mecahnicsc > Resources > #269-technology-reward-effect") for more info about what this resource does.

### 11.181. cAttributeUnitRepairCost[¶](#11181-cattributeunitrepaircost "Permanent link")

Value: `int 270`

ID of the player resource Unit Repair Cost. Check [here](../../resources/resources/#270-unit-repair-cost "Jump to: Game Mecahnicsc > Resources > #270-unit-repair-cost") for more info about what this resource does.

### 11.182. cAttributeBuildingRepairCost[¶](#11182-cattributebuildingrepaircost "Permanent link")

Value: `int 271`

ID of the player resource Building Repair Cost. Check [here](../../resources/resources/#271-building-repair-cost "Jump to: Game Mecahnicsc > Resources > #271-building-repair-cost") for more info about what this resource does.

### 11.183. cAttributeElevationDamageHigher[¶](#11183-cattributeelevationdamagehigher "Permanent link")

Value: `int 272`

ID of the player resource Elevation Damage Higher. Check [here](../../resources/resources/#272-elevation-higher-damage "Jump to: Game Mecahnicsc > Resources > #272-elevation-higher-damage") for more info about what this resource does.

### 11.184. cAttributeElevationDamageLower[¶](#11184-cattributeelevationdamagelower "Permanent link")

Value: `int 273`

ID of the player resource Elevation Damage Lower. Check [here](../../resources/resources/#273-elevation-lower-damage "Jump to: Game Mecahnicsc > Resources > #273-elevation-lower-damage") for more info about what this resource does.

### 11.185. cAttributeInfantryKillReward[¶](#11185-cattributeinfantrykillreward "Permanent link")

Value: `int 274`

ID of the player resource Infantry Kill Reward. Check [here](../../resources/resources/#274-infantry-kill-reward "Jump to: Game Mecahnicsc > Resources > #274-infantry-kill-reward") for more info about what this resource does.

### 11.186. cAttributeMilitaryCanConvert[¶](#11186-cattributemilitarycanconvert "Permanent link")

Value: `int 279`

ID of the player resource Military Can Convert. Check [here](../../resources/resources/#279-military-can-convert "Jump to: Game Mecahnicsc > Resources > #279-military-can-convert") for more info about what this resource does.

### 11.187. cAttributeMilitaryConversionRangeAdj[¶](#11187-cattributemilitaryconversionrangeadj "Permanent link")

Value: `int 280`

ID of the player resource Military Conversion Range Adj. Check [here](../../resources/resources/#280-military-convert-range "Jump to: Game Mecahnicsc > Resources > #280-military-convert-range") for more info about what this resource does.

### 11.188. cAttributeMilitaryConversionChance[¶](#11188-cattributemilitaryconversionchance "Permanent link")

Value: `int 281`

ID of the player resource Military Conversion Chance. Check [here](../../resources/resources/#281-military-convert-chance "Jump to: Game Mecahnicsc > Resources > #281-military-convert-chance") for more info about what this resource does.

### 11.189. cAttributeMilitaryConversionRechargeRate[¶](#11189-cattributemilitaryconversionrechargerate "Permanent link")

Value: `int 282`

ID of the player resource Military Conversion Recharge Rate. Check [here](../../resources/resources/#282-military-convert-recharge "Jump to: Game Mecahnicsc > Resources > #282-military-convert-recharge") for more info about what this resource does.

### 11.190. cAttributeSpawnStayInside[¶](#11190-cattributespawnstayinside "Permanent link")

Value: `int 283`

ID of the player resource Spawn Stay Inside. Check [here](../../resources/resources/#283-spawn-inside "Jump to: Game Mecahnicsc > Resources > #283-spawn-inside") for more info about what this resource does.

### 11.191. cAttributeCavalryKillReward[¶](#11191-cattributecavalrykillreward "Permanent link")

Value: `int 284`

ID of the player resource Cavalry Kill Reward. Check [here](../../resources/resources/#284-cavalry-kill-reward "Jump to: Game Mecahnicsc > Resources > #284-cavalry-kill-reward") for more info about what this resource does.

### 11.192. cAttributeTriggerSharedVisibility[¶](#11192-cattributetriggersharedvisibility "Permanent link")

Value: `int 285`

ID of the player resource Trigger Shared Visibility. Check [here](../../resources/resources/#285-shared-visibility "Jump to: Game Mecahnicsc > Resources > #285-shared-visibility") for more info about what this resource does.

### 11.193. cAttributeTriggerSharedExploration[¶](#11193-cattributetriggersharedexploration "Permanent link")

Value: `int 286`

ID of the player resource Trigger Shared Exploration. Check [here](../../resources/resources/#286-shared-exploration "Jump to: Game Mecahnicsc > Resources > #286-shared-exploration") for more info about what this resource does.

### 11.194. cAttributeMilitaryFoodTrickle[¶](#11194-cattributemilitaryfoodtrickle "Permanent link")

Value: `int 287`

ID of the player resource Military Food Trickle. Check [here](../../resources/resources/#287-military-food-productivity "Jump to: Game Mecahnicsc > Resources > #287-military-food-productivity") for more info about what this resource does.

### 11.195. cAttributePastureFoodAmount[¶](#11195-cattributepasturefoodamount "Permanent link")

Value: `int 288`

ID of the player resource Pasture Food Amount. Check [here](../../resources/resources/#288-pasture-food-amount "Jump to: Game Mecahnicsc > Resources > #288-pasture-food-amount") for more info about what this resource does.

### 11.196. cAttributePastureAnimalCount[¶](#11196-cattributepastureanimalcount "Permanent link")

Value: `int 289`

ID of the player resource Pasture Animal Count. Check [here](../../resources/resources/#289-pasture-animal-count "Jump to: Game Mecahnicsc > Resources > #289-pasture-animal-count") for more info about what this resource does.

### 11.197. cAttributePastureHerderCount[¶](#11197-cattributepastureherdercount "Permanent link")

Value: `int 290`

ID of the player resource Pasture Herder Count. Check [here](../../resources/resources/#290-pasture-herder-count "Jump to: Game Mecahnicsc > Resources > #290-pasture-herder-count") for more info about what this resource does.

### 11.198. cAttributeDisableAnimalDecay[¶](#11198-cattributedisableanimaldecay "Permanent link")

Value: `int 292`

ID of the player resource Disable Animal Decay. Check [here](../../resources/resources/#292-animal-decay-prevention "Jump to: Game Mecahnicsc > Resources > #292-animal-decay-prevention") for more info about what this resource does.

### 11.199. cAttributeHerdingFoodProductivity[¶](#11199-cattributeherdingfoodproductivity "Permanent link")

Value: `int 293`

ID of the player resource Herding Food Productivity. Check [here](../../resources/resources/#293-herder-food-productivity "Jump to: Game Mecahnicsc > Resources > #293-herder-food-productivity") for more info about what this resource does.

### 11.200. cAttributeShepherdingFoodProductivity[¶](#11200-cattributeshepherdingfoodproductivity "Permanent link")

Value: `int 294`

ID of the player resource Shepherding Food Productivity. Check [here](../../resources/resources/#294-shepherd-food-productivity "Jump to: Game Mecahnicsc > Resources > #294-shepherd-food-productivity") for more info about what this resource does.

### 11.201. cAttributeGaiaKills[¶](#11201-cattributegaiakills "Permanent link")

Value: `int 300`

ID of the player resource Gaia Kills. Check [here](../../resources/resources/#300-killed-gaia "Jump to: Game Mecahnicsc > Resources > #300-killed-gaia") for more info about what this resource does.

### 11.202. cAttributePlayer1Kills[¶](#11202-cattributeplayer1kills "Permanent link")

Value: `int 301`

ID of the player resource Player1 Kills. Check [here](../../resources/resources/#301-killed-p1 "Jump to: Game Mecahnicsc > Resources > #301-killed-p1") for more info about what this resource does.

### 11.203. cAttributePlayer2Kills[¶](#11203-cattributeplayer2kills "Permanent link")

Value: `int 302`

ID of the player resource Player2 Kills. Check [here](../../resources/resources/#302-killed-p2 "Jump to: Game Mecahnicsc > Resources > #302-killed-p2") for more info about what this resource does.

### 11.204. cAttributePlayer3Kills[¶](#11204-cattributeplayer3kills "Permanent link")

Value: `int 303`

ID of the player resource Player3 Kills. Check [here](../../resources/resources/#303-killed-p3 "Jump to: Game Mecahnicsc > Resources > #303-killed-p3") for more info about what this resource does.

### 11.205. cAttributePlayer4Kills[¶](#11205-cattributeplayer4kills "Permanent link")

Value: `int 304`

ID of the player resource Player4 Kills. Check [here](../../resources/resources/#304-killed-p4 "Jump to: Game Mecahnicsc > Resources > #304-killed-p4") for more info about what this resource does.

### 11.206. cAttributePlayer5Kills[¶](#11206-cattributeplayer5kills "Permanent link")

Value: `int 305`

ID of the player resource Player5 Kills. Check [here](../../resources/resources/#305-killed-p5 "Jump to: Game Mecahnicsc > Resources > #305-killed-p5") for more info about what this resource does.

### 11.207. cAttributePlayer6Kills[¶](#11207-cattributeplayer6kills "Permanent link")

Value: `int 306`

ID of the player resource Player6 Kills. Check [here](../../resources/resources/#306-killed-p6 "Jump to: Game Mecahnicsc > Resources > #306-killed-p6") for more info about what this resource does.

### 11.208. cAttributePlayer7Kills[¶](#11208-cattributeplayer7kills "Permanent link")

Value: `int 307`

ID of the player resource Player7 Kills. Check [here](../../resources/resources/#307-killed-p7 "Jump to: Game Mecahnicsc > Resources > #307-killed-p7") for more info about what this resource does.

### 11.209. cAttributePlayer8Kills[¶](#11209-cattributeplayer8kills "Permanent link")

Value: `int 308`

ID of the player resource Player8 Kills. Check [here](../../resources/resources/#308-killed-p8 "Jump to: Game Mecahnicsc > Resources > #308-killed-p8") for more info about what this resource does.

### 11.210. cAttributeKillsByGaia[¶](#11210-cattributekillsbygaia "Permanent link")

Value: `int 325`

ID of the player resource Kills By Gaia. Check [here](../../resources/resources/#325-kills-by-gaia "Jump to: Game Mecahnicsc > Resources > #325-kills-by-gaia") for more info about what this resource does.

### 11.211. cAttributeKillsByPlayer1[¶](#11211-cattributekillsbyplayer1 "Permanent link")

Value: `int 326`

ID of the player resource Kills By Player1. Check [here](../../resources/resources/#326-kills-by-p1 "Jump to: Game Mecahnicsc > Resources > #326-kills-by-p1") for more info about what this resource does.

### 11.212. cAttributeKillsByPlayer2[¶](#11212-cattributekillsbyplayer2 "Permanent link")

Value: `int 327`

ID of the player resource Kills By Player2. Check [here](../../resources/resources/#327-kills-by-p2 "Jump to: Game Mecahnicsc > Resources > #327-kills-by-p2") for more info about what this resource does.

### 11.213. cAttributeKillsByPlayer3[¶](#11213-cattributekillsbyplayer3 "Permanent link")

Value: `int 328`

ID of the player resource Kills By Player3. Check [here](../../resources/resources/#328-kills-by-p3 "Jump to: Game Mecahnicsc > Resources > #328-kills-by-p3") for more info about what this resource does.

### 11.214. cAttributeKillsByPlayer4[¶](#11214-cattributekillsbyplayer4 "Permanent link")

Value: `int 329`

ID of the player resource Kills By Player4. Check [here](../../resources/resources/#329-kills-by-p4 "Jump to: Game Mecahnicsc > Resources > #329-kills-by-p4") for more info about what this resource does.

### 11.215. cAttributeKillsByPlayer5[¶](#11215-cattributekillsbyplayer5 "Permanent link")

Value: `int 330`

ID of the player resource Kills By Player5. Check [here](../../resources/resources/#330-kills-by-p5 "Jump to: Game Mecahnicsc > Resources > #330-kills-by-p5") for more info about what this resource does.

### 11.216. cAttributeKillsByPlayer6[¶](#11216-cattributekillsbyplayer6 "Permanent link")

Value: `int 331`

ID of the player resource Kills By Player6. Check [here](../../resources/resources/#331-kills-by-p6 "Jump to: Game Mecahnicsc > Resources > #331-kills-by-p6") for more info about what this resource does.

### 11.217. cAttributeKillsByPlayer7[¶](#11217-cattributekillsbyplayer7 "Permanent link")

Value: `int 332`

ID of the player resource Kills By Player7. Check [here](../../resources/resources/#332-kills-by-p7 "Jump to: Game Mecahnicsc > Resources > #332-kills-by-p7") for more info about what this resource does.

### 11.218. cAttributeKillsByPlayer8[¶](#11218-cattributekillsbyplayer8 "Permanent link")

Value: `int 333`

ID of the player resource Kills By Player8. Check [here](../../resources/resources/#333-kills-by-p8 "Jump to: Game Mecahnicsc > Resources > #333-kills-by-p8") for more info about what this resource does.

### 11.219. cAttributeGaiaRazings[¶](#11219-cattributegaiarazings "Permanent link")

Value: `int 350`

ID of the player resource Gaia Razings. Check [here](../../resources/resources/#350-gaia-razings "Jump to: Game Mecahnicsc > Resources > #350-gaia-razings") for more info about what this resource does.

### 11.220. cAttributePlayer1Razings[¶](#11220-cattributeplayer1razings "Permanent link")

Value: `int 351`

ID of the player resource Player1 Razings. Check [here](../../resources/resources/#351-p1-razings "Jump to: Game Mecahnicsc > Resources > #351-p1-razings") for more info about what this resource does.

### 11.221. cAttributePlayer2Razings[¶](#11221-cattributeplayer2razings "Permanent link")

Value: `int 352`

ID of the player resource Player2 Razings. Check [here](../../resources/resources/#352-p2-razings "Jump to: Game Mecahnicsc > Resources > #352-p2-razings") for more info about what this resource does.

### 11.222. cAttributePlayer3Razings[¶](#11222-cattributeplayer3razings "Permanent link")

Value: `int 353`

ID of the player resource Player3 Razings. Check [here](../../resources/resources/#353-p3-razings "Jump to: Game Mecahnicsc > Resources > #353-p3-razings") for more info about what this resource does.

### 11.223. cAttributePlayer4Razings[¶](#11223-cattributeplayer4razings "Permanent link")

Value: `int 354`

ID of the player resource Player4 Razings. Check [here](../../resources/resources/#354-p4-razings "Jump to: Game Mecahnicsc > Resources > #354-p4-razings") for more info about what this resource does.

### 11.224. cAttributePlayer5Razings[¶](#11224-cattributeplayer5razings "Permanent link")

Value: `int 355`

ID of the player resource Player5 Razings. Check [here](../../resources/resources/#355-p5-razings "Jump to: Game Mecahnicsc > Resources > #355-p5-razings") for more info about what this resource does.

### 11.225. cAttributePlayer6Razings[¶](#11225-cattributeplayer6razings "Permanent link")

Value: `int 356`

ID of the player resource Player6 Razings. Check [here](../../resources/resources/#356-p6-razings "Jump to: Game Mecahnicsc > Resources > #356-p6-razings") for more info about what this resource does.

### 11.226. cAttributePlayer7Razings[¶](#11226-cattributeplayer7razings "Permanent link")

Value: `int 357`

ID of the player resource Player7 Razings. Check [here](../../resources/resources/#357-p7-razings "Jump to: Game Mecahnicsc > Resources > #357-p7-razings") for more info about what this resource does.

### 11.227. cAttributePlayer8Razings[¶](#11227-cattributeplayer8razings "Permanent link")

Value: `int 358`

ID of the player resource Player8 Razings. Check [here](../../resources/resources/#358-p8-razings "Jump to: Game Mecahnicsc > Resources > #358-p8-razings") for more info about what this resource does.

### 11.228. cAttributeRazingsByGaia[¶](#11228-cattributerazingsbygaia "Permanent link")

Value: `int 375`

ID of the player resource Razings By Gaia. Check [here](../../resources/resources/#375-razings-by-gaia "Jump to: Game Mecahnicsc > Resources > #375-razings-by-gaia") for more info about what this resource does.

### 11.229. cAttributeRazingsByPlayer1[¶](#11229-cattributerazingsbyplayer1 "Permanent link")

Value: `int 376`

ID of the player resource Razings By Player1. Check [here](../../resources/resources/#376-razings-by-p1 "Jump to: Game Mecahnicsc > Resources > #376-razings-by-p1") for more info about what this resource does.

### 11.230. cAttributeRazingsByPlayer2[¶](#11230-cattributerazingsbyplayer2 "Permanent link")

Value: `int 377`

ID of the player resource Razings By Player2. Check [here](../../resources/resources/#377-razings-by-p2 "Jump to: Game Mecahnicsc > Resources > #377-razings-by-p2") for more info about what this resource does.

### 11.231. cAttributeRazingsByPlayer3[¶](#11231-cattributerazingsbyplayer3 "Permanent link")

Value: `int 378`

ID of the player resource Razings By Player3. Check [here](../../resources/resources/#378-razings-by-p3 "Jump to: Game Mecahnicsc > Resources > #378-razings-by-p3") for more info about what this resource does.

### 11.232. cAttributeRazingsByPlayer4[¶](#11232-cattributerazingsbyplayer4 "Permanent link")

Value: `int 379`

ID of the player resource Razings By Player4. Check [here](../../resources/resources/#379-razings-by-p4 "Jump to: Game Mecahnicsc > Resources > #379-razings-by-p4") for more info about what this resource does.

### 11.233. cAttributeRazingsByPlayer5[¶](#11233-cattributerazingsbyplayer5 "Permanent link")

Value: `int 380`

ID of the player resource Razings By Player5. Check [here](../../resources/resources/#380-razings-by-p5 "Jump to: Game Mecahnicsc > Resources > #380-razings-by-p5") for more info about what this resource does.

### 11.234. cAttributeRazingsByPlayer6[¶](#11234-cattributerazingsbyplayer6 "Permanent link")

Value: `int 381`

ID of the player resource Razings By Player6. Check [here](../../resources/resources/#381-razings-by-p6 "Jump to: Game Mecahnicsc > Resources > #381-razings-by-p6") for more info about what this resource does.

### 11.235. cAttributeRazingsByPlayer7[¶](#11235-cattributerazingsbyplayer7 "Permanent link")

Value: `int 382`

ID of the player resource Razings By Player7. Check [here](../../resources/resources/#382-razings-by-p7 "Jump to: Game Mecahnicsc > Resources > #382-razings-by-p7") for more info about what this resource does.

### 11.236. cAttributeRazingsByPlayer8[¶](#11236-cattributerazingsbyplayer8 "Permanent link")

Value: `int 383`

ID of the player resource Razings By Player8. Check [here](../../resources/resources/#383-razings-by-p8 "Jump to: Game Mecahnicsc > Resources > #383-razings-by-p8") for more info about what this resource does.

### 11.237. cAttributeGaiaKillValue[¶](#11237-cattributegaiakillvalue "Permanent link")

Value: `int 400`

ID of the player resource Gaia Kill Value. Check [here](../../resources/resources/#400-gaia-kill-value "Jump to: Game Mecahnicsc > Resources > #400-gaia-kill-value") for more info about what this resource does.

### 11.238. cAttributePlayer1KillValue[¶](#11238-cattributeplayer1killvalue "Permanent link")

Value: `int 401`

ID of the player resource Player1 Kill Value. Check [here](../../resources/resources/#401-p1-kill-value "Jump to: Game Mecahnicsc > Resources > #401-p1-kill-value") for more info about what this resource does.

### 11.239. cAttributePlayer2KillValue[¶](#11239-cattributeplayer2killvalue "Permanent link")

Value: `int 402`

ID of the player resource Player2 Kill Value. Check [here](../../resources/resources/#402-p2-kill-value "Jump to: Game Mecahnicsc > Resources > #402-p2-kill-value") for more info about what this resource does.

### 11.240. cAttributePlayer3KillValue[¶](#11240-cattributeplayer3killvalue "Permanent link")

Value: `int 403`

ID of the player resource Player3 Kill Value. Check [here](../../resources/resources/#403-p3-kill-value "Jump to: Game Mecahnicsc > Resources > #403-p3-kill-value") for more info about what this resource does.

### 11.241. cAttributePlayer4KillValue[¶](#11241-cattributeplayer4killvalue "Permanent link")

Value: `int 404`

ID of the player resource Player4 Kill Value. Check [here](../../resources/resources/#404-p4-kill-value "Jump to: Game Mecahnicsc > Resources > #404-p4-kill-value") for more info about what this resource does.

### 11.242. cAttributePlayer5KillValue[¶](#11242-cattributeplayer5killvalue "Permanent link")

Value: `int 405`

ID of the player resource Player5 Kill Value. Check [here](../../resources/resources/#405-p5-kill-value "Jump to: Game Mecahnicsc > Resources > #405-p5-kill-value") for more info about what this resource does.

### 11.243. cAttributePlayer6KillValue[¶](#11243-cattributeplayer6killvalue "Permanent link")

Value: `int 406`

ID of the player resource Player6 Kill Value. Check [here](../../resources/resources/#406-p6-kill-value "Jump to: Game Mecahnicsc > Resources > #406-p6-kill-value") for more info about what this resource does.

### 11.244. cAttributePlayer7KillValue[¶](#11244-cattributeplayer7killvalue "Permanent link")

Value: `int 407`

ID of the player resource Player7 Kill Value. Check [here](../../resources/resources/#407-p7-kill-value "Jump to: Game Mecahnicsc > Resources > #407-p7-kill-value") for more info about what this resource does.

### 11.245. cAttributePlayer8KillValue[¶](#11245-cattributeplayer8killvalue "Permanent link")

Value: `int 408`

ID of the player resource Player8 Kill Value. Check [here](../../resources/resources/#408-p8-kill-value "Jump to: Game Mecahnicsc > Resources > #408-p8-kill-value") for more info about what this resource does.

### 11.246. cAttributeGaiaRazingValue[¶](#11246-cattributegaiarazingvalue "Permanent link")

Value: `int 425`

ID of the player resource Gaia Razing Value. Check [here](../../resources/resources/#425-gaia-razing-value "Jump to: Game Mecahnicsc > Resources > #425-gaia-razing-value") for more info about what this resource does.

### 11.247. cAttributePlayer1RazingValue[¶](#11247-cattributeplayer1razingvalue "Permanent link")

Value: `int 426`

ID of the player resource Player1 Razing Value. Check [here](../../resources/resources/#426-p1-razing-value "Jump to: Game Mecahnicsc > Resources > #426-p1-razing-value") for more info about what this resource does.

### 11.248. cAttributePlayer2RazingValue[¶](#11248-cattributeplayer2razingvalue "Permanent link")

Value: `int 427`

ID of the player resource Player2 Razing Value. Check [here](../../resources/resources/#427-p2-razing-value "Jump to: Game Mecahnicsc > Resources > #427-p2-razing-value") for more info about what this resource does.

### 11.249. cAttributePlayer3RazingValue[¶](#11249-cattributeplayer3razingvalue "Permanent link")

Value: `int 428`

ID of the player resource Player3 Razing Value. Check [here](../../resources/resources/#428-p3-razing-value "Jump to: Game Mecahnicsc > Resources > #428-p3-razing-value") for more info about what this resource does.

### 11.250. cAttributePlayer4RazingValue[¶](#11250-cattributeplayer4razingvalue "Permanent link")

Value: `int 429`

ID of the player resource Player4 Razing Value. Check [here](../../resources/resources/#429-p4-razing-value "Jump to: Game Mecahnicsc > Resources > #429-p4-razing-value") for more info about what this resource does.

### 11.251. cAttributePlayer5RazingValue[¶](#11251-cattributeplayer5razingvalue "Permanent link")

Value: `int 430`

ID of the player resource Player5 Razing Value. Check [here](../../resources/resources/#430-p5-razing-value "Jump to: Game Mecahnicsc > Resources > #430-p5-razing-value") for more info about what this resource does.

### 11.252. cAttributePlayer6RazingValue[¶](#11252-cattributeplayer6razingvalue "Permanent link")

Value: `int 431`

ID of the player resource Player6 Razing Value. Check [here](../../resources/resources/#431-p6-razing-value "Jump to: Game Mecahnicsc > Resources > #431-p6-razing-value") for more info about what this resource does.

### 11.253. cAttributePlayer7RazingValue[¶](#11253-cattributeplayer7razingvalue "Permanent link")

Value: `int 432`

ID of the player resource Player7 Razing Value. Check [here](../../resources/resources/#432-p7-razing-value "Jump to: Game Mecahnicsc > Resources > #432-p7-razing-value") for more info about what this resource does.

### 11.254. cAttributePlayer8RazingValue[¶](#11254-cattributeplayer8razingvalue "Permanent link")

Value: `int 433`

ID of the player resource Player8 Razing Value. Check [here](../../resources/resources/#433-p8-razing-value "Jump to: Game Mecahnicsc > Resources > #433-p8-razing-value") for more info about what this resource does.

### 11.255. cAttributeGaiaTribute[¶](#11255-cattributegaiatribute "Permanent link")

Value: `int 450`

ID of the player resource Gaia Tribute. Check [here](../../resources/resources/#450-gaia-tribute "Jump to: Game Mecahnicsc > Resources > #450-gaia-tribute") for more info about what this resource does.

### 11.256. cAttributePlayer1Tribute[¶](#11256-cattributeplayer1tribute "Permanent link")

Value: `int 451`

ID of the player resource Player1 Tribute. Check [here](../../resources/resources/#451-p1-tribute "Jump to: Game Mecahnicsc > Resources > #451-p1-tribute") for more info about what this resource does.

### 11.257. cAttributePlayer2Tribute[¶](#11257-cattributeplayer2tribute "Permanent link")

Value: `int 452`

ID of the player resource Player2 Tribute. Check [here](../../resources/resources/#452-p2-tribute "Jump to: Game Mecahnicsc > Resources > #452-p2-tribute") for more info about what this resource does.

### 11.258. cAttributePlayer3Tribute[¶](#11258-cattributeplayer3tribute "Permanent link")

Value: `int 453`

ID of the player resource Player3 Tribute. Check [here](../../resources/resources/#453-p3-tribute "Jump to: Game Mecahnicsc > Resources > #453-p3-tribute") for more info about what this resource does.

### 11.259. cAttributePlayer4Tribute[¶](#11259-cattributeplayer4tribute "Permanent link")

Value: `int 454`

ID of the player resource Player4 Tribute. Check [here](../../resources/resources/#454-p4-tribute "Jump to: Game Mecahnicsc > Resources > #454-p4-tribute") for more info about what this resource does.

### 11.260. cAttributePlayer5Tribute[¶](#11260-cattributeplayer5tribute "Permanent link")

Value: `int 455`

ID of the player resource Player5 Tribute. Check [here](../../resources/resources/#455-p5-tribute "Jump to: Game Mecahnicsc > Resources > #455-p5-tribute") for more info about what this resource does.

### 11.261. cAttributePlayer6Tribute[¶](#11261-cattributeplayer6tribute "Permanent link")

Value: `int 456`

ID of the player resource Player6 Tribute. Check [here](../../resources/resources/#456-p6-tribute "Jump to: Game Mecahnicsc > Resources > #456-p6-tribute") for more info about what this resource does.

### 11.262. cAttributePlayer7Tribute[¶](#11262-cattributeplayer7tribute "Permanent link")

Value: `int 457`

ID of the player resource Player7 Tribute. Check [here](../../resources/resources/#457-p7-tribute "Jump to: Game Mecahnicsc > Resources > #457-p7-tribute") for more info about what this resource does.

### 11.263. cAttributePlayer8Tribute[¶](#11263-cattributeplayer8tribute "Permanent link")

Value: `int 458`

ID of the player resource Player8 Tribute. Check [here](../../resources/resources/#458-p8-tribute "Jump to: Game Mecahnicsc > Resources > #458-p8-tribute") for more info about what this resource does.

### 11.264. cAttributeTributeFromGaia[¶](#11264-cattributetributefromgaia "Permanent link")

Value: `int 475`

ID of the player resource Tribute From Gaia. Check [here](../../resources/resources/#475-tribute-from-gaia "Jump to: Game Mecahnicsc > Resources > #475-tribute-from-gaia") for more info about what this resource does.

### 11.265. cAttributeTributeFromPlayer1[¶](#11265-cattributetributefromplayer1 "Permanent link")

Value: `int 476`

ID of the player resource Tribute From Player1. Check [here](../../resources/resources/#476-tribute-from-p1 "Jump to: Game Mecahnicsc > Resources > #476-tribute-from-p1") for more info about what this resource does.

### 11.266. cAttributeTributeFromPlayer2[¶](#11266-cattributetributefromplayer2 "Permanent link")

Value: `int 477`

ID of the player resource Tribute From Player2. Check [here](../../resources/resources/#477-tribute-from-p2 "Jump to: Game Mecahnicsc > Resources > #477-tribute-from-p2") for more info about what this resource does.

### 11.267. cAttributeTributeFromPlayer3[¶](#11267-cattributetributefromplayer3 "Permanent link")

Value: `int 478`

ID of the player resource Tribute From Player3. Check [here](../../resources/resources/#478-tribute-from-p3 "Jump to: Game Mecahnicsc > Resources > #478-tribute-from-p3") for more info about what this resource does.

### 11.268. cAttributeTributeFromPlayer4[¶](#11268-cattributetributefromplayer4 "Permanent link")

Value: `int 479`

ID of the player resource Tribute From Player4. Check [here](../../resources/resources/#479-tribute-from-p4 "Jump to: Game Mecahnicsc > Resources > #479-tribute-from-p4") for more info about what this resource does.

### 11.269. cAttributeTributeFromPlayer5[¶](#11269-cattributetributefromplayer5 "Permanent link")

Value: `int 480`

ID of the player resource Tribute From Player5. Check [here](../../resources/resources/#480-tribute-from-p5 "Jump to: Game Mecahnicsc > Resources > #480-tribute-from-p5") for more info about what this resource does.

### 11.270. cAttributeTributeFromPlayer6[¶](#11270-cattributetributefromplayer6 "Permanent link")

Value: `int 481`

ID of the player resource Tribute From Player6. Check [here](../../resources/resources/#481-tribute-from-p6 "Jump to: Game Mecahnicsc > Resources > #481-tribute-from-p6") for more info about what this resource does.

### 11.271. cAttributeTributeFromPlayer7[¶](#11271-cattributetributefromplayer7 "Permanent link")

Value: `int 482`

ID of the player resource Tribute From Player7. Check [here](../../resources/resources/#482-tribute-from-p7 "Jump to: Game Mecahnicsc > Resources > #482-tribute-from-p7") for more info about what this resource does.

### 11.272. cAttributeTributeFromPlayer8[¶](#11272-cattributetributefromplayer8 "Permanent link")

Value: `int 483`

ID of the player resource Tribute From Player8. Check [here](../../resources/resources/#483-tribute-from-p8 "Jump to: Game Mecahnicsc > Resources > #483-tribute-from-p8") for more info about what this resource does.

### 11.273. cAttributeChoppingFoodProductivity[¶](#11273-cattributechoppingfoodproductivity "Permanent link")

Value: `int 502`

This constant is set incorrectly, it should be 291

## 12. Damage Class[¶](#12-damage-class "Permanent link")

### 12.1. cDamageClassInfantry[¶](#121-cdamageclassinfantry "Permanent link")

Value: `int 1`

ID of the Damage Class Infantry

### 12.2. cDamageClassCapitalShips[¶](#122-cdamageclasscapitalships "Permanent link")

Value: `int 2`

ID of the Damage Class Capital Ships

### 12.3. cDamageClassPierce[¶](#123-cdamageclasspierce "Permanent link")

Value: `int 3`

ID of the Damage Class Pierce

### 12.4. cDamageClassMelee[¶](#124-cdamageclassmelee "Permanent link")

Value: `int 4`

ID of the Damage Class Melee

### 12.5. cDamageClassElephantUnits[¶](#125-cdamageclasselephantunits "Permanent link")

Value: `int 5`

ID of the Damage Class Elephant Units

### 12.6. cDamageClassCavalry[¶](#126-cdamageclasscavalry "Permanent link")

Value: `int 8`

ID of the Damage Class Cavalry

### 12.7. cDamageClassAllBuildings[¶](#127-cdamageclassallbuildings "Permanent link")

Value: `int 11`

ID of the Damage Class All Buildings

### 12.8. cDamageClassStoneDefense[¶](#128-cdamageclassstonedefense "Permanent link")

Value: `int 13`

ID of the Damage Class Stone Defense

### 12.9. cDamageClassPredatorAnimals[¶](#129-cdamageclasspredatoranimals "Permanent link")

Value: `int 14`

ID of the Damage Class Predator Animals

### 12.10. cDamageClassArchers[¶](#1210-cdamageclassarchers "Permanent link")

Value: `int 15`

ID of the Damage Class Archers

### 12.11. cDamageClassShips[¶](#1211-cdamageclassships "Permanent link")

Value: `int 16`

ID of the Damage Class Ships

### 12.12. cDamageClassRams[¶](#1212-cdamageclassrams "Permanent link")

Value: `int 17`

ID of the Damage Class Rams

### 12.13. cDamageClassTrees[¶](#1213-cdamageclasstrees "Permanent link")

Value: `int 18`

ID of the Damage Class Trees

### 12.14. cDamageClassUniqueUnits[¶](#1214-cdamageclassuniqueunits "Permanent link")

Value: `int 19`

ID of the Damage Class Unique Units

### 12.15. cDamageClassSiegeWeapons[¶](#1215-cdamageclasssiegeweapons "Permanent link")

Value: `int 20`

ID of the Damage Class Siege Weapons

### 12.16. cDamageClassStandardBuildings[¶](#1216-cdamageclassstandardbuildings "Permanent link")

Value: `int 21`

ID of the Damage Class Standard Buildings

### 12.17. cDamageClassWallsAndGates[¶](#1217-cdamageclasswallsandgates "Permanent link")

Value: `int 22`

ID of the Damage Class Walls And Gates

### 12.18. cDamageClassGunpowderUnits[¶](#1218-cdamageclassgunpowderunits "Permanent link")

Value: `int 23`

ID of the Damage Class Gunpowder Units

### 12.19. cDamageClassBoars[¶](#1219-cdamageclassboars "Permanent link")

Value: `int 24`

ID of the Damage Class Boars

### 12.20. cDamageClassMonks[¶](#1220-cdamageclassmonks "Permanent link")

Value: `int 25`

ID of the Damage Class Monks

### 12.21. cDamageClassCastles[¶](#1221-cdamageclasscastles "Permanent link")

Value: `int 26`

ID of the Damage Class Castles

### 12.22. cDamageClassSpearmen[¶](#1222-cdamageclassspearmen "Permanent link")

Value: `int 27`

ID of the Damage Class Spearmen

### 12.23. cDamageClassCavalryArchers[¶](#1223-cdamageclasscavalryarchers "Permanent link")

Value: `int 28`

ID of the Damage Class Cavalry Archers

### 12.24. cDamageClassShockInfantry[¶](#1224-cdamageclassshockinfantry "Permanent link")

Value: `int 29`

ID of the Damage Class Shock Infantry

### 12.25. cDamageClassCamelUnits[¶](#1225-cdamageclasscamelunits "Permanent link")

Value: `int 30`

ID of the Damage Class Camel Units

### 12.26. cDamageClassCondottieri[¶](#1226-cdamageclasscondottieri "Permanent link")

Value: `int 32`

ID of the Damage Class Condottieri

### 12.27. cDamageClassFishingShips[¶](#1227-cdamageclassfishingships "Permanent link")

Value: `int 34`

ID of the Damage Class Fishing Ships

### 12.28. cDamageClassMamelukes[¶](#1228-cdamageclassmamelukes "Permanent link")

Value: `int 35`

ID of the Damage Class Mamelukes

### 12.29. cDamageClassHeroesAndKings[¶](#1229-cdamageclassheroesandkings "Permanent link")

Value: `int 36`

ID of the Damage Class Heroes And Kings

### 12.30. cDamageClassHeavySiege[¶](#1230-cdamageclassheavysiege "Permanent link")

Value: `int 37`

ID of the Damage Class Heavy Siege

### 12.31. cDamageClassSkirmishers[¶](#1231-cdamageclassskirmishers "Permanent link")

Value: `int 38`

ID of the Damage Class Skirmishers

### 12.32. cDamageClassRoyalHeirs[¶](#1232-cdamageclassroyalheirs "Permanent link")

Value: `int 39`

ID of the Damage Class Royal Heirs

## 13. Task Attribute[¶](#13-task-attribute "Permanent link")

### 13.1. cTaskAttrWorkValue1[¶](#131-ctaskattrworkvalue1 "Permanent link")

Value: `int 0`

ID for the task amount Task Attribute Work Value1.

Usages per task type:

* [Aura Task](./#1442-ctasktypeaura): Quantity to mul/add to the attribute modified

### 13.2. cTaskAttrWorkValue2[¶](#132-ctaskattrworkvalue2 "Permanent link")

Value: `int 1`

ID for the task amount Task Attribute Work Value2

Usages per task type:

* [Aura Task](./#1442-ctasktypeaura): Min number of units required to activate the effect. See Monaspa

### 13.3. cTaskAttrWorkRange[¶](#133-ctaskattrworkrange "Permanent link")

Value: `int 2`

ID for the task amount Task Attribute Work Range

### 13.4. cTaskAttrWorkFlag2[¶](#134-ctaskattrworkflag2 "Permanent link")

Value: `int 3`

ID for the task amount Task Attribute Work Flag2

### 13.5. cTaskAttrSearchWaitTime[¶](#135-ctaskattrsearchwaittime "Permanent link")

Value: `int 4`

ID for the task amount Task Attribute Search Wait Time

Usages per task type:

* [Aura Task](./#1442-ctasktypeaura): The attribute to modify. Not all attributes are supported. Known attributes:
  + [Hit Points](./#91-chitpoints)
  + [Line of Sight](./#92-clineofsight)
  + [Movement Speed](./#96-cmovementspeed)
  + [Attack](./#99-cattack)
  + [Attack Reload Time](./#910-cattackreloadtime)
  + [Work Rate](./#913-cworkrate)
  + [Regeneration Rate](./#9101-cregenerationrate)
  + [Conversion Chance Modifier](./#9105-cconversionchancemod)
  + 116: Melee Armor
  + 117: Pierce Armor
  + [Regeneration Hp Percent](./#9110-cregenerationhppercent)

### 13.6. cTaskAttrCombatLevelFlag[¶](#136-ctaskattrcombatlevelflag "Permanent link")

Value: `int 5`

ID for the task amount Task Attribute Combat Level Flag

Usages per task type:

* [Aura Task](./#1442-ctasktypeaura): Combinable bit-field:
  + 1: Multiply instead of Add
  + 2: Circular instead of Rectangular radius
  + 4: Range indicator shown
  + 8: Temporary Aura
  + 16: Use with 8 - applies buffs only units around when the ability is triggered
  + 32: Translucent

### 13.7. cTaskAttrOwnerType[¶](#137-ctaskattrownertype "Permanent link")

Value: `int 6`

ID for the task amount Task Attribute Owner Type

### 13.8. cTaskAttrTerrain[¶](#138-ctaskattrterrain "Permanent link")

Value: `int 7`

ID for the task amount Task Attribute Terrain

### 13.9. cTaskAttrResourceIn[¶](#139-ctaskattrresourcein "Permanent link")

Value: `int 8`

ID for the task amount Task Attribute Resource In

### 13.10. cTaskAttrProductivityResource[¶](#1310-ctaskattrproductivityresource "Permanent link")

Value: `int 9`

ID for the task amount Task Attribute Productivity Resource

### 13.11. cTaskAttrResourceOut[¶](#1311-ctaskattrresourceout "Permanent link")

Value: `int 10`

ID for the task amount Task Attribute Resource Out

### 13.12. cTaskAttrUnusedResource[¶](#1312-ctaskattrunusedresource "Permanent link")

Value: `int 11`

ID for the task amount Task Attribute Unused Resource

### 13.13. cTaskAttrMovingGraphic[¶](#1313-ctaskattrmovinggraphic "Permanent link")

Value: `int 12`

ID for the task amount Task Attribute Moving Graphic

### 13.14. cTaskAttrProceedingGraphic[¶](#1314-ctaskattrproceedinggraphic "Permanent link")

Value: `int 13`

ID for the task amount Task Attribute Proceeding Graphic

### 13.15. cTaskAttrWorkingGraphic[¶](#1315-ctaskattrworkinggraphic "Permanent link")

Value: `int 14`

ID for the task amount Task Attribute Working Graphic

### 13.16. cTaskAttrCarryingGraphic[¶](#1316-ctaskattrcarryinggraphic "Permanent link")

Value: `int 15`

ID for the task amount Task Attribute Carrying Graphic

### 13.17. cTaskAttrGatheringSound[¶](#1317-ctaskattrgatheringsound "Permanent link")

Value: `int 16`

ID for the task amount Task Attribute Gathering Sound

### 13.18. cTaskAttrGatheringSoundEvent[¶](#1318-ctaskattrgatheringsoundevent "Permanent link")

Value: `int 17`

ID for the task amount Task Attribute Gathering Sound Event

### 13.19. cTaskAttrGatheringSoundInt32[¶](#1319-ctaskattrgatheringsoundint32 "Permanent link")

Value: `int 18`

ID for the task amount Task Attribute Gathering Sound Int32

### 13.20. cTaskAttrDepositSound[¶](#1320-ctaskattrdepositsound "Permanent link")

Value: `int 19`

ID for the task amount Task Attribute Deposit Sound

### 13.21. cTaskAttrDepositSoundEvent[¶](#1321-ctaskattrdepositsoundevent "Permanent link")

Value: `int 20`

ID for the task amount Task Attribute Deposit Sound Event

### 13.22. cTaskAttrDepositSoundInt32[¶](#1322-ctaskattrdepositsoundint32 "Permanent link")

Value: `int 21`

ID for the task amount Task Attribute Deposit Sound Int32

### 13.23. cTaskAttrAutoSearch[¶](#1323-ctaskattrautosearch "Permanent link")

Value: `int 22`

ID for the task amount Task Attribute Auto Search

### 13.24. cTaskAttrCarryCheck[¶](#1324-ctaskattrcarrycheck "Permanent link")

Value: `int 23`

ID for the task amount Task Attribute Carry Check

### 13.25. cTaskAttrBuildingPick[¶](#1325-ctaskattrbuildingpick "Permanent link")

Value: `int 24`

ID for the task amount Task Attribute Building Pick

### 13.26. cTaskAttrGatherType[¶](#1326-ctaskattrgathertype "Permanent link")

Value: `int 25`

ID for the task amount Task Attribute Gather Type

### 13.27. cTaskAttrEnableTargeting[¶](#1327-ctaskattrenabletargeting "Permanent link")

Value: `int 26`

ID for the task amount Task Attribute Enable Targeting

### 13.28. cTaskAttrEnabled[¶](#1328-ctaskattrenabled "Permanent link")

Value: `int 27`

ID for the task amount Task Attribute Enabled

## 14. Task Type[¶](#14-task-type "Permanent link")

### 14.1. cTaskTypeMoveTo[¶](#141-ctasktypemoveto "Permanent link")

Value: `int 1`

ID for the task Move To

### 14.2. cTaskTypeFollow[¶](#142-ctasktypefollow "Permanent link")

Value: `int 2`

ID for the task Follow

### 14.3. cTaskTypeGarrison[¶](#143-ctasktypegarrison "Permanent link")

Value: `int 3`

ID for the task Garrison

### 14.4. cTaskTypeExplore[¶](#144-ctasktypeexplore "Permanent link")

Value: `int 4`

ID for the task Explore

### 14.5. cTaskTypeGatherRebuild[¶](#145-ctasktypegatherrebuild "Permanent link")

Value: `int 5`

ID for the task Gather Rebuild

### 14.6. cTaskTypeGraze[¶](#146-ctasktypegraze "Permanent link")

Value: `int 6`

ID for the task Graze

### 14.7. cTaskTypeCombat[¶](#147-ctasktypecombat "Permanent link")

Value: `int 7`

ID for the task Combat

### 14.8. cTaskTypeShoot[¶](#148-ctasktypeshoot "Permanent link")

Value: `int 8`

ID for the task Shoot

### 14.9. cTaskTypeAttack[¶](#149-ctasktypeattack "Permanent link")

Value: `int 9`

ID for the task Attack

### 14.10. cTaskTypeFly[¶](#1410-ctasktypefly "Permanent link")

Value: `int 10`

ID for the task Fly

### 14.11. cTaskTypeUnloadBoatLike[¶](#1411-ctasktypeunloadboatlike "Permanent link")

Value: `int 12`

ID for the task Unload Boat Like

### 14.12. cTaskTypeGuard[¶](#1412-ctasktypeguard "Permanent link")

Value: `int 13`

ID for the task Guard

### 14.13. cTaskTypeUnloadOverWall[¶](#1413-ctasktypeunloadoverwall "Permanent link")

Value: `int 14`

ID for the task Unload Over Wall

### 14.14. cTaskTypeMake[¶](#1414-ctasktypemake "Permanent link")

Value: `int 21`

ID for the task Make

### 14.15. cTaskTypeBuild[¶](#1415-ctasktypebuild "Permanent link")

Value: `int 101`

ID for the task Build

### 14.16. cTaskTypeMakeUnit[¶](#1416-ctasktypemakeunit "Permanent link")

Value: `int 102`

ID for the task Make Unit

### 14.17. cTaskTypeMakeTech[¶](#1417-ctasktypemaketech "Permanent link")

Value: `int 103`

ID for the task Make Tech

### 14.18. cTaskTypeConvert[¶](#1418-ctasktypeconvert "Permanent link")

Value: `int 104`

ID for the task Convert

### 14.19. cTaskTypeHeal[¶](#1419-ctasktypeheal "Permanent link")

Value: `int 105`

ID for the task Heal

### 14.20. cTaskTypeRepair[¶](#1420-ctasktyperepair "Permanent link")

Value: `int 106`

ID for the task Repair

### 14.21. cTaskTypeGetAutoConverted[¶](#1421-ctasktypegetautoconverted "Permanent link")

Value: `int 107`

ID for the task Get Auto Converted

### 14.22. cTaskTypeDiscoveryArtifact[¶](#1422-ctasktypediscoveryartifact "Permanent link")

Value: `int 108`

ID for the task Discovery Artifact

### 14.23. cTaskTypeHunt[¶](#1423-ctasktypehunt "Permanent link")

Value: `int 110`

ID for the task Hunt

### 14.24. cTaskTypeTrade[¶](#1424-ctasktypetrade "Permanent link")

Value: `int 111`

ID for the task Trade

### 14.25. cTaskTypeGenerateWonderVictory[¶](#1425-ctasktypegeneratewondervictory "Permanent link")

Value: `int 120`

ID for the task Generate Wonder Victory

### 14.26. cTaskTypeDeselectWhenTasked[¶](#1426-ctasktypedeselectwhentasked "Permanent link")

Value: `int 121`

ID for the task Deselect When Tasked

### 14.27. cTaskTypeLootGather[¶](#1427-ctasktypelootgather "Permanent link")

Value: `int 122`

ID for the task Loot Gather

### 14.28. cTaskTypeHousing[¶](#1428-ctasktypehousing "Permanent link")

Value: `int 123`

ID for the task Housing

### 14.29. cTaskTypePack[¶](#1429-ctasktypepack "Permanent link")

Value: `int 124`

ID for the task Pack

### 14.30. cTaskTypeUnpackAndAttack[¶](#1430-ctasktypeunpackandattack "Permanent link")

Value: `int 125`

ID for the task Unpack And Attack

### 14.31. cTaskTypeOffMapTrade[¶](#1431-ctasktypeoffmaptrade "Permanent link")

Value: `int 131`

ID for the task Off Map Trade

### 14.32. cTaskTypePickupUnit[¶](#1432-ctasktypepickupunit "Permanent link")

Value: `int 132`

ID for the task Pickup Unit

### 14.33. cTaskTypeChargeAttack[¶](#1433-ctasktypechargeattack "Permanent link")

Value: `int 133`

ID for the task Charge Attack

### 14.34. cTaskTypeTransformUnit[¶](#1434-ctasktypetransformunit "Permanent link")

Value: `int 134`

ID for the task Transform Unit

### 14.35. cTaskTypeKidnapUnit[¶](#1435-ctasktypekidnapunit "Permanent link")

Value: `int 135`

ID for the task Kidnap Unit

### 14.36. cTaskTypeDepositUnit[¶](#1436-ctasktypedepositunit "Permanent link")

Value: `int 136`

ID for the task Deposit Unit

### 14.37. cTaskTypeShear[¶](#1437-ctasktypeshear "Permanent link")

Value: `int 149`

ID for the task Shear

### 14.38. cTaskTypeGenerateResources[¶](#1438-ctasktypegenerateresources "Permanent link")

Value: `int 151`

ID for the task Generate Resources

### 14.39. cTaskTypeMovementDamage[¶](#1439-ctasktypemovementdamage "Permanent link")

Value: `int 152`

ID for the task Movement Damage

### 14.40. cTaskTypeMovableDropsite[¶](#1440-ctasktypemovabledropsite "Permanent link")

Value: `int 153`

ID for the task Movable Dropsite

### 14.41. cTaskTypeLoot[¶](#1441-ctasktypeloot "Permanent link")

Value: `int 154`

ID for the task Loot

### 14.42. cTaskTypeAura[¶](#1442-ctasktypeaura "Permanent link")

Value: `int 155`

ID for the task Aura

### 14.43. cTaskTypeExtraSpawn[¶](#1443-ctasktypeextraspawn "Permanent link")

Value: `int 156`

ID for the task Extra Spawn

### 14.44. cTaskTypeStinger[¶](#1444-ctasktypestinger "Permanent link")

Value: `int 157`

ID for the task Stinger

### 14.45. cTaskTypeHPTransform[¶](#1445-ctasktypehptransform "Permanent link")

Value: `int 158`

ID for the task H P Transform

### 14.46. cTaskTypeHPModifier[¶](#1446-ctasktypehpmodifier "Permanent link")

Value: `int 160`

ID for the task H P Modifier

## 15. Tech State[¶](#15-tech-state "Permanent link")

### 15.1. cTechStateNotReady[¶](#151-ctechstatenotready "Permanent link")

Value: `int 0`

Enum value for the tech state Not Ready

### 15.2. cTechStateReady[¶](#152-ctechstateready "Permanent link")

Value: `int 1`

Enum value for the tech state Ready

### 15.3. cTechStateQueued[¶](#153-ctechstatequeued "Permanent link")

Value: `int 4`

Enum value for the tech state Queued

### 15.4. cTechStateResearching[¶](#154-ctechstateresearching "Permanent link")

Value: `int 2`

Enum value for the tech state Researching

### 15.5. cTechStateDone[¶](#155-ctechstatedone "Permanent link")

Value: `int 3`

Enum value for the tech state Done

### 15.6. cTechStateDisabled[¶](#156-ctechstatedisabled "Permanent link")

Value: `int -1`

Enum value for the tech state Disabled

### 15.7. cTechStateInvalid[¶](#157-ctechstateinvalid "Permanent link")

Value: `int -2`

Enum value for the tech state Invalid

## 16. Object Type[¶](#16-object-type "Permanent link")

### 16.1. cObjectTypeEyeCandy[¶](#161-cobjecttypeeyecandy "Permanent link")

Value: `int 10`

Enum value for the object type Eye Candy

### 16.2. cObjectTypeTrees[¶](#162-cobjecttypetrees "Permanent link")

Value: `int 15`

Enum value for the object type Trees

### 16.3. cObjectTypeAnimated[¶](#163-cobjecttypeanimated "Permanent link")

Value: `int 20`

Enum value for the object type Animated

### 16.4. cObjectTypeDoppleganger[¶](#164-cobjecttypedoppleganger "Permanent link")

Value: `int 25`

Enum value for the object type Doppleganger

### 16.5. cObjectTypeMoving[¶](#165-cobjecttypemoving "Permanent link")

Value: `int 30`

Enum value for the object type Moving

### 16.6. cObjectTypeActing[¶](#166-cobjecttypeacting "Permanent link")

Value: `int 40`

Enum value for the object type Acting

### 16.7. cObjectTypeCombat[¶](#167-cobjecttypecombat "Permanent link")

Value: `int 50`

Enum value for the object type Combat

### 16.8. cObjectTypeProjectile[¶](#168-cobjecttypeprojectile "Permanent link")

Value: `int 60`

Enum value for the object type Projectile

### 16.9. cObjectTypeCreatable[¶](#169-cobjecttypecreatable "Permanent link")

Value: `int 70`

Enum value for the object type Creatable

### 16.10. cObjectTypeBuilding[¶](#1610-cobjecttypebuilding "Permanent link")

Value: `int 80`

Enum value for the object type Building

### 16.11. cObjectTypeLegacyTree[¶](#1611-cobjecttypelegacytree "Permanent link")

Value: `int 90`

Enum value for the object type Legacy Tree

Was this page helpful?

Thanks for your feedback!

Thanks for your feedback! Help us improve this page by using our [feedback form](...).

Back to top


Made with
[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
