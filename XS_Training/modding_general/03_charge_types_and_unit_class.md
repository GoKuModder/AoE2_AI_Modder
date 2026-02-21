# Modding - New Charge Types and Unit Class

## New Charge Types

### Ignore Melee Attack

- Charge Type `5`: Ignores melee attacks, consumes one charge per attack

### Projectile Attacks

- Charge Type `6`: Fires only Charge projectiles, sets Total Projectiles to the value of Max Total Projectiles
- Charge Type `7`: Fires `1` Charge projectile and additional Secondary Projectiles, sets Total Projectiles to the value of Max Total Projectiles
- Charge Event: Max range modifier for this charge attack

### Active Temporary Transformation

- Charge Type `-1`: Temporarily transforms into another unit
- Charge Event: Duration of the transformation
  - If `0`, transforms until performs one attack
  - If `-1`, performs an attack ground on its location
- Transforms into the unit set in Trait Piece

### Active Targeted Transformation

- Charge Type `-2`: Transforms into another unit when tasked to a valid target after pressing the ability button
- Charge Event: Duration of the transformation
  - If set to `0`, transforms until it performs one attack
  - If Charge Target is set to `-1`, uses attack ground targeting
- Transforms into the unit set in Trait Piece

### Active Aura Ability

- Charge Type `-3`: Activates a power up aura when pressing the button
- Charge Event: Duration of the ability
- Requires Task `155` Aura with Unused Flag `8`

### Conversion Ability

- Charge Type `-4`: Conversion for non Monk type units
- Charge Event: Conversion range
- May be overwritten by the conversion tasks
- Charge Target: Conversion percent chance
- Requires Task `104`: Convert

### Spawn Unit

- Charge Type `-5`: Spawn building set in Trait Piece on top of the unit
- Displays the spawn object's icon and train tooltip by default; these can be overwritten by the ability button attributes

## New Unit Class

### Land Mine

- Class `64`: Self detonate unit, deals damage on death (like petard class). Does not trigger AI retaliation.
