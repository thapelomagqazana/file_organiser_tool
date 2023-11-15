import sys

# Add the project root to sys.path
sys.path.append('/home/thapelo/file_organizer_tool/src')

from rule_parser import RuleParser
import unittest
from unittest.mock import patch

class TestRuleParser(unittest.TestCase):
    def test_apply_rules_for_filename(self):
        rules = {".*\.txt$": "TextFiles", ".*\.jpg$": "Images", ".*": "Other"}
        rule_parser = RuleParser(rules)

        # Positive test cases
        self.assertEqual(rule_parser.apply_rules_for_filename("file.txt"), "TextFiles")
        self.assertEqual(rule_parser.apply_rules_for_filename("image.jpg"), "Images")
        # Negative test case
        self.assertEqual(rule_parser.apply_rules_for_filename("document.webp"), "Other")

    def test_load_rules(self):
        # Mock input to simulate user input during testing
        with patch("builtins.input", side_effect=["test_rules.json"]):
            rules = RuleParser.load_rules()
            self.assertIsNotNone(rules)

if __name__ == "__main__":
    unittest.main()
