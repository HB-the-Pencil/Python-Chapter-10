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
try:
    with open("Candy_Request_Responses.csv", newline="") as c:
        candy_choices = {}
        for row in csv.reader(c):
            if row[0] == "Timestamp":
                continue
            candy_choices[row[1].strip().lower()] = row[2].strip().lower()

except FileNotFoundError:
    print("There is no Candy_Request_Responses.csv file.")
    print("Creating an empty file.")

    dt = datetime.datetime.now()
    date = f"{dt.month}/{dt.day}/{dt.year}"
    time = f"{dt.hour}:{dt.minute}:{dt.second}"

    timestamp = f"{date} {time}"

    with open("Candy_Request_Responses.csv", "w", newline="") as c:
        writer = csv.writer(c)
        writer.writerow(["Timestamp","Name","What's your favorite candy?"])
        writer.writerow([timestamp, "Example User", "Example Candy"])

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

def add_user():
    """
    Add a user's receipt.

    :return: Once the user enters the appropriate information, add it to the
        CSV file.
    """
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
        print("Exiting...\n")
        return

    # Repeat for the candy.
    candy = input("Enter the candy you're ordering. "
                  "Type CANCEL to cancel.\nADD:> ")
    candy = candy.strip().lower()

    if "," in candy:
        print("Removing commas from your entry.")
        candy = candy.replace(",", "")

    while candy == "":
        print("You didn't enter anything.")
        candy = input("Enter the candy you're ordering. "
                      "Type CANCEL to cancel.\nADD:> ")
        candy = candy.strip().lower()

    if candy == "cancel":
        print("Exiting...\n")
        return

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

def view_user(user):
    """
    View a user's receipt.

    :param user: The specified user's name.
    :return: Prints the user's order or a polite error.
    """
    if user in candy_choices.keys():
        print(f"{user.title()}'s order:")
        print(f"\t{candy_choices[user].title()}")
    else:
        if user == "":
            print("Error: missing argument. Make sure to specify a user.")
        else:
            print("Error: no such user. Type REG to view a list of "
                  "registered users.")

def del_user(user):
    """
    Delete a user from the CSV file.

    :param user: The specified user's name.
    :return: Removes the user from the CSV file.
    """
    if user in candy_choices.keys():
        print("WARNING!")
        print(f"This will PERMANENTLY delete the data associated with "
              f"{user.title()}.\n")
        confirm = input("To confirm, type the name of the user whose "
                        "data you are trying to delete:\nDEL:> ")
        confirm = confirm.strip().lower()

        if confirm == user:
            try:
                with open("Candy_Request_Responses.csv", "r") as r, \
                        open("temp.csv", "a", newline="") as w:
                    writer = csv.writer(w)

                    for row in csv.reader(r):
                        if row[1].strip().lower() != user:
                            writer.writerow(row)

                # Swap the temporary file and the real file.
                os.remove("Candy_Request_Responses.csv")
                os.rename("temp.csv", "Candy_Request_Responses.csv")

                candy_choices.pop(user)
            except:
                print("There was an error removing the user.\n"
                      "Exiting...\n")
            else:
                print("User removed successfully!\nExiting...\n")

        else:
            print("User confirmation failed.\nExiting...\n")

    else:
        if user == "":
            print("Error: missing argument. Make sure to specify a user.")
        else:
            print("Error: no such user. Type REG to view a list of "
                  "registered users.")

def update_user(user):
    """
    Update a user's order.

    :param user: The specified user's name.
    :return: Modifies the data in the CSV file associated with the user.
    """
    if user in candy_choices.keys():
        print("WARNING!")
        print(f"This will PERMANENTLY alter the data associated with "
              f"{name.title()}.\n")
        confirm = input("Are you sure you want to proceed? (y/n):\nUPD:> ")
        confirm = confirm.strip().lower()

        if confirm == "y":
            new_candy = input("What is your new order? Type CANCEL to "
                              "cancel.\nUPD:> ")
            new_candy = new_candy.strip().lower()

            while new_candy == "":
                print("You didn't enter anything.")
                new_candy = input("Enter your new order. Type CANCEL to "
                                  "cancel.\nUPD:> ")
                new_candy = new_candy.strip().lower()

            if new_candy == "cancel":
                print("Order update cancelled.\n")
                return

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
                        if row[1].strip().lower() != user:
                            writer.writerow(row)

                    writer.writerow([timestamp, user, new_candy])

                # Swap the temporary file and the real file.
                os.remove("Candy_Request_Responses.csv")
                os.rename("temp.csv", "Candy_Request_Responses.csv")

                candy_choices[user] = new_candy
            except:
                print("There was an error updating your order.\n"
                      "Exiting...\n")
            else:
                print("Order updated successfully!\nExiting...\n")

        else:
            print("Update confirmation failed.\nExiting...\n")

    else:
        if user == "":
            print("Error: missing argument. Make sure to specify a user.")
        else:
            print("Error: no such user. Type REG to view a list of "
                  "registered users.")

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
        add_user()

    # View a user's data.
    elif "view" in entry:
        name = entry.split("view")[1].strip().lower()
        view_user(name)

    # Delete a user's data. (Careful!)
    elif "del" in entry:
        name = entry.split("del")[1].strip().lower()
        del_user(name)

    # Update a user's order. This is a modified version of the delete code.
    elif "update" in entry:
        name = entry.split("update")[1].strip().lower()
        update_user(name)

    # This is to mock how actual shells will let you enter an empty line.
    elif entry == "":
        continue

    # The catch-all.
    else:
        print("Command not recognized. Type HELP for a list of commands.")