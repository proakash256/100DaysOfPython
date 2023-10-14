import art

print(art.logo)


def add(a, b):
    """ Adds Two Numbers """
    return a + b


def subtract(a, b):
    """ Subtracts Two Numbers """
    return a - b


def multiply(a, b):
    """ Multiplies Two Numbers """
    return a * b


def divide(a, b):
    """ Divides Two Numbers """
    return a / b


def calculator():
    operations = {"+": add, "-": subtract, "*": multiply, "/": divide}
    a = float(input("Enter the First Number : "))
    should_continue = True
    while should_continue:
        for i in operations:
            print(i)
        s = input("Pick one operation : ")
        b = float(input("Enter the Next Number : "))
        answer = operations[s](a, b)
        print(f"{a} {s} {b} = {answer}")
        print("Type y to continue the calculation")
        print("Type n to start a new calculation")
        print("Type q to quit")
        c = input("Enter your choice: ")
        if c == "y":
            a = answer
        elif c == "n":
            should_continue = False
            calculator()
        else:
            return


calculator()
