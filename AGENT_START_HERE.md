# Agent Start Here

This repository is meant to function as a local AoE2:DE knowledge base for coding agents. Its job is to help you answer and implement tasks in `XS`, `AI scripts`, `scenario triggers`, and `.dat/genie tooling` without guessing where the authoritative files live.

The agent-facing layer now lives under `docs/agent/`. Use the folder indexes if you want to understand the hierarchy before reading the individual guides:

- `docs/README.md`
- `docs/agent/README.md`
- `docs/agent/scenario_builder/README.md`

## Read Order

Open files in this order:

1. `docs/agent/navigation/KNOWLEDGE_MAP.md`
2. `docs/agent/navigation/RETRIEVAL_RULES.md`
3. `docs/agent/scenario_builder/WHERE_TO_FIND_THINGS.md` if the task is about building a scenario or map system
4. The domain guide that matches the task
5. `docs/agent/navigation/CROSS_DOMAIN_WORKFLOWS.md` if the task spans more than one domain

Domain guides:

- `docs/agent/domains/XS_AGENT_GUIDE.md`
- `docs/agent/domains/AI_SCRIPT_AGENT_GUIDE.md`
- `docs/agent/domains/TRIGGER_AGENT_GUIDE.md`
- `docs/agent/domains/TRIGGER_CONDITIONS_EFFECTS_GUIDE.md`
- `docs/agent/domains/DAT_AGENT_GUIDE.md`

Scenario builder guides:

- `docs/agent/scenario_builder/WHERE_TO_FIND_THINGS.md`
- `docs/agent/scenario_builder/TRIGGER_LOOKUP_INDEX.md`
- `docs/agent/scenario_builder/PARSER_MANAGERS_GUIDE.md`
- `docs/agent/scenario_builder/XS_PROJECT_FILES_GUIDE.md`
- `docs/agent/scenario_builder/GENIE_WORKFLOW_GUIDE.md`
- `docs/agent/scenario_builder/DAT_LOOKUP_INDEX.md`
- `docs/agent/scenario_builder/MAP_IDEA_TO_IMPLEMENTATION.md`

Machine-readable helpers:

- `docs/agent/routing/knowledge_map.json`
- `docs/agent/routing/query_router.json`
- `docs/agent/routing/agent_query_map.json`
- `src/retrieval/aoe_unified_retriever.py`
- `src/retrieval/aoe_compact_retriever.py`
- `src/retrieval/genie_dat_retriever.py`
- `docs/agent_database/genie_dat_concepts.json`
- `docs/trigger_knowledge/condition_usage_playbook.json`
- `docs/trigger_knowledge/effect_usage_playbook.json`
- `docs/trigger_knowledge/conditions_knowledge.json`
- `docs/trigger_knowledge/effects_knowledge.json`
- `docs/trigger_knowledge/condition_project_usage.json`
- `docs/trigger_knowledge/effect_project_usage.json`
- `docs/agent/references/patterns/README.md`
- `docs/agent/references/patterns/trigger_xs_patterns.json`
- `docs/agent/references/patterns/genie_workflow_patterns.json`

Curated external references:

- `docs/agent/references/REFERENCE_PROJECTS.md`
- `docs/agent/references/reference_projects.json`

Compact recipe datasets:

- `docs/agent/references/recipes/README.md`
- `docs/agent/references/recipes/scenario_recipes.json`
- `docs/agent/references/recipes/parser_manager_patterns.json`
- `docs/agent/references/recipes/genie_recipes.json`
- `docs/agent/references/recipes/reference_recipes_eval.json`

Curated examples:

- `examples/xs/README.md`

## How To Route A Query

- If the task mentions XS functions, constants, arrays, rules, vectors, or `xs*` symbols, start with `docs/agent/domains/XS_AGENT_GUIDE.md`.
- If the task mentions `.per`, `.ai`, `defrule`, goals, taunts, or AI command usage, start with `docs/agent/domains/AI_SCRIPT_AGENT_GUIDE.md`.
- If the task mentions effects, attributes, variables, trigger scripting, AoE2ScenarioParser, or object IDs in scenario editing, start with `docs/agent/domains/TRIGGER_AGENT_GUIDE.md`.
- If the task is specifically about parser conditions, parser effects, or "how is this used in a real trigger project", open `docs/agent/domains/TRIGGER_CONDITIONS_EFFECTS_GUIDE.md` immediately after `docs/agent/domains/TRIGGER_AGENT_GUIDE.md`.
- If the task mentions Genie Editor, `.dat`, units, techs, tasks, armor classes, train locations, or broad data-modding relationships, start with `docs/agent/domains/DAT_AGENT_GUIDE.md`.
- If the task is specifically about `.dat` fields or dat-model concepts like `standing_sprite_id1`, `dead_unit_id`, `particle_effect_name`, `modify_tech`, `set_required_tech`, or `civ_manager.add_resource`, open `docs/agent/scenario_builder/DAT_LOOKUP_INDEX.md` immediately after `docs/agent/domains/DAT_AGENT_GUIDE.md`.

If a task spans more than one domain, identify the primary domain first, answer from its canonical sources, then use `docs/agent/navigation/CROSS_DOMAIN_WORKFLOWS.md` to connect it to the other domains.

If you need real project-scale examples after the canonical pass, use `docs/agent/references/REFERENCE_PROJECTS.md` instead of searching arbitrary external folders.
If you need a worked XS script example after the canonical pass, use `examples/xs/README.md`.
If the task starts from a map idea or design brief and the goal is implementation, open `docs/agent/scenario_builder/MAP_IDEA_TO_IMPLEMENTATION.md`.
If the task matches a common implementation workflow, prefer the compact recipe datasets and `src/retrieval/aoe_compact_retriever.py`.
If you need one low-token runtime that can answer both implementation questions and exact symbol lookups, use `src/retrieval/aoe_unified_retriever.py`.
If the query is `.dat`-only and you want the smallest dedicated context, use `src/retrieval/genie_dat_retriever.py`.

## Truth Model

Treat files in this order of authority:

1. Agent-facing markdown guides
   These explain where to look and which files are canonical.
2. Generated structured artifacts
   Use JSON / JSONL files for precise retrieval, IDs, and machine-readable truth.
3. Raw source corpora
   Use these for deeper explanation, examples, and gaps not covered by generated artifacts.
4. Runtime Python code
   Use this to understand what is already operationalized for retrieval or validation.

Do not assume example scripts or source corpora are canonical just because they are more verbose.

## What "Good Usage" Looks Like

- Open the domain guide before searching broadly.
- Prefer exact symbols, IDs, and canonical names over paraphrases.
- Use generated datasets for precise lookup and the markdown guides for routing and task framing.
- Distinguish between "reference coverage exists" and "runtime support exists".
- Be explicit when a domain currently has weaker coverage, especially `.dat/genie tooling`.
- If a task requires writing a generated `.xs` file and no project config defines the destination, ask the user where the file should be placed instead of inventing a machine-specific path.

## Required Questions You Should Be Able To Answer

After reading the files above, you should know:

- where to look first for `XS`
- where to look first for `AI scripts`
- where to look first for `scenario triggers`
- where to look first for `.dat/genie tooling`
- which files are teaching material versus structured retrieval truth
- how the domains interact

If you cannot answer those questions quickly, return to `docs/agent/navigation/KNOWLEDGE_MAP.md` and the relevant domain guide.

