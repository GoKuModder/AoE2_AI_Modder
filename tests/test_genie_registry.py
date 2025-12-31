import unittest
from src.knowledge_builders.genie_registry_builder import build_genie_registry

class TestGenieRegistry(unittest.TestCase):
    def test_build_registry_merging(self):
        """
        Verify merging and priority logic.
        """
        datasets = {
            "heroes": {100: "Hero Unit"},
            "units": {100: "Regular Unit", 200: "Soldier"},
            "buildings": {300: "House", 200: "Barracks"}, # Conflict ID 200 with unit (unlikely but possible test case)
            "other": {400: "Tree"}
        }
        
        registry = build_genie_registry(datasets)
        # Should have 100, 200, 300, 400
        self.assertEqual(len(registry), 4)
        
        # ID 100: Hero vs Unit -> Hero Name wins
        r100 = next(r for r in registry if r["genie_id"] == 100)
        self.assertEqual(r100["name"], "Hero Unit")
        self.assertIn("heroes", r100["sources"])
        self.assertIn("units", r100["sources"])
        self.assertTrue(r100["facets"]["is_hero"])
        self.assertTrue(r100["facets"]["is_unit_dataset"])
        self.assertTrue(r100["facets"]["is_movable"]) # Hero -> True
        self.assertIn("Name conflict", r100["issues"][0])
        self.assertIn("Regular Unit", r100["aliases"])
        
        # ID 200: Unit vs Building -> Unit Name wins (Units > Buildings)
        # Movable? Unit says True, Building says False.
        # Heuristic: if is_building -> False.
        r200 = next(r for r in registry if r["genie_id"] == 200)
        self.assertEqual(r200["name"], "Soldier")
        self.assertTrue(r200["facets"]["is_unit_dataset"])
        self.assertTrue(r200["facets"]["is_building"])
        self.assertFalse(r200["facets"]["is_movable"]) # Building overrides unit movability in our heuristic?
        # Checked code: if is_building: is_movable = False. So yes.
        
        # ID 300: Building
        r300 = next(r for r in registry if r["genie_id"] == 300)
        self.assertEqual(r300["name"], "House")
        self.assertFalse(r300["facets"]["is_movable"])
        
        # ID 400: Other
        r400 = next(r for r in registry if r["genie_id"] == 400)
        self.assertEqual(r400["name"], "Tree")
        self.assertFalse(r400["facets"]["is_movable"])

if __name__ == '__main__':
    unittest.main()
