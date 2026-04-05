# Reference Projects

These are curated external projects that should be treated as high-value pattern references when expanding this knowledge base. They are not the canonical truth for the main repo, but they are trusted examples for real project structure, workflows, and recipes.

## How To Use These References

- Use these projects to mine repeated patterns, recipes, edge cases, and evaluation examples.
- Do not treat them as the first lookup source for normal repo usage.
- Prefer them when you need real, battle-tested examples rather than abstract guidance.
- Convert repeated patterns from them into structured datasets and local docs inside this repo.

## Priority Order

1. `Lords of Diplomacy`
   Primary trigger + XS workflow reference.
2. `RPG GoKu`
   Primary `.dat/genie tooling` workflow reference.
3. `RPG GoKu`
   Secondary mixed-system reference, excluding the `Difficulty` folder.
4. `F13 Dark Hunt`
   Strong XS detail reference, but not the preferred structure model.

## Project Notes

## Lords of Diplomacy

Role:

- primary reference for trigger + XS interaction
- primary reference for hand-authored system structure in scenario work

Use this project for:

- trigger-variable workflows
- XS variable generation patterns
- scenario initialization with AoE2ScenarioParser
- practical trigger + XS system decomposition

Representative signals:

- root `xs_scripts.py`
- root `game_initialization.py`
- `XS_Scripts/`
- `Genie_Dat/`

Why it matters:

- you identified this as the best reference for how triggers work
- it shows a real project that combines triggers, parser usage, and XS in a way you trust

## RPG GoKu (Genie Tooling Project)

Role:

- primary reference for `.dat/genie tooling`
- primary reference for real GenieWorkspace-style data editing workflows

Use this project for:

- workspace load / edit / save flows
- module-per-system data edits
- item, unit, class, and world data modification patterns
- project structure for larger genie-based mods

Representative signals:

- `main/main.py`
- `config/`
- `Classes/`
- `World/`
- `Inventory_System/`
- `Skill_Tree/`
- `Genie_utils_Skill_Tree/`

Why it matters:

- it is your "perfect example" for genie dat tooling
- it shows how real edits are orchestrated instead of discussed abstractly

## RPG GoKu (Mixed Systems Project)

Role:

- secondary reference for mixed trigger / XS systems
- secondary reference for AI-assisted system expansion

Use this project for:

- additional trigger + XS recipes
- validation workflows
- mixed-system folder conventions

Representative signals:

- `XS_Scripts/`
- `Validate_XS/`
- `run_xs_validation.py`
- `World/`
- `Abilities/`

Caveat:

- ignore the `Difficulty` folder when mining patterns from this project

## F13 Dark Hunt

Role:

- detailed XS reference
- useful for generator-based organization and validation flow

Use this project for:

- detailed XS runtime patterns
- generated XS validation flow
- objective / runtime decomposition ideas

Representative signals:

- `PLAN.md`
- `Builder/`
- `Runtime/`
- `Objectives/`
- `run_xs_validation.py`

Caveat:

- this project works well, but its structure is not the preferred readability model for the knowledge base
- mine it for detailed XS patterns, not for the teaching architecture

## What To Extract Next

These projects should feed the next knowledge-base expansions:

- trigger + XS cross-domain recipes
- structured trigger workflow datasets
- `.dat/genie tooling` structured catalogs and edit recipes
- real eval questions based on completed project behavior
