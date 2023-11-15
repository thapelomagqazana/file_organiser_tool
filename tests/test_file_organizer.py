import sys
# Adjust the Python path to include the 'src' directory
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# Add the project root to sys.path
sys.path.append('/home/thapelo/file_organizer_tool/src')

from file_organizer import FileOrganizer
# test_file_organizer.py
import unittest
from unittest.mock import patch

class TestFileOrganizer(unittest.TestCase):
    def test_organize_files(self):
        # Mock input to simulate user input during testing
        with patch("builtins.input", side_effect=["test_source", "test_destination", "test_rules.json"]):
            file_organizer = FileOrganizer()
            # Add additional mock data for source and destination directories
            with patch("os.listdir", return_value=["file.txt", "image.jpg", "document.docx"]):
                with patch("os.path.isfile", return_value=True):
                    with patch("shutil.move") as mock_move:
                        file_organizer.organize_files()

                        # Verify that shutil.move is called with the expected arguments
                        mock_move.assert_any_call("test_source/file.txt", "test_destination/TextFiles/file.txt")
                        mock_move.assert_any_call("test_source/image.jpg", "test_destination/Images/image.jpg")
                        mock_move.assert_any_call("test_source/document.docx", "test_destination/Other/document.docx")

if __name__ == "__main__":
    unittest.main()
