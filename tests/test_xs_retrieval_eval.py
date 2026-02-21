import json
import tempfile
import unittest
from pathlib import Path

from src.eval.xs_retrieval_eval import evaluate_golden, main


def _write_json(path: Path, payload: object) -> None:
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


class TestXSRetrievalEval(unittest.TestCase):
    def _create_dataset(self, root: Path) -> Path:
        dataset_dir = root / "dataset"
        dataset_dir.mkdir(parents=True, exist_ok=True)

        metadata = {
            "commands": [
                {
                    "command": "xssetrulepriority",
                    "source_file": "functions.md",
                    "description": "Set rule priority.",
                    "examples": [
                        {
                            "template": "functions.md",
                            "snippet": "xsSetRulePriority(\"rush\", 50);",
                        }
                    ],
                }
            ]
        }
        chunks = [
            {
                "source_file": "constants.md",
                "title": "XS constants",
                "text": "cDarkAge maps to value 0 and cImperialAge maps to 3.",
            }
        ]

        _write_json(dataset_dir / "metadata_index.json", metadata)
        (dataset_dir / "document_store.jsonl").write_text(
            "\n".join(json.dumps(row) for row in chunks) + "\n",
            encoding="utf-8",
        )
        return dataset_dir

    def _create_golden(self, root: Path) -> Path:
        golden = {
            "cases": [
                {
                    "id": "function-answerable",
                    "query": "xsSetRulePriority",
                    "expected_any": ["xssetrulepriority"],
                    "kind": "answerable",
                },
                {
                    "id": "constant-answerable",
                    "query": "cDarkAge",
                    "expected_any": ["cdarkage"],
                    "kind": "answerable",
                },
                {
                    "id": "negative-miss",
                    "query": "zzzz_unmapped_token",
                    "kind": "miss",
                },
            ]
        }

        golden_path = root / "golden.json"
        _write_json(golden_path, golden)
        return golden_path

    def test_evaluate_golden_computes_metrics(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp_path = Path(tmpdir)
            dataset_dir = self._create_dataset(tmp_path)
            golden_path = self._create_golden(tmp_path)

            result = evaluate_golden(
                dataset_dir=dataset_dir,
                golden_path=golden_path,
                k=5,
                min_recall=0.5,
                min_mrr=0.5,
            )

            self.assertAlmostEqual(result["metrics"]["recall_at_k"], 1.0)
            self.assertAlmostEqual(result["metrics"]["mrr"], 1.0)
            self.assertEqual(result["metrics"]["miss_pass_rate"], 1.0)
            self.assertTrue(result["thresholds_passed"])

    def test_evaluate_golden_thresholds_fail_when_single_metric_misses(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp_path = Path(tmpdir)
            dataset_dir = self._create_dataset(tmp_path)
            golden_path = self._create_golden(tmp_path)

            result = evaluate_golden(
                dataset_dir=dataset_dir,
                golden_path=golden_path,
                k=5,
                min_recall=1.0,
                min_mrr=1.1,
            )

            self.assertAlmostEqual(result["metrics"]["recall_at_k"], 1.0)
            self.assertAlmostEqual(result["metrics"]["mrr"], 1.0)
            self.assertFalse(result["thresholds_passed"])

    def test_main_returns_zero_when_metrics_equal_thresholds(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp_path = Path(tmpdir)
            dataset_dir = self._create_dataset(tmp_path)
            golden_path = self._create_golden(tmp_path)

            exit_code = main(
                [
                    "--dataset-dir",
                    str(dataset_dir),
                    "--golden",
                    str(golden_path),
                    "--k",
                    "5",
                    "--min-recall",
                    "1.0",
                    "--min-mrr",
                    "1.0",
                ]
            )

            self.assertEqual(exit_code, 0)

    def test_main_returns_non_zero_when_thresholds_fail(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp_path = Path(tmpdir)
            dataset_dir = self._create_dataset(tmp_path)
            golden_path = self._create_golden(tmp_path)

            exit_code = main(
                [
                    "--dataset-dir",
                    str(dataset_dir),
                    "--golden",
                    str(golden_path),
                    "--k",
                    "5",
                    "--min-recall",
                    "1.1",
                    "--min-mrr",
                    "1.1",
                ]
            )

            self.assertEqual(exit_code, 1)

    def test_main_returns_zero_when_thresholds_pass(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp_path = Path(tmpdir)
            dataset_dir = self._create_dataset(tmp_path)
            golden_path = self._create_golden(tmp_path)

            exit_code = main(
                [
                    "--dataset-dir",
                    str(dataset_dir),
                    "--golden",
                    str(golden_path),
                    "--k",
                    "5",
                    "--min-recall",
                    "0.8",
                    "--min-mrr",
                    "0.8",
                ]
            )

            self.assertEqual(exit_code, 0)


if __name__ == "__main__":
    unittest.main()
