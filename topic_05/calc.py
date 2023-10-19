from functions import*
from operations import*

def main():
    operation = input("Введіть операцію (+, -, *, /): ")
    a = float(input("Введіть перше значення: "))
    b = float(input("Введіть друге значення: "))

    result = perform_operation(operation, a, b)
    if result is None:
        print("Невідома операція")
    else:
        print("Результат:", result)

if __name__ == "__main__":
    main()

