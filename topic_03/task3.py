def test_dict_functions():
   
    dict = {"a": "1", "b": 2,}
   
    dict.update({"a": 1, "b": 2})
    print("update():", dict)

    del dict["b"]
    print("Після використання del():", dict)

    dict.clear()
    print("Після використання clear():", dict)
 
    dict = {"name": "Dasha", "age": 15, "city": "London"}

    keys = dict.keys()
    print("Ключі словника:", keys)

    values = dict.values()
    print("Значення словника:", values)
 
    items = dict.items()
    print("Елементи словника:", items)

test_dict_functions()
 