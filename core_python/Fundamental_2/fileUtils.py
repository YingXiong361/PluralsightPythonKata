import os, shutil


def read_file(file_path):
    """Reads the content of a file and returns it as a string."""
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def read_file_lines(file_path):
    """Reads the content of a file and returns it as a list of lines."""
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

def write_file(file_path, content):
    """Writes the given content to a file."""
    with open(file_path, 'w') as file:
        file.write(content)

    # append to file
def append_to_file(file_path, content):
    """Appends the given content to a file."""
    with open(file_path, 'a') as file:
        file.write(content)
def write_lines_to_file(file_path, lines):
    """Writes a list of lines to a file."""
    with open(file_path, 'w') as file:
        file.writelines(lines)

def lazy_read_file(file_path):
    """Generator that yields lines from a file one at a time."""
    with open(file_path, 'r') as file:
        for line in file:
            yield line


def file_exists(file_path):
    """Checks if a file exists at the given path."""
    return os.path.isfile(file_path)    


def delete_file(file_path):
    """Deletes the file at the given path."""
    if os.path.isfile(file_path):
        os.remove(file_path)

def list_files_in_directory(directory_path):
    """Lists all files in the given directory."""
    return [f for f in os.scandir(directory_path) if os.path.isfile(f.path)]   

def get_file_size(file_path):
    """Returns the size of the file in bytes."""
    return os.path.getsize(file_path)

def get_file_name(file_path):
    """Returns the file name from the given file path."""
    return os.path.basename(file_path)

def get_file_directory(file_path):
    """Returns the directory of the given file path."""
    return os.path.dirname(file_path)

def get_file_creation_date(file_path):
    """Returns the creation date of the file."""
    import os, time, datetime
    from zoneinfo import ZoneInfo
    creation_time = os.path.getctime(file_path)

    # Example 1 — fixed-offset timezone (e.g. UTC+8)
    tz = datetime.timezone(datetime.timedelta(hours=8))  # change offset as needed
    created_dt = datetime.datetime.fromtimestamp(creation_time, tz)

    # Example 2 — IANA timezone (Python 3.9+)
    try:
        created_dt_zone = datetime.datetime.fromtimestamp(creation_time, ZoneInfo("Asia/Shanghai"))  # change zone
    except Exception:
        created_dt_zone = None  # zoneinfo not available

    # Example 3 — UTC
    created_utc = datetime.datetime.fromtimestamp(creation_time, datetime.timezone.utc)
    ts = os.path.getctime("file.txt")        # numeric timestamp (float)
    readable = time.ctime(ts)                # human-readable local-time string
    iso = datetime.datetime.fromtimestamp(ts).isoformat()

    print(ts)      # 169... (float)
    print(readable)  # "Tue Dec 02 12:34:56 2025"
    print(iso)       # "2025-12-02T12:34:56"

def get_file_extension(file_path):
    """Returns the file extension of the given file."""
    _, ext = os.path.splitext(file_path)
    return ext

def copy_file(source_path, destination_path):
    """Copies a file from source to destination."""
    shutil.copy2(source_path, destination_path)

def move_file(source_path, destination_path):
    """Moves a file from source to destination."""
    shutil.move(source_path, destination_path)

def rename_file(old_path, new_path):
    """Renames a file from old_path to new_path."""
    os.rename(old_path, new_path)

def count_lines_in_file(file_path):
    """Counts the number of lines in a file."""
    with open(file_path, 'r') as file:
        return sum(1 for line in file)
    
