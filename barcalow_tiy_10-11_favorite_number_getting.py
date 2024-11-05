from pathlib import Path
import json

location = Path("favorite_number.json")
contents = location.read_text()
favorite_number = json.loads(contents)

print(f"I know your favorite number! It's {favorite_number}!")