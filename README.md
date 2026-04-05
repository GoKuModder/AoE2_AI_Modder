# aoe2-ai-modder

AoE2:DE agent knowledge base for expert coding work in `XS`, `AI scripts`, `scenario triggers`, and `.dat/genie tooling`.

This package is designed so a coding agent can be pointed at the repo, orient itself quickly, and retrieve the right local knowledge without wasting tokens on broad searches. It packages AoE2:DE coding knowledge into agent-facing docs, compact datasets, and retrieval utilities so an AI can answer implementation questions, symbol lookups, and architecture questions with much less context-hunting.

The main value is the combination of:

- agent-facing guidance that explains how to use the repo
- structured datasets for retrieval
- source corpora and reference material for deeper lookup
- small runtime utilities that already support some retrieval workflows

Status: git install only. Not published to PyPI.

## What This Package Does

- teaches an AI where AoE2:DE knowledge lives in the repo
- provides compact local retrieval for `XS`, `AI scripts`, `scenario triggers`, and `.dat/genie tooling`
- stores exact symbol catalogs, trigger/effect datasets, project patterns, and implementation recipes
- helps an AI move from "what does this symbol mean?" to "how should I build this system?"

This is primarily a local knowledge and retrieval package. It is strongest when used as a low-token support library for an agent that is coding an AoE2:DE project.

## Start Here

If you are an agent or are preparing context for one, open these files first:

1. `AGENT_START_HERE.md`
2. `docs/README.md`
3. `docs/agent/README.md`
4. `docs/agent/scenario_builder/README.md`
5. `docs/agent/navigation/KNOWLEDGE_MAP.md`
6. `docs/agent/navigation/RETRIEVAL_RULES.md`
7. The domain guide for the task you are answering

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

Cross-domain interactions:

- `docs/agent/navigation/CROSS_DOMAIN_WORKFLOWS.md`

Machine-readable routing support:

- `docs/agent/routing/knowledge_map.json`
- `docs/agent/routing/query_router.json`
- `docs/agent/routing/agent_query_map.json`

Curated external project references:

- `docs/agent/references/REFERENCE_PROJECTS.md`
- `docs/agent/references/reference_projects.json`

Structured architecture pattern datasets:

- `docs/agent/references/patterns/README.md`
- `docs/agent/references/patterns/trigger_xs_patterns.json`
- `docs/agent/references/patterns/genie_workflow_patterns.json`

Compact recipe datasets:

- `docs/agent/references/recipes/README.md`
- `docs/agent/references/recipes/scenario_recipes.json`
- `docs/agent/references/recipes/parser_manager_patterns.json`
- `docs/agent/references/recipes/genie_recipes.json`
- `docs/agent/references/recipes/reference_recipes_eval.json`

Dedicated `.dat` concept lookup:

- `docs/agent_database/genie_dat_concepts.json`
- `src/retrieval/genie_dat_retriever.py`

Trigger condition and effect datasets:

- `docs/trigger_knowledge/conditions_knowledge.json`
- `docs/trigger_knowledge/effects_knowledge.json`
- `docs/trigger_knowledge/condition_usage_playbook.md`
- `docs/trigger_knowledge/effect_usage_playbook.md`
- `docs/trigger_knowledge/condition_usage_playbook.json`
- `docs/trigger_knowledge/effect_usage_playbook.json`
- `docs/trigger_knowledge/condition_project_usage.json`
- `docs/trigger_knowledge/effect_project_usage.json`
- `docs/trigger_knowledge/project_usage_knowledge.md`

Curated XS examples:

- `examples/xs/README.md`
- `examples/xs/codex_teleport_barracks.xs`
- `examples/xs/codex_magic_following_spell.xs`
- `examples/xs/gemini_teleport_barracks.xs`
- `examples/xs/xs_arrays_full_project_demo.xs`

## Domain Map

- `XS`
  XS scripting knowledge, function and constant catalogs, runtime retrieval, and bridge-aware scripting references.
