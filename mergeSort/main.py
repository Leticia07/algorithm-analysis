
def mergeSort(array):
    if len(array) > 1:
        middle = len(array) // 2 # Get the middle of array
        left = array[:middle] # get the left part of array
        right = array[middle:] # get the right part of array

        mergeSort(left) # sorting the left part of array
        mergeSort(right) # sorting the right part of array

        i = j = k = 0 # start each partition on position 0

        # loop through left and right array and merging the elements on the array
        while i < len(left) and j < len(right):
            if left[i] < right[j]: # check if element i on left array is greater than element j on right array
                array[k] = left[i] # adding element i on left array to the final array
                i += 1 # it goes to next position of the left array
            else:
                array[k] = right[j] # adding element j on right array to the final array
                j += 1 # it goes to next position of the right array
            k += 1 # it goes to next position on the final array

        # Checking if any element was left on the left array
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
        
        # Checking if any element was left on the right array
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
        
        return array

if __name__ == '__main__':
    print("============== Merge sort ==============")
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

    array = mergeSort(array)
    
    print("Sorted array {}".format(array))
    print("============================================")
