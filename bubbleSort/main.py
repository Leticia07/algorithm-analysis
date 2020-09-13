
def swap(array, position):
    aux = array[position - 1]
    array[position - 1] = array[position]
    array[position] = aux

def bubbleSort(array):
    swapped = True
    lastUnsortedElement = len(array)
    # loop through array till elements are on the right position
    while swapped:
        # sets swapped to false, cause at first no elements were swapped
        swapped = False
        # loop through 1 till last unsorted index
        for i in range(1, lastUnsortedElement):
            # checking if left element is bigger than right element
            if array[i - 1] > array[i]:
                # swaps elements
                swap(array, i)
                # sets swapped to true which indicates that maybe the array is not sorted yet and garantees that the external loop continues
                swapped = True
        # when the previous loop ends the last element on array is on the right position
        lastUnsortedElement -= 1

    return array

if __name__ == '__main__':
    print("============== Bubble sort ==============")
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
            array = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
            break
        try:
            array.append(int(element))
        except Exception as e:
            print(e)

    print("Array to sort {}".format(array))

    array = bubbleSort(array)
    
    print("Sorted array {}".format(array))
    print("============================================")
