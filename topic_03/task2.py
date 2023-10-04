def test_list_functions():
    
    list = [1, 2, 3, 4, 5]
    
    new_elements = [6, 7, 8]
    list.extend(new_elements)
    print("Після використання extend():", list)
    
    list.append(9)
    print("Після використання append():", list)

    list.insert(2, 10)
    print("Після використання insert():", list)

    list.remove(3)
    print("Після використання remove():", list)

    list.clear()
    print("Після використання clear():", list)
  
    list = [5, 3, 1, 4, 2]

    list.sort()
    print("Після використання sort():", list)

    list.reverse()
    print("Після використання reverse():", list)

    copied_list = list.copy()
    print("Копія списку:", copied_list)

test_list_functions()
