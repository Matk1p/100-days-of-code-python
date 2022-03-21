from audioop import mul
import CalculatorArt
import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def operations_printer():
    for symbol in operations:
        print(symbol)

operations = {
        "+" : add,
        "-" : subtract,
        "*" : multiply,
        "/" : divide,
    }

# putting it in a function so that we could call it recursively
def calculator():
    n1 = float(input("What's your first number: "))
    should_continue = True

    operations_printer()
    operation_symbol = input("Pick an operation from the line above: ")
    n2 = float(input("What's your second number: "))

    calculation_operation = operations[operation_symbol]
    answer = calculation_operation(n1, n2)
    print(f"{n1} {operation_symbol} {n2} = {answer}")

    while should_continue:
        choice = input(f'Type "Y" to continue calculating with current answer: {answer} and "N" to start a new calculation, "ac" to stop:' ).lower()
        if choice == "n":
            clearConsole()
            print(CalculatorArt.logo)
            calculator()
        elif choice == "ac":
            should_continue = False
            break
        operations_printer()
        operation_symbol = input("Pick an operation from the line above: ")
        n = float(input("Pick the next number: "))
        calculation_operation = operations[operation_symbol]
        latest_answer = calculation_operation(answer, n)
        print(f"{answer} {operation_symbol} {n} = {latest_answer}")

print(CalculatorArt.logo)
calculator()