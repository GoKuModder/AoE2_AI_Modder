# Modding - New/Updated Attributes

## Reload Time

Controls Faith recharge rate of monk and boarding boat class units (previously by resources `35` and `83`).

## Shown Reload Time

Controls conversion roll duration of all units with conversion ability (previously by reload time for monk class units)

## Friendly Fire Multiplier

- Attribute `119`: Multiplier on the amount of friendly fire received through splash damage by the unit
- For Projectiles with Smart Mode 2, damage multiplier for pass through damage

## Damage Reflection

- Attribute `118`: Damage percentage of the received damage to be reflected on the attacker (only for melee damage)

## HP based regeneration

- Attribute `120`: Percentage of the unit's max HP that is regenerated over a minute

## Attack Priority

- Attribute `128`: defines what type of target the unit will prioritize:
  - Units > Buildings
  - Buildings > Units
  - Buildings only

## Invulnerability Level

- Attribute `129`: Sets an HP threshold after which a unit no longer receives damage when attacked
  - If `> 0`, used as multiplier of base HP
  - If `< 0`, sets a value of HP

## Vanish Mode

- Attribute `68`: New Flag `2`: always spawns dead unit when projectile lands

## Special Ability

- Attribute N/A: New mode `7`: Building is placed directly on top of the unit instead of giving placement option
- Must be combined with Trait `4`: Military units can build

## Availability

- Attribute `126`: New: when Disabled flag `2` or `4` is set, sets value for number of trainable unit
- Will use units paired in `LinkedUnits.json` to count them together.
- Use Modify Attribute `126` rather than Enable Unit to enable a unit with limited training.

## Disabled

- Attribute `127`: New: uses flags
  - `1` - Disabled
  - `2` - Limited training. Cannot be retrained after death
  - `4` - Limited training. Can be retrained after death

## Terrain Defense Bonus

- Allowed modifying with add attribute effect type.

## Combat Ability

- Attribute `63`:
  - `1` - Armor ignoring ability
  - `2` - Resist Armor ignoring ability - cancels enemy's armor ignoring effect if it has
  - `4` - Armor damaging ability - damages enemy melee and pierce armor by 1 independently with every attack, cannot reduce below 0
  - `8` - Attack ground ability
  - `16` - Bulk Volley Release - all projectiles of the unit are released together
  - `32` - Influence ability - allows unit/building to modify attributes of units in influence range - see Task `155`
  - `64` - Inverse influence - (requires flag `32`) makes other units boost self, instead of the unit boosting other units - If the unit has several power up tasks, all except the first task need to have Auto Search attribute set to `1` - see Task `155`
  - New: `128` - Activate Stingers, triggered when performing an attack - see Task `157`

## Garrison Fire Power

- Attribute `130`: Adds to the damage of the unit to calculate the number of garrison arrows to fire
  - If `> 0`: Acts as multiplier
  - If `< 0`: Flat dps value added to the unit's dps

## Obstruction Type

- Attribute `78`: Controls the type of obstruction a unit/building has. New flags:
  - `11`: consider the selection size of a radius entirely as opposed to the actual defined collision size.
  - `12`: ignore hard obstructions entirely and just consider the space occupied with no obstruction at all.
  - `13`: consider the selection radius when placing other objects, but use the original obstruction size for hard obstructions.

## Shared Selection

- Attribute N/A (Run Pattern in AGE): Control the double click selection behavior:
  - `0`: current behavior: selects units with the same class and name ID
  - `1+`: select together with units that have the same run pattern. Disables current behavior of selected units with same class and name ID
  - `255`: disables current behavior of selected units with same name. Only units with same ID are selected.

## Charge Event

- Allowed modifying with add attribute effect type.

## Charge Target

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

## Charge Projectile

- Attribute N/A: Projectile units for Charge Types `6` and `7`

## Ability Button Icon ID

- Attribute `121`: Override for Transform/Active Ability Icon. Uses ID from `Materials.json`

## Ability Short Tooltip

- Attribute `122`: Override for Transform/Active Ability Short Tooltip

## Ability Long Tooltip

- Attribute `123`: Override for Transform/Active Ability Long Tooltip

## Ability Hotkey Action

- Attribute `124`: button_action_list when pressing button/hotkey for the ability or transformation

## Attack Graphic 2

- Attribute `131`: Second attack graphic of the unit; alternates with the first attack graphic when assigned

## Conversion Range

- Now also controls the reveal radius of Monuments in King of the Hill games.

## Undead Graphic

- Now can be used for assigning the decay graphic to units which don't have Undead Mode attribute set to `1`; for them undead graphic overwrites the standing graphic of the object's dead unit.
