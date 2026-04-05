# Trigger Lookup Index

This file exists so an agent does not have to guess where trigger information is stored.

## If You Need A Trigger Condition

Open:

1. `docs/trigger_knowledge/conditions_knowledge.json`
2. `docs/trigger_knowledge/condition_usage_playbook.md`
3. `docs/trigger_knowledge/condition_project_usage.json`

Use this sequence for:

- exact condition name
- parameters
- what the condition actually does
- how it is used in real projects

## If You Need A Trigger Effect

Open:

1. `docs/trigger_knowledge/effects_knowledge.json`
2. `docs/trigger_knowledge/effect_usage_playbook.md`
3. `docs/trigger_knowledge/effect_project_usage.json`

Use this sequence for:

- exact effect name
- parameters
- player-visibility semantics
- real project usage

## If You Need Trigger Attributes

Open:

1. `docs/trigger_knowledge/attributes_dataset.json`
2. `docs/trigger_knowledge/attributes_knowledge.md`

Use this for:

- parser enum mapping
- object attribute names
- modify-attribute workflows

## If You Need To Know How Triggers Are Structured In A Real Project

Open:

1. `docs/agent/domains/TRIGGER_AGENT_GUIDE.md`
2. `docs/agent/references/patterns/trigger_xs_patterns.json`
3. `docs/agent/references/REFERENCE_PROJECTS.md`

Best structure references:

- `LordsOfDiplomacy - Easy Mode`
- `GoKu RPG Project`

## Best File Per Question

- "Where are conditions?"
  `docs/trigger_knowledge/conditions_knowledge.json`
- "Where are effects?"
  `docs/trigger_knowledge/effects_knowledge.json`
- "How is this condition used?"
  `docs/trigger_knowledge/condition_usage_playbook.md`
- "How is this effect used?"
  `docs/trigger_knowledge/effect_usage_playbook.md`
- "Show me real project examples."
  `docs/trigger_knowledge/condition_project_usage.json`
  `docs/trigger_knowledge/effect_project_usage.json`