- `AI scripts`
  `.per` / `.ai` command knowledge, retrieval datasets, safe command guidance, and validation utilities.
- `Scenario triggers`
  condition, effect, attribute, real-project usage, and genie object lookup for AoE2ScenarioParser-oriented work.
- `.dat/genie tooling`
  current repo coverage now includes a dedicated `.dat` concept dataset and retriever, plus recipe/pattern layers for implementation guidance.

## Truth Model

Use the repo in this order:

1. Agent-facing markdown guides explain where truth lives and how to route the query.
2. Generated JSON / JSONL artifacts provide structured retrieval truth.
3. Raw source corpora provide supporting context and examples.
4. Runtime Python modules show what is already productized for retrieval or validation.

Do not start with the raw training corpora unless the guides tell you to. In this repo, source material is supporting evidence, not the default entrypoint.

## Repository Roles

- `AGENT_START_HERE.md`, `docs/README.md`, and `docs/agent/`
  Agent onboarding, hierarchy discovery, routing, domain usage, and workflow guidance.
- `docs/ai_scripting_knowledge/`, `docs/xs_knowledge/`, `docs/trigger_knowledge/`, `docs/agent_database/`
  Generated or structured retrieval artifacts.
- `examples/`
  Curated example scripts and teaching material intended to stay in the published repo.
- `AoE2_AI_Scripting_Guide/`, `XS_Training/`
  Raw guide sources, training material, and external references.
- `src/retrieval/`, `src/integration/`, `src/builds/`, `tools/`
  Runtime utilities, knowledge builders, and verification scripts.

## Quick Start

Requirements: Python 3.10+

```bash
git clone https://github.com/GoKuModder/AoE2_AI_Modder
cd AoE2_AI_Modder
py -3 -m pip install -e .
```

Or install directly from git:

```bash
py -3 -m pip install "aoe2-ai-modder @ git+https://github.com/GoKuModder/AoE2_AI_Modder.git"
```

Run tests:

```bash
py -3 -m unittest discover -s tests -p "test_*.py"
```

## Existing Runtime Entry Points

Current retrieval / validation modules:

- `src/retrieval/ai_script_retriever.py`
- `src/retrieval/aoe_compact_retriever.py`
- `src/retrieval/genie_dat_retriever.py`
- `src/retrieval/aoe_unified_retriever.py`
- `src/retrieval/ai_script_validator.py`
- `src/retrieval/xs_script_retriever.py`
- `src/retrieval/xs_script_validator.py`

Current build scripts:

- `tools/build_ai_scripting_knowledge.py`
- `tools/build_xs_knowledge.py`
- `tools/build_trigger_knowledge.py`

## External Tools

These tools should be available in the environment when an agent is expected to work directly on AoE2:DE projects:

- Scenario triggers and scenario design: [AoE2ScenarioParser](https://github.com/KSneijders/AoE2ScenarioParser)
- XS linting and validation: [xs-check](https://github.com/Divy1211/xs-check)
- `.dat` and genie data modding: [aoe2-genie-tooling](https://github.com/GoKuModder/aoe2-genie-tooling)

## Credits

This library is built from a mix of curated source material, generated datasets, and real project references.

Core source references used in this repo include:

- [ugc.aoe2.rocks](https://ugc.aoe2.rocks/)
- [Genie Editor article on Age of Empires Fandom](https://ageofempires.fandom.com/wiki/Genie_Editor)
- Official Patch Notes
- imported and curated training material under `AoE2_AI_Scripting_Guide/` and `XS_Training/`

Real project references used to shape the retrieval layer and teaching material include:

- `Lords of Diplomacy`
- `RPG GoKu`
- `F13 Dark Hunt`

Those sources were then reorganized into the local agent docs, datasets, playbooks, recipes, and retrievers that ship in this package.

## Support

For now, use GitHub Issues for bug reports and feature requests.

Security issues: see `SECURITY.md`.

