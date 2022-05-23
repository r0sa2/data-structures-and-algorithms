from typing import List

def bubble_sort(ls: List[int]):
    """
    Sorts the input list in-place using the bubble sort algorithm
    """
    for i in range(len(ls)):
        swapped: bool = False

        for j in range(len(ls) - i - 1):
            if ls[j] > ls[j + 1]:
                swapped = True
                ls[j], ls[j + 1] = ls[j + 1], ls[j]
        
        if not swapped:
            return


