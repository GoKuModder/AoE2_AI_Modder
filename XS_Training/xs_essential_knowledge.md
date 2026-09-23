# XS Essential Knowledge

This page records core XS practices that affect how agents write scripts and scenario trigger code. The Script Call condition behavior has additional details that will be added when documented.

## Script Call: execution and function definitions

Keep these two uses of Script Call separate:

1. **Execute XS code from a trigger.** A Script Call condition or effect is essentially executable XS code. It does not require the trigger to be exclusively enabled or dedicated to that Script Call.
2. **Define reusable XS functions.** Prefer Script Call effects for function definitions because Script Call conditions have additional behavior documented separately.

The trigger containing function definitions must appear before triggers that use those functions. Place the definitions in the first trigger when possible.

The usual pattern is to define reusable functions in one or more Script Call effects on a turned-off trigger. Later Script Call conditions or effects can call those functions as needed.

For example, a Script Call effect on the first, turned-off trigger can contain:

```xs
void showNumber(int value) {
    xsChatData("" + value);
}
```

A later Script Call can call it:

```xs
showNumber(7);
```

Define functions at the top level, outside other functions, and give them unique names.

## When to use `extern` for XS variables

The declaration rule depends on where the variable is defined:

- **Variable defined in an `.xs` file:** use `extern` if another file or a trigger needs to access it.
- **Variable defined in a Script Call on a turned-off trigger:** do not use `extern`.
- Whether a non-`extern` variable defined in that Script Call can be accessed from an `.xs` file is untested. Do not assume either behavior.

## Script Call condition details

Script Call conditions have additional behavior. Keep condition-specific guidance separate from the general function-definition pattern until those details are documented.

## Script Call Conditions and Loading-Screen Lag

XS code placed inside a **Script Call condition** can significantly increase scenario loading time.

Keep Script Call condition code as short as possible. Define reusable functions elsewhere, then call those functions from the condition instead of repeating large blocks of XS code.

In practice, Script Call conditions longer than roughly **5 lines** can start noticeably increasing loading time when repeated across many triggers. For example, a condition containing around **6–7 lines** of XS code and used in approximately **400 triggers** can add roughly **1 minute** to the loading screen. A scenario that normally loads in 7 seconds could therefore take around **1 minute and 7 seconds**. A previous scenario reached loading times of around **2 minutes and 30 seconds** because of this.

This is especially risky in multiplayer scenarios: players may assume the game or scenario has frozen. AoE2 has no back button during the loading screen, so players must keep waiting or force-close the game. If players hard-crash the game to leave, this can cause additional loading delays for the remaining players. On an 8-player map, the delays can become a major problem.

**Keep the condition itself as short as possible and move repeated or complex logic into reusable functions.**

## Unit ID Terminology: DAT, Scenario, and XS

The terms used for unit identifiers differ between the DAT/scenario side and XS.

In the Genie Editor, DAT file, Scenario Editor, scenario file, and AoE2ScenarioParser, **Unit ID** means the ID of a unit definition in the DAT file. For example, if 20 Archer units are placed on the map, all 20 share the same DAT unit ID:

```text
Archer → Unit ID 4
```

Each placed unit is an individual scenario object and receives its own unique **Reference ID**. Depending on context, this may also be called a **Reference ID**, **Object ID**, or **Object**. Here, an object means one individual object placed in the scenario: multiple objects can share a DAT unit ID while having different Reference IDs.

XS uses different names for these identifiers:

| Meaning | DAT or Scenario terminology | XS terminology |
| --- | --- | --- |
| Unit definition from the DAT file | Unit ID | `ObjectId` |
| Unique individual unit on the map | Reference ID | `UnitId` |

The distinction appears in official XS function signatures:

```xs
xsGetObjectAttribute(int playerId, int objectId, int attribute, int damageClass)
```

```xs
xsGetUnitAttribute(int unitId, int attribute, int damageClass)
```

The parameter is named `damageClass` in the current function reference. For train-location attributes, Update 185872 also lets this parameter select a Train Location Entry Mod.

`xsGetObjectAttribute` accesses the DAT unit definition, so it also takes a `playerId`: the same DAT unit can have different attributes for different players. For example, Player 1's Archer may have 4 attack while Player 2's Archer has 5 attack.

`xsGetUnitAttribute` accesses a specific individual unit on the map. It does not need a player parameter because its `unitId` uniquely identifies that unit, including its owner.

**Key mapping:** DAT/scenario `Unit ID` = XS `ObjectId`; scenario `Reference ID` = XS `UnitId`.
