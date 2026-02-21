# Modding

## General

Added or updated a very large number of attributes to support new gameplay functionalities, most notably alternative ranged attacks and hero active abilities such as special attacks or temporary auras.

## New Data Functionalities

Items in *Italics* are pre existing functionalities, with their updated elements noted in **bold**.

### New Resources

- `288`: Pasture Food Amount
- `289`: Pasture Animal Count
- `290`: Pasture Herder Count

### New/Updated Attributes

#### Reload Time

Controls Faith recharge rate of monk and boarding boat class units (previously by resources `35` and `83`).

#### Shown Reload Time

Controls conversion roll duration of all units with conversion ability (previously by reload time for monk class units)

#### Friendly Fire Multiplier

- Attribute `119`: Multiplier on the amount of friendly fire received through splash damage by the unit
- For Projectiles with Smart Mode 2, damage multiplier for pass through damage

#### Damage Reflection

- Attribute `118`: Damage percentage of the received damage to be reflected on the attacker (only for melee damage)

#### HP based regeneration

- Attribute `120`: Percentage of the unit's max HP that is regenerated over a minute

#### Attack Priority

- Attribute `128`: defines what type of target the unit will prioritize:
  - Units > Buildings
  - Buildings > Units
  - Buildings only

#### Invulnerability Level

- Attribute `129`: Sets an HP threshold after which a unit no longer receives damage when attacked
  - If `> 0`, used as multiplier of base HP
  - If `< 0`, sets a value of HP

#### Vanish Mode

- Attribute `68`: New Flag `2`: always spawns dead unit when projectile lands

#### Special Ability

- Attribute N/A: New mode `7`: Building is placed directly on top of the unit instead of giving placement option
- Must be combined with Trait `4`: Military units can build

#### Availability

- Attribute `126`: New: when Disabled flag `2` or `4` is set, sets value for number of trainable unit
- Will use units paired in `LinkedUnits.json` to count them together.
- Use Modify Attribute `126` rather than Enable Unit to enable a unit with limited training.

#### Disabled

- Attribute `127`: New: uses flags
  - `1` - Disabled
  - `2` - Limited training. Cannot be retrained after death
  - `4` - Limited training. Can be retrained after death

#### Terrain Defense Bonus

- Allowed modifying with add attribute effect type.

#### Combat Ability

- Attribute `63`:
  - `1` - Armor ignoring ability
  - `2` - Resist Armor ignoring ability - cancels enemy's armor ignoring effect if it has
  - `4` - Armor damaging ability - damages enemy melee and pierce armor by 1 independently with every attack, cannot reduce below 0
  - `8` - Attack ground ability
  - `16` - Bulk Volley Release - all projectiles of the unit are released together
  - `32` - Influence ability - allows unit/building to modify attributes of units in influence range - see Task `155`
  - `64` - Inverse influence - (requires flag `32`) makes other units boost self, instead of the unit boosting other units - If the unit has several power up tasks, all except the first task need to have Auto Search attribute set to `1` - see Task `155`
  - New: `128` - Activate Stingers, triggered when performing an attack - see Task `157`

#### Garrison Fire Power

- Attribute `130`: Adds to the damage of the unit to calculate the number of garrison arrows to fire
  - If `> 0`: Acts as multiplier
  - If `< 0`: Flat dps value added to the unit's dps

#### Obstruction Type

- Attribute `78`: Controls the type of obstruction a unit/building has. New flags:
  - `11`: consider the selection size of a radius entirely as opposed to the actual defined collision size.
  - `12`: ignore hard obstructions entirely and just consider the space occupied with no obstruction at all.
  - `13`: consider the selection radius when placing other objects, but use the original obstruction size for hard obstructions.

#### Shared Selection

- Attribute N/A (Run Pattern in AGE): Control the double click selection behavior:
  - `0`: current behavior: selects units with the same class and name ID
  - `1+`: select together with units that have the same run pattern. Disables current behavior of selected units with same class and name ID
  - `255`: disables current behavior of selected units with same name. Only units with same ID are selected.

#### Charge Event

- Allowed modifying with add attribute effect type.

#### Charge Target

- Attribute N/A: List of Flags of valid targets for the charge attack:
  - `-1`: All targets
  - `0`: All targets except Buildings
  - Flags:
    - `1`: Infantry
    - `2`: Cavalry
    - `4`: Archers
    - `8`: Cavalry Archers
    - `16`: Monks
    - `32`: Villagers/Trade Carts
    - `64`: Ships
    - `128`: Siege
    - `256`: Buildings

#### Charge Projectile

- Attribute N/A: Projectile units for Charge Types `6` and `7`

#### Ability Button Icon ID

- Attribute `121`: Override for Transform/Active Ability Icon. Uses ID from `Materials.json`

