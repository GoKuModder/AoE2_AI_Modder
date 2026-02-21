# AI Scripting Knowledge Dataset

This dataset is generated from `AoE2_AI_Scripting_Guide/` and is designed for LLM retrieval.

## Artifacts

- `metadata_index.json`
  - deterministic command lookup
  - allowed/blocked status
  - command descriptions and template snippets

- `document_store.jsonl`
  - chunked guide content for context retrieval
  - one JSON object per line

- `retrieval_manifest.json`
  - build metadata (counts, source paths, generated timestamp)

## Build command

```bash
py tools/build_ai_scripting_knowledge.py
```

## Retrieval and validation entry points

- `src/retrieval/ai_script_retriever.py`
- `src/retrieval/ai_script_validator.py`
