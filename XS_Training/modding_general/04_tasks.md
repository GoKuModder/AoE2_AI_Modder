# Modding - New/Updated Tasks

## Task 107: Get Auto-converted

- Search Wait Time: String ID to display when capturing the herdable animal

## Task 111: Hunt

- New: if "Unused Resource" is set to a value and the corresponding is set to `1`
- Animals hunted by the Villager don't decay
- If a Villager with the Resource set to `0` starts gathering from the carcass, it starts decaying again

## Task 132: Pickup Unit and Task 136: Deposit Unit

- Work Value 1: unit ID to transform into after picking up or depositing a relic

## Task 151: Resource Generation

- Work Value 1: Amount of Resource received
- Resource Out: Resource type to receive
- Productivity Resource: if set, the value of this resource is used as multiplier of the amount received
- When target class/unit is set, requires to attack this unit to generate resources
- If no target is set, generates resources passively
- New: Units require Unused Flag `2` for passive generation

## Task 154: Loot

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

## Task 155: Aura

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

## Task 156: Additional Spawn

- Spawns additional units when the unit is trained
- Work Value 1: ID of the additional unit to spawn
- Work Value 2: number of units to spawn
- Productive Resource: if set in the task, the value of the corresponding resource is added to the number of units to spawn

## Task 157: Stingers

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

## Task 158: HP Transformation

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
