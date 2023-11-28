from art_calculator import logo

# Calculator
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


# function for the whole calculation
def calculation():
    print(logo)
    num1 = float(input("What's the first number? "))

    # Variable for the while-loop
    exit_calculator = False

    # print out keys to show in output
    while not exit_calculator:
        for key in operations:
            print(key)

        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number? "))

        if operation_symbol in operations:
            calculation_call = operations[operation_symbol]
            answer = calculation_call(num1, num2)

            print(f"{num1} {operation_symbol} {num2} = {answer}")

            input_answer = input(f"Type 'y' to continue calculating with {answer}, "
                                 f"type 'c' to clear or type 'n' to exit. \n")

            if input_answer == "y":
                num1 = answer
            elif input_answer == "c":
                print(logo)
                num1 = float(input("What's the first number? "))
            elif input_answer == "n":
                print("Goodbye.")
                exit_calculator = True
            else:
                print("Invalid input. Please try again.")
        else:
            print("Invalid operation. Please try again.")

calculation()
