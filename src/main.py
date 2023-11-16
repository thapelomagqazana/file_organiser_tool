from file_organizer import FileOrganizer
from gui import FileOrganizerGUI
import argparse
import tkinter as tk


def main():
    parser = argparse.ArgumentParser(description="File Organizer Tool")
    parser.add_argument("--gui", action="store_true", help="Run the GUI version")
    args = parser.parse_args()

    if args.gui:
        root = tk.Tk()
        app = FileOrganizerGUI(root)
        root.mainloop()
    else:
        file_organizer = FileOrganizer()
        file_organizer.organize_files()
        

if __name__ == "__main__":
    main()
