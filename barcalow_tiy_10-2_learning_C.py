from pathlib import Path
path = Path("learning_python.txt")
contents = path.read_text()

print("Entire file:")
print(contents.replace("Python", "C"))

print("\nBy line:")
lines = contents.splitlines()
for line in lines:
    print(line.replace("Python", "C"))