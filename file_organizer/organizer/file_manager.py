from pathlib import Path

class FileManager:
    def __init__(self, destination: str):
        self.destination = Path(destination)

    def list_files(self):
        return [file_path for file_path in self.destination.rglob("*") if file_path.is_file()]

    def move_file(self, source_dir, target_dir):
        if not Path(target_dir).exists():
            Path(target_dir).mkdir(parents=True, exist_ok=True)

        old_path = Path(source_dir)
        new_name = Path(target_dir) / old_path.name
        old_path.rename(new_name)
