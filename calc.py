import math
def get_input(prompt):
    return int(input(prompt))
def add():
    x = get_input("Enter the 1st number: ")
    y = get_input("Enter the 2nd number: ")
    print(f"The sum is {x + y}"
def multiply():
    x = get_input("Enter the 1st number: ")
    y = get_input("Enter the 2nd number: ")
    print(f"The product is {x * y}")
def subtract():
    x = get_input("Enter the 1st number: ")
    y = get_input("Enter the 2nd number: ")
    print(f"The difference is {x - y}")
def divide():
    x = get_input("Enter the 1st number: ")
    y = get_input("Enter the 2nd number: ")
    if y == 0:
        print("Division by zero is not allowed.")
    else:
        print(f"The division result is {x / y}")
