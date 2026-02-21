import unittest
import json
import tempfile
import os
from pathlib import Path

# Import the validator function
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))
from tools.check_manifest import validate_entry


class TestManifestValidation(unittest.TestCase):
    """Tests for manifest schema validation."""
    
    def test_valid_entry(self):
        """Happy path: valid manifest entry passes validation."""
        entry = {
            "dataset_id": "xs_functions",
            "path": "docs/agent_database/xs_functions_catalog.json",
            "record_count": 172,
            "primary_key": "name",
            "notes": "Catalog of XS functions"
        }
        
        base_dir = Path(".")  # Project root
        errors = validate_entry(0, entry, base_dir)
        
        self.assertEqual(errors, [], f"Expected no errors, got: {errors}")
    
    def test_missing_dataset_id(self):
        """Error case: missing dataset_id fails validation."""
        entry = {
            "path": "docs/agent_database/xs_functions_catalog.json",
            "record_count": 172,
            "primary_key": "name",
            "notes": "Catalog"
        }
        
        base_dir = Path("docs/agent_database")
        errors = validate_entry(0, entry, base_dir)
        
        self.assertTrue(len(errors) > 0)
        self.assertTrue(any("dataset_id" in e for e in errors))
    
    def test_missing_record_count(self):
        """Error case: missing record_count fails validation."""
        entry = {
            "dataset_id": "xs_functions",
            "path": "docs/agent_database/xs_functions_catalog.json",
            "primary_key": "name",
            "notes": "Catalog"
        }
        
        base_dir = Path("docs/agent_database")
        errors = validate_entry(0, entry, base_dir)
        
        self.assertTrue(len(errors) > 0)
        self.assertTrue(any("record_count" in e for e in errors))
    
    def test_negative_record_count(self):
        """Error case: negative record_count fails validation."""
        entry = {
            "dataset_id": "xs_functions",
            "path": "docs/agent_database/xs_functions_catalog.json",
            "record_count": -1,
            "primary_key": "name",
            "notes": "Catalog"
        }
        
        base_dir = Path("docs/agent_database")
        errors = validate_entry(0, entry, base_dir)
        
        self.assertTrue(len(errors) > 0)
        self.assertTrue(any("record_count must be >= 0" in e for e in errors))
    
    def test_invalid_record_count_type(self):
        """Error case: non-integer record_count fails validation."""
        entry = {
            "dataset_id": "xs_functions",
            "path": "docs/agent_database/xs_functions_catalog.json",
            "record_count": "172",  # string instead of int
            "primary_key": "name",
            "notes": "Catalog"
        }
        
        base_dir = Path("docs/agent_database")
        errors = validate_entry(0, entry, base_dir)
        
        self.assertTrue(len(errors) > 0)
        self.assertTrue(any("record_count must be an integer" in e for e in errors))
    
    def test_missing_path(self):
        """Error case: missing path fails validation."""
        entry = {
            "dataset_id": "xs_functions",
            "record_count": 172,
            "primary_key": "name",
            "notes": "Catalog"
        }
        
        base_dir = Path("docs/agent_database")
        errors = validate_entry(0, entry, base_dir)
        
        self.assertTrue(len(errors) > 0)
        self.assertTrue(any("path" in e for e in errors))
    
    def test_missing_primary_key(self):
        """Error case: missing primary_key fails validation."""
        entry = {
            "dataset_id": "xs_functions",
            "path": "docs/agent_database/xs_functions_catalog.json",
            "record_count": 172,
            "notes": "Catalog"
        }
        
        base_dir = Path("docs/agent_database")
        errors = validate_entry(0, entry, base_dir)
        
        self.assertTrue(len(errors) > 0)
        self.assertTrue(any("primary_key" in e for e in errors))
    
    def test_missing_notes(self):
        """Error case: missing notes fails validation."""
        entry = {
            "dataset_id": "xs_functions",
            "path": "docs/agent_database/xs_functions_catalog.json",
            "record_count": 172,
            "primary_key": "name"
        }
        
        base_dir = Path("docs/agent_database")
        errors = validate_entry(0, entry, base_dir)
        
        self.assertTrue(len(errors) > 0)
        self.assertTrue(any("notes" in e for e in errors))
    
    def test_file_not_found(self):
        """Error case: non-existent file path fails validation."""
        entry = {
            "dataset_id": "nonexistent_dataset",
            "path": "docs/agent_database/nonexistent_file.json",
            "record_count": 100,
            "primary_key": "id",
            "notes": "This file does not exist"
        }
        
        base_dir = Path("docs/agent_database")
        errors = validate_entry(0, entry, base_dir)
        
        self.assertTrue(len(errors) > 0)
        self.assertTrue(any("not found" in e for e in errors))
    
    def test_xs_datasets_in_manifest(self):
        """Verify XS datasets are present in the manifest."""
        manifest_path = Path(__file__).parent.parent / "docs/agent_database/database_manifest.json"
        
        with open(manifest_path, encoding="utf-8") as f:
            manifest = json.load(f)
        
        dataset_ids = [entry["dataset_id"] for entry in manifest]
        
        self.assertIn("xs_functions", dataset_ids)
        self.assertIn("xs_constants", dataset_ids)
        
        # Verify XS dataset details
        xs_funcs = next(e for e in manifest if e["dataset_id"] == "xs_functions")
        self.assertEqual(xs_funcs["record_count"], 172)
        self.assertEqual(xs_funcs["primary_key"], "name")
        
        xs_consts = next(e for e in manifest if e["dataset_id"] == "xs_constants")
        self.assertEqual(xs_consts["record_count"], 761)
        self.assertEqual(xs_consts["primary_key"], "name")


if __name__ == '__main__':
    unittest.main()
