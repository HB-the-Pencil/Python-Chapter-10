print("Addition calculator! Enter 2 numbers to see the result.\n")
first = input("Enter the first number to add: ")
second = input("Enter the second number to add: ")

try:
    print(f"Result: {int(first) + int(second)}")
except ValueError:
    print("Error! Make sure you enter two numbers.")