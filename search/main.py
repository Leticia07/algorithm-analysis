from search import Search

if __name__ == '__main__':

    print("============== Search ==============")
    array = []
    ans = 1

    typeArray = input("The array are going to be string or integer? (s - String/ i - Integer): ")
    while typeArray.lower() != "s" and typeArray != "i":
        typeArray = input("The array are going to be string or integer? (s - String/ i - Integer): ")

    print("Insert 'd' to select default array")
    while ans != "q":
        print('** You can insert "q" to confirm the array')
        element = input("Insert a element: ")
        if element == "q":
            break
        elif element == "d":
            if typeArray.lower() == "i":
                array = [14, 31, 57, 65, 76, 85, 92]
            else:
                array = ["14", "31", "57", "65", "76", "85", "92"]
            break
        try:
            if typeArray.lower() == "i":
                array.append(int(element))
            else:
                array.append(element)
        except Exception as e:
            print(e)

    print("Array: {}".format(array))
    s = Search(array)
    
    valueToSearch = input("Insert the value you want to search: ")
    while True:
        try:
            if typeArray == "i":
                valueToSearch = int(valueToSearch)
            break
        except Exception as e:
            print(e)
            valueToSearch = input("Insert the value you want to search: ")

    needsToSort = input("The array is already sorted? (Y/n) \n**It is important to the binary search ")
    while needsToSort.lower() != "y" and needsToSort.lower() != "n":
        needsToSort = input("The array is already sorted? (Y/n) ")

    if needsToSort.lower() == "n":
        array = s.mergeSort(array)
        print(array)

    positionLinear = s.linearSearch(valueToSearch)
    positionBinary = s.binarySearch(0, len(array) - 1,valueToSearch)
    print("The position of element is: {}".format(positionBinary))

    print("============== Execution time ==============")
    s.executionTime(array)
