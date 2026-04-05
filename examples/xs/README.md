# XS Examples

These are curated XS examples kept for teaching and demonstration.

Use them after consulting the canonical XS datasets:

- `docs/agent_database/xs_functions_catalog.json`
- `docs/agent_database/xs_constants_catalog.json`
- `docs/xs_knowledge/document_store.jsonl`

## Examples

- `codex_teleport_barracks.xs`
  Teleports a unit across a barracks when it activates from the left side.
- `codex_magic_following_spell.xs`
  Spawns and configures units around a source unit, demonstrating creation, position logic, and attribute mutation.
- `gemini_teleport_barracks.xs`
  Alternate teleport implementation kept as a comparison example.
- `xs_arrays_full_project_demo.xs`
  Demonstrates array-driven project structure for hero-slot and state-sync style workflows.
- `xs_array_injection_demo_generated.xs`
  Generated example showing injector output for array setup and retrieval.
- `XS_ARRAYS_PROJECT_GUIDE.md`
  Companion guide that explains the array-driven demo and the intended project pattern.

## Usage Rules

- Treat these files as worked examples, not canonical truth for function signatures.
- Prefer the structured XS catalogs for exact names, signatures, and constants.
- Use the examples to show organization, guard patterns, loops, and mechanic-specific structure.
