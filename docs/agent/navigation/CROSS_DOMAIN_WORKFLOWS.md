# Cross-Domain Workflows

Many AoE2DE tasks span more than one domain. Use this file when the task is not purely `XS`, purely `AI scripts`, purely `scenario triggers`, or purely `.dat/genie tooling`.

## AI Scripts <-> XS

Primary files:

- `AI_Scripting/rpg_xs_bridge_v3.ai`
- `AI_Scripting/rpg_xs_bridge_v3.per`
- `AI_Scripting/rpg_xs_bridge_v3.xs`
- `src/integration/xs_bridge_contract.py`
- `src/integration/xs_injector.py`

Use this workflow when:

- AI rules need to hand off information to XS
- you need to preserve bridge semantics
- the task mentions trigger variables being written from AI / XS bridge code

Routing rule:

- start in `docs/agent/domains/AI_SCRIPT_AGENT_GUIDE.md` if the question is mainly about `.per` logic
- start in `docs/agent/domains/XS_AGENT_GUIDE.md` if the question is mainly about XS code behavior
- then inspect the bridge files above

## Scenario Triggers <-> XS

Primary files:

- `docs/agent/domains/TRIGGER_AGENT_GUIDE.md`
- `docs/agent/domains/XS_AGENT_GUIDE.md`
- `docs/trigger_knowledge/effects_knowledge.md`

Typical interaction:

- scenario trigger uses a script call or variable change
- XS reacts to trigger variables or scenario state

Routing rule:

- if the task is about trigger authoring, start with the trigger guide
- if the task is about the XS script itself, start with the XS guide

## Scenario Triggers <-> AI Scripts

Primary files:

- `docs/agent/domains/TRIGGER_AGENT_GUIDE.md`
- `docs/agent/domains/AI_SCRIPT_AGENT_GUIDE.md`
- `docs/trigger_knowledge/effects_knowledge.md`

Typical interaction:

- trigger effects change AI goals or acknowledge AI signals
- AI scripts react to signals, goals, or scenario state

Routing rule:

- start with triggers when the question is about what the scenario editor can do
- start with AI scripts when the question is about `.per` reactions to those effects

## .dat/Genie Tooling <-> Triggers

Primary files:

- `docs/agent/domains/DAT_AGENT_GUIDE.md`
- `docs/agent/domains/TRIGGER_AGENT_GUIDE.md`
- `docs/trigger_knowledge/genie_registry.json`

Typical interaction:

- trigger effects reference unit or object IDs whose meaning comes from game data
- trigger attribute choices often reflect `.dat` relationships

Routing rule:

- start with triggers for effect / attribute syntax
- start with `.dat/genie tooling` for object identity, relationships, and data-model meaning

## .dat/Genie Tooling <-> XS

Primary files:

- `docs/agent/domains/DAT_AGENT_GUIDE.md`
- `docs/agent/domains/XS_AGENT_GUIDE.md`
- `XS_Training/modding_general/07_genie_editor_xs_bridge.md`

Typical interaction:

- XS logic depends on unit classes, tasks, technologies, or other base data relationships
- mod changes alter the meaning of XS constants or runtime assumptions

Routing rule:

- start with XS for code-level behavior
- use `.dat/genie tooling` references to understand the underlying game data being manipulated

## Escalation Rule

If a task crosses domains and you are unsure which side is primary:

1. choose the language or system the user is actively editing
2. answer from that domainâ€™s canonical sources first
3. pull supporting context from the related domain only after the primary answer is grounded

If you need project-scale examples for a cross-domain flow, use `docs/agent/references/REFERENCE_PROJECTS.md` to choose the right external reference project instead of searching blindly.

