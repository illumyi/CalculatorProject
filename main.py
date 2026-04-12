# Get chosen operator from user + validation
while True:
    operators = ["+", "-", "*", "/", "%", "**"]
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

    # Functions for the calculation options
    def add(first, second):
        return first + second
    def subtract(first, second):
        return first - second
    def multiply(first, second):
        return first * second
    def divide(first, second):
        return first / second
    def modulo(first, second):
        return first % second
    def power(first, second):
        return first ** second

    # Dictionary to access results via functions
    operations = {"+": add,
                "-": subtract,
                "*": multiply,
                "/": divide,
                "%": modulo,
                "**": power}

    # Return results + loop / break the program
    print("Result = ", operations[operation](first, second))
    print("Would you like to calculate again? (y/n): ")
    loop_status = str(input())

    # Option selection + user input validation 
    if loop_status.lower() == "y" or loop_status.lower() == "yes":
        continue
    elif loop_status.lower() == "n" or loop_status.lower() == "no":
        break
    else:
        print("Invalid input, enter yes or no")
    break