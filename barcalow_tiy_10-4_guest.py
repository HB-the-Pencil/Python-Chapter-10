from pathlib import Path

path = Path("guest.txt")
guest = input("What is your name, guest? ")
path.write_text(guest)