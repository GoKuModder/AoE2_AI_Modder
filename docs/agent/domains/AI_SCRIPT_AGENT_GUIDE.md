# AI Script Agent Guide

Use this guide for AoE2DE `AI scripts` tasks, especially `.per` / `.ai` command questions and rule authoring.

## What This Domain Is For

This domain covers AI command knowledge, `.per` rule logic, command safety, and retrieval guidance for script generation. It has structured knowledge and runtime utilities, but it is less productized than the XS domain.

## Canonical Sources In This Repo

Open these first:

- `docs/ai_scripting_knowledge/README.md`
- `docs/ai_scripting_knowledge/metadata_index.json`
- `docs/ai_scripting_knowledge/document_store.jsonl`
- `AoE2_AI_Scripting_Guide/README.md`

Runtime support:

- `src/retrieval/ai_script_retriever.py`
- `src/retrieval/ai_script_validator.py`

Supporting source material:

- `AoE2_AI_Scripting_Guide/`
- `AI_Scripting/`

## Primary Files To Open First

- exact AI command question
  Open `docs/ai_scripting_knowledge/metadata_index.json`
- conceptual AI scripting question
  Open `docs/ai_scripting_knowledge/document_store.jsonl` and `AoE2_AI_Scripting_Guide/`
- AI validation / safe command question
  Open `src/retrieval/ai_script_validator.py`
- AI bridge question
  Open `AI_Scripting/rpg_xs_bridge_v3.per` and `docs/agent/navigation/CROSS_DOMAIN_WORKFLOWS.md`

## Common Task Types

- confirm whether an AI command is allowed or blocked
- explain `.per` patterns like `defrule`, goals, taunts, and strategic logic
- retrieve example snippets for a known AI command
- validate generated AI script output
- connect AI scripts to XS or triggers

## Core Recipes

### Recipe: exact command lookup

1. Search `docs/ai_scripting_knowledge/metadata_index.json` by exact command name.
2. Use the command status and template snippets as primary truth.
3. Use the guide corpus only if you need explanation or a broader pattern.

### Recipe: conceptual AI query

1. Open this guide.
2. Search `docs/ai_scripting_knowledge/document_store.jsonl`.
3. Fall back to `AoE2_AI_Scripting_Guide/` for richer explanation.

### Recipe: validate generated AI output

1. Use `src/retrieval/ai_script_validator.py`.
2. Check blocked commands, unknown commands, and warnings separately.
3. Do not assume AI and XS validation rules are interchangeable.

## Known Pitfalls / Engine Quirks

- Do not mix `.per` AI syntax with XS syntax.
- Command legality lives in the AI metadata and validator, not in example scripts alone.
- Example files in `AI_Scripting/` show patterns, but they are not the full command truth.
- Bridge questions often require both this guide and the XS guide.

## Cross-Domain Dependencies

- `XS`
  Use for AI <-> XS bridge flows and trigger-variable handoff logic.
- `scenario triggers`
  Use when trigger effects set AI goals or acknowledge AI signals.
- `.dat/genie tooling`
  Use when AI behavior depends on unit classes, technologies, or data-model assumptions rather than script syntax itself.

