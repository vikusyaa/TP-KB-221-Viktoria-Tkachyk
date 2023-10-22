from functions import add, subtract, multiply, divide

def get_numbers():
    num1 = float(input("Введіть перше число: "))
    num2 = float(input("Введіть друге число: "))
    return num1, num2

def perform_operation(operation, num1, num2):
    if operation == "+":
        return add(num1, num2)
    elif operation == "-":
        return subtract(num1, num2)
    elif operation == "*":
        return multiply(num1, num2)
    elif operation == "/":
        return divide(num1, num2)
    else:
        print("Невідома операція")
        return None
    #update