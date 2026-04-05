import unittest

from src.retrieval import AoEUnifiedKnowledgeRetriever, UnifiedRetrievalResult


class TestUnifiedRetrieverImports(unittest.TestCase):
    def test_imports_work(self):
        self.assertTrue(hasattr(AoEUnifiedKnowledgeRetriever, "__init__"))
        result = UnifiedRetrievalResult(
            dataset_id="xs_functions_catalog.json",
            entry_id="xsTriggerVariable",
            title="xsTriggerVariable",
            score=1.0,
            domain="xs",
            source_kind="exact_lookup",
            summary="Reads a trigger variable.",
            payload={},
        )
        self.assertEqual("xs", result.domain)


class TestUnifiedRetrieverBehavior(unittest.TestCase):
    def setUp(self):
        self.retriever = AoEUnifiedKnowledgeRetriever()

    def test_feature_query_returns_compact_recipe(self):
        results = self.retriever.search("How do I build a teleport system?", limit=5)
        self.assertTrue(results)
        first = results[0]
        self.assertEqual("compact_recipe", first.source_kind)
        self.assertEqual("teleport_system", first.entry_id)

    def test_exact_xs_function_lookup(self):
        results = self.retriever.search("xsTriggerVariable", limit=5)
        ids = {(result.dataset_id, result.entry_id) for result in results}
        self.assertIn(("xs_functions_catalog.json", "xsTriggerVariable"), ids)

    def test_trigger_effect_lookup_prefers_trigger_domain(self):
        results = self.retriever.search("display_timer", limit=6)
        self.assertTrue(
            any(
                result.entry_id == "display_timer" and result.domain == "scenario_triggers"
                for result in results
            )
        )

    def test_parser_manager_query_returns_pattern(self):
        results = self.retriever.search(
            "How do I use UnitManager to clear units from a region?", limit=5
        )
        self.assertTrue(
            any(result.entry_id == "unit_manager_cleanup_regions" for result in results)
        )

    def test_shop_query_returns_shop_recipe(self):
        results = self.retriever.search(
            "How should I structure an NPC shop with item prices and purchase rewards?",
            limit=5,
        )
        self.assertTrue(any(result.entry_id == "shop_system_flow" for result in results))

    def test_boss_query_returns_boss_recipe(self):
        results = self.retriever.search(
            "How should I build a staged boss encounter with phase transitions and rewards?",
            limit=5,
        )
        self.assertTrue(any(result.entry_id == "boss_encounter_flow" for result in results))

    def test_summon_query_returns_summon_recipe(self):
        results = self.retriever.search(
            "How should I build a summon system for temporary helper units with cleanup?",
            limit=5,
        )
        self.assertTrue(any(result.entry_id == "summon_spawn_system" for result in results))

    def test_tech_unlock_query_returns_tech_recipe(self):
        results = self.retriever.search(
            "How do I unlock a unit through a tech effect in the dat workflow?",
            limit=5,
        )
        self.assertTrue(any(result.entry_id == "apply_tech_effect_unlock" for result in results))

    def test_fail_reset_query_returns_reset_recipe(self):
        results = self.retriever.search(
            "How should I build a checkpoint fail state and reset flow for a boss room?",
            limit=5,
        )
        self.assertTrue(any(result.entry_id == "fail_and_reset_flow" for result in results))

    def test_tech_gated_production_query_returns_recipe(self):
        results = self.retriever.search(
            "How do I create a tech-gated production chain for a custom trained unit?",
            limit=5,
        )
        self.assertTrue(any(result.entry_id == "tech_gated_production_chain" for result in results))

    def test_exact_dat_field_lookup_prefers_dat_domain(self):
        results = self.retriever.search("standing_sprite_id1", limit=5)
        self.assertTrue(
            any(
                result.entry_id == "unit_sprite_link_fields"
                and result.domain == "dat_genie_tooling"
                for result in results
            )
        )

    def test_bundle_query_returns_multiple_compact_recipes(self):
        context = self.retriever.build_context(
            "Design a boss dungeon map idea with staged boss phases, checkpoint resets, reward tables, and boss reward payout.",
            limit=4,
        )
        ids = {row["entry_id"] for row in context["retrieved"]}
        self.assertIn("boss_encounter_flow", ids)
        self.assertIn("fail_and_reset_flow", ids)
        self.assertIn("reward_table_resolution", ids)
        self.assertIn("boss_reward_distribution", ids)

    def test_build_context_contains_small_unified_fields(self):
        context = self.retriever.build_context("What does xsTriggerVariable do?", limit=4)
        self.assertIn("domains_detected", context)
        self.assertIn("retrieved", context)
        self.assertLessEqual(len(context["retrieved"]), 4)
        if context["retrieved"]:
            first = context["retrieved"][0]
            self.assertIn("source_kind", first)
            self.assertIn("domain", first)
            self.assertIn("exact_symbols", first)
            self.assertIn("signature", first)


if __name__ == "__main__":
    unittest.main()
