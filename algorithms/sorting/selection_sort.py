from typing import List

def selection_sort(ls: List[int]):
    """
    Sorts the input list in-place using the selection sort algorithm
    """
    for i in range(len(ls) - 1):
        min_index: int = i

        for j in range(i + 1, len(ls)):
            if ls[j] < ls[min_index]:
                min_index = j

        ls[i], ls[min_index] = ls[min_index], ls[i]