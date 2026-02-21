---
source_url: https://ugc.aoe2.rocks/general/xs/bugs/Crashes/
fetched_at: 2026-02-08T19:30:28+00:00
---

Crashes - AoE2DE UGC Guide






[Skip to content](#1-crash-on-using-symbols-in-xschatdata)

AoE2DE UGC Guide

Crashes



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
    - [Chat Data](../Chat%20Data/)
    - Crashes

      [Crashes](./)



      Table of contents
      * [1. Crash On Using % Symbols In xsChatData()](#1-crash-on-using-symbols-in-xschatdata)
      * [2. Using goto With A Non Existent Label Crashes The Game](#2-using-goto-with-a-non-existent-label-crashes-the-game)
      * [3. Crash On Using An Integer Larger Than 999\_999\_999 In Chat Data](#3-crash-on-using-an-integer-larger-than-999_999_999-in-chat-data)
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

* [1. Crash On Using % Symbols In xsChatData()](#1-crash-on-using-symbols-in-xschatdata)
* [2. Using goto With A Non Existent Label Crashes The Game](#2-using-goto-with-a-non-existent-label-crashes-the-game)
* [3. Crash On Using An Integer Larger Than 999\_999\_999 In Chat Data](#3-crash-on-using-an-integer-larger-than-999_999_999-in-chat-data)

# Crashes

### 1. Crash On Using `%` Symbols In `xsChatData()`[¶](#1-crash-on-using-symbols-in-xschatdata "Permanent link")

Description: Cannot escape `%` symbols in the message, since they are considered special characters because of the `%d` and `%f` usage.

Expected Behaviour: It should be possible to escape the `%` character by using a backslash `\`.

Reproduction Steps:

1. Create a new scenario or RMS
2. Create a new XS script with the following code:

   |  |  |
   | --- | --- |
   | ``` 1 2 3 4 5 6 7 8 9 ``` | ``` void main() {     // This crashes the game altogether      // prints `this  will not appear in game`     xsChatData("this % will not appear in game");      // prints `neither will this \ appear in game`     xsChatData("neither will this \% appear in game"); } ``` |
3. Include the script in the scenario or RMS
4. When a game is played using the scenario or RMS, the game will crash

### 2. Using `goto` With A Non Existent Label Crashes The Game[¶](#2-using-goto-with-a-non-existent-label-crashes-the-game "Permanent link")

Description: If a goto statement is used as shown below, it crashes the game. How to define a working label in XS is currently unknown

Expected Behaviour: The game should warn about wrong usage of `goto` to a non existent label. How is a label defined in the first place in XS?

Reproduction Steps:

1. Create a new scenario or RMS
2. Create a new XS script with the following code:

   |  |  |
   | --- | --- |
   | ``` 1 2 3 ``` | ``` void main() {     goto non_existent_label; } ``` |
3. Include the script in the scenario or RMS
4. When a game is played using the scenario or RMS, A crash will occur

### 3. Crash On Using An Integer Larger Than `999_999_999` In Chat Data[¶](#3-crash-on-using-an-integer-larger-than-999_999_999-in-chat-data "Permanent link")

Description: Trying to chan an `int` that is bigger than `999_999_999` with `%d` in `xsChatData` causes a crash

Expected Behaviour: The int value should be printed properly as expected

Reproduction Steps:

1. Create a new scenario or RMS
2. Create a new XS script with the following code:

   |  |  |
   | --- | --- |
   | ``` 1 2 3 4 5 6 7 ``` | ``` void main() {     int a = 999999999+1;      xsChatData("t %d", a); // crashes the game         // xsChatData("t "+a); // this works normally } ``` |
3. Include the script in the scenario or RMS
4. When a game is played using the scenario or RMS, A crash will occur

Was this page helpful?

Thanks for your feedback!

Thanks for your feedback! Help us improve this page by using our [feedback form](...).

Back to top


Made with
[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
