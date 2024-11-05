from pathlib import Path
import json

while True:
    try:
        favorite_number = int(input("What is your favorite number? "))
        break
    except ValueError:
        print("Make sure to enter a whole number!")

location = Path("favorite_number.json")
contents = json.dumps(favorite_number)
location.write_text(contents)