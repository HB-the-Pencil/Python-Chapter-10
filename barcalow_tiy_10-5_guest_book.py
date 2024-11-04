from pathlib import Path

path = Path("guest_book.txt")

contents = ""
while True:
    guest = input("Enter the name of a new guest.\n"
                  "Type QUIT to quit. > ")
    if guest.lower() == "quit":
        break
    contents += guest + "\n"

path.write_text(contents)