---
source_url: https://ageofempires.fandom.com/wiki/Genie_Editor
source_format: mediawiki_wikitext_via_api
fetched_at: 2026-02-08T20:19:03+00:00
---

{{Infobox Software
|Name = Advanced Genie Editor
|Icon = AGE icon.png
|Game = {{1icons}}<br />{{1icons|Definitive Edition}}<br />{{2icons}}<br />{{2icons|HD Edition}}<br />{{2icons|Definitive Edition}}
|Developer = Mikko Tapio Partonen (Tapsa) <small>(since 2.0b (2011))</small><br />Manuel Winocur <small>(since 2023)</small><br />Charles Harbord <small>(since 2024)</small><br />Igor Djordjevic (BugA_the_Great) <small>(since 2024)</small><br />Armin Preiml (Apre) - genieutils <small>(from 2011 to 2013)</small><br />Estien Nifo (StSB77) <small>(from 1.0a to 2.0a)</small>
|Date = 
|Version = 2025.6.3
|Site = Game files <small>(Latest version)</small><br />[https://github.com/Tapsa/AGE AGE] on Github <small>(Old version)</small><br />[http://aok.heavengames.com/blacksmith/showfile.php?fileid=11002 Advanced Genie Editor 2025] on AoK Heaven <small>(Old version)</small>
|Discord = 
}}
The '''Genie Editor''' is a program designed to edit the game files of games that use the [[Genie Engine]]. The initial version is not capable of editing ''[[Age of Empires]]'' files, but the '''Advanced Genie Editor''', provided officially in the game files of ''[[Age of Empires II: Definitive Edition]]'', can now edit both ''[[Age of Empires II: The Age of Kings|Age of Empires II]]'' and ''Age of Empires'' files, along with all expansions.

Things such as a unit's ID in the language.dll file, its graphics, sounds, actual and displayed unit statistics, and more can be modified with the Editor.

== Advanced Genie Editor ==
[[File:Genieui.png|thumb|The AdvancedGenieEditor3 user interface]]
The Advanced Genie Editor (AdvancedGenieEditor3) is a program for editing data of genie (DAT and DLL) files. It can edit properties of units, civilizations, technologies, graphics, terrains, sounds, player colors, and some other things.

The latest version of the Advanced Genie Editor is found in the game files of ''[[Age of Empires II: Definitive Edition]]'', in the <code>Tools_Builds</code> directory.

Most of the lists below are based on ''[[Age of Empires II: Definitive Edition]]'', and can sometimes be used for ''[[Age of Empires: Definitive Edition]]'' and ''[[Age of Empires II: Definitive Edition - Return of Rome|Return of Rome]]'' as well.

== Accessing game files ==
[[File:Genie settings.jpg|thumb]]
Selecting the game upon opening the program will fill in the default values. However, they are described here as well:
* Compressed data set (*.dat)
* Language file
* Language x1 file: Modded language file. Using it is optional.
* DRS files: Graphic files. Useful only when viewing graphics.
* Palette configuration
* Player color palette
* Drive letter (default C): The drive in which the game is installed. Changing the drive letter and selecting the game again will fill in the changed drive letter.
* Language (default en): The language of game files. Procedure to change it is same as changing the drive letter.

=== {{2icons|RoR|30}} ===
There is no default game options for ''Return of Rome''. All values have to filled in manually. In essence, <code>\AoE2DE</code> has to be changed to <code>\AoE2DE\modes\Pompeii</code> in all locations except palettes. Precisely, these are the locations:
* Compressed data set: C:\Program Files (x86)\Steam\steamapps\common\AoE2DE\modes\Pompeii\resources\_common\dat\empires2_x2_p1.dat
* Language file: C:\Program Files (x86)\Steam\steamapps\common\AoE2DE\modes\Pompeii\resources\en\strings\key-value\key-value-strings-utf8.txt
* Language x1 file: C:\Program Files (x86)\Steam\steamapps\common\AoE2DE\modes\Pompeii\resources\en\strings\key-value\key-value-modded-strings-utf8.txt
* DRS files: C:\Program Files (x86)\Steam\steamapps\common\AoE2DE\modes\Pompeii\resources\_common\drs

== Commands ==
* 0 - Attribute Modifier (Set)^
* 1 - Resource Modifier (Set/+/-)<sup>$</sup> - Can be used in conjugation with multiplication of any resource (use numbers < 0 to disable multiplication)
* 2 - Enable/Disable unit
** 0 to disable
** Anything else to enable
* 3 - Upgrade unit
** -1 - all
** 2 - selected (building-specific upgrade)
** 3 - "all including master"
** Anything else to upgrade units already present on the map (example - [[Flemish Revolution]])
* 4 - Attribute Modifier (+/-)^
* 5 - Attribute Modifier (Multiply)^
* 6 - Resource Modifier (Multiply)
* 7 - Spawn Unit
** If Resource 234 is not used, all available buildings are allowed to spawn
** If Resource 234 is used, only the first ''Resource 234'' buildings among the available buildings are allowed to spawn
* 8 - Modify Technology
* 9 - Set Player Civilization Name
** Data and Action fields are useless
** Lang ID reads the new civilization name from game language files
* 10 to 19 - have the same effects as 0 to 9 respectively, affecting the entire team (player and allies)
* 20 to 29 - have the have the same effects as 0 to 9 respectively, affecting all enemies
* 30 to 39 - have the have the same effects as 0 to 9 respectively, affecting all neutral players
* 40 to 48 - have the have the same effects as 0 to 8 respectively, affecting Gaia
* 101 - Technology Cost Modifier (Set/+/-)<sup>#</sup> - Setting resource as -1 modifies all resources
* 102 - Disable Technology
* 103 - Technology Time Modifier (Set/+/-)<sup>#</sup>
* 200 - Set attribute value for the local building where the technology applying this effect was researched from
* 201 - Add/subtract from an attribute for the local building where the technology applying this effect was researched from
<sup>$</sup> = 0 to set, anything else to add
<sup>#</sup> = 0 to set, 1 to add, 2 to multiply
^ = If any non-negative number is input in class field, the effect applies to the given class, and not the unit

== Technology ==
* -3 - Multiply Tech Time
* -2 - Add Time
* -1 - Set Time
* 0 - Set Food Cost
* 1 - Set Wood Cost
* 2 - Set Stone Cost
* 3 - Set Gold Cost
* 4 - Set Research Building
* 5 - Set Research Button
* 6 - Set Icon
* 7 - Set Name (String ID)
* 8 - Set Description (String ID)
* 9 - Set Stacking (enable 256x stacking for specific tech)
* 10 - Set Stacking Research Cap (256 by default. Max = 65535)
* 11 - Set Hotkey
* 12 - Set State (0: Disabled, 1: Enabled)
* 13 - Multiply Food Cost
* 14 - Multiply Wood Cost
* 15 - Multiply Stone Cost
* 16 - Multiply Gold Cost
* 17 - Multiply All Costs
* 18 - Set Effect
* 16384 - Add Food Cost
* 16385 - Add Wood Cost
* 16386 - Add Stone Cost
* 16387 - Add Gold Cost
* Techology cost deduction type flag
** 0 - Unpaid (requires player to have given amount of resources, but does not deduct the resources)
** 1 - Paid (deducts the resources globally after the player has started researching the technology)
** 2 - Deducts the resource from the building's repository of resources
* Technology attribute flag
** 0 - Normal technologies
** 2 - Shows research progress in the Age up bar
** 32 - Building specific upgrade, will only apply the effects to the building it is researched in, and can be researched at multiple instances of the research location separately
** 33 - Repeatable technology, can be researched as long as it is available, even if already researched
* Full tech tree mode - allows a technology to be available only in this mode
** 0 - Available in full tech tree (for civilization specific techs)
** 1 - Disabled in FTT
** 2 - Random map
** 3 - Deathmatch
** 4 - Empire Wars or Empire Wars Mode
** 5 - Wonder Race
** 6 - Defend the Wonder
** 7 - Sudden Death or Sudden Death Mode
** 8 - King of the Hill
** 9 - Capture the Relic
** 10 - Battle Royale
** 11 - Regicide
** 12 - Turbo Mode
** 13 - Scenario or Campaign game
** 14 - Regicide Mode
** 15 - Scenario Editor
** 16 - D3
** 17 - Solid Farms
** 18 - Shared Exploration
** 19 - Default Starting Resources
** 20 - Low Starting Resources
** 21 - Medium Starting Resources
** 22 - High Starting Resources
** 23 - Ultra-High Starting Resources
** 24 - Infinite Starting Resources
** 25 - Random Starting Resources
** 26 - Enable 'Antiquity Mode' stuff*
** 27 - Dark Age Start
** 28 - Feudal Age Start
** 29 - Castle Age Start
** 30 - Imperial Age Start
** 31 - Post-Imperial Age Start
** 32 - Feudal Age Start or later
** 33 - Castle Age Start or later
** 34 - Imperial Age Start or later
** <math>-x</math>: Technology is available in all modes except mode x

== Resources ==
* 0 - Food Storage
* 1 - Wood Storage
* 2 - Stone Storage
* 3 - Gold Storage
* 4 - Population Headroom - population space left (negative for units and Feitorias, positive for buildings which give population)
* 5 - Conversion Range - unused
* 6 - Current Age - 0 for [[Stone Age|Stone]]/[[Dark Age (Age of Empires II)|Dark Age]], 1 for [[Tool Age|Tool]]/[[Feudal Age (Age of Empires II)|Feudal Age]], 2 for [[Bronze Age|Bronze]]/[[Castle Age (Age of Empires II)|Castle Age]], 3 for [[Iron Age|Iron]]/[[Imperial Age (Age of Empires II)|Imperial Age]]
* 7 - Relics Captured
* 8 - Unused (Trade Bonus)
* 9 - Trade Goods
* 10 - Unused (Trade Population)
* 11 - Current Population
* 12 - Corpse Decay Time - conventionally (any other resource can be used and it will fill the same purpose) used to determine the number of seconds (since the resource decay is 1) for which dead bodies and rubble will remain visible - not a global resource, is used for dead units individually
* 13 - Remarkable Discovery
* 14 - Monuments Captured
* 15 - Meat Storage
* 16 - Berry Storage
* 17 - Fish Storage
* 18 - Unused
* 19 - Total Units Owned
* 20 - Units Killed
* 21 - Technology Count
* 22 - % Map Explored
* 23 - Castle Age Tech ID - default: 102
* 24 - Imperial Age Tech ID - default: 103
* 25 - Feudal Age Tech ID - default: 101
* 26 - Attack Warning Sound ID
* 27 - Enable Monk Conversion
* 28 - Enable Building Conversion
* 29 - Enable Siege Conversion
* 30 - Unused (Building Limit)
* 31 - Unused (Food Limit)
* 32 - Bonus Population Cap - increases maximum population by this amount; default: 0, set to 10 in the Imperial Age for Goths
* 33 - Food Maintenance - calls XS script Effects.xs (in C:\Program Files (x86)\Steam\steamapps\common\AoE2DE\resources\_common\xs) with entry provided as value
* 34 - Faith - unused
* 35 - (obsolete) Faith Recharge Rate - percentage of Monk faith restored per second; default: 1.6 in ''Age of Empires II''
* 36 - Farm Food Amount - additional food present on the Farm; default: 0, set to 175 at an unknown stage
* 37 - Civilian Population
* 38 - Villager Population
* 39 - All Techs Achieved - default: 178
* 40 - Military Population
* 41 - Conversions
* 42 - Standing Wonders
* 43 - Razings
* 44 - Kill Ratio
* 45 - Survival to Finish
* 46 - Tribute Inefficiency - Resources lost while sending to other players
* 47 - Gold Mining Productivity
* 48 - Town Center Unavailable
* 49 - Gold Counter
* 50 - Reveal Ally - 1 to enable Cartography behavior (seeing what allies can see)
* 51 - unused
* 52 - Monasteries
* 53 - Tribute Sent
* 54 - All Monuments Captured
* 55 - All Relics Captured
* 56 - Ore Storage
* 57 - Kidnap Storage
* 58 - Dark Age Tech ID - default: 104
* 59 - unused
* 60 - unused
* 61 - unused
* 62 - Building Housing Rate
* 63 - Tax Gather Rate
* 64 - Gather Accumulator
* 65 - Salvage Decay Rate
* 66 - Unused (Allow Formations) - enables formations
* 67 - Can Convert - allows general conversion
* 68 - Hit Points Killed
* 69 - Farm Food Multiplier
* 70 - Source Market or Dock X Coordinate
* 71 - Source Market or Dock Y Coordinate
* 72 - unused
* 73 - unused
* 74 - unused
* 75 - unused
* 76 - unused
* 77 - Conversion Resistance
* 78 - Market Exchange Inefficiency - 0.3 by default in ''Age of Empires II'', and 0.5 in ''Return of Rome''
* 79 - Stone Mining Productivity
* 80 - Queued Units
* 81 - Training Count
* 82 - Start With Unit 444 (PTWC) - start with [[Packed Town Center]] when enabled
* 83 - (obsolete) Boarding Recharge Rate - percentage of [[Boarding Galley]] faith restored per second; default: 2
* 84 - Starting Villagers - starting villagers in non-scenario starts; default: 3
* 85 - Research Cost Modifier - Research cost of technologies except Ages multiplied by this resource, set to 1 at an unknown stage
* 86 - Research Time Modifier - Research time of technologies except Ages multiplied by this resource, set to 1 at an unknown stage
* 87 - Convert Boats
* 88 - Fish Trap Food Amount - default: 700
* 89 - Heal Rate Modifier - set to 1 at an unknown stage
* 90 - Healing Range - set to 4 at start of the game
* 91 - Starting Food - adds to starting food in non-scenario starts
* 92 - Starting Wood - adds to starting wood in non-scenario starts
* 93 - Starting Stone - adds to starting stone in non-scenario starts
* 94 - Starting Gold - adds to starting gold in non-scenario starts
* 95 - Enable PTWC / Kidnap / Loot - Among other things, enables Town Centers to pack to become Packed Town Centers
* 96 - No Dropsite Farmers - 1 for [[Khmer]] (previously hardcoded); previously Berserker Heal Timer - used for setting time it takes for Berserks to regenerate 1 HP
* 97 - Dominant Sheep Control - default: 0, 1 for Celts
* 98 - Building Cost Sum
* 99 - Tech Cost Sum
* 100 - Relic Income Sum
* 101 - Trade Income Sum
* 102 - unused
* 103 - unused
* 104 - unused
* 105 - unused
* 106 - unused
* 107 - unused
* 108 - unused
* 109 - unused
* 110 - unused
* 111 - unused
* 112 - unused
* 113 - unused
* 114 - unused
* 115 - unused
* 116 - unused
* 117 - unused
* 118 - unused
* 119 - unused
* 120 - unused
* 121 - unused
* 122 - unused
* 123 - unused
* 124 - unused
* 125 - unused
* 126 - unused
* 127 - unused
* 128 - unused
* 129 - unused
* 130 - unused
* 131 - unused
* 132 - unused
* 133 - unused
* 134 - Standing Castles
* 135 - Hit Points Razed
* 136 - unused
* 137 - unused
* 138 - unused
* 139 - unused
* 140 - unused
* 141 - unused
* 142 - unused
* 143 - unused
* 144 - unused
* 145 - unused
* 146 - unused
* 147 - unused
* 148 - unused
* 149 - unused
* 150 - unused
* 151 - unused
* 152 - Value Killed by Others
* 153 - Value Razed by Others
* 154 - Killed by Others
* 155 - Razed by Others
* 156 - unused
* 157 - unused
* 158 - unused
* 159 - unused
* 160 - unused
* 161 - unused
* 162 - unused
* 163 - unused
* 164 - Value Current Units
* 165 - Value Current Buildings
* 166 - Food Total
* 167 - Wood Total
* 168 - Stone Total
* 169 - Gold Total
* 170 - Total Value of Kills
* 171 - Total Tribute Received
* 172 - Total Value of Razings
* 173 - Total Castles Built
* 174 - Total Wonders Built
* 175 - Tribute score
* 176 - Convert Min Adjustment
* 177 - Convert Max Adjustment
* 178 - Convert Resist Min Adjustment
* 179 - Convert Resist Max Adjustment
* 180 - Convert Building Min
* 181 - Convert Building Max
* 182 - Convert Building Chance
* 183 - Reveal Enemy - 1 to enable Spies (seeing what enemies and neutral players can see)
* 184 - Value Wonders Castles
* 185 - Food Score
* 186 - Wood Score
* 187 - Stone Score
* 188 - Gold Score
* 189 - Wood Chopping Productivity - wood collected by villager for every wood depleted from trees
* 190 - Food-Gathering Productivity - food collected by villager for every food depleted from food source - specifically excludes Shepherds, Hunters and Fishermen
* 191 - Relic Gold Production Rate - gold generated per relic per minute
* 192 - Converted Units Die - 1 enables Heresy behavior (converted units die instead of converting)
* 193 - Theocracy - 1 enables Theocracy behavior (only 1 monk loses faith when a group of monks is converting)
* 194 - (obsolete) Crenellations - 1 enables infantry to fire arrows from buildings like Villagers
* 195 - Construction Rate Modifier - 1.3 is used for Spanish bonus
* 196 - Hun Wonder Bonus - Wonder and Relic countdown increased for all by 0.1x the value - 1000 is used for [[Atheism]]
* 197 - Spies Discount - ?
* 198 - unused
* 199 - unused
* 200 - unused
* 201 - unused
* 202 - unused
* 203 - Reveal Map
** 0 - default
** 1 - Entire map is explored (similar to cheat code "Marco") - used by [[Circumnavigation]]
** 2 - Entire map is visible (similar to cheat codes "Marco" + "Polo")
* 204 - Reveal Unit On Map
** When unit value is in 900 series (between 900 and 999, both inclusive), it applies on unit classes instead of units
** When the ID is positive, explores the units at the time of creation and/or resource assignment
** When the ID is negative, makes the units fully visible
* 205 - Feitoria Food Productivity - Feitorias produce 1.6x the food per second
* 206 - Feitoria Wood Productivity - Feitorias produce 0.7x the wood per second
* 207 - Feitoria Stone Productivity - Feitorias produce 0.3x the stone per second
* 208 - Feitoria Gold Productivity - Feitorias produce 1x the gold per second
* 209 - Reveal Enemy Town Center - 5 is used for Vietnamese bonus
* 210 - Reveal Unit Class On Map At Gamestart - can be used to make an object class of Gaia visible, not necessarily Relics
** -1 by default
** 42 for the Burmese team bonus because Relics belong to class 42
** Works only when used before start of the game, like Dark Age civilization bonuses, team bonuses or map scripts. Fails to work when used after start of the game, like using triggers, modifying it using a technology or a bonus needing some other technology to be researched first (like the Feudal Age)
* 211 - Elevation Higher Bonus - Add to the multiplier of damage when attacking from uphill - <math>DamageGiven = (Attack - Armor) \times (1.25 + Resource211)</math>
* 212 - Elevation Lower Bonus - Add to the multiplier of damage when attacking from downhill - <math>DamageGiven = (Attack - Armor) \times (0.75 + Resource212)</math>
* 213 - Raiding Productivity - Gold generated by [[Keshik (Age of Empires II)|Keshiks]] during combat for every 100 attacks - 50 by default, so generates 0.5 gold for every attack
* 214 - Mercenary Kipchak Count - the number of free [[Cuman Mercenaries|Elite Kipchaks]] that can be trained
* 215 - Mercenary Kipchak Limit - unused
* 216 - Shepherd Productivity - food collected by villager for every food depleted from herdables
* 217 - Shared Line of Sight - ?
* 218 - Early Town Center Limit - number of Town Centers allowed to be built before they are made freely available in Castle Age (this can be disabled on some maps, so this resource is applicable after Feudal Age too)
* 219 - Fishing Productivity - food collected by fishing ship for every food depleted from fishing source
* 220 - unused
* 221 - Monument Food Productivity - Monuments produce 0.8x the food per second
* 222 - Monument Wood Productivity - Monuments produce 0.8x the wood per second
* 223 - Monument Stone Productivity - Monuments produce 0.8x the stone per second
* 224 - Monument Gold Productivity - Monuments produce 0.8x the gold per second
* 225 - Relic Food Production Rate - food generated per relic per minute
* 226 - Villagers Killed by Gaia
* 227 - Villagers Killed by Animals
* 228 - Villagers Killed by AI Players
* 229 - Villagers Killed by Human Players
* 230 - Food Generation Rate
* 231 - Wood Generation Rate
* 232 - Stone Generation Rate
* 233 - Gold Generation Rate
* 234 - Spawn Limit - spawn limit at the moment (used in Conjugation with Spawn Command) - maximum number of available buildings allowed to spawn
* 235 - Flemish Militia Population - number of [[Flemish Militia]] obtained from [[Flemish Revolution]] - contributes to [[Spies (Age of Empires II)|Spies]]
* 236 - Farming Gold Productivity - gold generated per farmer|during farming, not during walking) per 100 seconds
* 237 - Folwark Collection Amount - amount of resource withdrawn and directly deposited into resource bank from farms
* 238 - Folwark Attribute Type - the resource with which this happens
** -1 by default
** 0 (for Food) upon researching the [[Folwark]] technology
* 239 - Folwark Building Type - the building with which Folwark is linked
** -1 by default
** 68 (Dark Age Mill) upon researching the Folwark technology
* 240 - Units Converted
* 241 - Stone Mining Gold Productivity - gold generated per stone miner (during mining, not during walking) per 100 seconds
* 242 - Trade Workshop Food Generation - (Special) Trade Workshops produce 2.25x the food per second - 1 by default
* 243 - Trade Workshop Wood Generation - (Special) Trade Workshops produce 2.25x the wood per second - 1 by default
* 244 - Trade Workshop Stone Generation - (Special) Trade Workshops produce 2.25x the stone per second - 0 by default
* 245 - Trade Workshop Gold Generation - (Special) Trade Workshops produce 2.25x the gold per second - 1 by default
* 246 - Units Value Total
* 247 - Buildings Value Total
* 248 - Villagers Created Total
* 249 - Villagers Idle Periods Total
* 250 - Villagers Idle Seconds Total
* 251 - Trade Food Percent - Food generated by Trade Units per 100 Gold
* 252 - Trade Wood Percent - Wood generated by Trade Units per 100 Gold
* 253 - Trade Stone Percent - Stone generated by Trade Units per 100 Gold
* 254 - Livestock Food Productivity - Resource which allows garrisoned [[Herdable animal]]s to produce food as <math>Resource 254 \times \ln \left( \frac{FoodAmount}{200} + 1 \right)</math> - 15 for [[Gurjaras]]
* 255 - obsolete
* 256 - obsolete
* 257 - obsolete
* 258 - obsolete
* 259 - obsolete
* 260 - obsolete
* 261 - obsolete
* 262 - (obsolete) Civilization Name Override
* 263 - Starting Scout ID - unit which is generated as a scout on random maps
* 264 - Relic Wood Production Rate - wood generated per relic per minute
* 265 - Relic Stone Production Rate - stone generated per relic per minute
* 266 - Lumbering Gold Productivity - gold generated per lumberjack (during gathering, not during walking) per 100 seconds - 1.5 with [[Paper Money]]
* 267 - Foraging Wood Productivity - wood generated per forager per 100 seconds
* 268 - Hunter Productivity - food collected by villager for every food depleted from hunt
* 269 - Technology Reward Effect - gold rewarded for researching any technology - includes [[Age]] ups by default - effect executed when any technology is researched
* 270 - Unit Repair Cost - repairing them costs ''Resource270'' times their build cost - 0.5 by default
* 271 - Building Repair Cost - repairing them costs ''Resource271'' times their build cost - 0.5 by default
* 272 - Elevation Higher Damage - Add to the multiplier of resistance when receiving damage from uphill - <math>DamageReceived = (Attack - Armor) \times (1.25 + Resource272)</math>
* 273 - Elevation Lower Damage - Add to the multiplier of resistance when receiving damage from downhill - <math>DamageReceived = (Attack - Armor) \times (0.75 + Resource273)</math>
* 274 - Infantry Kill Reward - Multiplier for gold generated for killing Monks, trade units, and Villagers using infantry (multiplied by 20, 20, and 5 respectively) - 1 with [[Chieftains]]
* 275 - unused
* 276 - (obsolete) Used for regenerating hit points in combat, see [[Ordo Cavalry]]
* 277 - Red Cliffs Tactics Damage - Multiplier for stingers effect of [[Red Cliffs Tactics]]
* 278 - unused
* 279 - Military Can Convert - Allows civilization's military units (if given non-zero value) to convert if they have a conversion task - enables conversion button at slot 15 in UI
* 280 - Military Convert Range - Military units' bonus conversion range - Conversion of military units = ''Resource280'' + work range of convert task - increased by 3 with [[Block Printing]]
* 281 - Military Convert Chance - Military units' conversion success chance - Chance to convert with every chant - default is 25, same as that of a Monk originally
* 282 - Military Convert Recharge - Military units' faith recharge rate - Faith to perform conversion restored per second - default is 1.6, same as that of a Monk - increased by 1.4 with [[Illumination]]
* 283 - Spawn Inside - Spawn Stance at the moment - Units spawned will be garrisoned by default if given non-zero value
* 284 - Cavalry Kill Reward - Gold generated for killing military units using mounted units
* 285 - Shared Visibility - ?
* 286 - Shared Exploration - ?
* 287 - Military Food Productivity - Military food production per 100 seconds - 3 after researching [[Tuntian]]
* 288 - [[Pasture (Age of Empires II)|Pasture]] Food Amount
* 289 - Pasture Animal Count - Number of animals in Pasture
* 290 - Pasture Herder Count - Maximum number of Villagers working in the Pasture
* 291 - Chopping Food Productivity - (probably unused in favor of resource 502) food generated while chopping wood
* 292 - Animal Decay Prevention - [[Hunt]]ed animals by civilization's Villagers do not decay
* 293 - Herder Food Productivity
* 294 - Shepherd Food Productivity
<!-- unused in between - Chronicles starts here -->
* 501 - [[Polemarch]] limit
* 502 - Lumbering Food Productivity - food generated per lumberjack (during gathering, not during walking) per 100 seconds - 4 for [[Athenians]] and 3.9 for [[Shu]]
* 503 - Wood Trade Ratio - Its value is between 0 and 1. If its value is 0.25, Trade Cogs generate {{Resources|wood = 25%|gold = 75%}}
* 506 - Achaemenid Town Center Local Upgrade - Hidden resource cost for Town Center upgrades - this prevents more than one upgrade to be researched at the same building
* 507 - (obsolete) Something related to Athenians policies
* 508 - Fortified Outpost Local Upgrade - Hidden resource cost for Outpost upgrades - this prevents more than one upgrade to be researched at the same building
* 509 - Mercenary Hoplite Productivity - Gold generated while attacking buildings (other than walls and Farms) for every 100 attacks
* 510 - Odomantian Raiders Productivity
* 511 - Dii Plunderers Productivity
* 512 - Stone Mining Food Productivity - food generated per {{Resources|stone = 4}} collected - 1 for [[Puru]]
* 513 - Emplacement Local Upgrade
* 520 - Unknown kill award - Multiplier for gold generated for killing units and buildings (multiplied by 5 and 10 respectively)
* 521 - Fort Gold Productivity - gold generated per [[Fort (Chronicles)|Fort]] per 3 seconds - 1 with [[Peloponnesian League]]
* 550 - Unknown kill award - Multiplier for gold generated for killing military units, Monks, buildings, and civilian units (multiplied by 2, 2, 5, and 1 respectively)
* 551 - Melee unit kill units award - Multiplier for gold generated for killing units using infantry, cavalry, or Monoremes (multiplied by 3) - 1 with [[Military Policy]]
* 560 - Fortified Outpost regeneration aura multiplier - 1 with [[Ends of the World]]
* 561 - [[Pattiyodha Longbowman]] aura enabler 1
* 562 - Pattiyodha Longbowman aura enabler 2
* 563 - Shepherding and Hunting Gold Productivity - gold generated per {{Resources|food = 20}} collected - 1 for [[Thracians]]

