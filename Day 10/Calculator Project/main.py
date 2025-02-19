import art


def main():
    #print calculator logo
    print(art.logo)
    #get user input for the first float
    n1 = float(input('Input the first number: '))
    print('+ - * /')
    #get the user input for the second float and what operation to do
    operation, n2 = continue_func()
    total = 0

    #calculation dictionary
    calc_dict = {'+': add, '-': subtract, '*': multiply, '/': divide}

    #calculate the total and print it to the screen
    total = calculate(calc_dict, operation, n1, n2, total)

    #check if user wants to continue the current calculation
    continue_input = input(f"Type 'y' to continue calculation with {total}. Type 'n' to start new calculation: ")
    while continue_input.lower() == 'y':
        #the first float becomes the total of the last operation
        n1 = total
        # get the user input for the second float and what operation to do
        operation, n2 = continue_func()
        #calculate new total
        total = calculate(calc_dict, operation, n1, n2, total)
        #check if the user want to continue the current calculation
        continue_input = input(f"Type 'y' to continue calculation with {total}. Type 'n' to start new calculation: ")
    #restart program if user inputs n
    if continue_input.lower() == 'n':
        main()


def add(n1, n2):
    """add(n1, n2) returns the sum of two floats"""
    return n1 + n2


def subtract(n1, n2):
    """subtract(n1, n2) returns the subtraction of two floats"""
    return n1 - n2


def multiply(n1, n2):
    """multiply(n1, n2) returns the multiplication of two floats"""
    return n1 * n2


def divide(n1, n2):
    """divide(n1, n2) returns the division of two floats"""
    return n1 / n2


def continue_func():
    """continue_func() returns the user input for second float
    and what operation to do"""
    operation = input('Pick and operation: ')
    n2 = float(input('Input the second number: '))
    return operation, n2


def calculate(calc_dict, operation, n1, n2, total):
    """calculate(calc_dict, operation, n1, n2, total)
    returns the total of the chosen operation betweens two floats"""
    for operator in calc_dict:
        if operator == operation:
            total = calc_dict[operator](n1, n2)
            print(f"{n1} {operator} {n2} = {total}")

    return total


main()