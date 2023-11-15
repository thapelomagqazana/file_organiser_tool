Feature: File Organizer

    Scenario: User organizes files based on rules
        Given the source directory is "test_source"
        And the destination directory is "test_destination"
        And the rules are defined in "test_rules.json"
        When the user runs the File Organizer
        Then files should be organized successfully
    
    Scenario: User provides invalid source directory
        Given the source directory is "nonexistent_source"
        And the destination directory is "test_destination"
        And the rules are defined in "test_rules.json"
        When the user runs the File Organizer
        Then an error should be displayed

    Scenario: User provides invalid destination directory
        Given the source directory is "test_source"
        And the destination directory is "nonexistent_destination"
        And the rules are defined in "test_rules.json"
        When the user runs the File Organizer
        Then an error should be displayed
