# Get inputs from user + operator validation
while True:
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

    # Return results + break or continue
    print("Result = ", operations[operation](first, second))
    print("Would you like to continue? (Y/N): ")
    loop_status = str(input())


    if loop_status.lower() == "y" or loop_status.lower() == "yes":
        continue
    elif loop_status.lower() == "n" or loop_status.lower() == "no":
        break
    else:
        print("Invalid input, enter yes or no")
    break