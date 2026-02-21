# Gemini Agent Context for `AoE2_AI_Modder`

This repository supports Gemini-based agent work.

## Task Source
Gemini should load tasks from the dedicated queue file below:

@./GEMINI_TASKS.md

If multiple tasks are `pending`, execute the first one unless the user asks for batch execution.

## Project Focus
- AoE2:DE XS scripting workflows.
- Trigger/knowledge tooling under `src/`, `docs/`, `tools/`.
- Long-term goal: build a reliable knowledge database AI agents can use to code AoE scenarios/scripts.

## Working Rules for Gemini
1. Respect task scope and path constraints exactly.
2. For XS drafts, default output path is `Gemini XS functions/` unless task says otherwise.
3. Do not redefine built-in XS engine functions in production scripts.
4. Validate XS files with:
   - `C:\Users\user\Downloads\xs-check.exe "<file>"`
5. Report exact file paths and lint output in the final handoff.
6. Preferred Gemini lane in this repo: JSON/data curation, indexing, and manifests. Avoid gameplay logic tasks unless explicitly assigned.
7. Do not edit files in `CODEX XS functions/` unless a task explicitly permits it.

## Handoff Format
- `Files changed`
- `Validation run`
- `Open issues / assumptions`
