
class FileSorter:

    EXTENSION_MAP = {
        "Images": [
            ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg", ".webp"
        ],
        "Documents": [
            ".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt", ".ppt", ".pptx", ".xls", ".xlsx", ".csv"
        ],
        "Data": [
            ".json", ".xml", ".yaml", ".yml", ".sql", ".db", ".sqlite", ".mdb"
        ],
        "Audio": [
            ".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a", ".wma"
        ],
        "Videos": [
            ".mp4", ".mkv", ".mov", ".avi", ".flv", ".wmv", ".webm"
        ],
        "Archives": [
            ".zip", ".rar", ".tar", ".gz", ".bz2", ".7z", ".iso"
        ],
        "Scripts": [
            ".py", ".js", ".html", ".css", ".php", ".java", ".cpp", ".c", ".cs", ".sh", ".bat", ".rb", ".ts"
        ],
        "Executables": [
            ".exe", ".msi", ".apk", ".bin", ".jar", ".deb", ".rpm", ".appimage"
        ],
        "Design": [
            ".psd", ".ai", ".xd", ".fig", ".sketch", ".indd"
        ],
        "Fonts": [
            ".ttf", ".otf", ".woff", ".woff2"
        ],
    }

    def get_folder_name(self, file_extension: str) -> str:
        """Return folder name based on file extension."""
        for folder, extensions in self.EXTENSION_MAP.items():
            if file_extension.lower() in extensions:
                return folder
        return "Others"

     