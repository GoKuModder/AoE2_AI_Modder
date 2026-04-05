import unittest

from src.retrieval.aoe_compact_retriever import (
    AoECompactKnowledgeRetriever,
    CompactRetrievalResult,
)


class TestCompactRetrieverImports(unittest.TestCase):
    def test_imports_work(self):
        self.assertTrue(hasattr(AoECompactKnowledgeRetriever, "__init__"))
        result = CompactRetrievalResult(
            dataset_id="recipes.json",
            entry_id="quest_system_flow",
            title="Quest",
            score=1.0,
            summary="summary",
            payload={},
        )
        self.assertEqual("quest_system_flow", result.entry_id)


class TestCompactRetrieverBehavior(unittest.TestCase):
    def setUp(self):
        self.retriever = AoECompactKnowledgeRetriever()

    def test_detect_domains_for_trigger_recipe(self):
        domains = self.retriever.detect_domains("How do I build a quest system?")
        self.assertIn("scenario_triggers", domains)

    def test_detect_domains_for_genie_recipe(self):
        domains = self.retriever.detect_domains(
            "How do I create a unit with a linked graphic in GenieWorkspace?"
        )
        self.assertIn("dat_genie_tooling", domains)

    def test_search_returns_scenario_recipe(self):
        results = self.retriever.search("How should I structure a multi-stage NPC quest system?")
        ids = {result.entry_id for result in results}
        self.assertIn("quest_system_flow", ids)

    def test_search_prefers_matching_recipe_terms(self):
        results = self.retriever.search("How do I build a teleport system?", limit=3)
        self.assertTrue(results)
        self.assertEqual("teleport_system", results[0].entry_id)

    def test_search_returns_parser_pattern(self):
        results = self.retriever.search("How do I clear existing units from source map regions?")
        ids = {result.entry_id for result in results}
        self.assertIn("unit_manager_cleanup_regions", ids)

    def test_search_returns_genie_recipe(self):
        results = self.retriever.search("How do I link a main unit, dead unit, and graphics?")
        ids = {result.entry_id for result in results}
        self.assertIn("link_main_and_dead_units", ids)

    def test_search_prefers_create_unit_linked_graphic_recipe(self):
        results = self.retriever.search(
            "How do I create a new unit and link it to a custom graphic in GenieWorkspace?",
            limit=3,
        )
        self.assertTrue(results)
        self.assertEqual("create_unit_with_linked_graphic", results[0].entry_id)

    def test_search_prefers_shop_system_recipe(self):
        results = self.retriever.search(
            "How should I structure an NPC shop with item prices and purchase rewards?",
            limit=3,
        )
        self.assertTrue(results)
        self.assertEqual("shop_system_flow", results[0].entry_id)

    def test_search_prefers_upgrade_chain_recipe(self):
        results = self.retriever.search(
            "How do I create an upgraded unit variant chain unlocked by a tech?",
            limit=3,
        )
        self.assertTrue(results)
        self.assertEqual("create_upgrade_variant_chain", results[0].entry_id)

    def test_search_prefers_summon_recipe(self):
        results = self.retriever.search(
            "How should I build a summon system for temporary helper units with cleanup?",
            limit=3,
        )
        self.assertTrue(results)
        self.assertEqual("summon_spawn_system", results[0].entry_id)

    def test_search_prefers_tech_unlock_recipe(self):
        results = self.retriever.search(
            "How do I unlock a unit through a tech effect in the dat workflow?",
            limit=3,
        )
        self.assertTrue(results)
        self.assertEqual("apply_tech_effect_unlock", results[0].entry_id)

    def test_search_prefers_fail_reset_recipe(self):
        results = self.retriever.search(
            "How should I build a checkpoint fail state and reset flow for a boss room?",
            limit=3,
        )
        self.assertTrue(results)
        self.assertEqual("fail_and_reset_flow", results[0].entry_id)

    def test_search_prefers_tech_gated_production_recipe(self):
        results = self.retriever.search(
            "How do I create a tech-gated production chain for a custom trained unit?",
            limit=3,
        )
        self.assertTrue(results)
        self.assertEqual("tech_gated_production_chain", results[0].entry_id)

    def test_build_context_is_compact(self):
        context = self.retriever.build_context(
            "How do I build a teleport system?", limit=3
        )
        self.assertIn("query", context)
        self.assertIn("domains_detected", context)
        self.assertIn("retrieved", context)
        self.assertLessEqual(len(context["retrieved"]), 3)
        if context["retrieved"]:
            first = context["retrieved"][0]
            self.assertIn("steps", first)
            self.assertIn("best_files", first)
            self.assertIn("pitfalls", first)


if __name__ == "__main__":
    unittest.main()
