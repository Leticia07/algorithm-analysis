import pandas as pd
import matplotlib.pyplot as plt
import math

class Calculation:

    def __init__(self, elements, processing):
        self.elements = elements
        self.processing = processing

    def sortCalculation(self, complexity):
        try:
            return complexity / self.processing
        except Exception as e:
            print(e)

    def insertionSort(self):
        complexity = 2 * (self.elements) ** 2
        self.insertionSortExecution = self.sortCalculation(complexity)
        return self.insertionSortExecution
    
    def intercalationSort(self):
        complexity = self.elements * math.log(self.elements, 10)
        self.intercalationSortExecution = self.sortCalculation(complexity)
        return self.intercalationSortExecution

    def chart(self):
        columns = ['type', 'value']
        values = [["Insertion", round(self.insertionSort(), 2)],["Intercalation", round(self.intercalationSort(), 2)]]
        sort = pd.DataFrame(values, columns=columns)
        textstr = "Insertion - {}\nIntercalation - {}".format(round(self.insertionSort(), 2), round(self.intercalationSort(), 2))
        print(sort)
        ax = sort.plot('type', 'value', kind='bar', legend=False, rot=0)
        plt.gcf().text(0.02, 0.5, textstr, fontsize=10)
        plt.gcf().canvas.set_window_title('Execution Time')
        ax.set_xlabel("Types", fontsize=6)
        ax.set_ylabel("Execution time", fontsize=6)
        plt.subplots_adjust(left=0.35)
        plt.show()