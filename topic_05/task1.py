import random

def play_game():
    user = input("Оберіть Камінь, Ножиці, Папір: ")
    options = ['Камінь', 'Ножиці', 'Папір']
    computer = random.choice(options)

    print(f"Ваш вибір: {user}")
    print(f"Вибір комп'ютера: {computer}")

    if user == computer:
        print("Нічия!")
    elif (user == 'Камінь' and computer == 'Ножиці') or (user == 'Ножиці' and computer == 'Папір') or (user == 'Папір' and computer == 'Камінь'):
        print("Ви перемогли!")
    else:
        print("Переміг комп'ютер!")

play_game()