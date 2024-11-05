print("Addition calculator! Enter 2 numbers to see the result.\n")

while True:
    first = input("Enter the first number to add.\n"
                  "Type QUIT to quit: ")
    if first.lower() == "quit":
        break
    second = input("Enter the second number to add.\n"
                   "Type QUIT to quit: ")
    if second.lower() == "quit":
        break

    try:
        print(f"Result: {int(first) + int(second)}\n")
    except ValueError:
        print("Error! Make sure you enter two numbers.\n")