#### Ability Short Tooltip

- Attribute `122`: Override for Transform/Active Ability Short Tooltip

#### Ability Long Tooltip

- Attribute `123`: Override for Transform/Active Ability Long Tooltip

#### Ability Hotkey Action

- Attribute `124`: button_action_list when pressing button/hotkey for the ability or transformation

#### Attack Graphic 2

- Attribute `131`: Second attack graphic of the unit; alternates with the first attack graphic when assigned

#### Conversion Range

- Now also controls the reveal radius of Monuments in King of the Hill games.

#### Undead Graphic

- Now can be used for assigning the decay graphic to units which don't have Undead Mode attribute set to `1`; for them undead graphic overwrites the standing graphic of the object's dead unit.

### New Charge Types

#### Ignore Melee Attack

- Charge Type `5`: Ignores melee attacks, consumes one charge per attack

#### Projectile Attacks

- Charge Type `6`: Fires only Charge projectiles, sets Total Projectiles to the value of Max Total Projectiles
- Charge Type `7`: Fires `1` Charge projectile and additional Secondary Projectiles, sets Total Projectiles to the value of Max Total Projectiles
- Charge Event: Max range modifier for this charge attack

#### Active Temporary Transformation

- Charge Type `-1`: Temporarily transforms into another unit
- Charge Event: Duration of the transformation
  - If `0`, transforms until performs one attack
  - If `-1`, performs an attack ground on its location
- Transforms into the unit set in Trait Piece

#### Active Targeted Transformation

- Charge Type `-2`: Transforms into another unit when tasked to a valid target after pressing the ability button
- Charge Event: Duration of the transformation
  - If set to `0`, transforms until it performs one attack
  - If Charge Target is set to `-1`, uses attack ground targeting
- Transforms into the unit set in Trait Piece

#### Active Aura Ability

- Charge Type `-3`: Activates a power up aura when pressing the button
- Charge Event: Duration of the ability
- Requires Task `155` Aura with Unused Flag `8`

#### Conversion Ability

- Charge Type `-4`: Conversion for non Monk type units
- Charge Event: Conversion range
- May be overwritten by the conversion tasks
- Charge Target: Conversion percent chance
- Requires Task `104`: Convert

#### Spawn Unit

- Charge Type `-5`: Spawn building set in Trait Piece on top of the unit
- Displays the spawn object's icon and train tooltip by default; these can be overwritten by the ability button attributes

### New Unit Class

#### Land Mine

- Class `64`: Self detonate unit, deals damage on death (like petard class). Does not trigger AI retaliation.

### New/Updated Tasks

#### Task 107: Get Auto-converted

- Search Wait Time: String ID to display when capturing the herdable animal

#### Task 111: Hunt

- New: if "Unused Resource" is set to a value and the corresponding is set to `1`
- Animals hunted by the Villager don't decay
- If a Villager with the Resource set to `0` starts gathering from the carcass, it starts decaying again

#### Task 132: Pickup Unit and Task 136: Deposit Unit

- Work Value 1: unit ID to transform into after picking up or depositing a relic

#### Task 151: Resource Generation

- Work Value 1: Amount of Resource received
- Resource Out: Resource type to receive
- Productivity Resource: if set, the value of this resource is used as multiplier of the amount received
- When target class/unit is set, requires to attack this unit to generate resources
- If no target is set, generates resources passively
- New: Units require Unused Flag `2` for passive generation

#### Task 154: Loot

- Triggered when Killing/Converting a target
- unit ID and class ID control which object it can be. If neither are set, then it is any object. Has to be an object that can increase the kill/razing/conversions stats
- Work Value 1: Amount of Resource received
- Resource Out: Resource type to receive
- Productivity Resource: if set, task only activate the task if:
  - If positive value: requires the value of the associated resource to be != `0`
  - the value of this resource is used as multiplier of the amount received
  - If negative value: requires the tech of the associated ID to have been researched
- Resource in: if set, the tech effect with that ID will fire
- Unused 4th resource: if set, the tech effect with ID of this resource's value will fire
- Work range: if `0`, all above effects apply to the player who owns the attacking object. If `!= 0`, then to the target object's player
- New: Proceeding Graphic: Graphic to be played over the unit when triggered
- New: Resource Gathering Sound: Sound to be played when triggered
- New: Work Flag: if set, maximum number of time this unit can trigger the task
- New: Carry Check: if set, all Tasks `154` with the same Carry Check ID will count towards the same cap
- New: If Unused Flag is set to `1`, unit veterancy effect:
  - Search Wait Time: Attribute ID to improve
  - Gather Type: Value of the improvement

#### Task 155: Aura

