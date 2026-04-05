# XS Agent Guide

Use this guide for AoE2DE `XS` scripting tasks.

## What This Domain Is For

This domain covers XS functions, constants, retrieval-ready scripting knowledge, and bridge-aware scripting workflows. It is the strongest and most productized domain in the repo today.

## Canonical Sources In This Repo

Open these first:

- `docs/xs_knowledge/README.md`
- `docs/agent_database/xs_functions_catalog.json`
- `docs/agent_database/xs_constants_catalog.json`
- `docs/xs_knowledge/metadata_index.json`
- `docs/xs_knowledge/document_store.jsonl`

Runtime support:

- `src/retrieval/xs_script_retriever.py`
- `src/retrieval/xs_script_validator.py`

Supporting source material:

- `XS_Training/`
- `examples/xs/`

## Primary Files To Open First

- exact function or constant question
  Open `docs/agent_database/xs_functions_catalog.json` or `docs/agent_database/xs_constants_catalog.json`
- conceptual XS question
  Open `docs/xs_knowledge/document_store.jsonl` and `docs/xs_knowledge/README.md`
- practical XS example question
  Open `examples/xs/README.md` and then the most relevant curated script
- runtime retrieval / validation question
  Open `src/retrieval/xs_script_retriever.py` and `src/retrieval/xs_script_validator.py`
- bridge question
  Open `src/integration/xs_bridge_contract.py` and `AI_Scripting/rpg_xs_bridge_v3.xs`

## Common Task Types

- find the exact signature of an XS function
- find the value or meaning of an XS constant
- answer "how do I do X in XS?"
- validate generated XS code against known command metadata
- connect XS code to AI or trigger workflows
- show a practical XS example for a mechanic or pattern
- explain how to declare XS variables in a scenario project
- explain how to generate or assemble a project XS file safely
- explain where a generated XS file should be written

## Core Recipes

### Recipe: exact function lookup

1. Search `docs/agent_database/xs_functions_catalog.json` by exact function name.
2. Use the function signature and parameter list as primary truth.
3. Use `docs/xs_knowledge/document_store.jsonl` only if you need explanation or examples.

### Recipe: exact constant lookup

1. Search `docs/agent_database/xs_constants_catalog.json`.
2. Preserve the canonical constant name and value in the answer.
3. Use prose sources only for meaning or usage context.

### Recipe: conceptual XS query

1. Open this guide.
2. Search `docs/xs_knowledge/document_store.jsonl` or the supporting XS markdown.
3. If the task is bridge-related, open `docs/agent/navigation/CROSS_DOMAIN_WORKFLOWS.md`.

### Recipe: practical XS example query

1. Open `examples/xs/README.md`.
2. Pick the closest curated example by mechanic or pattern.
3. Use the example to demonstrate structure and engine usage, then anchor exact API claims in the structured catalogs.

### Recipe: XS project architecture or generation query

1. Open this guide.
2. Open `docs/agent/references/patterns/trigger_xs_patterns.json`.
3. Start with the semantic pattern:
   - centralized XS variable registry
   - centralized trigger-variable registry
   - centralized XS file assembly
4. If the task includes writing a generated `.xs` file, check project config first.
5. If no project-configured output destination exists, ask the user where the generated `.xs` file should be placed before writing it.

## XS Variables Versus Trigger Variables

Keep these two systems separate:

- XS variables
  Script-level XS state that lives inside the `.xs` runtime.
- trigger variables
  Scenario variables shared through trigger logic and XS bridge calls.

For scenario-style XS globals that must persist in the generated `.xs` file, prefer explicit global declarations such as:

```xs
extern int xsVariable1 = -1;
extern int gCounter = 0;
```

In the project patterns you showed, `extern` is the important part for persistent XS globals in scenario work.

Trigger variables are different:

- read them from XS with `xsTriggerVariable(variable_id)`
- write them from XS with `xsSetTriggerVariable(variable_id, value)`

Rule of thumb:

