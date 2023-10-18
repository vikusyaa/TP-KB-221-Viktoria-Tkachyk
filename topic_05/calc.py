from functions import*
from operations import*

def main():
    operation = input("Введіть операцію (+, -, *, /): ")
    num1 = float(input("Введіть першу цифру: "))
    num2 = float(input("Введіть другу цифру: "))

    result = perform_operation(operation, num1, num2)
    if result is None:
        print("Невідома операція")
    else:
        print("Результат:", result)

if __name__ == "__main__":
    main()

