import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.check_boundaries import check_boundaries


class TestBoundaries(unittest.TestCase):
    def setUp(self):
        self.contract_path = ROOT / "docs" / "architecture" / "ai_xs_boundary.json"

    def test_legal_fixture_has_no_violations(self):
        fixture_root = ROOT / "tests" / "fixtures" / "boundaries" / "legal"
        violations = check_boundaries(
            root=fixture_root,
            contract_path=self.contract_path,
            scan_paths=["src"],
        )
        self.assertEqual([], violations)

    def test_illegal_fixture_reports_violation(self):
        fixture_root = ROOT / "tests" / "fixtures" / "boundaries" / "illegal"
        violations = check_boundaries(
            root=fixture_root,
            contract_path=self.contract_path,
            scan_paths=["src"],
        )
        self.assertGreater(len(violations), 0)
        self.assertEqual("src/retrieval/illegal_ai_module.py", violations[0]["path"])
        self.assertEqual("no_direct_ai_to_xs_import", violations[0]["rule"])
        self.assertEqual("src.integration.illegal_xs_module", violations[0]["import"])


if __name__ == "__main__":
    unittest.main()
