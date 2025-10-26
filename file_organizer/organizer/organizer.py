from .file_manager import FileManager
from .file_sorter import FileSorter

class FileOrganizer:
    def __init__(self, destination: str):
        self.manager = FileManager(destination)
        self.sorter = FileSorter()

    def organize(self):
        files = self.manager.list_files()

        if not files:
            print("No file found.")
            return

        for file in files:
            folder_name = self.sorter.get_folder_name(file.suffix)
            target_dir = self.manager.destination / folder_name
            self.manager.move_file(file, target_dir)
        
        print("Organize completed!")