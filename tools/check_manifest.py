#!/usr/bin/env python3
"""
Manifest validator - validates database_manifest.json schema and file existence.
"""
import json
import sys
from pathlib import Path


def validate_manifest(manifest_path: str = "docs/agent_database/database_manifest.json") -> int:
    """
    Validate the manifest file structure and referenced files.
    
    Returns:
        0 on success, 1 on validation failure
    """
    errors = []
    manifest_file = Path(manifest_path)
    
    # Check manifest file exists
    if not manifest_file.exists():
        print(f"ERROR: Manifest file not found: {manifest_path}")
        return 1
    
    # Load manifest
    try:
        with open(manifest_file, encoding="utf-8") as f:
            manifest = json.load(f)
    except json.JSONDecodeError as e:
        print(f"ERROR: Invalid JSON in manifest: {e}")
        return 1
    
    # Validate manifest is a list
    if not isinstance(manifest, list):
        print("ERROR: Manifest must be a JSON array")
        return 1
    
    # Validate each entry
    for idx, entry in enumerate(manifest):
        entry_errors = validate_entry(idx, entry, manifest_file.parent)
        errors.extend(entry_errors)
    
    # Report results
    if errors:
        print("MANIFEST VALIDATION FAILED")
        for error in errors:
            print(f"  - {error}")
        return 1
    else:
        print(f"MANIFEST VALIDATION PASSED ({len(manifest)} datasets)")
        return 0


def validate_entry(idx: int, entry: dict, base_dir: Path) -> list[str]:
    """
    Validate a single manifest entry.
    
    Required fields:
        - dataset_id: string
        - path: string
        - record_count: int (must be >= 0)
        - primary_key: string
        - notes: string
    """
    errors = []
    dataset_id = entry.get("dataset_id", f"<entry {idx}>")
    
    # Required string fields
    required_strings = ["dataset_id", "path", "primary_key", "notes"]
    for field in required_strings:
        if field not in entry:
            errors.append(f"[{dataset_id}] Missing required field: {field}")
        elif not isinstance(entry[field], str):
            errors.append(f"[{dataset_id}] Field '{field}' must be a string, got {type(entry[field]).__name__}")
    
    # Validate record_count
    if "record_count" not in entry:
        errors.append(f"[{dataset_id}] Missing required field: record_count")
    elif not isinstance(entry["record_count"], int):
        errors.append(f"[{dataset_id}] record_count must be an integer, got {type(entry['record_count']).__name__}")
    elif entry["record_count"] < 0:
        errors.append(f"[{dataset_id}] record_count must be >= 0, got {entry['record_count']}")
    
    # Validate path exists (if path is present)
    if "path" in entry and isinstance(entry["path"], str):
        file_path = Path(entry["path"])  # Paths are relative to project root
        if not file_path.exists():
            errors.append(f"[{dataset_id}] Referenced file not found: {entry['path']}")
    
    return errors


if __name__ == "__main__":
    sys.exit(validate_manifest())
