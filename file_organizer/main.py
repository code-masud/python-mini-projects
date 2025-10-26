
from organizer import FileOrganizer
from pathlib import Path

def main():
    print("=== File Organizer ===")
    folder_path = input("Enter the folder path to organize: ").strip()

    if not Path(folder_path).exists():
        print("The specified folder does not exist.")
        return

    organizer = FileOrganizer(folder_path)
    organizer.organize()

if __name__ == "__main__":
    main()