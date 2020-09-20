import math

class Search:

    def __init__(self, array):
        self.array = array

    def linearSearch(self, value):
        # loop through array
        for i in range(0, len(self.array)):
            # check if the i element is equal to the searched value
            if self.array[i] == value:
                return i
        return -1

    def binarySearch(self, first, last, value):
        # this search considers the array sorted
        # checks if the first there is still elements to search
        if first <= last:
            middle = (first + last)//2 # get the middle of the array
            if self.array[middle] == value: # checks if the searched element is the middle element
                return middle
            elif self.array[middle] > value: # checks if the searched element is smaller than the middle element
                return self.binarySearch(0, middle - 1, value) # if searched element is smaller than the middle element, it executes binary search again but with last elment being the value of middle - 1
            else:
                return self.binarySearch(middle + 1, last, value) # if searched element is greater than the middle element, it executes binary search again but with first elment being the value of middle + 1
        else:
            return -1

    def executionTime(self, array):
        elements = len(self.array)
        processing = 10000000

        linearComplexity = elements
        executionTime = linearComplexity / processing
        print("Linear Search execution time: {}".format(executionTime))

        binaryComplexity = math.log(elements, 2)
        executionTime = binaryComplexity / processing
        print("Binary Search execution time: {}".format(executionTime))

       

    def mergeSort(self, array):
        if len(array) > 1:
            middle = len(array) // 2 # Get the middle of array
            left = array[:middle] # get the left part of array
            right = array[middle:] # get the right part of array

            self.mergeSort(left) # sorting the left part of array
            self.mergeSort(right) # sorting the right part of array

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

