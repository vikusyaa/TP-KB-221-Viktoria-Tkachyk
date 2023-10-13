def findMinElemWithIndex(listForSearch):
    min_elem = min(listForSearch)
    min_index = listForSearch.index(min_elem)
    return min_index, min_elem

def findMaxElemWithIndex(listForSearch):
    max_elem = max(listForSearch)
    max_index = listForSearch.index(max_elem)
    return max_index, max_elem

def main():
    listOfData = [11, 14, 22, 33, 7, 88, 123, 345, 64, 10, 5, 55, 66, 44, 20]
    
    result = findMinElemWithIndex(listOfData)
    print(f"Min id: {result[0]}, Min value: {result[1]}") # 10

    result = findMaxElemWithIndex(listOfData)
    print(f"Max id: {result[0]}, Max value: {result[1]}") # 7

if __name__ == "__main__":
    main()