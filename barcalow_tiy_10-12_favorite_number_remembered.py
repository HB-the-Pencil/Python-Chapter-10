from pathlib import Path
import json


def get_favorite_number(path: Path):
    """
    Get the user's favorite number.

    :param path: Path to the json file.
    :return: Returns the favorite number if it exists or else None.
    """
    if path.exists():
        contents = path.read_text()
        favorite_number = json.loads(contents)
        return favorite_number
    else:
        return None


def set_favorite_number(path: Path):
    """
    Set the user's favorite number.

    :path: Path to the json file.
    :return: Update the file at the specified path.
    """
    while True:
        try:
            favorite_number = int(input("What is your favorite number? "))
            break
        except ValueError:
            print("Make sure to enter a whole number!")

    contents = json.dumps(favorite_number)
    path.write_text(contents)


def read_favorite_number():
    """
    Get the user's favorite number if it exists, or set it if it doesn't.

    :return: Either prints the user's favorite number or sets it.
    """
    location = Path("favorite_number.json")
    favorite_number = get_favorite_number(location)

    if favorite_number:
        print(f"I know your favorite number! It's {favorite_number}!")
    else:
        set_favorite_number(location)
        print("Your favorite number has been stored!")


read_favorite_number()
