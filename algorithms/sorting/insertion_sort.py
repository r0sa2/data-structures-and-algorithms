from  typing import List

def insertion_sort(ls: List[int]):
    """
    Sorts the input list in-place using the insertion sort algorithm
    """
    for i in range(1, len(ls)):
        val: int = ls[i]
        j: int = i - 1
        
        while j >= 0 and ls[j] > val:
            ls[j + 1] = ls[j]
            j -= 1

        ls[j + 1] = val