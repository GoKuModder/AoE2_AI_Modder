---
source_url: https://ugc.aoe2.rocks/general/xs/bugs/Individual%20Tech%20Modifiers/
fetched_at: 2026-02-08T19:30:31+00:00
---

Task - AoE2DE UGC Guide






[Skip to content](#1-csettechcost-caddtechcost-cmodtechtime-and-their-gaia-equivalent-no-longer-work)

AoE2DE UGC Guide

Task



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
    - [Important](../Important/)
    - [Language Syntax](../Language%20Syntax/)
    - [Task](../Task/)
    - Task

      [Task](./)



      Table of contents
      * [1. cSetTechCost, cAddTechCost, cModTechTime and their gaia equivalent no longer work](#1-csettechcost-caddtechcost-cmodtechtime-and-their-gaia-equivalent-no-longer-work)
* [Mods](../../../../mods/)

  Mods
* [RMS](../../../../rms/)

  RMS
* [AI](../../../../ai/)

  AI
* [Audio](../../../../audio/)

  Audio

Table of contents

* [1. cSetTechCost, cAddTechCost, cModTechTime and their gaia equivalent no longer work](#1-csettechcost-caddtechcost-cmodtechtime-and-their-gaia-equivalent-no-longer-work)

# Task

### 1. `cSetTechCost`, `cAddTechCost`, `cModTechTime` and their gaia equivalent no longer work[¶](#1-csettechcost-caddtechcost-cmodtechtime-and-their-gaia-equivalent-no-longer-work "Permanent link")

Description: Attempting to set or change tech time and cost with these `xsEffectAmount` commands no longer work and they do not do anything.

Expected Behaviour: These commands should let you modify tech cost or time. They should even let you set arbitrary resources. It does not work with any combination.

Reproduction Steps:

1. Create a new scenario with a Town Center in dark age
2. Create a new XS script with the following code:

   |  |  |
   | --- | --- |
   | ``` 1 2 3 4 ``` | ``` void main() {     xsEffectAmount(cSetTechCost, 22, cAttributeGold, 10, 1);     xsEffectAmount(cModTechTime, 22, cAttributeSet, 1, 1); } ``` |
3. Include the script in the scenario
4. When a game is played using the scenario, Loom tech cost and time does not change

Was this page helpful?

Thanks for your feedback!

Thanks for your feedback! Help us improve this page by using our [feedback form](...).

Back to top


Made with
[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
