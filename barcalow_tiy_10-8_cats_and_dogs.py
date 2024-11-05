from pathlib import Path

dogs_path = Path("dogs.txt")
cats_path = Path("cats.txt")

def safe_read(path: Path):
    """
    A function to safely read a file from a path.

    :param path: Path to search.
    :return: Returns the text contained in the file or a gentle error message.
    """
    try:
        return path.read_text()
    except FileNotFoundError:
        return f"Error: {path} not found"

print(safe_read(dogs_path))
print(safe_read(cats_path))