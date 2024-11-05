from pathlib import Path
import json


def get_user(path: Path):
    """
    Get the user's information, if it exists.

    :param path: Path to the username.json file.
    :return: Returns the info if it exists, otherwise None.
    """
    if path.exists():
        contents = path.read_text()
        user_info = json.loads(contents)
        return user_info
    else:
        return None


def set_user(path: Path):
    """
    Set the user's name.

    :param path: Path to the username.json file.
    :return: Returns username and updates user_info.json file.
    """
    user_name = input("Please enter your name: ")
    user_favorite_num = input(f"What is your favorite number, {user_name}? ")
    user_favorite_col = input(f"What is your favorite color? ")
    user_favorite_food = input(f"Favorite food? ")
    user_favorite_thing = input(f"Coolest thing? ")

    user_info = {
        "name": user_name,
        "favorite_number": user_favorite_num,
        "favorite_color": user_favorite_col,
        "favorite_food": user_favorite_food,
        "favorite_thing": user_favorite_thing,
    }
    contents = json.dumps(user_info)
    path.write_text(contents)
    return user_name


def greet_user():
    """
    Greet the user if they exist, or add the user to the username file.

    :return: Updates username.json.
    """
    path = Path("user_info.json")
    user_info = get_user(path)

    if user_info:
        print(f"Hello, {user_info["name"]}!")
        print("\nHere's what we remember about you:")
        print(f"\tFavorite number: {user_info["favorite_number"]}")
        print(f"\tFavorite color: {user_info["favorite_color"]}")
        print(f"\tFavorite food: {user_info["favorite_food"]}")
        print(f"\tCoolest thing: {user_info["favorite_thing"]}")
    else:
        username = set_user(path)
        print(f"We'll remember you when you come back, {username}!")


greet_user()