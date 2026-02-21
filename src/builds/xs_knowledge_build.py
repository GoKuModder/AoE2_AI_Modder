from __future__ import annotations

import argparse
import hashlib
from pathlib import Path
from typing import Any

from src.knowledge_builders.xs_builder import (
    build_chunk_store,
    build_metadata_index,
    collect_source_documents,
    parse_source_page_index,
)
from src.writers.json_writer import write_json, write_jsonl


PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
DEFAULT_SOURCE_ROOT = PROJECT_ROOT / "XS_Training"
DEFAULT_OUT_DIR = PROJECT_ROOT / "docs" / "xs_knowledge"


def _sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run_build(*, source_root: Path = DEFAULT_SOURCE_ROOT, out_dir: Path = DEFAULT_OUT_DIR) -> int:
    if not source_root.exists() or not source_root.is_dir():
        print(f"[FAIL] Missing XS source directory: {source_root}")
        return 1

    source_index_path = source_root / "SOURCE_PAGE_INDEX.md"
    if not source_index_path.exists() or not source_index_path.is_file():
        print(f"[FAIL] Missing SOURCE_PAGE_INDEX.md: {source_index_path}")
        return 1

    index_entries = parse_source_page_index(source_index_path)
    documents = collect_source_documents(source_root, index_entries)
    if not documents:
        print("[FAIL] No XS markdown source documents were discovered from SOURCE_PAGE_INDEX.md")
        return 1

    out_dir.mkdir(parents=True, exist_ok=True)

    metadata = build_metadata_index(documents)
    chunks = build_chunk_store(documents)

    metadata_path = out_dir / "metadata_index.json"
    chunk_store_path = out_dir / "document_store.jsonl"
    manifest_path = out_dir / "retrieval_manifest.json"

    write_json(metadata_path, metadata, sort_keys=True)
    chunk_count = write_jsonl(chunk_store_path, chunks)

    manifest: dict[str, Any] = {
        "dataset": "xs_knowledge",
        "schema_version": 1,
        "sources": {
            "source_root": str(source_root).replace("\\", "/"),
            "source_index": str(source_index_path).replace("\\", "/"),
        },
        "artifacts": {
            "metadata_index": "metadata_index.json",
            "document_store": "document_store.jsonl",
            "retrieval_manifest": "retrieval_manifest.json",
        },
        "counts": {
            "source_documents": metadata["counts"]["source_documents"],
            "chunks_total": chunk_count,
        },
        "checksums": {
            "metadata_index_sha256": _sha256_file(metadata_path),
            "chunk_store_sha256": _sha256_file(chunk_store_path),
        },
    }
    write_json(manifest_path, manifest, sort_keys=True)

    print("[OK] XS knowledge build complete")
    print(f"  - {metadata_path}")
    print(f"  - {chunk_store_path}")
    print(f"  - {manifest_path}")
    return 0


def build_xs_knowledge() -> int:
    parser = argparse.ArgumentParser(description="Build XS knowledge dataset")
    parser.add_argument("--all", action="store_true", help="Compatibility flag")
    _ = parser.parse_args()
    return run_build()
