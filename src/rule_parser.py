import json
import re

class RuleParser:
    """Parses and applies user-defined organization rules."""

    def __init__(self, rules):
        """
        Initialize RuleParser with a set of rules.

        Parameters:
        - rules (dict): A dictionary containing user-defined rules.
        """
        self.rules = rules

    @classmethod
    def load_rules(cls):
        """
        Load organization rules

        Returns:
        - dict: A dictionary containing the loaded rules.
        """

        try:
            rules_file_path = "/home/thapelo/file_organizer_tool/src/organization_rules.json"
            with open(rules_file_path, "r") as file:
                rules = json.load(file)
            return rules
        except (FileNotFoundError, json.JSONDecodeError):
            # Handle file not found or invalid JSON gracefully
            print("Error loading rules. Using default rules.")
            return {}
        
    
    @classmethod
    def apply_rules(cls, rules, filename):
        """
        Apply organization rules to determine the destination folder for a filename.

        Parameters:
        - rules (dict): A dictionary containing organization rules.
        - filename (str): The filename to be organized.

        Returns:
        - str: The destination folder based on the rules.
        """
        for pattern, destination in rules.items():
            if re.match(pattern, filename):
                return destination
        # Default rule if no match is found
        return "Other"
    
    def apply_rules_for_filename(self, filename):
        """
        Apply organization rules to determine the destination folder for a filename.

        Parameters:
        - filename (str): The filename to be organized.

        Returns:
        - str: The destination folder based on the rules.
        """
        return self.apply_rules(self.rules, filename)

        

