import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from src.builds.xs_knowledge_build import run_build
from src.knowledge_builders.xs_builder import (
    _chunk_markdown,
    build_chunk_store,
    build_metadata_index,
    collect_source_documents,
    parse_source_page_index,
)


def _sha256_text(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class TestXsKnowledgeBuild(unittest.TestCase):
    def test_run_build_fails_for_missing_source_root(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            missing_source = tmp_path / "missing_xs_training"
            out_dir = tmp_path / "out"

            status = run_build(source_root=missing_source, out_dir=out_dir)

            self.assertEqual(status, 1)
            self.assertFalse(out_dir.exists())

    def test_run_build_is_deterministic_for_same_input(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            source_root = tmp_path / "XS_Training"
            source_root.mkdir(parents=True, exist_ok=True)

            source_index = source_root / "SOURCE_PAGE_INDEX.md"
            page_a = source_root / "ugc.aoe2.rocks" / "general" / "xs" / "index.md"
            page_b = source_root / "github.com" / "Divy1211" / "AoE2DE_UGC_Guide" / "docs" / "general" / "xs" / "functions.md"
            page_a.parent.mkdir(parents=True, exist_ok=True)
            page_b.parent.mkdir(parents=True, exist_ok=True)
            page_a.write_text("# XS Index\n\nIntro paragraph.\n", encoding="utf-8")
            page_b.write_text("# Functions\n\n## xsFoo\nDetails.\n", encoding="utf-8")
            source_index.write_text(
                "\n".join(
                    [
                        "# XS Training Source Index",
                        "",
                        "- `ugc.aoe2.rocks/general/xs/index.md` <- https://ugc.aoe2.rocks/general/xs/",
                        "- `github.com/Divy1211/AoE2DE_UGC_Guide/docs/general/xs/functions.md` <- https://github.com/Divy1211/AoE2DE_UGC_Guide/blob/HEAD/docs/general/xs/functions.md",
                        "",
                    ]
                ),
                encoding="utf-8",
            )

            out_1 = tmp_path / "build_one"
            out_2 = tmp_path / "build_two"

            status_1 = run_build(source_root=source_root, out_dir=out_1)
            status_2 = run_build(source_root=source_root, out_dir=out_2)

            self.assertEqual(status_1, 0)
            self.assertEqual(status_2, 0)

            artifacts = ["metadata_index.json", "document_store.jsonl", "retrieval_manifest.json"]
            for artifact in artifacts:
                self.assertTrue((out_1 / artifact).exists())
                self.assertTrue((out_2 / artifact).exists())
                self.assertEqual(_sha256_text(out_1 / artifact), _sha256_text(out_2 / artifact))

            manifest = json.loads((out_1 / "retrieval_manifest.json").read_text(encoding="utf-8"))
            self.assertEqual(manifest["dataset"], "xs_knowledge")
            self.assertEqual(manifest["counts"]["source_documents"], 2)
            self.assertEqual(manifest["counts"]["chunks_total"], 3)
            self.assertEqual(
                manifest["checksums"]["chunk_store_sha256"],
                _sha256_text(out_1 / "document_store.jsonl"),
            )


class TestParseSourcePageIndex(unittest.TestCase):
    """Unit tests for parse_source_page_index function."""

    def test_parses_valid_index_with_single_entry(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            idx = Path(tmp) / "index.md"
            idx.write_text(
                "- `path/to/doc.md` <- https://example.com/doc\n", encoding="utf-8"
            )

            result = parse_source_page_index(idx)

            self.assertEqual(len(result), 1)
            self.assertEqual(result[0]["relative_path"], "path/to/doc.md")
            self.assertEqual(result[0]["source_url"], "https://example.com/doc")

    def test_parses_multiple_entries_sorted_by_path(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            idx = Path(tmp) / "index.md"
            idx.write_text(
                "- `z_file.md` <- https://z.com\n"
                "- `a_file.md` <- https://a.com\n"
                "- `m_file.md` <- https://m.com\n",
                encoding="utf-8",
            )

            result = parse_source_page_index(idx)

            self.assertEqual(len(result), 3)
            # Should be sorted alphabetically by relative_path
            self.assertEqual(result[0]["relative_path"], "a_file.md")
            self.assertEqual(result[1]["relative_path"], "m_file.md")
            self.assertEqual(result[2]["relative_path"], "z_file.md")

    def test_deduplicates_duplicate_paths(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            idx = Path(tmp) / "index.md"
            idx.write_text(
                "- `doc.md` <- https://first.com\n"
                "- `doc.md` <- https://second.com\n",
                encoding="utf-8",
            )

            result = parse_source_page_index(idx)

            # Should have only one entry (deduped)
            self.assertEqual(len(result), 1)
            self.assertEqual(result[0]["relative_path"], "doc.md")

    def test_ignores_lines_without_backtick_format(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            idx = Path(tmp) / "index.md"
            idx.write_text(
                "# Source Index\n"
                "\n"
                "Some description text.\n"
                "\n"
                "- `valid.md` <- https://example.com\n",
                encoding="utf-8",
            )

            result = parse_source_page_index(idx)

            self.assertEqual(len(result), 1)
            self.assertEqual(result[0]["relative_path"], "valid.md")

    def test_handles_windows_backslash_in_path(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            idx = Path(tmp) / "index.md"
            idx.write_text(
                "- `path\\\\to\\\\doc.md` <- https://example.com\n", encoding="utf-8"
            )

            result = parse_source_page_index(idx)

            self.assertEqual(len(result), 1)
            # replace("\\", "/") replaces EACH backslash, so path\\to\\doc.md -> path//to//doc.md
            self.assertEqual(result[0]["relative_path"], "path//to//doc.md")


class TestCollectSourceDocuments(unittest.TestCase):
    """Unit tests for collect_source_documents function."""

    def test_collects_existing_markdown_files(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "source"
            root.mkdir(parents=True, exist_ok=True)

            # Create markdown file
            doc = root / "doc.md"
            doc.write_text("# Test Document\n\nContent here.", encoding="utf-8")

            index_entries = [{"relative_path": "doc.md", "source_url": "https://ex.com"}]

            docs = collect_source_documents(root, index_entries)

            self.assertEqual(len(docs), 1)
            self.assertEqual(docs[0]["relative_path"], "doc.md")
            self.assertEqual(docs[0]["source_url"], "https://ex.com")
            self.assertIn("sha256", docs[0])
            self.assertIn("text", docs[0])

    def test_skips_non_markdown_files(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "source"
            root.mkdir(parents=True, exist_ok=True)

            txt_file = root / "doc.txt"
            txt_file.write_text("Not markdown", encoding="utf-8")

            index_entries = [{"relative_path": "doc.txt", "source_url": "https://ex.com"}]

            docs = collect_source_documents(root, index_entries)

            # Should skip .txt file
            self.assertEqual(len(docs), 0)

    def test_skips_missing_files(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "source"
            root.mkdir(parents=True, exist_ok=True)

            index_entries = [{"relative_path": "missing.md", "source_url": "https://ex.com"}]

            docs = collect_source_documents(root, index_entries)

            self.assertEqual(len(docs), 0)

    def test_sorts_by_relative_path(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "source"
            root.mkdir(parents=True, exist_ok=True)

            (root / "z.md").write_text("# Z", encoding="utf-8")
            (root / "a.md").write_text("# A", encoding="utf-8")

            index_entries = [
                {"relative_path": "z.md", "source_url": "https://z.com"},
                {"relative_path": "a.md", "source_url": "https://a.com"},
            ]

            docs = collect_source_documents(root, index_entries)

            # Should be sorted alphabetically
            self.assertEqual(docs[0]["relative_path"], "a.md")
            self.assertEqual(docs[1]["relative_path"], "z.md")


class TestBuildMetadataIndex(unittest.TestCase):
    """Unit tests for build_metadata_index function."""

    def test_builds_correct_schema(self) -> None:
        documents = [
            {
                "relative_path": "doc1.md",
                "source_url": "https://ex.com/1",
                "sha256": "abc123",
                "text": "content",
            },
            {
                "relative_path": "doc2.md",
                "source_url": "https://ex.com/2",
                "sha256": "def456",
                "text": "more content",
            },
        ]

        result = build_metadata_index(documents)

        self.assertEqual(result["schema_version"], 1)
        self.assertEqual(result["dataset"], "xs_knowledge")
        self.assertEqual(result["counts"]["source_documents"], 2)
        self.assertEqual(len(result["documents"]), 2)

    def test_document_ids_are_prefixed(self) -> None:
        documents = [
            {
                "relative_path": "test.md",
                "source_url": "https://ex.com",
                "sha256": "hash123",
                "text": "content",
            }
        ]

        result = build_metadata_index(documents)

        self.assertTrue(result["documents"][0]["id"].startswith("doc::"))


class TestBuildChunkStore(unittest.TestCase):
    """Unit tests for build_chunk_store and _chunk_markdown functions."""

    def test_chunks_markdown_by_headings(self) -> None:
        documents = [
            {
                "relative_path": "test.md",
                "source_url": "https://ex.com",
                "sha256": "abc123",
                "text": "# Title\n\nIntro.\n\n## Section A\n\nContent A.\n\n## Section B\n\nContent B.",
            }
        ]

        chunks = build_chunk_store(documents)

        # Should have chunks for: Title, Section A, Section B
        self.assertGreaterEqual(len(chunks), 3)
        titles = [c["title"] for c in chunks]
        self.assertIn("Title", titles)
        self.assertIn("Section A", titles)
        self.assertIn("Section B", titles)

    def test_chunk_ids_include_source_and_index(self) -> None:
        documents = [
            {
                "relative_path": "test.md",
                "source_url": "https://ex.com",
                "sha256": "abc123",
                "text": "# Title\n\nContent.",
            }
        ]

        chunks = build_chunk_store(documents)

        # Chunk ID should reference source file
        self.assertTrue(chunks[0]["id"].startswith("test.md::"))

    def test_empty_document_produces_no_chunks(self) -> None:
        documents = [
            {
                "relative_path": "empty.md",
                "source_url": "https://ex.com",
                "sha256": "abc123",
                "text": "",
            }
        ]

        chunks = build_chunk_store(documents)

        # Empty text should produce no chunks
        self.assertEqual(len(chunks), 0)

    def test_document_without_headings_has_single_chunk(self) -> None:
        documents = [
            {
                "relative_path": "plain.md",
                "source_url": "https://ex.com",
                "sha256": "abc123",
                "text": "Just plain text without any headings.",
            }
        ]

        chunks = build_chunk_store(documents)

        # Should have single chunk with default title
        self.assertEqual(len(chunks), 1)
        self.assertEqual(chunks[0]["title"], "document")


if __name__ == "__main__":
    unittest.main()
