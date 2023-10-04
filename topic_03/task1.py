def calculator():
    print("Вітаю в калькуляторі!")

    while True:
        print("Оберіть операцію:")
        print("1. Додавання")
        print("2. Віднімання")
        print("3. Множення")
        print("4. Ділення")
        print("0. Вийти")

        choice = input("Ваш вибір (0/1/2/3/4): ")
        
        if choice == '0':
            print("Дякую за використання калькулятора!")
            break

        num1 = float(input("Введіть перше число: "))
        num2 = float(input("Введіть друге число: "))

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

        print()  


calculator()
