---
source_url: https://ugc.aoe2.rocks/general/xs/bugs/Chat%20Data/
fetched_at: 2026-02-08T19:30:27+00:00
---

Chat Data - AoE2DE UGC Guide






[Skip to content](#1-cannot-print-0-or-1-at-the-start-of-the-line-in-xschatdata)

AoE2DE UGC Guide

Chat Data



Initializing search

[AoE2DE\_UGC\_Guide](https://github.com/Divy1211/AoE2DE_UGC_Guide "Go to repository")

* [AoE2DE UGC Guide](../../../..)
* [Game Mechanics](../../../)
* [Custom Scenarios](../../../../scenarios/)
* [XS Scripting](../../)
* [Mods](../../../../mods/)
* [RMS](../../../../rms/)
* [AI](../../../../ai/)
* [Audio](../../../../audio/)



AoE2DE UGC Guide

[AoE2DE\_UGC\_Guide](https://github.com/Divy1211/AoE2DE_UGC_Guide "Go to repository")

* [AoE2DE UGC Guide](../../../..)
* [Game Mechanics](../../../)

  Game Mechanics
  + [Damage Calculation](../../../damage_calculation/)
  + [Attributes](../../../attributes/attributes/)
  + [Resources](../../../resources/resources/)
  + [Hotkeys](../../../hotkeys/hotkeys/)
* [Custom Scenarios](../../../../scenarios/)

  Custom Scenarios
  + [Triggers](../../../../scenarios/triggers/)

    Triggers
    - [Effects](../../../../scenarios/triggers/effects/effects/)
  + Useful Tools




    Useful Tools
    - [AoE2ScenarioParser](../../../../scenarios/useful_tools/parser/)

      AoE2ScenarioParser
* [XS Scripting](../../)

  XS Scripting
  + [For Beginners](../../beginner/)
  + [For Programmers](../../programmer/)
  + [Tricks](../../tricks/)
  + [Functions Reference](../../functions/)
  + [Constant Reference](../../constants/)
  + [Useful Resources](../../useful/)
  + [Known Bugs](../)

    Known Bugs
    - Chat Data

      [Chat Data](./)



      Table of contents
      * [1. Cannot Print 0 Or 1 At The Start Of The Line In xsChatData()](#1-cannot-print-0-or-1-at-the-start-of-the-line-in-xschatdata)
    - [Crashes](../Crashes/)
    - [Editor](../Editor/)
    - [Effect Amount](../Effect%20Amount/)
    - [Important](../Important/)
    - [Language Syntax](../Language%20Syntax/)
    - [Task](../Task/)
    - [Task](../Individual%20Tech%20Modifiers/)
* [Mods](../../../../mods/)

  Mods
* [RMS](../../../../rms/)

  RMS
* [AI](../../../../ai/)

  AI
* [Audio](../../../../audio/)

  Audio

Table of contents

* [1. Cannot Print 0 Or 1 At The Start Of The Line In xsChatData()](#1-cannot-print-0-or-1-at-the-start-of-the-line-in-xschatdata)

# Chat Data

### 1. Cannot Print `0` Or `1` At The Start Of The Line In `xsChatData()`[¶](#1-cannot-print-0-or-1-at-the-start-of-the-line-in-xschatdata "Permanent link")

Description: If a `0` or `1` character occurs at the beginning of a string that is being chatted to the screen using `xsChatData`, then the `0` or `1` characters do not appear in the message.

Expected Behaviour: `0` or `1` should be shown correctly at the beginning of the line if used in an `xsChatData` function

Reproduction Steps:

1. Create a new scenario or RMS
2. Create a new XS script with the following code:

   |  |  |
   | --- | --- |
   | ``` 1 2 3 4 5 6 7 8 9 ``` | ``` void main() {     // expected `1 the one at the start isn't visible` but     // prints ` the one at the start isn't visible`     xsChatData("1 the one at the start isn't visible");      // expected `0 the zero at the start isn't visible` but     // prints ` the zero at the start isn't visible`     xsChatData("0 the zero at the start isn't visible"); } ``` |
3. Include the script in the scenario or RMS
4. When a game is played using the scenario or RMS, any `1` or `0` at the beginning of the lines are omitted in the resulting message on screen.

Was this page helpful?

Thanks for your feedback!

Thanks for your feedback! Help us improve this page by using our [feedback form](...).

Back to top


Made with
[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
