import unittest
from src.knowledge_builders.attributes_builder import build_attributes_knowledge

# Sample UGC HTML excerpt for testing
SAMPLE_UGC_HTML = """
<h2>0. Hit Points</h2>
<p>Hit points description...</p>
<h2>1. Line of Sight</h2>
<p>LoS description...</p>
<h2>2. Garrison Capacity</h2>
<p>Garcap...</p>
<h2>5. Movement Speed</h2>
<p>Speed...</p>
<h2>12. Maximum Range</h2>
<p>Range...</p>
<h2>13. Work Rate</h2>
<p>Work...</p>
<h2>14. Carry Capacity</h2>
<p>Carry...</p>
<h2>112. Train Location</h2>
<p>Train Loc...</p>
<h2>113. Train Button</h2>
<p>Train Btn...</p>
<h2>192. Available Unit Flag</h2>
<p>Avail...</p>
<h2>193. Disabled Unit Flag</h2>
<p>Disabled...</p>
"""

# Sample Enum Mapping
SAMPLE_ENUMS = {
    0: "HIT_POINTS",
    1: "LINE_OF_SIGHT",
    2: "GARRISON_CAPACITY",
    5: "MOVEMENT_SPEED",
    12: "MAXIMUM_RANGE",
    13: "WORK_RATE",
    14: "CARRY_CAPACITY",
    112: "TRAIN_LOCATION",
    113: "TRAIN_BUTTON",
    192: "AVAILABLE_UNIT_FLAG",
    193: "DISABLED_UNIT_FLAG",
}

class TestKnowledgeIntegration(unittest.TestCase):
    def test_attributes_builder_mapping(self):
        """
        Verifies that the builder correctly merges UGC data with Parser Enums.
        """
        # Run the builder with our fixtures
        result = build_attributes_knowledge(SAMPLE_UGC_HTML, SAMPLE_ENUMS)
        
        # Check specific mappings requested
        expected_mappings = {
            0: "HIT_POINTS",
            1: "LINE_OF_SIGHT",
            2: "GARRISON_CAPACITY",
            5: "MOVEMENT_SPEED",
            12: "MAXIMUM_RANGE",
            13: "WORK_RATE",
            14: "CARRY_CAPACITY",
            112: "TRAIN_LOCATION",
            113: "TRAIN_BUTTON",
            192: "AVAILABLE_UNIT_FLAG",
            193: "DISABLED_UNIT_FLAG",
        }
        
        for aid, enum_name in expected_mappings.items():
            self.assertIn(aid, result, f"ID {aid} missing from result")
            record = result[aid]
            self.assertEqual(record["parser_enum_name"], enum_name, f"ID {aid} mapped to {record['parser_enum_name']}, expected {enum_name}")
            self.assertEqual(record["parser_enum_value"], aid)
            self.assertIn("usage_hint", record)
            self.assertIn(f"ObjectAttribute.{enum_name}", record["usage_hint"])
            
        # Check data quality
        for aid, record in result.items():
            self.assertEqual(record["id"], aid)
            self.assertIsNotNone(record["ugc_name"])
            self.assertIsNotNone(record["parser_enum_name"])
            
    def test_missing_enum_mapping(self):
        """
        Verifies that UGC attributes without matching Enums are handled.
        """
        html = "<h2>9999. Ghost Attribute</h2><p>Spooky</p>"
        enums = {} # Empty
        
        result = build_attributes_knowledge(html, enums)
        
        self.assertIn(9999, result)
        record = result[9999]
        self.assertEqual(record["ugc_name"], "Ghost Attribute")
        self.assertIsNone(record["parser_enum_name"])
        self.assertIsNone(record["usage_hint"])

if __name__ == '__main__':
    unittest.main()
