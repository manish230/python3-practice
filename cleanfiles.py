import os
import shutil
from pathlib import Path

# Define file categories and associated extensions
FILE_CATEGORIES = {
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"},
    "Documents": {".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".odt"},
    "Archives": {".zip", ".rar", ".7z", ".tar", ".gz"},
}

def get_desktop_path():
    """Return the user's desktop path."""
    return Path.home() / "devops"

def organize_desktop():
    desktop_path = get_desktop_path()
    print(f"Organizing files in: {desktop_path}\n")

    for item in desktop_path.iterdir():
        if item.is_file():
            ext = item.suffix.lower()
            moved = False

            for category, extensions in FILE_CATEGORIES.items():
                if ext in extensions:
                    target_dir = desktop_path / category
                    target_dir.mkdir(exist_ok=True)

                    target_path = target_dir / item.name

                    # Avoid overwriting files
                    if target_path.exists():
                        base, extension = os.path.splitext(item.name)
                        counter = 1
                        while target_path.exists():
                            target_path = target_dir / f"{base}_{counter}{extension}"
                            counter += 1

                    shutil.move(str(item), str(target_path))
                    print(f"Moved '{item.name}' to '{category}/'")
                    moved = True
                    break

            if not moved:
                print(f"Skipped: {item.name} (Unknown file type)")
    print("\nDone organizing.")

if __name__ == "__main__":
    organize_desktop()
