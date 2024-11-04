from pathlib import Path
path = Path("learning_python.txt")
contents = path.read_text()

print("Entire file:")
print(contents)

print("\nBy line:")
lines = contents.splitlines()
for line in lines:
    print(line)

# This one was just for fun, to see if I can look for words by name later.
# And/or replace words in a file.
# print("\nBy word?")
# words = contents.split()
# for word in words:
#     print(word)
