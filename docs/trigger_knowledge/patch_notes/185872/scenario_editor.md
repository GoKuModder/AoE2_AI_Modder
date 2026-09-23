# Scenario Editor Update: Build 185872

This curated overlay records verified Scenario Editor changes from [the official Update 185872 notes](https://www.ageofempires.com/news/age-of-empires-ii-definitive-edition-update-185872/). It supplements parser method catalogs: editor controls are not treated as new AoE2ScenarioParser method parameters unless the release notes establish that API change.

## Units tab

- **Capture Flag** is a new dropdown controlling whether units are allowed to be auto-converted. The notes say “Never (Gaia Aggressive)” may be used to let Gaia units act aggressively. Some units may still convert under “Never” or “Never (Gaia Aggressive)” when they have the Auto-Convert task; sheep and monuments are the examples given. The notes do not list every dropdown value.
- **Unit State** is a new dropdown for changing a unit’s state. The notes do not enumerate its values.

## Conditions

- **Object is Visible (MP)** has a new **Allow in Fog** checkbox. The notes do not state its default or describe additional semantics. The parser catalog stores this as an editor note rather than inventing a Python parameter.

## Effects

- **Object Modified State** replaces **Master Filter** on certain Modify Object Attribute effects. **All** remains the default. **Shared Master** is renamed **Previously Unmodified**, restricting the effect to map units not previously modified by a Modify Object Attribute effect. **Own Master** is renamed **Previously Modified**, restricting it to map units previously modified by one of those effects.
- **Stop Object**, **Freeze Object**, and **Task Object** with the **Stop** action now correctly clear building production queues.
- Task Object’s **Unload** action is renamed **Unload All** and works like the regular Unload effect.
- Task Object’s **Ungarrison** action is renamed **Ungarrison Specific** with unchanged behavior: it instructs the selected object to leave the unit it is currently garrisoned inside.

The corresponding structured record is [scenario_editor.json](scenario_editor.json). The condition/effect parser catalogs receive only the relevant editor notes; their parser signatures remain unchanged.
