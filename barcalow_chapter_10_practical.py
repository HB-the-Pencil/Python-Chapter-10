"""
[X] Create a program that creates a Dictionary of Candies using the name of
    the person and the candy they would like.

[X] Your program should also allow you to update the file with new names and
    candy and write these new additions to the file.

[X] Please make sure that there is no way to cause the program to crash
    because of the wrong input.

[X] Please display the different candies without duplicates with a statement
    that shows both; the name of the person that requested the candy and the
    candy they would like. For example, if Alex and Joe both select Kit Kats
    your program should show on one line that Alex and Joe would like Kit Kats
    on individual lines.
"""
import csv
import os
import datetime

# I wrote this myself this time! Thank goodness for Python's great docs.
with open("Candy_Request_Responses.csv", newline="") as c:
    candy_choices = {}
    for row in csv.reader(c):
        if row[0] == "Timestamp":
            continue
        candy_choices[row[1].strip().lower()] = row[2].strip().lower()


title = """+================================+
|~~ Candy Store Receipt Viewer ~~|
|                                |
| Enter VIEW <name> to view a    |
| receipt. Type REG to see all   |
| registered users and QUIT to   |
| quit.                          |
| Type HELP for more info about  |
| adding, updating, or removing  |
| user data.                     |
+================================+"""

help_commands = """+================================+
|~~  HELP MENU: Command List   ~~|
| VIEW <name>: view receipt      |
| REG: view all registered users |
| QUIT: quit the program         |
| ADD: add a user to the file    |
| DEL <name>: remove user from   |
|   the file                     |
| UPDATE <name>: update an order |
+================================+"""


print(title)

while True:
    entry = input("CMD:> ")
    entry = entry.strip().lower()

    # Quit the program.
    if entry == "quit":
        print("Goodbye!")
        break

    # View registered users.
    elif entry == "reg":
        print("Registered users:")
        for name in candy_choices.keys():
            print(f"\t{name.title()}")

    # Print help list.
    elif entry == "help":
        print(help_commands)

    # Add a user to the file.
    elif entry == "add":
        print("~~ USER REGISTRATION ~~")
        user = input("Enter your name. Type CANCEL to cancel.\nADD:> ")
        user = user.strip().lower()

        # Remove commas to prevent issues when reading the CSV file.
        if "," in user:
            print("Removing commas from your entry.")
            user = user.replace(",", "")

        # Validate the data (no duplicates).
        while user in candy_choices.keys() or user == "":
            if user == "":
                print("You didn't enter a value.")
            else:
                print("That user already exists.\n")
            user = input("Enter your name. Type CANCEL to cancel.\nADD:> ")
            user = user.strip().lower()
            if user == "cancel":
                break

        if user == "cancel":
            print("Exiting...\n")
            continue

        # Repeat for the candy.
        candy = input("Enter the candy you're ordering. "
                      "Type CANCEL to cancel.\nADD:> ")
        candy = candy.strip().lower()

        if "," in candy:
            print("Removing commas from your entry.")
            candy = candy.replace(",", "")

        while candy == "":
            candy = input("Enter the candy you're ordering. "
                          "Type CANCEL to cancel.\nADD:> ")
            candy = candy.strip().lower()
            if candy == "cancel":
                break

        if candy == "cancel":
            print("Exiting...\n")
            continue

        # Generate a timestamp for the CSV file.
        dt = datetime.datetime.now()
        date = f"{dt.month}/{dt.day}/{dt.year}"
        time = f"{dt.hour}:{dt.minute}:{dt.second}"

        timestamp = f"{date} {time}"

        # Add the user to the dictionary and the CSV file.
        try:
            with open("Candy_Request_Responses.csv", "a", newline="") as c:
                writer = csv.writer(c)
                writer.writerow([timestamp, user, candy])
            candy_choices.update({user: candy})
        except:
            print("There was an error adding the user.\nExiting...\n")
        else:
            print("User added successfully!\nExiting...\n")

    # View a user's data.
    elif "view" in entry:
        name = entry.split("view")[1].strip().lower()
        if name in candy_choices.keys():
            print(f"{name.title()}'s order:")
            print(f"\t{candy_choices[name].title()}")
        else:
            if name == "":
                print("Error: missing argument. Make sure to specify a user.")
            else:
                print("Error: no such user. Type REG to view a list of "
                      "registered users.")

    # Delete a user's data. (Careful!)
    elif "del" in entry:
        name = entry.split("del")[1].strip().lower()
        if name in candy_choices.keys():
            print("WARNING!")
            print(f"This will PERMANENTLY delete the data associated with "
                  f"{name.title()}.")
            confirm = input("To confirm, type the name of the user whose "
                            "data you are trying to delete:\nDEL:> ")
            confirm = confirm.strip().lower()

            if confirm == name:
                try:
                    with open("Candy_Request_Responses.csv", "r") as r, \
                        open("temp.csv", "a", newline="") as w:
                        writer = csv.writer(w)

                        for row in csv.reader(r):
                            if row[1].strip().lower() != name:
                                writer.writerow(row)

                    # Swap the temporary file and the real file.
                    os.remove("Candy_Request_Responses.csv")
                    os.rename("temp.csv", "Candy_Request_Responses.csv")

                    candy_choices.pop(name)
                except:
                    print("There was an error removing the user.\n"
                          "Exiting...\n")
                else:
                    print("User removed successfully!\nExiting...\n")

            else:
                print("User confirmation failed.\nExiting...\n")

        else:
            if name == "":
                print("Error: missing argument. Make sure to specify a user.")
            else:
                print("Error: no such user. Type REG to view a list of "
                      "registered users.")

    # Update a user's order. This is a modified version of the delete code.
    elif "update" in entry:
        name = entry.split("update")[1].strip().lower()
        if name in candy_choices.keys():
            print("WARNING!")
            print(f"This will PERMANENTLY alter the data associated with "
                  f"{name.title()}.")
            confirm = input("Are you sure you want to proceed? (y/n):\n"
                            "UPD:> ")
            confirm = confirm.strip().lower()

            if confirm == "y":
                new_candy = input("What is your new order? Type CANCEL to "
                                  "cancel.\nUPD:> ")
                new_candy = new_candy.strip().lower()

                if new_candy == "cancel":
                    print("Order update cancelled.\n")
                    continue

                # Generate a timestamp for the CSV file.
                dt = datetime.datetime.now()
                date = f"{dt.month}/{dt.day}/{dt.year}"
                time = f"{dt.hour}:{dt.minute}:{dt.second}"

                timestamp = f"{date} {time}"

                try:
                    with open("Candy_Request_Responses.csv", "r") as r, \
                        open("temp.csv", "a", newline="") as w:
                        writer = csv.writer(w)

                        for row in csv.reader(r):
                            if row[1].strip().lower() != name:
                                writer.writerow(row)
                            else:
                                writer.writerow([timestamp, name, new_candy])

                    # Swap the temporary file and the real file.
                    os.remove("Candy_Request_Responses.csv")
                    os.rename("temp.csv", "Candy_Request_Responses.csv")

                    candy_choices[name] = new_candy
                except:
                    print("There was an error updating your order.\n"
                          "Exiting...\n")
                else:
                    print("Order updated successfully!\nExiting...\n")

            else:
                print("Update confirmation failed.\nExiting...\n")

        else:
            if name == "":
                print("Error: missing argument. Make sure to specify a user.")
            else:
                print("Error: no such user. Type REG to view a list of "
                  "registered users.")

    # This is to mock how actual shells will let you enter an empty line.
    elif entry == "":
        continue

    # The catch-all.
    else:
        print("Command not recognized. Type HELP for a list of commands.")