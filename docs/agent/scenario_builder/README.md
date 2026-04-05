# Scenario Builder Docs

This folder exists to answer one practical question:

If an agent is given a map idea or feature brief, which files should it open to actually build the scenario and XS-side systems?

Use this folder when the task is implementation-oriented rather than pure symbol lookup.

## Files

- `WHERE_TO_FIND_THINGS.md`
  Fast topic-to-file index for triggers, conditions, effects, parser managers, XS variables, and XS file generation.
- `TRIGGER_LOOKUP_INDEX.md`
  Clear entrypoints for trigger conditions, effects, attributes, and real-project usage.
- `PARSER_MANAGERS_GUIDE.md`
  How to use `UnitManager` and `MapManager` in real AoE2ScenarioParser projects, backed by your reference projects.
- `XS_PROJECT_FILES_GUIDE.md`
  How to declare XS variables, generate support includes, and decide where the final `.xs` file should go.
- `GENIE_WORKFLOW_GUIDE.md`
  How to use `GenieWorkspace`, asset managers, component linking, and `.dat` save outputs in a real genie project.
- `DAT_LOOKUP_INDEX.md`
  Direct index for `.dat` concepts such as sprite links, particle fields, tech chains, resource slots, and output-path policy.
- `MAP_IDEA_TO_IMPLEMENTATION.md`
  Workflow for turning a map idea document into modular trigger, parser-manager, and XS implementation work.

## Recommended Read Order

1. `WHERE_TO_FIND_THINGS.md`
2. `TRIGGER_LOOKUP_INDEX.md`
3. `PARSER_MANAGERS_GUIDE.md`, `XS_PROJECT_FILES_GUIDE.md`, `GENIE_WORKFLOW_GUIDE.md`, or `DAT_LOOKUP_INDEX.md` depending on the task
4. `MAP_IDEA_TO_IMPLEMENTATION.md` for end-to-end build planning
