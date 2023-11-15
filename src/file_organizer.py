import os
import shutil
from rule_parser import RuleParser
import logging

class FileOrganizer:
    """Organizes files based on the defined rules."""

    def __init__(self, log_file="file_organizer.log"):
       """
        Initialize FileOrganizer by prompting the user for input.

        - source_dir (str): The source directory containing files to be organized.
        - destination_dir (str): The destination directory where files will be organized.
        - rule_parser (RuleParser): An instance of RuleParser to handle organization rules.
        """
       self.source_dir = os.path.expanduser(input("Enter the source directory 'e.g ~/Documents': ")) 
       self.destination_dir = os.path.expanduser(input("Enter the destination directory 'e.g ~/Pictures': "))
       self.rule_parser = RuleParser(self.get_rules())
       self.log_file = log_file
       self.setup_logging()
    

    def setup_logging(self):
        logging.basicConfig(
            filename=self.log_file,
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )


    def get_rules(self):
       """
        Get organization rules from the user using RuleParser.

        Returns:
        - dict: A dictionary containing organization rules.
        """
       return RuleParser.load_rules() 
       
    def organize_files(self):
        """
        Organize files from the source directory to the destination directory based on rules.
        """
        try:
            # Ask for user confirmation before moving the file
            user_confirmation = input("Confirm re-organizing files? (y/n): ").lower()
            
            if user_confirmation == "y":
                logging.info("File organization started...")
                print("File organization started...\n")
                count = 1
                for filename in os.listdir(self.source_dir):
                    source_path = os.path.join(self.source_dir, filename)
                    if os.path.isfile(source_path):
                        destination_folder = self.rule_parser.apply_rules_for_filename(filename)
                        destination_path = os.path.join(self.destination_dir, destination_folder)
                        if not os.path.exists(destination_path):
                            os.makedirs(destination_path)

                        shutil.move(source_path, os.path.join(destination_path, filename))
                        print(f"File_count : {count} - (Moved '{filename}' to '{destination_folder}')")
                        logging.info(f"File_count : {count} - (Moved '{filename}' to '{destination_folder}')")
                        count += 1

                print("\nFile organization completed successfully.")
                logging.info("\nFile organization completed successfully.")
                    
                        
            else:
                print("Operation cancelled!")
                logging.info("Operation cancelled!")
        except Exception as e:
            print(f"Error organizing files: {e}")
            logging.error(f"Error organizing files: {e}")