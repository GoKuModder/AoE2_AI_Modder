# Retrieval Rules

Use these rules when answering questions or generating code from this repository.

## Core Workflow

Follow this order:

1. Identify the primary domain.
2. Open that domain's agent guide.
3. Search exact symbols, IDs, or command names first.
4. Search structured generated artifacts second.
5. Use recipes and supporting source corpora only after the canonical data pass.
6. Check cross-domain workflows if the task touches more than one system.

Short version: exact symbol first, then concept docs, then recipes, then pitfalls.

## Runtime Entry Points

- Use `src/retrieval/aoe_unified_retriever.py` when you want one low-token runtime over compact recipes plus exact `XS`, trigger, AI, and genie datasets.
- Use `src/retrieval/aoe_compact_retriever.py` when you only need the smallest implementation-oriented recipe layer.
- Use `src/retrieval/genie_dat_retriever.py` when the task is `.dat`-only and you want the smallest dedicated dat-model context.
- Use domain-specific retrievers only when the task is clearly specialized, for example `src/retrieval/xs_script_retriever.py` for XS-heavy lookup.
- Use `src/eval/unified_retrieval_eval.py` and `tools/eval_unified_retrieval.py` when you need to verify that retrieval quality still meets the repo's compactness budgets.

## Routing Rules

- `XS`
  Trigger words: `xs`, `xsSet`, `xsGet`, constants beginning with `c`, arrays, vectors, rules, timers, trigger variables used from XS.
- `AI scripts`
  Trigger words: `.per`, `.ai`, `defrule`, facts, goals, taunts, AI commands.
- `Scenario triggers`
  Trigger words: effect, attribute, trigger variable, condition, AoE2ScenarioParser, script call, modify attribute, modify resource.
- `.dat/genie tooling`
  Trigger words: `.dat`, Genie Editor, unit ID, tech tree, armor class, class IDs, task IDs, train location, graphics, resource storage.

If two domains match:

- prefer `AI scripts` over `XS` when the question is about `.per` syntax or command legality
- prefer `XS` over `scenario triggers` when the question is about actual XS code behavior
- prefer `scenario triggers` over `.dat/genie tooling` when the question is about trigger effects or attributes inside the scenario editor
- prefer `.dat/genie tooling` when the question is about base game data relationships rather than trigger-time or script-time behavior

## Naming Normalization

- Search exact official names first.
- Normalize user input by lowercasing and stripping punctuation when you need fuzzy routing.
- Preserve official casing and spelling in final answers.
- Treat aliases as routing hints, not canonical output.

Examples:

- `xssetunitposition` routes to `xsSetUnitPosition`
- `defrule` routes to AI scripts
- `train location` may touch both `scenario triggers` and `.dat/genie tooling`

## Preferred Sources By Task Type

### Exact symbol lookup

- XS function or constant
  Open `docs/agent_database/xs_functions_catalog.json` or `docs/agent_database/xs_constants_catalog.json`
- AI command
  Open `docs/ai_scripting_knowledge/metadata_index.json`
- Trigger effect or attribute
  Open `docs/trigger_knowledge/effects_knowledge.json` or `docs/trigger_knowledge/attributes_dataset.json`
- Trigger condition
  Open `docs/trigger_knowledge/conditions_knowledge.json`
- Deep trigger teaching lookup
  Open `docs/trigger_knowledge/condition_usage_playbook.json` or `docs/trigger_knowledge/effect_usage_playbook.json`
- Real trigger condition or effect usage
  Open `docs/trigger_knowledge/condition_project_usage.json` or `docs/trigger_knowledge/effect_project_usage.json`
- Genie object ID
  Open `docs/trigger_knowledge/genie_registry.json`
- `.dat` field or concept such as `standing_sprite_id1`, `particle_effect_name`, `modify_tech`, or `add_research_location`
  Open `docs/agent_database/genie_dat_concepts.json`

### Conceptual "how do I" query

- Open the domain guide first.
- If the task is "build this scenario/map/system from an idea document", open `docs/agent/scenario_builder/MAP_IDEA_TO_IMPLEMENTATION.md` and `docs/agent/scenario_builder/WHERE_TO_FIND_THINGS.md` before drilling into domain data.
- For common implementation requests, check the compact recipe datasets in `docs/agent/references/recipes/` before opening broader markdown guides.
- For low-token runtime retrieval across both recipes and exact lookup datasets, prefer `src/retrieval/aoe_unified_retriever.py`.
- For `.dat`-specific concept lookup, prefer `docs/agent/scenario_builder/DAT_LOOKUP_INDEX.md` and `src/retrieval/genie_dat_retriever.py`.
- For parser-surface trigger questions, open `docs/agent/domains/TRIGGER_CONDITIONS_EFFECTS_GUIDE.md` after the main trigger guide.
- Then open the domain's generated markdown or document store.
- Use raw source corpora only if the structured artifacts do not answer the question.
- If the task involves generating or writing a project artifact such as a final `.xs` file, look for project configuration first and ask the user for the output location when it is not already defined.

### Cross-domain workflow

- Start with the primary domain guide.
- Then open `docs/agent/navigation/CROSS_DOMAIN_WORKFLOWS.md`.

## Answer Construction Rules

- Prefer canonical names, IDs, signatures, and file paths.
- Separate "what exists in the repo" from "what is not yet productized".
- If coverage is partial, say so clearly instead of implying full support.
- When using raw corpora, state that they are supporting material rather than the primary retrieval source.
- When describing generated-file placement, use generalized project-relative guidance instead of machine-specific absolute paths unless the user explicitly provides the destination.

## Common Mistakes To Avoid

- Do not start in `XS_Training/` or `AoE2_AI_Scripting_Guide/` before checking the domain guide and structured artifacts.
- Do not confuse `AI scripts` with `XS`; they are different languages and different runtime surfaces.
- Do not treat trigger effect knowledge as a substitute for `.dat` knowledge.
- Do not imply a full `.dat` editing runtime exists in this repo today.
- Do not rely on example scripts alone when a structured artifact exists.
- Do not invent a hardcoded XS output path on behalf of the user when the project does not already define one.

