from typing import List

def merge(ls: List[int], left_index: int, mid_index: int, right_index: int):
    """
    Helper function for merge_sort. Merges the sorted subarrays ls[left_index : mid_index + 1]
    and ls[mid_index + 1 : right_index + 1] into the sorted subarray ls[left_index : right_index + 1].
    """
    L: List[int] = [0] * (mid_index - left_index + 1)
    R: List[int] = [0] * (right_index - mid_index)

    for i in range(len(L)):
        L[i] = ls[left_index + i]
    for i in range(len(R)):
        R[i] = ls[mid_index + 1 + i]

    i: int = 0
    j: int = 0
    k: int = left_index

    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            ls[k] = L[i]
            i += 1
        else:
            ls[k] = R[j]
            j += 1
        k += 1
    
    while i < len(L):
        ls[k] = L[i]
        i += 1
        k += 1
    
    while j < len(R):
        ls[k] = R[j]
        j += 1
        k += 1

def merge_sort(ls: List[int], left_index: int, right_index: int):
    """
    Sorts the subarray ls[left_index : right_index + 1] in-place using the merge sort algorithm
    """
    if left_index >= right_index:
        return
    
    mid_index: int = (left_index + right_index) // 2

    merge_sort(ls, left_index, mid_index)
    merge_sort(ls, mid_index + 1, right_index)
    merge(ls, left_index, mid_index, right_index)