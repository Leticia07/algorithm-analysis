## Algorithm Analysis

Code created to the UNIT's Algorithm Analysis Laboratory class

## Libs
 - [Pandas](https://pandas.pydata.org/)
 - [matplotlib](https://matplotlib.org/)
 - [math](https://docs.python.org/3/library/math.html)

## Complexity Calculation

To run the code

```bash
# Clone this repository
git clone https://github.com/Leticia07/algorithm-analysis.git

# Go into the directory
cd complexityCalculation

# Run the main file
python main.py
```

Brief 

Complexity calculation is a way of describing the efficiency of an algorithm. Each algorithm has its complexity and it can affect the execution time. To calculate the execution time we need to know the number of instructions that the algorithm will make and how many instructions the computer can execute per second.
The formula we use is:

![equation](https://latex.codecogs.com/gif.latex?%5Cfrac%7Balgorithm%7D%7Bcomputer%7D)

In this code we can calculate the execution time of two algorithms:
- Insertion Sort: complexity = ![equation](https://latex.codecogs.com/gif.latex?2n%5E2)
- Intercalation Sort: complexity = ![equation](https://latex.codecogs.com/gif.latex?nlog%28n%29)

## Insertion Sort

To run the code

```bash
# Clone this repository, if you haven't done it
git clone https://github.com/Leticia07/algorithm-analysis.git

# Go into the directory
cd insertionSort

# Run the main file
python main.py
```

Brief 

This algorithm sorts an array as an element is inserted. We start from the second position of an array (position 1) and then we go checking if the new element is smaller than the other so we maintain our array sorted. As we confirm if the inserted element is smaller than the element on the left, we move this element to the right by one.

---
Made with ♥ by Letícia Aragão :wave: [Get in touch!](https://www.linkedin.com/in/leticiaaragao/)