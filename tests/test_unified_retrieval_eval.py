import tempfile
import unittest
from pathlib import Path

from src.eval.unified_retrieval_eval import DEFAULT_GOLDEN_PATH, evaluate_golden, main

DESIGN_GOLDEN_PATH = (
    Path(__file__).resolve().parents[1]
    / "docs"
    / "agent"
    / "references"
    / "recipes"
    / "design_brief_eval.json"
)


class TestUnifiedRetrievalEval(unittest.TestCase):
    def test_default_golden_exists(self):
        self.assertTrue(DEFAULT_GOLDEN_PATH.exists())

    def test_design_golden_exists(self):
        self.assertTrue(DESIGN_GOLDEN_PATH.exists())

    def test_evaluate_golden_passes_repo_thresholds(self):
        result = evaluate_golden()
        self.assertTrue(result["thresholds_passed"])
        self.assertGreaterEqual(result["metrics"]["recall_at_k"], 0.9)
        self.assertGreaterEqual(result["metrics"]["budget_pass_rate"], 1.0)

    def test_design_brief_golden_passes_repo_thresholds(self):
        result = evaluate_golden(golden_path=DESIGN_GOLDEN_PATH)
        self.assertTrue(result["thresholds_passed"])
        self.assertGreaterEqual(result["metrics"]["recall_at_k"], 0.9)
        self.assertGreaterEqual(result["metrics"]["budget_pass_rate"], 1.0)

    def test_main_returns_zero_when_thresholds_pass(self):
        exit_code = main([])
        self.assertEqual(exit_code, 0)

    def test_main_returns_non_zero_when_budget_threshold_is_impossible(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            golden_copy = Path(tmpdir) / "golden.json"
            golden_copy.write_text(DEFAULT_GOLDEN_PATH.read_text(encoding="utf-8"), encoding="utf-8")
            exit_code = main(
                [
                    "--golden",
                    str(golden_copy),
                    "--min-budget-pass-rate",
                    "1.1",
                ]
            )
            self.assertEqual(exit_code, 1)


if __name__ == "__main__":
    unittest.main()
