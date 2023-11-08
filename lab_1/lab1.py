
list = [
    {"name": "Den", "phone": "0631234567", "age": 20, "email": "den@gmail.com"},
    {"name": "Anna", "phone": "0631234567", "age": 22, "email": "anna@gmail.com"},
    {"name": "Max",  "phone": "0631234567", "age": 21, "email": "max@gmail.com"},
    {"name": "Kate",  "phone": "0631234567", "age": 23, "email": "kate@gmail.com"}
]

def printAllList():
    for elem in list:
        strForPrint = "Student name is " + elem["name"] + ", Phone is " + elem["phone"] + ", Age is " + str(elem["age"]) + ", Email is " + elem["email"]
        print(strForPrint)
    return

def addNewElement():
    name = input("Please enter student's name: ")
    phone = input("Please enter student's phone: ")
    age = input("Please enter student's age: ")
    email = input("Please enter student's email: ")
    newItem = {"name": name, "phone": phone, "age": age, "email": email}
    
    insertPosition = 0
    for item in list:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    list.insert(insertPosition, newItem)
    print("New element has been added")
    return

def deleteElement():
    name = input("Please enter name to be deleted: ")
    deletePosition = -1
    for item in list:
        if name == item["name"]:
            deletePosition = list.index(item)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        print("Delete position: " + str(deletePosition))
        del list[deletePosition]
    return


def updateElement():
    name = input("Please enter name to be updated: ")
    updatePosition = -1
    for item in list:
        if name == item["name"]:
            updatePosition = list.index(item)
            break
    if updatePosition == -1:
        print("Element was not found")
    else:
        phone = input("Please enter updated phone: ")
        age = input("Please enter updated age: ")
        email = input("Please enter updated email: ")
        updatedItem = {"name": name, "phone": phone, "age": age, "email": email}
        list[updatePosition] = updatedItem
        print("Element has been updated")
    return

def main():
    while True:
        choice = input("Please specify the action [ C create, U update, D delete, P print, X exit ] ")
        if choice.lower() == "c":
            print("New element will be created:")
            addNewElement()
        elif choice.lower() == "u":
            print("Existing element will be updated")
            updateElement()
        elif choice.lower() == "d":
            print("Element will be deleted")
            deleteElement()
        elif choice.lower() == "p":
            print("List will be printed")
            printAllList()
        elif choice.lower() == "x":
            print("Exit()")
            break
        else:
            print("Wrong choice")

main()
