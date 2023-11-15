students_list = [
    {"name": "Bob", "phone": "0631234567", "age": 20, "email": "bob@gmail.com"},
    {"name": "Emma", "phone": "0631234567", "age": 22, "email": "emma@gmail.com"},
    {"name": "Jon", "phone": "0631234567", "age": 21, "email": "jon@gmail.com"},
    {"name": "Zak", "phone": "0631234567", "age": 19, "email": "zak@gmail.com"}
]


def print_all_list():
    sorted_students = sorted(students_list, key=lambda x: x["name"])  
    for student in sorted_students:
        str_for_print = f"Student name {student['name']}, age {student['age']}, phone {student['phone']}, email {student['email']}"
        print(str_for_print)
    print()


def add_new_element():
    name = input("Please enter the name of the student: ")
    age = int(input("Please enter the age of the student: "))
    phone = input("Please enter the student`s phone number: ")
    email = input("Please enter the student`s email: ")
    new_student = {"name": name, "phone": phone, "age": age, "email": email}
    
    students_list.append(new_student)
    students_list.sort(key=lambda x: x["name"])  
    print("New element has been added")
    print_all_list()


def delete_element(): 
    name = input("Please enter name to be deleted: ")
    delete_position = -1
    for student in students_list:
        if name == student["name"]:
            delete_position = students_list.index(student)
            break
    if delete_position == -1:
        print("Element was not found")
    else:
        del students_list[delete_position]
        print("Element has been removed")
        print_all_list()


def update_element():
    name = input("Please enter name to be updated: ")
    for index, student in enumerate(students_list):
        if name == student["name"]:
            new_name = input("Enter a new name: ")
            new_age = int(input("Enter a new age: "))
            new_phone = input("Enter a new phone: ")
            new_email = input("Enter a new email: ")
            new_element = {"name": new_name, "age": new_age, "phone": new_phone, "email": new_email}

            del students_list[index]
            insert_position = 0
            for pos, elem in enumerate(students_list):
                if new_name > elem["name"]:
                    insert_position = pos + 1
                else:
                    break
            students_list.insert(insert_position, new_element)
            print("Element has been updated")
            print_all_list()
            break
    else:
        print("Element was not found")


def main():
    while True:
        choice = input("Please specify the action [C create, U update, D delete, P print, X exit]: ")
        if choice.upper() == "C":
            print("New element will be created:")
            add_new_element()
        elif choice.upper() == "U":
            print("Existing element will be updated")
            update_element()
        elif choice.upper() == "D":
            print("Element will be deleted")
            delete_element()
        elif choice.upper() == "P":
            print("List will be printed")
            print_all_list()
        elif choice.upper() == "X":
            print("Exit")
            break
        else:
            print("Wrong choice")


main()
