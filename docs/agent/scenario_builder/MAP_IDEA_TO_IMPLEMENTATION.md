# Map Idea To Implementation

Use this workflow when the input is a design brief, feature list, or map idea document and the goal is to turn it into implementation work.

This is the closest thing in the repo to an autonomous scenario-build playbook.

## Step 1: Decompose The Idea Into Systems

Split the design brief into:

- world setup
- object placement
- quests
- player progression
- abilities
- event messaging
- AI behavior if any
- XS runtime helpers if any
- data edits if any

Each major mechanic should become a system folder or module boundary.

## Step 2: Decide Which Layer Owns Each Problem

- physical objects and terrain reads
  `UnitManager` / `MapManager`
- state flow, cooldowns, quest stages, event announcements
  triggers
- runtime calculations, bridge logic, arrays, repeated engine-side checks
  XS
- base-game data definitions
  `.dat/genie tooling`

This separation is required if you want an agent to scale beyond one-file scripts.

## Step 3: Build The Registry Layers First

Before implementing feature logic:

- create trigger-variable ownership in `aoe_variables`
- create XS-variable ownership in one XS variable module
- create balance/config ownership in `dictionary.py` or equivalent data files

This is what makes later balancing and large-scale refactors practical.

## Step 4: Build Scenario Content Setup

Use parser-manager modules for:

- unit placement
- map markers
- blockers
- revealers
- shops
- region objects
- cleanup of source-scenario objects

Open:

- `docs/agent/scenario_builder/PARSER_MANAGERS_GUIDE.md`

## Step 5: Build Trigger Systems

For each mechanic:

1. create one system folder
2. create one orchestration module or class
3. create submodules for narrow responsibilities
4. use `apply_` hierarchy so systems can be included or removed cleanly

Open:

- `docs/agent/domains/TRIGGER_AGENT_GUIDE.md`
- `docs/agent/scenario_builder/TRIGGER_LOOKUP_INDEX.md`

## Step 6: Build XS Support

If the feature needs XS:

1. decide which state is XS-owned versus trigger-owned
2. generate or declare persistent `extern` XS variables centrally
3. register helper functions and support include files
4. assemble the final runtime XS
5. use the configured output path or ask the user where to place the generated `.xs`

Open:

- `docs/agent/scenario_builder/XS_PROJECT_FILES_GUIDE.md`
- `docs/agent/domains/XS_AGENT_GUIDE.md`

## Step 7: Use Exact Trigger Knowledge

Once the system structure exists, use the trigger datasets for exact conditions and effects:

- `docs/trigger_knowledge/conditions_knowledge.json`
- `docs/trigger_knowledge/effects_knowledge.json`
- `docs/trigger_knowledge/condition_usage_playbook.md`
- `docs/trigger_knowledge/effect_usage_playbook.md`

## Step 7b: Use Compact Recipes First When They Match

Before opening long prose, check the compact recipe datasets:

- `docs/agent/references/recipes/scenario_recipes.json`
- `docs/agent/references/recipes/parser_manager_patterns.json`
- `docs/agent/references/recipes/genie_recipes.json`

These are the low-token retrieval layer for common implementation requests.

## Step 8: Validate And Iterate

At minimum:

- validate generated XS separately
- review trigger variable ownership
- review whether balance values are isolated in data files
- verify parser-manager setup is separated from gameplay state logic
- verify `.dat` edits are isolated by feature-level `apply_` modules and saved through one explicit workspace output pass

## Current Limitation

This workflow makes the repo much closer to autonomous execution, but it still does not guarantee full one-shot autonomy for every map idea.

The biggest remaining gaps are:

- deeper `.dat/genie tooling` retrieval
- more end-to-end worked examples
- more golden implementation tasks that prove the workflow on full scenario builds
