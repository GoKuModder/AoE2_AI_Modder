# XS Project Files Guide

Use this guide when the question is not just "how do I write XS syntax?" but "how should the project declare XS variables and produce the XS files?"

## What This Guide Covers

- XS globals versus trigger variables
- `extern` variable declarations
- centralized XS variable registries
- support include files
- final runtime XS assembly
- where the generated `.xs` file should be written

## XS Globals Versus Trigger Variables

- XS globals
  variables that live inside the `.xs` runtime
- trigger variables
  scenario-side shared state read with `xsTriggerVariable(...)` and written with `xsSetTriggerVariable(...)`

Use XS globals for XS-owned state.

Use trigger variables for shared trigger-and-XS state.

## Persistent XS Variables

For scenario-style persistent XS globals, use `extern` declarations in the generated support file or XS variable module.

Typical pattern:

```xs
extern int xsVariable1 = -1;
extern int xsVariable2 = -1;
```

This is the pattern shown in:

- `LordsOfDiplomacy - Easy Mode/xs_scripts.py`
- `GoKu RPG Project/XS_Variables.py`
- `Hide_and_Seek/XS_Variables.py`

## Centralized XS Variable Registry

Do not declare ad hoc XS globals all over the project.

Preferred structure:

1. one XS-variable module owns declaration and mapping
2. semantic meaning is mapped to generated variable names
3. feature systems retrieve variables through helper functions or mappings
4. final XS support content is assembled from that central source

This prevents scattered `xsVariableN` usage with no meaning attached.

## Two Real Project Patterns

### Direct-write pattern

Used in:

- `LordsOfDiplomacy - Easy Mode`
- `GoKu RPG Project`

Flow:

1. write the `extern int xsVariableN = -1;` block to the target `.xs`
2. append helper functions
3. append generated XS functions or templates

### Registry/include pattern

Used in:

- `Hide_and_Seek`

Flow:

1. generate semantic XS variable mappings
2. build a support include file with `extern` declarations and helper functions
3. assemble runtime XS separately
4. join includes and runtime body into the final XS output

This is the cleaner generalized pattern for publishable tooling.

## Where The XS File Should Go

The knowledge base should never teach one machine-specific PC path as the general answer.

Preferred rule:

- if the project already defines the XS output location in config or build code, use that
- otherwise ask the user where the generated `.xs` file should be created

Good generalized guidance:

- keep include filenames relative inside the XS content
- keep final output location configurable
- treat destination path as build configuration, not hardcoded repo truth

## If You Need Exact XS APIs

Open:

- `docs/agent_database/xs_functions_catalog.json`
- `docs/agent_database/xs_constants_catalog.json`

## If You Need Architecture Patterns

Open:

- `docs/agent/references/patterns/trigger_xs_patterns.json`
- `docs/agent/domains/XS_AGENT_GUIDE.md`
