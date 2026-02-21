---
source_url: https://ugc.aoe2.rocks/general/xs/bugs/Editor/
fetched_at: 2026-02-08T19:30:28+00:00
---

Editor - AoE2DE UGC Guide






[Skip to content](#1-script-call-a-function-with-parameters)

AoE2DE UGC Guide

Editor



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
    - [Crashes](../Crashes/)
    - Editor

      [Editor](./)



      Table of contents
      * [1. Script Call A Function With Parameters](#1-script-call-a-function-with-parameters)
      * [2. Script Call A Function With Comments](#2-script-call-a-function-with-comments)
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

* [1. Script Call A Function With Parameters](#1-script-call-a-function-with-parameters)
* [2. Script Call A Function With Comments](#2-script-call-a-function-with-comments)

# Editor

### 1. Script Call A Function With Parameters[¶](#1-script-call-a-function-with-parameters "Permanent link")

Description: When a function that takes arguments is defined in an XS file is called using script call, all XS execution stops. No syntax errors are shown, this happens completely silently

Expected Behaviour: Function call works as expected, without crashing the entirety of XS execution

Reproduction Steps:

1. Create a new scenario or RMS
2. Create a new XS script with the following code:

   |  |  |
   | --- | --- |
   | ``` 1 2 3 4 ``` | ``` void test(int a = 0, int b = 0) {     xsChatData("this is var a: %d", a);     xsChatData("this is var b: %d", b); } ``` |
3. Include the script in the scenario, and create a trigger with a script call condition/effect
4. Type `test(1, 2)`; in the message box for the script call
5. When the scenario is played, no text is chatted to the screen, execution fails silently

### 2. Script Call A Function With Comments[¶](#2-script-call-a-function-with-comments "Permanent link")

Description: When a function that contains comments is defined in a script call box, a parsing error is encountered

Expected Behaviour: Function call with comments should correctly ignore comments and parse

Reproduction Steps:

1. Create a new scenario
2. Create a new trigger with a script call effect
3. Place the following code inside the script call box:

   |  |  |
   | --- | --- |
   | ``` 1 2 3 4 ``` | ``` void main() {     // hello, world     xsChatData("hello, world"); } ``` |
4. When the effect is double clicked/the scenario is played, a parse error is shown

Was this page helpful?

Thanks for your feedback!

Thanks for your feedback! Help us improve this page by using our [feedback form](...).

Back to top


Made with
[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
