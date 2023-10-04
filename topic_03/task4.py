list = ["1", "2", "3"]

while True:
    new_value = input("Нове число (або 'вихід' щоб вийти): ")

    if new_value == 'вихід':
        break

    insert_index = 0

    for elem in list:
        if new_value > elem:
            insert_index += 1

    list.insert(insert_index, new_value)

    print("Result:", list)