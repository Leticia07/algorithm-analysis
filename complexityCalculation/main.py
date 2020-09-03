from calculation import Calculation

if __name__ == '__main__':

    while True:

        try:

            print("================ Calculating execution time ================")
            print("** You can insert 0 at any moment to stop")
            elements = int(input("Number of elements: "))
            if elements == 0:
                break
            processing = int(input("Number of instructions executed by the computer per second: "))
            if processing == 0:
                break
            
            calc = Calculation(elements, processing)

            while True:
                print("What do you want to do?")
                sort = int(input("1 - Insertion Sort\n2 - Intercalation Sort\n3 - See chart\n0 - Start Over\n"))

                if sort == 0:
                    break
                elif sort == 1:
                    print("================ Insertion Sort ================")
                    print("Number of elements: {}".format(elements))
                    print("Number of instructions executed by the computer per second: {}".format(processing))
                    print(calc.insertionSort())
                    print("================================================")
                elif sort == 2:
                    print("================ Intercalation Sort ================")
                    print("Number of elements: {}".format(elements))
                    print("Number of instructions executed by the computer per second: {}".format(processing))
                    print(calc.intercalationSort())
                    print("====================================================")
                elif sort == 3:
                    calc.chart()

        except Exception as e:
            print(e)

        