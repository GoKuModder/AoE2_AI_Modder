# Trigger Conditions And Effects Guide

Use this guide when the question is specifically about AoE2ScenarioParser trigger conditions or effects, especially when the agent needs both parser syntax and real project usage.

## Scope

This repo now teaches the trigger parser surface in two layers:

- exhaustive parser lookup
  use the canonical condition and effect datasets for IDs, method names, signatures, and parameters
- real project usage
  use the project-usage datasets to see how those same conditions and effects are used in working scenario projects

Current generated coverage:

- `41` parser conditions
- `102` parser effects

## Canonical Files

Open these first:

- `docs/trigger_knowledge/condition_usage_playbook.md`
- `docs/trigger_knowledge/effect_usage_playbook.md`
- `docs/trigger_knowledge/condition_usage_playbook.json`
- `docs/trigger_knowledge/effect_usage_playbook.json`
- `docs/trigger_knowledge/conditions_knowledge.json`
- `docs/trigger_knowledge/effects_knowledge.json`
- `docs/trigger_knowledge/condition_project_usage.json`
- `docs/trigger_knowledge/effect_project_usage.json`
- `docs/trigger_knowledge/project_usage_knowledge.md`

Human-readable versions:

- `docs/trigger_knowledge/conditions_knowledge.md`
- `docs/trigger_knowledge/effects_knowledge.md`

Project selection help:

- `docs/agent/references/REFERENCE_PROJECTS.md`

## What Each File Is For

- `condition_usage_playbook.md` and `effect_usage_playbook.md`
  deep teaching documents: what each parser feature is for, how it fits into a trigger architecture, what it commonly pairs with, and where it appears in your projects
- `condition_usage_playbook.json` and `effect_usage_playbook.json`
  the same deep teaching layer in machine-readable form, including communication semantics for player-facing effects
- `conditions_knowledge.json`
  canonical parser condition truth: ID, method name, signature, parameters, notes
- `effects_knowledge.json`
  canonical parser effect truth: ID, method name, signature, parameters, description
- `condition_project_usage.json`
  where each condition appears in the real reference projects, with counts and code examples
- `effect_project_usage.json`
  where each effect appears in the real reference projects, with counts and code examples
- `project_usage_knowledge.md`
  summary of the most common real-project trigger patterns

## Retrieval Workflow

### If the question is "what does this condition or effect do"

1. Open `conditions_knowledge.json` or `effects_knowledge.json`.
2. Match on `internal_name`, `display_name`, or ID.
3. Use the signature and parameters from the canonical dataset.
4. Use the markdown version only if you need a faster human-readable summary.

### If the question is "teach me how this is used"

1. Open `condition_usage_playbook.md` or `effect_usage_playbook.md` first.
2. Read `How It Is Used`, `Architecture Notes`, and `Common Pairings`.
3. If the effect is player-facing, also read `audience_scope`, `attention_strength`, `recommended_frequency`, and `best_use`.
4. Use the paired JSON playbook if the answer needs structured retrieval.
5. Only then join back to `conditions_knowledge.json` or `effects_knowledge.json` for exact syntax.

### If the question is "how is this used in a real project"

1. Open `condition_project_usage.json` or `effect_project_usage.json`.
2. Find the matching `internal_name`.
3. Check `usage_status`, `usage_count`, `used_in_projects`, and `examples`.
4. Open the highest-priority example path from the reference project set.

### If the question needs both syntax and real usage

Join the datasets by `internal_name`:

- architectural teaching from `condition_usage_playbook.json` or `effect_usage_playbook.json`
- canonical syntax from `conditions_knowledge.json` or `effects_knowledge.json`
- working examples from `condition_project_usage.json` or `effect_project_usage.json`

That join is the default trigger-answer pattern for this repo.

## Reference Project Priority

Use real project examples in this order:

1. `LordsOfDiplomacy - Easy Mode`
   primary hand-authored trigger + XS teaching reference
2. `GoKu RPG Project`
   secondary mixed-system trigger reference
   ignore `Difficulty`
3. `Hide_and_Seek`
   useful for dense XS and ability-driven trigger usage, but not the preferred teaching structure

## Common Condition Patterns In Real Projects

The highest-value conditions in your reference projects are not random. They form recurring trigger patterns:

- `variable_value`
  main state gate for cooldowns, toggles, level checks, quest state, and system progression
- `timer`
  loop timing, delayed activation, periodic ticks, and re-enable logic
- `script_call`
  trigger-to-XS bridge checks
- `and_` and `or_`
  combine area, timer, tech, and variable gates into one system-level condition set
- `objects_in_area`
  zone checks for teleports, ability activation, interaction points, and scenario events
- `researching_tech`
  button-like trigger activation pattern in technology-driven interfaces
- `accumulate_attribute` and `own_objects`
  resource and object-threshold gates

These are the conditions that define most real project flow control in the scanned scenarios.

## Common Effect Patterns In Real Projects

The most important effects in the reference projects fall into a few reusable roles:

- orchestration
  `activate_trigger`, `deactivate_trigger`
- XS bridge and runtime signaling
  `script_call`, `change_variable`
- object or stat mutation
  `modify_attribute`, `modify_resource`, `change_ownership`, `replace_object`
- feedback
  `send_chat`, `play_sound`, `display_instructions`, `display_timer`, `change_view`
- object lifecycle and world control
  `create_object`, `create_garrisoned_object`, `remove_object`, `task_object`

If an agent can explain those roles cleanly, it will usually understand the project-level trigger architecture.

## Communication Effect Selection

For player-facing global-event communication, do not treat all feedback effects as interchangeable.

- `display_timer`
  best for high-frequency shared notifications and recurring global-event visibility
- `display_instructions`
  best for low-frequency, high-importance shared announcements that should not keep flooding the screen
- `send_chat`
  best for debugging, quiet per-player messages, or player-specific communication that does not need shared visibility
- `change_view`
  best as a targeted support effect when one player or a selected set of players needs their attention pulled to the event location

Important distinctions stored in the playbook JSON:

- `display_timer` and `display_instructions`
  shared / all-player visible communication tools
- `send_chat`
  selected-player communication tool
- `change_view`
  targeted attention tool that can be applied per player

## How To Read The Usage Datasets

Each usage entry tells you:

- whether the condition or effect was observed in the scanned projects
- how many times it appeared
- which projects used it
- the best representative file paths
- direct example lines to open first

Important rule:

- `not_observed_in_reference_projects` does not mean the parser feature is invalid
- it only means this repo did not see that feature in the scanned local scenario projects

## Good Answer Pattern

For a strong answer about a trigger condition or effect:

1. name the parser method exactly
2. state the important parameters
3. explain the architectural role, not just the literal behavior
4. explain what it usually pairs with in a modular trigger system
5. cite the best local project example path
6. mention whether the pattern is common or rare in the scanned projects

## Cross-Domain Notes

- `script_call` conditions and effects should usually route into both this guide and `docs/agent/domains/XS_AGENT_GUIDE.md`
- trigger questions about variable registries should also open `docs/agent/domains/TRIGGER_AGENT_GUIDE.md`
- trigger questions that are really about unit or tech data relationships may need `docs/agent/domains/DAT_AGENT_GUIDE.md`
