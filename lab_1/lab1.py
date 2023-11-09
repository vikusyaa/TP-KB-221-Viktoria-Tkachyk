list = [
    {"name":"Bob", "phone":"0631234567", "email": "bob@example.com", "age": "25"},
    {"name":"Emma", "phone":"0631234567", "email": "emma@example.com", "age": "20"},
    {"name":"Jon",  "phone":"0631234567", "email": "jon@example.com", "age": "19"},
    {"name":"Zak",  "phone":"0631234567", "email": "zak@example.com", "age": "21"}
]

def printAllList():
    for elem in list:
        strForPrint = (
            "Student name is " + elem["name"] +
            ", Phone is " + elem["phone"] +
            ", Email is " + elem["email"] +
            ", Age is " + elem["age"]
        )
        print(strForPrint)
    return

def addNewElement():
    name = input("Please enter student name: ")
    phone = input("Please enter student phone: ")
    email = input("Please enter student email: ")
    age = input("Please enter student age: ")

    newItem = {"name": name, "phone": phone, "email": email, "age": age}
    
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
        del list[deletePosition]
        print("Element has been deleted")
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
        print("Updating information for " + name)
        phone = input("Please enter updated phone: ")
        email = input("Please enter updated email: ")
        age = input("Please enter updated age: ")

        updatedItem = {"name": name, "phone": phone, "email": email, "age": age}
        list[updatePosition] = updatedItem
        print("Element has been updated")
    return


def main():
    while True:
        choice = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ")
        match choice:
            case "C":
                print("New element will be created:")
                addNewElement()
                printAllList()
            case "U":
                print("Existing element will be updated")
                updateElement()
                printAllList()
            case "D":
                print("Element will be deleted")
                deleteElement()
                printAllList()
            case "P":
                print("List will be printed")
                printAllList()
            case "X":
                print("Exit()")
                break
            case _:
                print("Wrong choice")

main()
