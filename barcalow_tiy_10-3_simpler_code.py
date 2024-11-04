from pathlib import Path
path = Path("learning_python.txt")
contents = path.read_text()

print("Entire File:")
print(contents)

print("\nBy Line:")
for line in contents.splitlines():
    print(line)

print("\nLearning C Entire File:")
print(contents.replace("Python", "C"))

print("\nLearning C By Line:")
for line in contents.splitlines():
    print(line.replace("Python", "C"))
