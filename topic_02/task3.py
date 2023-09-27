value1 = float(input("Введіть першу цифру: "))
value2 = float(input("Введіть другу цифру: "))
operation = input("Введіть операцію (+, -, *, /): ")

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Ділення на нуль неможливе."
    return x / y

def calculator_match(value1, value2, operation):
     match operation:
        case '+': return add(value1, value2)
         
        case '-': return subtract(value1, value2)
         
        case '*': return multiply(value1, value2)
         
        case '/': return divide(value1, value2)
         
        case _: return "Будь ласка, введіть +, -, *, або /."

result = calculator_match(value1, value2, operation)
print(f"Результат: {result}")
