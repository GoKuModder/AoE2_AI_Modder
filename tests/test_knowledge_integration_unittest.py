import unittest
from unittest.mock import MagicMock, patch
import sys
import os

# Add project root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.knowledge_builders.attributes_builder import build_attributes_knowledge

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

class MockTag:
    def __init__(self, name, text):
        self.name = name
        self.text = text
        self.next_siblings = []

    def get_text(self, separator=" ", strip=True):
        return self.text

class MockSoup:
    def __init__(self, html, parser):
        self.html = html

    def find_all(self, tag_name):
        if tag_name != "h2":
            return []
        
        # Simple regex parser for the test HTML
        import re
        # This regex looks for <h2>...</h2> and following content until next <h2>
        # It's fragile but enough for the specific SAMPLE_UGC_HTML structure
        blocks = re.split(r'(?=<h2>)', self.html)
        results = []
        for block in blocks:
            if not block.strip().startswith("<h2>"):
                continue
            
            # Extract H2 text
            m_h2 = re.search(r"<h2>(.*?)</h2>", block)
            if not m_h2: 
                continue
                
            h2_text = m_h2.group(1)
            h2_tag = MockTag("h2", h2_text)
            
            # Extract content (everything after </h2>)
            content = block[m_h2.end():].strip()
            # Remove <p> tags for simplicity as clean_ws handles text
            content_text = content.replace("<p>", "").replace("</p>", "").strip()
            
            if content_text:
                p_tag = MockTag("p", content_text)
                h2_tag.next_siblings = [p_tag]
            
            results.append(h2_tag)
            
        return results

class TestAttributesBuilder(unittest.TestCase):
    
    @patch('src.knowledge_builders.attributes_builder.require_bs4')
    @patch('src.knowledge_builders.attributes_builder.BeautifulSoup')
    def test_attributes_builder_mapping(self, mock_bs, mock_require):
        mock_bs.side_effect = MockSoup
        
        result = build_attributes_knowledge(SAMPLE_UGC_HTML, SAMPLE_ENUMS)
        
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
            self.assertEqual(record["parser_enum_name"], enum_name, 
                             f"ID {aid} mapped to {record['parser_enum_name']}, expected {enum_name}")
            self.assertEqual(record["parser_enum_value"], aid)
            self.assertIn("usage_hint", record)
            self.assertIn(f"ObjectAttribute.{enum_name}", record["usage_hint"])
            
    @patch('src.knowledge_builders.attributes_builder.require_bs4')
    @patch('src.knowledge_builders.attributes_builder.BeautifulSoup')
    def test_missing_enum_mapping(self, mock_bs, mock_require):
        mock_bs.side_effect = MockSoup
        
        html = "<h2>9999. Ghost Attribute</h2><p>Spooky</p>"
        enums = {} 
        
        result = build_attributes_knowledge(html, enums)
        
        self.assertIn(9999, result)
        record = result[9999]
        self.assertEqual(record["ugc_name"], "Ghost Attribute")
        self.assertIsNone(record["parser_enum_name"])
        self.assertIsNone(record["usage_hint"])

if __name__ == '__main__':
    unittest.main()
