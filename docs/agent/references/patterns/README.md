# Reference Pattern Datasets

These datasets turn trusted external project patterns into structured retrieval assets inside this repository.

Use them when the question is about architecture, workflow, modularity, balancing layout, variable registries, or genie-editing structure rather than exact engine symbols.

The trigger-plus-XS pattern dataset also stores how to:

- declare persistent `extern` XS variables centrally
- keep semantic mappings for generated `xsVariableN` slots
- assemble support include files and runtime XS in phases
- decide where the final generated `.xs` file should be written without hardcoding one local PC path

## Datasets

- `trigger_xs_patterns.json`
  Architecture and workflow patterns for trigger-heavy projects that also use XS.
- `genie_workflow_patterns.json`
  Architecture and workflow patterns for `.dat/genie tooling` projects.
- `reference_patterns_eval.json`
  Golden architecture queries that should map cleanly onto the pattern datasets.

## How To Use Them

- Open these datasets after the domain guide when the task is architectural.
- Use them to answer "how should I organize this" and "what pattern should I use" questions.
- Treat them as normalized pattern summaries derived from trusted reference projects, not as raw project dumps.
- Use `reference_patterns_eval.json` to keep future retrieval work grounded in real architecture questions.
