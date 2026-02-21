# Gemini Task Queue

Use this file as the queue that Gemini reads via `GEMINI.md`.

## Queue Rules
1. Put new requests in `Pending`.
2. Move exactly one task to `In Progress` while being worked.
3. Move finished tasks to `Done` with changed files and validation notes.

## Pending
### T-001 (Template)
- Status: pending
- Goal: _Describe the task clearly._
- Scope: _Allowed paths to edit._
- Constraints: _Any hard rules (single-file edit, no refactor, etc.)._
- Validation: _How to verify success (command/output)._

## In Progress
- None

## Done
### T-101 - Build Database Manifest JSON
- Status: done
- Goal: Create a single machine-readable manifest for core knowledge datasets used by AI agents.
- Scope: created `docs/agent_database/database_manifest.json`.
- Validation:
  - JSON parses cleanly.
  - Record counts match source datasets.
  - Counts: trigger_attributes: 147, trigger_effects: 102, genie_objects: 1282, ai_metadata: 62.

### T-102 - Build XS Functions Catalog JSON
- Status: done
- Goal: Flatten XS function reference into one agent-friendly JSON catalog.
- Scope: created `docs/agent_database/xs_functions_catalog.json`.
- Validation:
  - JSON parses cleanly.
  - Total output rows: 172 (matches source entries across all categories).

### T-103 - Build XS Constants Catalog JSON
- Status: done
- Goal: Flatten XS constants reference into one agent-friendly JSON catalog.
- Scope: created `docs/agent_database/xs_constants_catalog.json`.
- Validation:
  - JSON parses cleanly.
  - Total output rows: 761 (matches source entries across all categories).

### T-104 - Build Agent Query Map JSON
- Status: done
- Goal: Create a small routing map that tells an AI agent which dataset to query for common intents.
- Scope: created `docs/agent_database/agent_query_map.json`.
- Validation:
  - JSON parses cleanly.
  - Paths point to existing files.
