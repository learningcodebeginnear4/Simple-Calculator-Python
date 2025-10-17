def add(x, y):
    return (x+y)
def subtract(x, y):
    return (x-y)
def multiply(x, y):
    return (x*y)
def divide(x, y):
    if y != 0:
        return (x, y)
    else:
        return(x/y)
while True:
    b = input("Do you want to use a calculator ? y/n:")
    if b == "y":
        x = int(input("Enter a number:"))
        y = int(input("Enter a number:"))
        op = input("Enter an operator +, -, /, or *: ")
        if op == '+':
            add(x, y)
            print(x+y)
        elif op == '-':
            subtract(x, y)
            print(x-y)
        elif op == '*':
            multiply(x, y)
            print(x*y)
        elif op=='/':
            divide(x, y)
            print(x/y)
        else:
            print("Invalid input. Please type out the provided options.")
            op = input("Type out a operation ('+', '-', '*', '/'):")
    elif b == "n":
        print("Done")
        break