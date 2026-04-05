import unittest

from src.retrieval import GenieDatKnowledgeRetriever, GenieDatRetrievalResult


class TestGenieDatRetrieverImports(unittest.TestCase):
    def test_imports_work(self):
        self.assertTrue(hasattr(GenieDatKnowledgeRetriever, "__init__"))
        result = GenieDatRetrievalResult(
            entry_id="unit_sprite_link_fields",
            title="Unit Sprite Link Fields",
            score=1.0,
            summary="summary",
            payload={},
        )
        self.assertEqual("unit_sprite_link_fields", result.entry_id)


class TestGenieDatRetrieverBehavior(unittest.TestCase):
    def setUp(self):
        self.retriever = GenieDatKnowledgeRetriever()

    def test_exact_standing_sprite_lookup(self):
        results = self.retriever.search("standing_sprite_id1", limit=3)
        self.assertTrue(results)
        self.assertEqual("unit_sprite_link_fields", results[0].entry_id)

    def test_resource_slot_lookup(self):
        results = self.retriever.search(
            "How do custom resource slots work with civ_manager.add_resource?",
            limit=3,
        )
        self.assertTrue(results)
        self.assertEqual("civ_global_resource_slots", results[0].entry_id)

    def test_research_location_lookup(self):
        results = self.retriever.search(
            "How does add_research_location fit into a tech workflow?",
            limit=3,
        )
        self.assertTrue(results)
        self.assertEqual("tech_definition_and_research_location", results[0].entry_id)

    def test_build_context_contains_dat_fields(self):
        context = self.retriever.build_context("particle_effect_name", limit=2)
        self.assertIn("query", context)
        self.assertIn("retrieved", context)
        self.assertLessEqual(len(context["retrieved"]), 2)
        if context["retrieved"]:
            first = context["retrieved"][0]
            self.assertIn("category", first)
            self.assertIn("owners", first)
            self.assertIn("exact_terms", first)
            self.assertIn("how_it_works", first)


if __name__ == "__main__":
    unittest.main()
