---
source_url: https://ugc.aoe2.rocks/general/xs/bugs/Important/
fetched_at: 2026-02-08T19:30:29+00:00
---

Important - AoE2DE UGC Guide






[Skip to content](#1-researching-a-technology-twice-in-xs-causes-a-crash)

AoE2DE UGC Guide

Important



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
    - [Editor](../Editor/)
    - [Effect Amount](../Effect%20Amount/)
    - Important

      [Important](./)



      Table of contents
      * [1. Researching a technology twice in XS causes a crash](#1-researching-a-technology-twice-in-xs-causes-a-crash)
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

* [1. Researching a technology twice in XS causes a crash](#1-researching-a-technology-twice-in-xs-causes-a-crash)

# Important

### 1. Researching a technology twice in XS causes a crash[¶](#1-researching-a-technology-twice-in-xs-causes-a-crash "Permanent link")

Description: Calling `xsResearchTechnology` twice for the same tech on the same player crashes the game

Expected Behaviour: These functions should work in an RMS as they do in scenarios

Reproduction Steps:

1. Create a new RMS/Scenario with the following code XS script included:

   |  |  |
   | --- | --- |
   | ``` 1 2 3 4 ``` | ``` void main() {     xsResearchTechnology(22, true, false, 1);     xsResearchTechnology(22, true, false, 1); } ``` |
2. When a game is played a crash occurs

Was this page helpful?

Thanks for your feedback!

Thanks for your feedback! Help us improve this page by using our [feedback form](...).

Back to top


Made with
[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
