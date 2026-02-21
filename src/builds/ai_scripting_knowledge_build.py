from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

from src.knowledge_builders.ai_scripting_builder import (
    build_document_store,
    build_metadata_index,
)
from src.writers.json_writer import write_json, write_jsonl


PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
GUIDE_DIR = PROJECT_ROOT / "AoE2_AI_Scripting_Guide"
TEMPLATE_DIR = GUIDE_DIR / "templates"
OUT_DIR = PROJECT_ROOT / "docs" / "ai_scripting_knowledge"


def _utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _discover_docs() -> list[Path]:
    docs: list[Path] = []

    if GUIDE_DIR.exists():
        docs.extend(sorted(p for p in GUIDE_DIR.glob("*.md") if p.is_file()))
    if TEMPLATE_DIR.exists():
        docs.extend(sorted(p for p in TEMPLATE_DIR.glob("*.per") if p.is_file()))

    return docs


def run_build() -> int:
    allowlist_path = GUIDE_DIR / "06_LLM_COMMAND_ALLOWLIST.md"
    if not allowlist_path.exists():
        print(f"[FAIL] Missing allowlist file: {allowlist_path}")
        return 1

    doc_paths = _discover_docs()
    template_paths = [p for p in doc_paths if p.suffix.lower() == ".per"]

    if not doc_paths:
        print("[FAIL] No guide files discovered. Expected AoE2_AI_Scripting_Guide content.")
        return 1

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    # 1) Metadata index for deterministic lookups and guardrails.
    metadata = build_metadata_index(allowlist_path=allowlist_path, template_paths=template_paths)
    write_json(OUT_DIR / "metadata_index.json", metadata, sort_keys=True)

    # 2) Document store for retrieval context assembly.
    chunks = build_document_store(doc_paths)
    chunk_count = write_jsonl(OUT_DIR / "document_store.jsonl", chunks)

    # 3) Manifest for auditability and future incremental updates.
    manifest = {
        "dataset": "ai_scripting_knowledge",
        "schema_version": 1,
        "generated_at": _utc_now_iso(),
        "sources": {
            "guide_dir": str(GUIDE_DIR).replace("\\", "/"),
            "doc_count": len(doc_paths),
            "template_count": len(template_paths),
        },
        "artifacts": {
            "metadata_index": "metadata_index.json",
            "document_store": "document_store.jsonl",
            "retrieval_manifest": "retrieval_manifest.json",
        },
        "counts": {
            "commands_total": metadata["counts"]["total"],
            "commands_allowed": metadata["counts"]["allowed"],
            "commands_blocked": metadata["counts"]["blocked"],
            "document_chunks": chunk_count,
        },
    }
    write_json(OUT_DIR / "retrieval_manifest.json", manifest, sort_keys=True)

    print("[OK] AI scripting knowledge build complete")
    print(f"  - {OUT_DIR / 'metadata_index.json'}")
    print(f"  - {OUT_DIR / 'document_store.jsonl'}")
    print(f"  - {OUT_DIR / 'retrieval_manifest.json'}")
    return 0


def build_ai_scripting_knowledge() -> int:
    parser = argparse.ArgumentParser(description="Build AI scripting knowledge dataset")
    parser.add_argument("--all", action="store_true", help="Compatibility flag")
    _ = parser.parse_args()
    return run_build()
