# AoE2DE Update 185872: AI scripting changes

Official release: 2026-09-22. This note records behavior and scheduling changes relevant to authors of .per AI scripts. It does not add or redefine AI commands.

## Rule processing and scheduling

- In the late game, the Definitive Edition AI now processes about 33% fewer rules per turn on average.
- Except at game start, AI player turns are processed one at a time and spaced out instead of being processed together.
- The number of AI turns is now more proportional to frame rate and may decrease when frame rate is very low.
- AI turn counts are now defined in terms of game speed, making testing and play at faster speeds more consistent with slower speeds.

When checking timing-sensitive rules, test at the intended game speed. Low frame rates can also reduce AI turn frequency.

## Script-visible fixes and behavior changes

- The gather-percentage system is less likely to send AI villagers to distant trees.
- **up-delete-distant-farms** no longer deletes another player's farm after the AI recently converted it.
- **up-set-target-by-id**, when used as a fact, no longer proceeds with an invalid unit ID.
- Escrow no longer prevents unit training in cases where an unresearched technology changes the resource types required for that unit.
- If an AI villager cannot path to a building foundation, the building is cancelled instead of remaining in the build queue indefinitely.
- **up-update-targets** has a lower performance impact.
- **object-data-next-attack** now reports the correct value while a unit is in its attack animation.
- Settlements are repaired when the AI has the **sn-object-repair-level** dropsite-repair flag.
- **up-reset-scouts** now resets only scouts that are actively exploring, not every scout that is merely in an explore group.
- A CD AI script error that occurred in Deathmatch has been fixed.

## Source

- [Age of Empires II: Definitive Edition – Update 185872](https://www.ageofempires.com/news/age-of-empires-ii-definitive-edition-update-185872/) — AI > General and AI > Scripting.