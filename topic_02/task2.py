def calculator():
    print("Вітаю в калькуляторі!")
    print("Оберіть операцію:")
    print("1. Додавання")
    print("2. Віднімання")
    print("3. Множення")
    print("4. Ділення")

    # Вибір операції
    choice = input("Ваш вибір (1/2/3/4): ")

    # Введення чисел
    num1 = float(input("Введіть перше число: "))
    num2 = float(input("Введіть друге число: "))

    # Виконання операції 
    if choice == '1':
        result = num1 + num2
        print("Результат додавання:", result)
    elif choice == '2':
        result = num1 - num2
        print("Результат віднімання:", result)
    elif choice == '3':
        result = num1 * num2
        print("Результат множення:", result)
    elif choice == '4':
        if num2 != 0:
            result = num1 / num2
            print("Результат ділення:", result)
        else:
            print("Помилка: Ділення на нуль неможливе!")
    else:
        print("Помилка: Невірний вибір операції!")

calculator()