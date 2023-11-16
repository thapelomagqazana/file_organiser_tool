import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
from file_organizer import FileOrganizer
import json
import re

class FileOrganizerGUI:
    def __init__(self, master):
        self.master = master
        master.title("File Organizer")

        self.source_label = tk.Label(master, text="Source Directory:")
        self.source_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

        self.source_entry = tk.Entry(master, width=50)
        self.source_entry.grid(row=0, column=1, padx=10, pady=10)

        self.browse_source_button = tk.Button(master, text="Browse", command=self.browse_source)
        self.browse_source_button.grid(row=0, column=2, padx=10, pady=10)

        self.destination_label = tk.Label(master, text="Destination Directory:")
        self.destination_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        self.destination_entry = tk.Entry(master, width=50)
        self.destination_entry.grid(row=1, column=1, padx=10, pady=10)

        self.browse_destination_button = tk.Button(master, text="Browse", command=self.browse_destination)
        self.browse_destination_button.grid(row=1, column=2, padx=10, pady=10)

        self.organize_button = tk.Button(master, text="Organize Files", command=self.organize_files)
        self.organize_button.grid(row=2, column=0, columnspan=3, pady=20)

    
    def browse_source(self):
        source_dir = filedialog.askdirectory()
        self.source_entry.delete(0, tk.END)
        self.source_entry.insert(0, source_dir)

    
    def browse_destination(self):
        destination_dir = filedialog.askdirectory()
        self.destination_entry.delete(0, tk.END)
        self.destination_entry.insert(0, destination_dir)

    
    def validate_directories(self, source_dir, destination_dir):
        if not source_dir or not destination_dir:
            raise ValueError("Please select source and destination directories.")
        
        if not os.path.exists(source_dir):
            raise FileNotFoundError(f"Source directory '{source_dir}' does not exist.")
        
        if not os.path.exists(destination_dir):
            raise FileNotFoundError(f"Destination directory '{destination_dir}' does not exist.")
        
    
    def load_rules(self, rules_file):
        try:
            with open(rules_file, "r") as f:
                rules = json.load(f)
            return rules
        except Exception as e:
            raise ValueError(f"Error loading rules from {rules_file}: {str(e)}")
    

    def apply_rules_for_filename(self, filename, rules):
        
        # Iterate through rules to find the first matching pattern
        for pattern, category in rules.items():
            if re.match(pattern, filename):
                return category

    def organize_files_based_on_rules(self, source_dir, destination_dir, rules):
        for filename in os.listdir(source_dir):
            source_path = os.path.join(source_dir, filename)

            # Check if it's a file and not a directory
            if os.path.isfile(source_path):
                category = self.apply_rules_for_filename(filename, rules)
                category_dir = os.path.join(destination_dir, category)

                # Create category directory if it doesn't exist
                if not os.path.exists(category_dir):
                    os.makedirs(category_dir)
                
                destination_path = os.path.join(category_dir, filename)

                # Move the file to the destinaton directory
                shutil.move(source_path, destination_path)
        
    def organize_files(self):
        source_dir = self.source_entry.get()
        destination_dir = self.destination_entry.get()

        try:

            self.validate_directories(source_dir, destination_dir)

            # Load organization rules from a JSON file
            rules_file = "src/organization_rules.json"
            rules = self.load_rules(rules_file)

            # Organize files based on rules
            self.organize_files_based_on_rules(source_dir, destination_dir, rules)

            # print(source_dir)
            # print(destination_dir)

            # FileOrganizer.organize_files()


            messagebox.showinfo("File Organizer", "File organization completed successfully.")
        
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    


if __name__ == "__main__":
    root = tk.Tk()
    app = FileOrganizerGUI(root)
    root.mainloop()