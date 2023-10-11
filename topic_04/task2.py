def addition(n1, n2):
    return n1 + n2

def subtraction(n1, n2):
    return n1 - n2

def mmultiplication(n1, n2):
    return n1 * n2

def ddivision(n1, n2):
    if n2 == 0:
        raise ValueError("Ділення на нуль неможливе")
    return n1 / n2

while True:
    print("Оберіть операцію:")
    print("1. Додавання = '+' ")
    print("2. Віднімання = '-' ")
    print("3. Множення = '*' ")
    print("4. Ділення = '/' ")
    print("5. Вихід = '0'")

    operation = input('Введіть знак операції:')

    if operation == '0':
        print("Дякую за використання калькулятора!")
        break

    if operation not in ('+', '-', '*', '/'):
        print("Дякую за використання калькулятора")
        continue

    try:
        n1 = float(input("Введіть першу цифру: "))
        n2 = float(input("Введіть другу цифру: "))

        result = None

        if operation == '+':
            result = addition(n1, n2)
        elif operation == '-':
            result = subtraction(n1, n2)
        elif operation == '*':
            result = mmultiplication(n1, n2)
        elif operation == '/':
            try:
                result = ddivision(n1, n2)
            except ValueError as e:
                print(f"Помилка: {e}")
                continue

        print("Результат:", result)
    except ValueError:
        print("Введення невірне. Введіть дійсні числа.")