=== Store Mode ===
* 0 - Keep (decayable resource) - resource decays in ''Amount of Resource left / Resource Decay'' seconds
* 1 - Keep - enables instantly, stays after death
* 2 - Give and Take - enables instantly, resets on death
* 4 - enables upon completion, resets on death
* 8 - enables upon completion, stays after death
* 16 - Stores the resource in the unit's/building's repository instead of being stored globally
* 32 - used by [[Konnik]] to prevent population to go down between its respawn

== Unit classes ==
* 0 - Archer - more accurately ''Foot Archer'', excludes [[Hand Cannoneer]] and [[Janissary (Age of Empires II)|Janissary]]
* 1 - Artifact - Relic Cart and Monument
* 2 - Trade Boat - Trade Cog and Junk
* 3 - Building - All buildings except [[tower]]s, [[wall]]s, gates and Monument
* 4 - Civilian - [[Villager (Age of Empires II)|Villagers]] and all their variations
* 5 - Ocean Fish - more commonly known as deep sea fish
* 6 - [[Infantry unit (Age of Empires II)|Infantry]] - includes [[Hunting Wolf]]
* 7 - [[Berry Bush]]
* 8 - [[Stone Mine]]
* 9 - Prey Animal - basically passive huntable animals ([[Deer]], [[Ibex]], [[Ostrich]], [[Zebra]]), and [[Wild Horse]], [[Wild Camel]] and [[Wild Bactrian Camel]]
* 10 - Predator Animals - basically aggressive huntable animals ([[Wild Boar]], [[Javelina]], [[Elephant]] and [[Rhinoceros]]), and [[Wolf]], [[Snow Leopard]], [[Komodo Dragon]], [[Tiger]], [[Crocodile]], [[Lion]], [[Bear (Age of Empires II)|Bear]], and [[Jaguar]]
* 11 - Miscenalleous - mostly dead bodies, projectiles and birds
* 12 - [[Cavalry unit (Age of Empires II)|Cavalry]] - excludes [[Scout Cavalry (Age of Empires II)|Scout Cavalry]], includes [[Ballista Elephant (Age of Empires II)|Ballista Elephant]] and [[Armored Elephant (Age of Empires II)|Armored Elephant]] lines
* 13 - Siege weapon - Rams, Mangonels, Organ Guns, Bombard Cannons, Siege Towers, and Flamethrowers
* 14 - Terrain - includes Statues, Stelae, Rubble and Visual Resources (like lumber and food carts)
* 15 - [[Tree]]
* 16 - Tree Stump
* 17 - Healer - unused
* 18 - [[Monk (Age of Empires II)|Monk]] - includes [[Missionary (Age of Empires II)|Missionary]], [[Priest (Age of Empires II)|Priest]], and healers ([[Chand Bardai]] and [[Jadwiga]])
* 19 - [[Trade Cart (Age of Empires II)|Trade Cart]] - includes Donkeys
* 20 - [[Transport Ship (Age of Empires II)|Transport Boat]]
* 21 - [[Fishing Ship (Age of Empires II)|Fishing Boat]]
* 22 - Warship - basically every ship except Fishing, Transport, Boarding, and Trade ships
* 23 - [[Conquistador (Age of Empires II)|Conquistador]] - includes [[Arambai]]
* 24 - War Elephant - unused
* 25 - Hero - unused
* 26 - Elephant Archer - unused
* 27 - [[Wall]] - includes empty buildings, excludes 39 - gates
* 28 - Phalanx - unused
* 29 - Domestic Animal - unused
* 30 - Flag
* 31 - Deep Sea Fish - unused
* 32 - [[Gold Mine]]
* 33 - [[Shore Fish]] - includes Box Turtles
* 34 - Cliff
* 35 - [[Petard (Age of Empires II)|Petard]] - includes [[Flaming Camel]]
* 36 - Cavalry Archer - all mounted archers except 23 - Conquistadors
* 37 - Doppelganger - unused (used by the Doppelganger, which is not even seen in the Scenario Editor)
* 38 - Bird - contrary to name, this refers to the invisible object which keeps player alive even if player owns nothing
* 39 - [[Gate (Age of Empires II)|Gate]]
* 40 - Salvage Pile - permanent Rubble of various sizes
* 41 - Resource Pile - Visually identical to regular Stone mine/Gold mine/Fallen tree/Forage bush, but it only has 1 resource
* 42 - [[Relic (Age of Empires II)|Relic]]
* 43 - Monk with Relic
* 44 - [[Hand Cannoneer]] - includes [[Janissary (Age of Empires II)|Janissary]]
* 45 - Two-Handed Swordsman - unused
* 46 - Pikeman - unused
* 47 - Scout - only the [[Scout Cavalry (Age of Empires II)|Scout Cavalry]], not even its upgrades
* 48 - Ore Mine - (removed feature)
* 49 - [[Farm (Age of Empires II)|Farm]] - includes [[Fish Trap]]
* 50 - Spearman - unused
* 51 - Packed unit - Packed Trebuchets and Packed Town Center
* 52 - Tower - [[Watch Tower (Age of Empires II)|Watch Tower]] line, [[Donjon]]s, [[Fire Tower]], [[Bombard Tower]], and [[Sea Tower]]
* 53 - [[Boarding Galley|Boarding Boat]] - Boats which can convert enemy boats at close range (removed feature)
* 54 - Unpacked Siege Unit - basically unpacked [[Trebuchet]]s
* 55 - Ballista - [[Scorpion (Age of Empires II)|Scorpions]] and [[Hussite Wagon]]s
* 56 - Raider - foot units with 0 attack and no armor classes (removed feature)
* 57 - Cavalry Raider - mounted units with 0 attack and no armor classes (removed feature)
* 58 - Livestock - [[Herdable animal]]s
* 59 - [[King (Age of Empires II)|King]] - includes [[Queen]] and [[Merchant (Age of Empires II)|Merchant]] (neither have the ability to attack) and Carts (visually similar to Trade Carts, but cannot Trade)
* 60 - Miscenalleous Building (unused)
* 61 - Controllable Animal - controllable variations of [[Horse]] and [[Camel]], which can be controlled and used to scout (cannot attack)
* 64 - Land Mine - Self detonate unit, deals damage on death (like petard class). Does not trigger AI retaliation.

