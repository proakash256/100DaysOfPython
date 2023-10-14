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
        c = input("Type y if you want to continue the calculation or type n to start a fresh calculation: ")
        if c == "y":
            a = answer
        else:
            should_continue = False
            calculator()


calculator()