- Requires Combat Ability `32`
- Search Wait Time - attribute number which is modified
- Work value 1 - attribute increase at the maximum power up.
- Work value 2 - units required for the maximum power up.
- Work range - range of the effect.
- Target diplomacy - players whose objects will be affected.
- New: Proceeding Graphic: Graphic displayed over the units receiving the aura
- New: Resource Gathering Sound: Short Tooltip for UI indicator
- New: Resource Deposit Sound: Long Tooltip for UI indicator
- New: Gather Type: UI indicator Icon displayed (per `icons.json`)
- Unused flag - flags to enable additional settings, can be combined with each other
  - `1`: use the amount in work value 1 as multiplier
  - `2`: round area of power up (square otherwise)
  - `4`: display the range indicator
  - New `8`: Temporary Aura, see Charge Type `-3`
  - New `16`: Used combined with `8`, applies buff only units around when the ability is triggered
  - New `32`: Advanced range indicator

#### Task 156: Additional Spawn

- Spawns additional units when the unit is trained
- Work Value 1: ID of the additional unit to spawn
- Work Value 2: number of units to spawn
- Productive Resource: if set in the task, the value of the corresponding resource is added to the number of units to spawn

#### Task 157: Stingers

- Requires Combat Ability `128`
- if Productivity Resource is set, the value of the corresponding resource needs to be `>0` for the Task to trigger
- Search Wait Time indicates which attribute to modify
- Includes: `5` (Movement Speed), `109` (Regeneration Rate), `10` (reload time), `120` (HP based regeneration)
- Work Value 1: value add
- Work Value 2: how long the effect will last (in seconds). If negative, apply permanently.
- Work Range:
  - If `0`, apply the modifier to the unit performing the attack.
  - If `1`, apply to the unit who receives the attack (including units which received splash damage)
- Unused flag: additional flags:
  - `1`: use Work Value 1 as multiplier
  - `2`: don't allow other tasks `156` that modify the same attribute to stack

#### Task 158: HP Transformation

- Transform into another unit based on current HP conditions
- If Productivity Resource is set, task only activates if:
  - If positive value: requires the value of the associated resource to be != `0`
  - If negative value: requires the tech of the associated ID to have been researched
- Work Value 1: ID of the unit to transform into
- Work Value 2: HP required to trigger to task.
  - If the value is positive, the task will trigger when the unit's current HP is higher than this value
  - If the value is negative, the task will trigger when the unit's current HP is lower than this value
- If Resource Out is set, add it to work value 2
- Unused Flag: if set to `1`, use work value 2 as a multiplier of max HP.

### Technology Attributes

#### Full Tech Mode

- `0` - Available in full tech tree (for civilization specific techs)
- `1` - Disabled in FTT
- Available only in the following game mode. Negative value for disable in that game mode (except `32`)
- `2` - Random map
- `3` - Deathmatch
- `4` - Empire Wars or Empire Wars Mode
- `5` - Wonder Race
- `6` - Defend the Wonder
- `7` - Sudden Death or Sudden Death Mode
- `8` - King of the Hill
- `9` - Capture the Relic
- `10` - Battle Royale
- `11` - Regicide
- `12` - Turbo Mode
- `13` - Scenario or Campaign game
- `14` - Regicide Mode
- `15` - Scenario Editor
- `16` - D3
- `17` - Solid Farms
- `18` - Shared Exploration
- `19` - Default Starting Resources
- `20` - Low Starting Resources
- `21` - Medium Starting Resources
- `22` - High Starting Resources
- `23` - Ultra-High Starting Resources
- `24` - Infinite Starting Resources
- `25` - Random Starting Resources
- `26` - Antiquity mode
- New: `27` - Dark Age Start
- New: `28` - Feudal Age Start
- New: `29` - Castle Age Start
- New: `30` - Imperial Age Start
- New: `31` - Post-Imperial Age Start
- New: `32` - Feudal Age Start or later
- New: `33` - Castle Age Start or later
- New: `34` - Imperial Age Start or later

### Technology Effects

- Tech Cost Modifier and Tech Time Modifier with Mode `2` will multiply technology costs or time by the specified amount.
- Resource to `-1` in Tech Cost Modifier effect will target all costs of the technology.
- Technology cost and time adjustment values now stack with the previously applied adjustments instead of overwriting them.
- Added new Modify Technology actions:
  - `-3` - Multiply Tech Time
  - `13` - Multiply Food Cost
  - `14` - Multiply Wood Cost
  - `15` - Multiply Stone Cost
  - `16` - Multiply Gold Cost
  - `17` - Multiply All Costs

### Scenario Editor

- Added new elevation height options up to `16` (from `7`).
- Fixed a crash when using Modify Attribute trigger effect with Graphics ID attributes originally set to `-1`.
- Added Item ID field to Research Technology trigger effect.
- Script Filename field now accepts file names with up to `100` characters.

### XS Scripting

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
