import os, shutil, pathlib
import argparse
import shutil as _shutil
import os as _os


folder = pathlib.Path(__file__).parent.parent.resolve()

# expanduser example to get desktop path
desktop_folder = os.path.join(os.path.expanduser("~"), "Desktop")

os.path.exists(desktop_folder)
os.pardir  # parent directory
os.getcwd()  # current working directory


# create a function to tell the age of a file
def get_file_age_in_days(file_path):    
    """Returns the age of the file in days."""
    creation_time = os.path.getctime(file_path)
    current_time = os.path.getmtime(file_path)
    age_in_seconds = current_time - creation_time
    age_in_days = age_in_seconds / (24 * 3600)
    return age_in_days

def main():
    for entry in os.scandir(folder):
        if entry.is_file():
            print(f"File: {entry.name} - Size: {os.path.getsize(entry.path)} bytes - Extension: {os.path.splitext(entry.name)[1]}")
        elif entry.is_dir():
            print(f"Directory: {entry.name}")


    # create a folder under the folder called zip
    zip_folder = os.path.join(folder, "zip")
    os.makedirs(zip_folder, exist_ok=True)

    for entry in os.scandir(folder):
        if entry.is_file() and entry.name.endswith('.zip'):
            # this can also be done with os.rename
            shutil.move(entry.path, zip_folder)



    for entry in os.scandir(folder):
        if entry.is_file():
            print(f"File: {entry.name} - Size: {os.path.getsize(entry.path)} bytes - Extension: {os.path.splitext(entry.name)[1]}")
        elif entry.is_dir():
            print(f"Directory: {entry.name}")

    for entry in os.walk(folder):
        print(f"Currently in directory: {entry[0]}")
        for file_name in entry[2]:
            print(f" - File: {file_name}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Move .zip files into a 'zip' subfolder. Use --dry-run to only show actions.")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be done without making any changes")
    args = parser.parse_args()
    if args.dry_run:
        print("Dry run enabled — no filesystem changes will be made. Actions shown below:")
        # Replace side-effecting functions with no-op printers
        def _fake_move(src, dst, *a, **k):
            print(f"[DRY-RUN] move: {src} -> {dst}")
        def _fake_makedirs(path, exist_ok=False):
            print(f"[DRY-RUN] makedirs: {path} (exist_ok={exist_ok})")
        _shutil.move = _fake_move
        _os.makedirs = _fake_makedirs
    main()