- use `extern` XS variables for XS-private state or generated XS support state
- use trigger variables when triggers and XS both need to observe or mutate the same scenario state

Do not treat XS globals and trigger variables as one shared registry. They are two different storage surfaces.

## How To Declare XS Variables In A Large Project

The recurring project pattern is:

1. one module owns XS variable allocation
2. that module emits `extern int xsVariableN = -1;` declarations
3. that module stores a semantic mapping from meaning to generated variable name
4. feature modules consume the mapping instead of inventing ad hoc variable names

This pattern appears in two forms in your reference projects:

- direct-write generation
  `LordsOfDiplomacy - Easy Mode` and `GoKu RPG Project` generate a block of `extern int xsVariableN = -1;` lines and write them to the target `.xs` file first, while also filling a Python mapping like `variable_mapping_xs`
- registry-driven generation
  `Hide_and_Seek` builds the `extern` declarations from a semantic registry, stores them in a named support include file, and lets the runtime builder assemble the final XS output later

The important lessons are:

- centralize ownership of XS variable names
- keep semantic meaning outside the raw `xsVariableN` names
- let feature code ask for a variable by meaning, not by slot number
- keep broad bridge constants or helper functions centralized

## How To Produce The XS File

There are two real patterns in your projects.

### Legacy direct-write pattern

Use one builder module to:

1. open the destination `.xs` file
2. write the full `extern int xsVariableN = -1;` block
3. append shared helper functions
4. append generated feature functions or templates
5. avoid duplicate template insertion when appending

This is a valid project pattern and matches how `LordsOfDiplomacy - Easy Mode` and `GoKu RPG Project` currently work.

### Preferred generalized registry/include pattern

Use one registry to hold:

- generated `extern` variable definitions
- shared helper function definitions
- named include-file contents
- runtime XS definitions that will become the final assembled script

Then:

1. register the support include content, such as `support_variables.xs`
2. generate the runtime XS string separately
3. assemble the final runtime XS from include statements plus generated body
4. let the outer build step decide where the final `.xs` file is written

This is the cleaner generalized pattern because:

- the XS support file content is reusable
- include filenames stay project-relative instead of machine-specific
- assembly logic is separated from destination-path logic
- agents can reason about generated support files without assuming one local machine layout

## Where To Place The Generated XS File

Do not hardcode a machine-specific path in the knowledge base guidance.

Preferred rule:

- if the project already has a configured XS output destination, use that configuration
- otherwise ask the user where the generated `.xs` file should be created

Good generalized guidance:

- the final script usually belongs in the mod or scenario XS output area chosen by the project
- support include filenames inside the generated XS should stay relative, for example `include "support_variables.xs";`
- the write destination itself should come from project config, build arguments, or explicit user choice

For an agent, the correct behavior is:

1. look for an existing project configuration or build variable that defines the XS output location
2. if none exists, ask the user where to place the generated `.xs` file
3. only then write the file

Do not invent a PC-specific absolute path.

## Known Pitfalls / Engine Quirks

- Do not confuse XS with `.per` AI script syntax.
- Prefer the structured function and constant catalogs over prose when they disagree on details.
- Some XS behavior is discussed in raw training material; use it as support, not as the first retrieval stop.
- If a task touches trigger variables or AI bridge behavior, treat it as cross-domain instead of pure XS.
- Example scripts are teaching aids, not the canonical source for exact signatures or constant values.
- Do not hallucinate trigger-variable APIs. Use `xsTriggerVariable(...)` to read and `xsSetTriggerVariable(...)` to write.
- Do not assume plain XS globals are automatically shared with triggers.
- Do not spread `extern int xsVariableN = -1;` declarations across many unrelated feature modules.
- Do not hardcode a machine-specific XS output path when documenting or generating reusable project tooling.

## Cross-Domain Dependencies

- `AI scripts`
  Use for bridge-driven AI <-> XS workflows.
- `scenario triggers`
  Use for script-call and trigger-variable workflows.
- `.dat/genie tooling`
  Use when XS behavior depends on unit classes, task IDs, technologies, or other game data relationships.

