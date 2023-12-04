import csv
from sys import argv
import os


def load_data(path):
    students = []
    try:
        with open(path, newline='') as file:
            reader = csv.DictReader(file)
            for student in reader:
                students.append(student)
        return students
    except FileNotFoundError:
        print("Файл не знайдено!")
        return None

def showData(data):
    for student in data:
        print("Ім'я: ", student["Name"], sep="")
        print("Номер телефону: +", student["Phone"], sep="", end="\n")

def saveData(path, data):
    flag = False
    try:
        with open(path, 'w', newline='') as file:
            if data:
                field_names = data[0].keys()
            else:
                field_names = []
            writer = csv.DictWriter(file, fieldnames=field_names)
            writer.writeheader()
            for student in data:
                writer.writerow(student)
        flag = True
    except IOError:
        print("Помилка при спробі зберегти дані")
    return flag

def addStudent(data):
    name = input("Введіть ім'я нового студента: ")
    phone_number = input("Введіть номер телефону нового студента: ")
    data.append({"Name": name, "Phone": phone_number})

def deleteUser(data):
    name_to_remove = input("Введіть ім'я користувача, якого треба видалит із файлу: ")

    result = [item for item in data if item['Name'] != name_to_remove]
    return result

def to_continue():
    user_input = input("Продовжуємо? (y/n): ")
    if user_input.lower() == 'y':
        return True
    return False

def main():
    if len(argv) < 2:
        print("Ім'я файлу не було передано в програму")
        return
    file_path = os.path.dirname(os.path.realpath(__file__)) + "\\" + argv[1]
    student_data = load_data(file_path)
    if(student_data):

        student_data = load_data(file_path)

        print("Оберіть дію: ", "\tОберіть '1', щоб отримати інформацію про студентів", "\tОберіть '2', щоб дописати нового студента до файлу", "\tОберіть '3', щоб видалити користувача з файлу", sep="\n")
        while True:
            user_action = input("Дія: ")
            if user_action == "1":
                showData(student_data)
            elif user_action == "2":
                addStudent(student_data)
            elif user_action == "3":
                student_data = deleteUser(student_data)
            else:
                print("Такої дії не існує!")
            if to_continue() != True:
                break
        if(saveData(file_path, student_data)):
            print(f"Дані збережено до {file_path}")

    else:
        print("Failed to read file!")
        return

if __name__ == "__main__":
    main()