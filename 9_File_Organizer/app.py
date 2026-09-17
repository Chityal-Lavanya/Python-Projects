import os
from pathlib import Path
import shutil

FILE_CATEGORIES = {

    "Images": [
        ".jpg",
        ".jpeg",
        ".png",
        ".gif",
        ".bmp",
        ".webp"
    ],

    "Documents": [
        ".doc",
        ".docx",
        ".txt",
        ".xls",
        ".xlsx",
        ".ppt",
        ".pptx"
    ],

    "Videos": [
        ".mp4",
        ".mkv",
        ".avi",
        ".mov",
        ".wmv"
    ],

    "PDFs": [
        ".pdf"
    ]
}

# Find Category
def get_category(extension):

    for category, extensions in FILE_CATEGORIES.items():

        if extension.lower() in extensions:
            return category

    return "Others"

# Organize Files
def organize_files(folder_path):

    folder = Path(folder_path)

    # Check whether folder exists
    if not folder.exists():
        print("Folder does not exist!")
        return

    if not folder.is_dir():
        print("The given path is not a folder!")
        return

    moved_files = 0

    # Loop through files
    for file in folder.iterdir():

        try:

            # Skip folders
            if file.is_dir():
                continue

            # Get file extension
            extension = file.suffix

            # Find category
            category = get_category(extension)

            # Create category folder
            category_folder = folder / category
            category_folder.mkdir(exist_ok=True)

            # Destination path
            destination = category_folder / file.name

            # Handle duplicate file names
            if destination.exists():

                name = file.stem
                extension = file.suffix

                counter = 1

                while destination.exists():

                    new_name = (
                        f"{name}_{counter}{extension}"
                    )

                    destination = (
                        category_folder / new_name
                    )

                    counter += 1

            # Move file
            shutil.move(str(file), str(destination))

            print(
                f"Moved: {file.name} → {category}/"
            )

            moved_files += 1

        except PermissionError:
            print(
                f"Permission denied: {file.name}"
            )

        except OSError as error:
            print(
                f"Error moving {file.name}: {error}"
            )

        except Exception as error:
            print(
                f"Unexpected error: {error}"
            )

    print("\n------------------------------")
    print("File organization completed!")
    print(f"Files moved: {moved_files}")
    print("--------------------------------")

# Main Program
print("---- FILE ORGANIZER ----")

folder_path = input(
    "Enter folder path to organize: "
).strip()

organize_files(folder_path)