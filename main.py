# Get inputs from user + operator validation
operators = ["+", "-", "*", "/"]
while True:
    print("What operation would you like to perform?: ")
    operation = input()
    if operation in operators:
        break
    else:
        print("Invalid operator, try again")
        continue

while True: # Number inputs validation 
    try:
        print("What is the first number?: ")
        first = float(input())
        break
    except ValueError:
        print("Invalid input, try again")

while True:
    try:
        print("What is the second number?: ")
        second = float(input())
        break
    except ValueError:
        print("Invalid input, try again")

# Calculation options
def add(first, second):
    return first + second
def subtract(first, second):
    return first - second
def multiply(first, second):
    return first * second
def divide(first, second):
    return first / second

# Results
operations = {"+": add,
              "-": subtract,
              "*": multiply,
              "/": divide}

print("Result = ", operations[operation](first, second))