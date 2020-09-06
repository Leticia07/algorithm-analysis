
def insertionSort(array):
    # loop through uunsorted elements, considering first element sorted
    for i in range(1, len(array)):
        # select first unsorted element
        elementToSort = array[i]
        # initialize position as the previous position
        position = i - 1
        # loop through last sorted index to index 0, checking if current element is greater than the elementToSort
        for j in range(i - 1, -1, -1):
            # checks if current element is greater than elementToSort
            if array[j] > elementToSort:
                # move sorted element to the right
                array[j + 1] = array[j]
                # sets the position of greater element to be the position where the elementToSort has to be inserted
                position = j
            else:
                # in this case the current element is smaller than elementToSort so elementToSort has to stay on the same position
                position = j + 1
                break
        array[position] = elementToSort
        print("{} - {}".format(i, array))
    
    return array

if __name__ == '__main__':
    print("============== Insertion sort ==============")
    #array = [4, 3, 2, 10, 12, 1, 5, 6]
    array = []
    ans = 1
    print("Insert 'd' to sort default array")
    while ans != "q":
        print('** You can insert "q" to confirm the array')
        element = input("Insert a element: ")
        if element == "q":
            break
        elif element == "d":
            array = [4, 3, 2, 10, 12, 1, 5, 6]
            break
        try:
            array.append(int(element))
        except Exception as e:
            print(e)

    print("Array to sort {}".format(array))

    array = insertionSort(array)
    
    print("Sorted array {}".format(array))
    print("============================================")