== Unit type ==
* 10 - Eye Candy
* 15 - Trees (AoK) - unused
* 20 - Animated
* 25 - Doppelganger - unused (used by the Doppelganger, which is not even seen in the Scenario Editor)
* 30 - Moving - Fish, Tree Stump and Dead bodies mainly (also includes Cactus)
* 40 - Actor - unused
* 50 - Superclass - unused
* 60 - Projectile
* 70 - Combatant
* 80 - [[Building (Age of Empires II)|Buildings]] - also included Packed units and Bridges
* 90 - Tree (AoE) - unused

== Attributes ==
* 0 - [[Hit points]]
* 1 - [[Line of Sight]]
* 2 - [[Garrison]] Capacity
* 3 - Unit Size X
* 4 - Unit Size Y
* 5 - [[Speed|Movement Speed]] [Speed in Unit Stats and search bar]
* 6 - Rotation Speed
* 7 - unused
* 8 - [[Armor]] (for more info, see [[Armor class]])
* 9 - [[Attack]] (for more info, see [[Armor class]])
* 10 - [[Rate of Fire|Attack Reload Time]]
** For military units: Number of seconds between attacks
** For Monks and [[Boarding Galley]]s: Percentage of conversion faith restored in 1 second (previously controlled by resources 35 and 83 respectively)
* 11 - Accuracy Percent
* 12 - [[Range|Maximum Range]]
* 13 - Work Rate
* 14 - Carry Capacity
* 15 - Base Armor (for more info, see [[Armor class]])
* 16 - (Primary) Projectile Unit
* 17 - Icon/Graphics Angle - Has two behaviors, one for icon on the building list of builder units, the other for the sprite rotation of building
** '''Icon''' behavior works as following
*** attribute 25 "icon" value + this attribue value = shown icon in the building list (originally intended to change the icon depending on current age, barracks for example) ''[needs further testing to be truly understood]''
** '''Graphic''' '''Angle''' behavior works as following
*** for multi-angle building sprites, such as Pavilions and Greek Tents, this attribute value will determine which "frame" of the sprite is rendered (refer to AGE graphics tab to see angle counts on sprites)
*** '''Further Information:''' For the rotation to work, the graphic must have multiple angles. The Greek Army Tent has 6 angles, 1 frame per angle, allowing this attribute to affect the Greek Army Tent graphic. The House has 1 angle, 3 frames per angle, disallowing this attribute to be applied to House graphics. The field "Sequence Type" in the graphic parameter seems also to affect the result, if it has the bit 4 "Sprite Randomized", it turns out to become very hard to affect the sprite rotation.
* 18 - Terrain Defense Bonus
** 4 - Buildings (-1 others)
* 19 - Enable Smart Projectile [Smart Mode in Unit stats and search bar]
** 1 - projectile can track moving target
** 2 - damage dealt by projectile is multiplied by receiving unit's friendly fire multiplier attribute, instead of getting multiplied by 0.5
* 20 - Minimum Range
* 21 - Amount of 1st Resource Storage
* 22 - [[Area of Effect#Blast Damage in Age of Empires II|Blast Width]]
* 23 - Search Radius
* 24 - Hidden Damage Resistance [Bonus Damage Resistance in Unit stats and search bar] (for more info, see [[Armor class]])
* 25 - Icon
* 26 - Amount of 2nd Resource Storage
* 27 - Amount of 3rd Resource Storage
* 28 - Fog Visibility - unique effect, cannot be combined
** 0 - Not visible
** 1 - Always visible
** 2 - Visible if alive - unused
** 3 - Inverted Visibility - unused (used by the Doppelganger, which is not even seen in the Scenario Editor)
** 4 - Check doppelganger - unused
* 29 - Occlusion Mode
** 0 - No outline
** 1 - Outline displayed through Occlusion
** 2 - Occludes others
** 4 - Outline displayed while constructing
** 8 - unknown - used by Gates and Forage/Fruit bushes
* 30 - [[Garrison]] Type
** 1 - Villager and Kings
** 2 - Infantry and Foot Archers
** 4 - Mounted units (including Mounted Siege units and Mounted Monks)
** 8 - Foot Monks
** 16 - Livestock
** 32 - Siege units
** 64 - Ships
* 32 - Unit Size Z
* 33 - Can Be Built On
* 34 - Foundation Terrain
* 40 - [[Hero (Age of Empires II)|Hero]] Status [Hero Mode in Unit stats and search bar]
** 1 - Full Hero Status (all effects from 2 to 64 and also appears in Hero tab in the scenario editor)
** 2 - Cannot be converted
** 4 - Regenerates 30 hit points/min (can be combined with Attribute 109 - Regeneration)
** 8 - Default Defensive Stance (does not work with buildings)
** 16 - Protected Formation - unit lies in centre when selected in group with other units (does not work with buildings)
** 32 - Safe Delete Confirmation - warning appears when trying to delete
** 64 - Glow
** 128 - Invert effect of one hero property (used in conjugation with 1 (since using it with 0 and not using it will be identical) and one of the above properties)
* 41 - [[Attack delay#Frame delay|Frame Delay]]
* 42 - Train Location
** for '''Units''' to be trainable '''from Buildings''' (common list only already used in the game, any building ID may be used) ''[untested building trained by building, may not work]''
** for '''Buildings''' to be buildable '''from Units''' (common list already used by the game, any unit ID may be used but animation issue may occure[?]) ''[untested unit trained by unit, may not work]''
** Examples:
*** 118 - Builder[Villager] (civilian / military tab location depends on the attribute '''"Interface Kind"''') - With '''"Interface Kind"''' value
**** 2 - Civilian building tab
**** 10 - Military building tab
**** ''11 - unknown unused "Shield" building tab according to AGE tooltips (may have no effect)''
*** 13 - Fishing Ship (used by Fishing Trap, with "Interface Kind" value of 2)
*** 2117 - Port
*** 2119 - Shipyard
* 43 - Train Button - determine grid placement of unit/building icon
** for '''Buildings''' to be buildable '''from Villager''' building tabs (both Civilian and Military)
*** 1 to 5 - Top row left to right
*** 6 to 10 - Center row left to right
*** 11 to 15 - Bottom row left to right
*** 14 - Switch between Civilian and Military building tab ''(verification needed, overriding untested)''
*** 15 - Cancel current action and return to villager default action list ''(verification needed, overriding untested)''
** for '''Units''' to be trainable '''from Building''' with garrison capacity but no regarrisonable capability once ungarrisoned like Barracks, Stable, etc ''('''"Garrison Capacity" > 0''' and '''"Garrison Type" = 0''')''
*** 1 to 5 - Top row left to right
*** 6 to 10 - Center row left to right
*** 11 to 15 - Bottom row left to right
*** 5 - Set rally point ''(verification needed, overriding untested)''
*** 10 - Ungarrison all units inside; toward Rally point if set / arround itself if no Rally point ''(verification needed, overriding untested)''
*** 15 - Cancel current action and return to building default action list ''(verification needed, overriding untested)''
** for '''Units''' to be trainable '''from Garrisonable Building''' with ungarrison/regarrison capability like Towers, Castle, etc ''('''"Garrison Capacity" > 0''' and '''"Garrison Type" > 0''')''
*** 1 to 5 - Top row left to right
*** 6 to 10 - Center row left to right
*** 11 to 15 - Bottom row left to right
*** 5 - Set rally Point ''(verification needed, overriding untested)''
*** 9 - Send back villager in garrison to work ''(verification needed, overriding untested)''
*** 10 - Ungarrison all units inside; toward Rally point if set / arround itself if no Rally point
*** 14 - Send back to work all villagers in garrison for self and surrounding buildings (only appears if villagers garrisoned in o nearby)
*** 15 - Cancel current action and return to building default action list
** for '''Units''' to be trainable '''from Town Center'''
*** 1 to 5 - Top row left to right
*** 6 to 10 - Center row left to right
*** 11 to 15 - Bottom row left to right
*** 5 - Set rally point
*** 10 - Ungarrison all units inside; toward Rally point if set / arround itself if no Rally point
*** 11 - Age Up technology slot
*** 14 - Send back to work all villagers in garrison for self and surrounding buildings (only appears if villagers garrisoned in o nearby)
*** 15 - behavior changes based on following
**** With action - Cancel current action and return to building default action list
**** Without action - Ring town Bell, behavior changes depends on following
***** Bell not Rung - Call nearby villagers to garrison into closest building
***** Bell Rung - Call nearby garrisoned villager into buildings to return to their previous work task
** for '''Units''' to be trainable '''from Market''' ''(also from the hidden unit Trade Workshop with trading mechanics similar to Market)''
*** 1 to 5 - Top row left to right
*** 6 to 10 - Center row left to right
*** 11 to 15 - Bottom row left to right
*** 5 - Set Rally point
*** 7 - Sell Wood
*** 8 - Sell Food
*** 9 - Sell Stone
*** 10 - Ungarrison all units inside; toward Rally point if set / arround itself if no Rally point
*** 12 - Buy Wood
*** 13 - Buy Food
*** 14 - Buy Stone
*** 15 - Cancel current action and return to building default action list
** for '''Units''' to be trainable '''from Mill'''
*** 1 to 5 - Top row left to right
*** 6 to 10 - Center row left to right
*** 11 to 15 - Bottom row left to right
*** 4 - Queue up '''Farm''' to rebuild on depletion
*** 5 - Toggle on/off auto '''Farm''' rebuild on depletion ''(may cause issue with set Rally point overriding?)''
*** 10 - Ungarrison all units inside; toward Rally point if set / arround itself if no Rally point
*** 15 - Cancel current action and return to building default action list
** for '''Units''' to be trainable '''from Dock''' ''(regular Dock and Malay Harbor only and cap, not the Port / Shipyard from Chronicles)''
*** 1 to 5 - Top row left to right on '''First''' page
*** 6 to 10 - Center row left to right on '''First''' page
*** 11 to 15 - Bottom row left to right on '''First''' page
*** 21 to 25 - Top row left to right on '''Second''' page
*** 26 to 30 - Center row left to right on '''Second''' page
*** 31 to 35 - Bottom row left to right on '''Second''' page
*** 5 ''(and 25 ?)'' - Set Rally point
*** 10 ''(and 30 ?)'' - Ungarrison all units inside; toward Rally point if set / arround itself if no Rally point
*** 11 ''(and 31 ?)'' - Queue up '''Fish Trap''' to rebuild on depletion
*** 12 ''(and 32 ?)'' - Toggle on/off auto '''Fish Trap''' rebuild on depletion
*** 15 ''(and 35 ?)'' - behavior changes based on following
**** Without action - Switch between '''First''' and '''Second''' pages
**** With action - Cancel current action and return to building default action list
** for '''Units''' to be trainable '''from Port''' ''(Civilian Ship building for Chronicles DLC civ)''
*** 1 to 5 - Top row left to right
*** 6 to 10 - Center row left to right
*** 11 to 15 - Bottom row left to right
*** 5 - Set Rally point
*** 10 - Ungarrison all units inside; toward Rally point if set / arround itself if no Rally point
*** 14 - Cycle antiquity trade ship income between: "25% Wood and 75% Gold" / "50% Wood and 50% Gold" / "75% Wood and 25% Gold"
*** 15 - Cancel current action and return to building default action list
** for '''Units''' to be trainable '''from Shipyard''' ''(Military Ship building for Chronicles)''
*** 1 to 5 - Top row left to right
*** 6 to 10 - Center row left to right
*** 11 to 15 - Bottom row left to right
*** 5 - Set Rally point
*** 10 - Ungarrison all units inside; toward Rally point if set / arround itself if no Rally point
*** 15 - Cancel current action and return to building default action list
** '''Further Informations:'''
*** Keep in mind that in the editor it is currently not possible(?) to modify Technology location / grid placement, same for core mechanics like rally point, garrisoning, town bell, market exchanging. With Datamod the player can modify everything as they want, if they find where to changes the thing they want to
*** When the player sets units/buildings/technology under the same gride position, they can enable/disable them to replace the wanted object in the slot they aim for, as it already works in the game for upgrades such as units/walls/linked technologies
* 44 - [[Area of Effect#Blast Damage in Age of Empires II|Blast Attack Level]] - combine one primary and one secondary effects
** Primary effect - unique effect, cannot be combined
*** 0 - damages resources
*** 1 - damages trees also
*** 2 - damages nearby units
*** 3 - damages only targeted units
** Secondary effect - unique effect, cannot be combined
*** 0 - equal damage in entire blast radius
*** 64 - tapering effect (only for melee units)
*** 128 - blast attack in the direction of attack
* 45 - Blast Defense Level - Receive Blast Attack from units which have same or lower primary Blast Attack Level
* 46 - Shown Attack
* 47 - Shown Range
* 48 - Shown Melee Armor
* 49 - Shown Pierce Armor
* 50 - Unit Name String - used to name/rename units with names existing in Language files
* 51 - Unit Short Description String - used to describe/redescribe units with descriptions existing in Language files
* 52 - unused
* 53 - Terrain Restriction (Terrain Table in Unit stats and Search bar) - determine what terrain table unit can walk on / building can be built on, and effect they render on corresponding terrain table (can be seen and altered in AGE "Terrain Tables" tab)
** 0 - All, no effect ''(projectile and building purpose)''
** 1 - Land and shallows, no effect ''(predator and prey animal purpose)''
** 3 - Water only, '''Large Wave''' effect ''(large ship and naval building purpose)''
** 4 - Land only, no effect ''(land building purpose)''
** 6 - Water only, no effect ''(naval building purpose)''
** 7 - All but water, '''Foot Dust''' effect ''(foot unit purpose)''
** 8 - Land but farm, no effect ''(mining resource pile purpose)''
** 10 - Land and beach, no effect ''(Wall and Gate purpose)''
** 11 - Land but farm, no effect ''(mountain, tree and food resource pile purpose)''
** 12 - All but bridge, '''Ground Impact''' effect ''(area damage projectile purpose)''
** 13 - Water only, '''Small Wave''' effect ''(small ship and fish spot purpose)''
** 14 - All but bridge, '''Arrow Decay''' effect ''(arrow projectile purpose)''
** 15 - Water only, '''Large Wave''' particle ''(Transport Ship)''
** 18 - All but bridge, '''Spear Decay''' effect ''(spear projectile purpose)''
** 19 - Only Water and ice, no effect ''(shore fish spot purpose)''
** 20 - All but water, '''Wheel Track''' effect ''(siege weapon purpose)''
** 21 - Shallow water only, no effect ''(Naval Wall and Tower purpose)''
** 22 - All but bridge, '''Dart Decay''' effect ''(dart projectile purpose)''
** 23 - All but bridge, '''Arrow Decay''' effect ''(arrow (fire) projectile purpose)''
** 24 - All but bridge, '''Ground Impact''' effect ''(area damage (fire) projectile purpose)''
** 25 - All but bridge, '''Spear Decay''' effect ''(spear (fire) projectile purpose)''
** 26 - All but brdige, '''Dart Decay''' effect ''(dart (fire) projectile purpose)''
** 27 - All but bridge, '''Laser Impact''' effect ''(laser projectile purpose)''
** 28 - All but water, '''Cavalry Dust''' effect ''(horseback unit purpose)''
** 29 - All but water, '''Wheel Track''' effect ''(Trebuchet Packed)''
** 30 - Water only, '''Medium Wave''' effect ''(medium ship purpose)''
** 31 - All but water, '''Wheel Track''' effect ''(bombard, hofnice)''
** 32 - Table, (?) effect ''(dromon (fire) projectile purpose)''
* 54 - Unit Trait [Trait in search bar]
** 1 - Garrison unit - for units which can garrison other units, like Transport Ships and Siege Towers
** 2 - Ship unit
** 4 - Builder unit - can place foundation of a single type of building (theoretically (the unit also needs a corresponding task to enable it to build)), which is given by Attribute 56
** 8 - Transformable unit - can transform into another unit which is given by Attribute 56, using the switch weapon button (only works for soldiers) ''[not related "transformation unit" attribute used by Trebuchet / packed town center, it's a different mechanic depending on unit class value 51 "packed unit" and the "transformation unit" attribute field]''
** 16 - Scout unit - enables [[Auto Scout]] button if modified and placed at start of the game
** 64 - Building to terrain transform - upon completion of building, it recalculates the traversability of terrain. It is used in [[Tyre Must Fall]] to swap water to be actual land.
** 128 - {{?}} - used by Macedonian human soldiers
* 55 - Unit Civilization [Civilization in Unit stats and search bar] - unused
* 56 - Unit Trait Piece [Trait Piece in Unit stats; Nothing in search bar]
** '''For Builder unit flag''': Units can build Unit Trait Piece only when the unit has Unit Trait flag 4 at least (but not 8), the Trait Piece is a building (in earlier versions, building creatable units like Transport Ships would crash the game), the building is enabled (like Castles are enabled in Castle Age but disabled before that), the unit has the task to enable building in general (like Builders and Fishing Ships) or enable building the Trait Piece (Serjeants have a task to enable building Donjons). Despite Fishing Ships having the task to build, they are hardcoded not to build any building other than Fish Traps, however this hardcoded behavior does not stop them from placing the foundation of the Trait Piece.
** '''For Transformable unit flag''': Unit Transformation among units is not reciprocal by default. Both units need to be modified to convert into one another. If the Unit Trait Piece is a building, the object turns into a Moveable Map Revealer, which contrary to its name, cannot move.
** '''For Active Transformation''' (see Charge Type): Transforms into this unit
* 57 - Dead Unit - unit which is left behind when the main unit dies
* 58 - Hotkey
* 59 - Maximum Charge
* 60 - Recharge Rate
* 61 - Charge Event
** For melee charge attacks: 1 - charge attack drops to 0 after using against units
** For ranged charge attack: Additional range when using charge attack (can be negative)
** For active transforms:
*** -1 - performs an attack ground on its location
*** 0 - transforms until performs one attack
*** Other - Duration of the transformation
** For active aura ability - Duration of the transformation
** For conversion ability - Conversion range (may be overwritten by the conversion tasks)
** all others - charge attack stays at full potential
* 62 - Charge Type - unique effect, cannot be combined
** 1 - Charge Attack
** 2 - Hit Points - unused
** 3 - Charge Area Attack
** 4 - Projectile Agility - ability to dodge projectiles - charge is reduced by 1 instead of hit points being reduced by damage for every projectile absorbed
** 5 - Melee Agility - ability to dodge melee attacks - charge is reduced by 1 instead of hit points being reduced by damage for every melee attack absorbed
** 6 and 7 - Charged Ranged Attack: Fires max total projectiles (related attributes: charge target, charge projectile unit)
** 6 - Charged Ranged Attack 1 - units attack with charged projectiles only
** 7 - Charged Ranged Attack 2 - used by Turtle Ships with 1 charged projectile and additional secondary projectiles
** -1 - Active Temporary Transformation - Temporarily transforms into another unit (set by Trait Piece)
** -2 - Active Targeted Transformation - Transforms into another unit when tasked to a valid target (set by Trait Piece) after pressing the ability button
** -3 - Active Aura Ability - Activates a power up aura when pressing the button; Requires Task 155 Aura with Unused Flag 8
** -4 - Conversion for non Monk type units; Requires Task 104: Convert; Charge Target: Conversion percent chance
** -5 - Spawn Unit - Spawn building set in Trait Piece on top of the unit; Displays the spawn object's icon and train tooltip by default; these can be overwritten by the ability button attributes
* 63 - Combat Ability [Break Off Combat in Unit stats and search bar]
** 1 - Armor ignoring ability (works for melee and pierce attacks, not attack bonuses)
** 2 - Resist Armor ignoring ability - cancels enemy's armor ignoring effect if it has, no effect otherwise
** 4 - Armor damaging ability - damages enemy melee and pierce armor by 1 independently with every attack, cannot reduce below 0
** 8 - [[Attack ground]] ability
** 16 - Bulk Volley Release - all projectiles of the unit are released together
** 32 - Influence ability - allows unit/building to modify attributes of units in influence range
** 64 - Inverse influence - (requires flag 32) makes other units boost self, instead of the unit boosting other units - If the unit has several power up tasks, all except the first task need to have Auto Search attribute set to 1
** 128 - Activate Stingers, triggered when performing an attack - see Task 157
* 64 - Attack Dispersion
* 65 - Secondary Projectile Unit
* 66 - Blood Unit - in some cases units have a Blood Unit in addition to having a Dead Unit, which serves as another dead unit basically
* 67 - (Projectile) Hit Mode
* 68 - (Projectile) Vanish Mode
** 1 - to allow [[pass-through damage]]
** 2 - spawns dead unit when projectile lands
* 69 - (Projectile) Arc
* 70 - Attack Graphic
* 71 - Standing Graphic
* 72 - Standing Graphic 2
* 73 - Dyning Graphics ID
* 74 - Undead Graphic - Used for assigning the decay graphic to units which don't have Undead Mode attribute set to 1; for them undead graphic overwrites the standing graphic of the object's dead unit.
* 75 - Walking Graphic - applies on all movement actions, including attacking target (may be overriden by Running Graphics on attack move, further test needed)
* 76 - Running Graphic - only applies when moving while attacking a target, also known as "Attack Move". Wolf/Predator units have special Running graphic, including hardcoded speed modifier within the graphic settings.
* 77 - Special Graphic - if specified, will apply the sprite when consuming "Maximum Charge" from a charged attack, use regular "Attack Graphic" value if unspecified (may not work on dodge mechanic, further test needed)
* 78 - Obstruction Type: Controls the type of obstruction a unit/building has:
** 0 - circle ground selection
** 1 - circle ground selection
** 2 - square ground selection
** 3 - square ground selection
** 4 - square ground selection
** 5 - circle ground selection
** 10 - square ground selection
** 11 - consider the selection size of a radius entirely as opposed to the actual defined collision size.
** 12 - ignore hard obstructions entirely and just consider the space occupied with no obstruction at all.
** 13 - consider the selection radius when placing other objects, but use the original obstruction size for hard obstructions.
** other value - invisible ground selection
* 78 - unknown - affect ground selection display once object moved (further testing needed)
<!-- unused in between -->
* 81 - Special Ability
** 0 - none
** 1 - Block: ''[untested] Activate "Special Graphic" on angled toward hit source, while receiving damage and not pursuing the attacker. While idle, should decrease taken damage by 1/3.''
** 2 - Counter Charge: ''[untested] Activate "Special Graphic" when idle and enemy is near. While idle, attacks back once on first received hit. Enemy must be unit type 70 and have less than 0.2 max range.''
** 3 - Speed Charge: On attacking a target, within set distance with charged attack ready, increase movement speed until first attack or cancelation of the unit current attack task (won't consume Charged attack if canceled) 
*** ''Seems to require "Maximum Charge" / "Recharge Rate" / "Charge Type" / "Charge Event" to be set for the unit to have a Charged attack to work, even without task 133 added, probably automatically set by the game if not manually added. Tested on cavalry units with custom dataset and is working as the Monoreme line, without adding task 133 to the said units.''
** '''''[unused/unimplemented?]''' - AGE Tooltips indicates informations, but game patchnote never said anything about those parameters (Note: parameter 3 in AGE is different than actual behavior in the game added with Chronicle DLC)''
** '''''[unused/unimplemented?]''' - AGE Tooltips indicates they were planned but never Implemented ships special attacks, described in the AoK design document''
** 4 - Ram: ''[untested] Charge against another ship, losing some hit points self. (Demo Ship / Saboteur behaviors share similarity)''
** 5 - Greek Fire: ''[untested] Fry units on ships passing through the player's sea of fire. (Fire Ship / Attack Ground behaviors share similarity)''
** 6 - Board: ''[untested] Attach to another ship, resulting in takeover or sinking. (Boarding Ships / Monk convertion behaviors share similarity)''
** 7 - Building is placed directly on top of the unit instead of giving placement option (must be combined with unit trait 4)
* 82 - Idle Attack Graphic
* 83 - Hero Glow Graphic
* 84 - Garrison Graphic
* 85 - Construction Graphic
* 86 - Snow Graphic
* 87 - Destruction Graphic
* 88 - Destruction Rubble Graphic
* 89 - Researching Graphic
* 90 - Research Completed Graphic
* 91 - Damage Graphic
* 92 - Selection Sound
* 93 - Selection Sound Event
* 94 - Dying Sound
* 95 - Dying Sound Event
* 96 - Train Sound
* 97 - Train Sound Event
* 98 - Damage Sound
* 99 - Damage Sound Event
* 100 - Resource Costs
* 101 - Train Time
* 102 - Total Missiles: Number of projectiles fired
* 103 - Food Costs
* 104 - Wood Costs
* 105 - Gold Costs
* 106 - Stone Costs
* 107 - Max Total Projectiles: Maximum number of projectiles which can be fired
** For buildings, the number of projectiles can be increased to this number by garrisoning units
** When using charged ranged attack, the number of projectiles fired will be this number
* 108 - Garrison Heal Rate (determine how many HP healed each second while garrisoned inside a building)
* 109 - Regeneration Rate [Backstab Bonus in Unit stats; Rear Attack Modifier in search bar] - hit points regenerated per minute
* 110 - Population Headroom Storage (negative for units and Feitorias, positive for buildings which give population)
* 111 - Additional Minimum Conversion Time
* 112 - Additional Maximum Conversion Time
* 113 - Additional Conversion Resistance Level
* 114 - [[Unit formation#Age of Empires II|Formation Category]] [Creatable Type in Unit stats and search bar]
** 0 - not applicable (Villagers, Fishing Ships, Trebuchets)
** 1 - mobile (cavalry)
** 2 - body (infantry)
** 3 - ranged (archers)
** 4 - long ranged (Hand Cannoneer-type and Scorpions)
** 5 - protected (all other siege, Monk, King, other civilians)
** 255 - buildings
* 115 - Area Damage - Blast damage dealt
** If less than 0: Absolute value of damage dealt - for example, if value is -3, trample damage deals 3 damage
** If more than 0: Used as multiplier - for example, if value is 0.5, attack is 10, and armor is 2, damage dealt is 4
* 116 - Melee armor when used by Aura task (155)
* 117 - Blockage Class - Pierce armor when used by Aura task (155)
** 0 - Forces default obstruction type
** 1 - Resource
** 2 - Unit
** 3 - Building
** 4 - Wall
** 5 - Gate, allows trespassing
** 6 - Cliff, blocks walling
* 118 - Melee damage deflection, see [[Lamellar Armor (Age of Empires II)|Lamellar Armor]]
* 119 - Friendly fire multiplier - when a projectile unit with area of effect damage attacks units, allied units receive damage too, which is called friendly fire. This multiplier can be used to modify said friendly fire. It works on the attacking units, not the recipient units. Default: 1.
* 120 - HP based regeneration - Percentage of maximum HP regenerated over a minute
* 121 - Ability icon - Override for Transform/Active Ability Icon
* 122 - Short Tooltip - Override for Transform/Active Ability Short Tooltip
* 123 - Long Tooltip - Override for Transform/Active Ability Long Tooltip
* 124 - Ability Hotkey - button_action_list when pressing button/hotkey for the ability or transformation
* 126 - Train limit for disabled units: when Disabled flag 2 or 4 is set, sets value for number of trainable unit
* 127 - Disabled flag
** 1 - Disabled
** 2 - Limited training. Cannot be retrained after death
** 4 - Limited training. Can be retrained after death
** 8 - Disabled after trained - remove the train/build button from UI if the train/build limit is reached
* 128 - Attack priority
*# Units > Buildings
*# Buildings > Units
*# Only buildings
* 129 - Invulnerability Level: Sets an HP threshold after which a unit no longer receives damage when attacked
** If > 0, used as multiplier of base HP
** If < 0, sets a value of HP
* 130 - Garrison Firepower
** <= 0: Absolute value of this number
** >= 0: Prodoct of pierce attack and this number
* 131 - Secondary attack graphics: Second attack graphic of the unit; alternates with the first attack graphic when assigned
* 132 - Command Sound
* 133 - Command Sound Event
* 134 - Move Sound
* 135 - Move Sound Event
* 136 - Construction Sound
* 137 - Construction Sound Event
* 138 - Transform Sound
* 139 - Transform Sound Event
* 140 - Shared Selection (Run Pattern in Unit Stats)
** 0 - selects units with the same class and name ID (default behavior)
** 1+ - select together with units that have the same run pattern
** 255 - only units with same ID are selected.
* 141 - Interface Kind
** 0 - visible
** 1 - Resource
** 2 - Building (appearing on Build page 1, related to "Train Location")
** 3 - Civilian (Villager actions list: Civilian Building / Military Building / Repair)
** 4 - Soldier (Military action list: Patrolling / Follow / Defend / Attack Move / Stances)
** 5 - Trade Unit (Trading behavior)
** 6 - Priest (Monk behavior)
** 7 - Transport Ship (load/unload behavior)
** 8 - Relic / Priest with Relic (relic behavior)
** 9 - Fishing Boat (fish trap construction)
** 10 - Military Building (appearing on Build page 2, related to "Train Location")
** 11 - Shield Building (AGE suggest "build page 3", unknown, probably unreleased feature for walls/gates as they are now in military buildings)
* 142 - Combat Level
* 143 - Interaction Mode
* 144 - Minimap Mode
* 145 - Trailing Unit
* 146 - Trail Mode
* 147 - Trail Density
* 148 - Projectile Graphic Displacement X
* 149 - Projectile Graphic Displacement Y
* 150 - Projectile Graphic Displacement Z
* 151 - Projectile Spawning Area Width
* 152 - Projectile Spawning Area Length
* 153 - Projectile Spawning Area Randomness
* 154 - Damage Graphics Entry Mod
* 155 - Damage Graphics Total Num
* 156 - Damage Graphic Percent
* 157 - Damage Graphic Apply Mode

; Not entirely known behavior
* 80 - unknown - affect hp bar display above unit on selection and on unit icon in group selection (further testing needed)
** -1 - '''invisible''' HP bar & '''invisible''' Icon HP bar in "unit list" when multiple units selected ''(probably considered invalid?)''
** 0 - '''visible''' HP bar & '''visible''' Icon HP bar in "unit list" when multiple units selected ''(probably default value?)''
** 1 - '''visible''' HP bar & '''visible''' Icon HP bar in "unit list" when multiple units selected
** 2 - '''invisible''' HP bar & '''invisible''' Icon HP bar in "unit list" when multiple units selected
** 3 - '''invisible''' HP bar & '''invisible''' Icon HP bar in "unit list" when multiple units selected
** ''above 3, behavior redo from 0 to 3 as if number were trunked between 0 and 3, may by related to civilisation?''
** ''below -1, behavior redo as -1, probably considering it beeing invalid?''
* 93 - unknown - seems to affect for/map releave interaction, hard to reproduce
** 6 - reveals larger area than norma Line of Sight value, on a circle radius based on the value, letting "black" tile inbetween that outer circle and the unit Line of Sight. The "black" tiles seems to then become unrevealable by the unit with that attribute modified, making them disapearing under the "black" tile and reapering on the revealed map tile once they passed that "black" area. Other units seems to be able to then reveals those "black" tile but not the one that initiated it. After unit death, the "circle" revealed stay revealed, but it seems to not work every time, maybe related to civilisation?
* 98 - unknown - seems to affect fog interaction, hard to reproduce
** 3 - on units: used to produce a strange behavior on fog, not able to reprocude it since

; Numbers unknown for Attributes mentioned in official patch notes
* Hide in (Scenario) Editor
** 0 - visible
** 1 - hidden
** 2 - visible in Others tab
* Formation Spacing [Flank bonus in Unit Stats; Flank Attack Modifier in search bar] - ''(controls the spacing between units when in formation, 1.0 for normal behavior)''

; Numbers unknown for Attributes not-mentioned in Patch notes, but present in AGE
* Selection Effect
** 0 - Has hit point bar
** 1 - Has hit point bar and outline
** 2 - No hit point bar or outline
** 3 - No hit point bar, but has outline
* Charge Target - types of units which enable the effect of Charged Ranged Attack ability
** -1 - All targets
** 0 - All targets except buildings (not same as flag 255 due to existence of miscellaneous unit types)
** 1 - Infantry
** 2 - Cavalry
** 4 - Foot archers
** 8 - Mounted archers
** 16 - Monks
** 32 - Villagers and Trade Carts
** 64 - Ships
** 128 - Siege weapons
** 256 - Buildings
* Garrison Firepower
* Charge Projectile Unit - projectile used for Charged Ranged Attack abilities
* Shown Reload Time
** For military units: Shown value of attack reload time
** For Monks and Boarding Galleys: Time spent on 1 chant during conversion

== Tasks ==
Note that most of them are obsolete, so description is provided only for the tasks which are useful. Tasks cannot be modified using the Scenario Editor.

* -32768 to -1 - invalid ability (does take these as valid inputs but these are not assigned)
* 0 - none
* 1 - Move to
* 2 - Follow
* 3 - Garrison - defines the ability to garrison in different structures, like transport boats, buildings and siege weapons. The garrison attribute of units and buildings defines which type of units can garrison in them, while the garrison task of units determines which types of units they can garrison in. For a unit to garrison in another unit or buildings, criteria should be fulfilled from both ends.
** Cavalry have garrison in buildings task, but Town Centers only allow monks, villagers, and foot soldiers to be garrisoned.
** [[Gurjaras|Gurjara]] Docks can garrison 10 Ships, but no Ship other than Fishing Ship has the task to garrison in the Dock.
** Even if Rams could allow mounted units to garrison inside them (via the Scenario Editor), mounted units themselves do not have the task to garrison inside siege units.
* 4 - Explore
* 5 - Gather/Rebuild - allows villagers to gather resource without damaging the source, used by Builders (only for Farms), Farmers, Foragers, Fishermen and Fisherwomen, Gold Miners, Stone Miners, and Fishing Ships
* 6 - Graze, deleted? - Property shared among animals [work value 1 = 20, work value 2 = 10 for all]
* 7 - Combat - allows buildings and units to attack
** Before the ''Definitive edition'', since ''The Age of Kings'', Houses, Markets, Stables, etc. had Combat Ability but no attack. If an enemy unit were attacking the said building, the player could command the building to attack the unit. Since the building did not have any attack stats, the attack would deal the minimum of 1 damage. This bug was first noticed with the Khmer houses in Rise of the Rajas, and people thought that this was a bug due the Khmer bonus.
** As a general rule, combat does not affect Trees, so Trebuchets, Onagers, Siege Onagers, and Ballista Elephants have a special combat task against Trees
* 8 - Shoot
* 9 - Attack
* 10 - Fly - used by Birds and Butterfliers to be able to fly
* 11 - Scare/Hunt, deleted? - property used by wolves and their variants [work value 1 = 1, work value 2 = 10] only for Deer (not variants)
* 12 - Unload (boat-Like) - property used by Transport Ship and the old [[Siege Tower (Age of Empires II)|Siege Tower]] to unload units
* 13 - Guard - purpose unknown
* 14 - Siege Tower Ability - gives Siege Towers the ability to unload units (only works against walls (in the Dataset))
* 20 - Escape, deleted?
* 21 - Make - property used by Farms and Fish Traps
* 101 - Build - allows units to build structures
** Fishing Ships could build any structure in Age of Kings. This was removed by hardcoding them to be only able to build Fish Traps.
** Serjeants too have this property but they can only make Donjons. Even if using Scenario Editor, Serjeants were given some other building as Trait Piece, they could build the building, and even then they could build Donjons if the foundation were placed.
* 102 - Make a unit
* 103 - Make a technology 
* 104 - Convert - allows Monks and Boarding Boats to convert enemy units
** Work Value 1 gives the minimum conversion threshold for units
** Work Value 2 gives the maximum conversion threshold for units
** Conversion of Buildings is governed by Resources 180 (similar to Work Value 1), 181 (similar to Work Value 2) and 182 (similar to accuracy for Monks - conversion chance in a chant)
** Conversion of Scouts is hardcoded
* 105 - Heal
** <math>Healing = WorkValue1 \times WorkRate</math>, where healing is the number of hit points healed per second (when healing continuously)
** Work Range does not determine anything since Healing Range is governed by Resource 90 for Monk-type units
** In case of pure healers like [[Chand Bardai]], healing range is increased in the UI by Block Printing, but does not change in practice
** Byzantine team bonus works by modifying Resource 89
* 106 - Repair - allows villagers to repair buildings and Serjeants to repair Donjons specifically
* 107 - Get auto-converted - allows herdables, [[Relic Cart (Age of Empires II)|Relic Carts]] and Monuments to get auto-converted
** Search Wait Time - String ID to display when capturing the herdable animal
* 108 - Discovery Artifact
* 109 - Unknown, nothing?
* 110 - Hunt - allows villagers to gather resources in which source needs to be attacks without killing the source, allows vanilla villagers to attack wolves, hunters to attack huntable animals, shepherds to attack herdables, lumberjacks to 'attack' trees, and in scenario editors, stone miners and gold miners to attack Stone (pile) and Gold (pile) respectively. Weirdly it also allows Throwing Axemen and Chakram Throwers to attack Falcons
** if "Unused Resource" is set to a value and the corresponding is set to 1
** Animals hunted by the Villager don't decay
** If a Villager with the Resource set to 0 starts gathering from the carcass, it starts decaying again
* 111 - Trade - tells Trade units which building to Trade with, so Market for Trade Carts and Donkeys, and Docks for Trade Cogs and Junk
* 120 - Generate Wonder Victory - allows wonders to start the countdown timer
* 121 - Deselect when Tasked (Farm) - probably prevents all builders and fishing ships to build all farms and fishing ships so that one of them starts working on the newly built one
* 122 - Loot (Gather)
* 123 - Housing
* 124 - Pack
* 125 - Unpack and Attack - task shared by packed Trebuchets, purpose unknown
* 130 - Unknown, nothing?
* 131 - Off-map Trade - Task shared by Trade Carts and Donkeys, but not Junks and Trade Cogs, purpose unknown
* 132 - Pickup Unit - allows Priests and Monks (but not hero Monks, since after picking up the Relic, they used to become normal Monks) to pick up Relics
** Work Value 1 - unit ID to transform into after picking up or depositing a relic
* 133 - Speed Charge (named Charge Attack in Editor) - requires "Special Ability" attribute to be 3 - increases speed of the Monoreme line
** Work Value 1: Minimum distance from the target for the speed up to start
** Work Value 2: Maximum distance from the target for the speed up to start
** Work Range: Multiplier on the unit speed while charging
** Work Flag 2: This must be set to 2001 for the task to work
* 134 - Transform Unit
* 135 - Kidnap Unit - allows [[Scythian Scout]] to kidnap villagers in their dying animation
* 136 - Deposit Unit - used for Monks with relics to tell about the drop site
** Work Value 1 - unit ID to transform into after picking up or depositing a relic
* 149 - Shear
* 150 - Regeneration - used for giving units regeneration ability before Attribute 109 was introduced which made tasks much simpler, was not used by Berserks, is still used by Babur, Musa-ibn-Nusayr and Arambai but with 0 effect
* 151 - Resource Generation - ability of a building to generate infinite resources
** Work Value 1: Amount of Resource received
** Resource Out: Resource type to receive
** Productivity Resource: if set, the value of this resource is used as multiplier of the amount received
** When target class/unit is set, requires to attack this unit to generate resources
** Units require Unused Flag 2 for passive generation
** When a class or unit is defined, the unit generates the said resources only when working on the unit or attacking the enemy unit
** When class or unit is not defined, the unit generates resources passively
* 152 - Movement damage
* 153 - Moveable Drop Site - used by [[Mule Cart]] to follow resource sources
* 154 - Pillage - generate resources upon killing enemy unit
* 155 - Influence ability (requires Combat Ability 32) (EX: xsTaskAmount(int taskFieldId, float value)
** (0, x) Sets "Work Value 1" the amount an attribute will be affected
** (1, x) Sets "Work Value 2" the units required for the maximum power up
** (2, x) Sets "Work Range" for the radius of the aura
** (3, x) Sets "Work Flag 2" the minimum number of units that have to be nearby to start the aura
** (4, x) Sets "Search Wait Time" Sets the attribute to modify
*** Only some attributes are supported: Movement Speed, Attack, Attack Reload Time, Work Rate, Regeneration Rate, Conversion Chance Modifier, 116 - Melee Armor, 117 - Pierce Armor)
** (5, x) Sets "Unused Flag" '''combination bit field''' Modifies the aura visuals and mathematical factors 
*** 1 - Multiply instead of Add
*** 2 - Circular instead of rectangular radius
*** 4 - Range indicator shown
*** 8 - Unused
*** 16 - Unused
*** 32 - Translucent
*** 128 - Hide powerup icon in UI
**(6, x) Sets "Target Diplomacy" Sets the diplomacy of the units to be affected. 
*** 0, 7+ - all objects
*** 1 - Own
*** 2 - Neutral and Enemy
*** 3 - Gaia
*** 4 - Gaia and team
*** 5 - Gaia, Neutral and Enemy
*** 6 - All but own
//VILL TC---------------------------------------------------------------------------------

void addVil() {

xsTaskAmount(0, 120); // AttributeID 109 (regeneration) will be added by 120 to the units specified by xsTask 

xsTaskAmount(1, 1); // One unit must be adjacent UnitID 109 (town center) to receive the buff as specified by xsTask

xsTaskAmount(2, 3); //This aura will span 3 tiles from the town center

xsTaskAmount(3, 0); // This aura will always provide 120 regeneration when active

xsTaskAmount(5, 38); // This aura will be translucent, have a range indicator, and be circular

xsTaskAmount(6, 4); // I want gaia, myself, and my allies to receive the buff

xsTaskAmount(4, 0.001 + 109); // a small decimal value (float) is added to the AttributeID when applying xsTask multiple times to the a unit

xsTask(109, 155, 906); // UnitID 109 (town center) will be given TaskID 155 (aura) that only effects (900+ClassID 6) 906 (class 6 AKA infantry)

xsTaskAmount(4, 0.002 + 109); // ensure the decimal value is descending when using this method 

xsTask(109, 155, 912); // 109 (town center) will be given task 155 (aura) that only effects 912 (class 12 AKA cavalry)

xsTaskAmount(4, 0.003 + 109); // you can change a single line of xsTaskAmount without changing the others to execute xsTask

xsTask(109, 155, 913); // 109 (town center) will be given task 155 (aura) that only effects 913 (class 13 AKA siege)

=== Task attributes ===
Unless specified otherwise, the following fields work as:
* Action Type - Task
* Class and Unit - If any non-negative number is input in class field, the effect applies to the given class, and not the unit. If both are set to -1, the effect may apply to everything.
* Productivity Resource - the task done is multiplied by this Resource number to calculate the output
* Resource Out - the output is delivered in the form of this resource
* Target diplomacy - the set of players this task works for
** 0, 7+ - all objects
** 1 - Own
** 2 - Neutral and Enemy
** 3 - Gaia
** 4 - Gaia and team
** 5 - Gaia, Neutral and Enemy
** 6 - All but own

== Trivia ==
* Resource 215 - Mercenary Kipchak Limit was used in the ''[[Age of Empires II: Definitive Edition]]'' beta to count the number of Mercenary Kipchaks left to be created. When this resource reached 10, it disabled the Elite Kipchaks from Cuman Mercenaries. Later, it was noticed that this is a drawback, since this disabled Elite Kipchaks even if the player could have created more, in case they had other Cuman allies to contribute too.

== See also ==
* [[SLX Studio]]
[[Category:Age of Empires]]
[[Category:Age of Empires II]]
[[Category:Modding]]
[[Category:Software]]
