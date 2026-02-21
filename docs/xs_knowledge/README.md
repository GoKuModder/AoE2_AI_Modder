# XS Knowledge Dataset

This dataset is generated from `XS_Training/` and is designed for deterministic retrieval.

## Artifacts

- `metadata_index.json`
  - deterministic source metadata index
  - source-relative paths and per-document checksums

- `document_store.jsonl`
  - heading-based markdown chunks
  - one JSON object per line, deterministic order

- `retrieval_manifest.json`
  - artifact names, counts, and artifact checksums
  - no volatile timestamp fields

## Build command

```bash
py -3 tools/build_xs_knowledge.py
```

## Determinism contract

For identical `XS_Training/` inputs, the build output keeps stable ordering and identical SHA-256 checksums for:

- `metadata_index.json`
- `document_store.jsonl`
- `retrieval_manifest.json`
