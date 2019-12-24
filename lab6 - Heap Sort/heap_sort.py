"""Contains code for Heap Sort
CPE 202
Lab 6
Author: Adrian Abarca
"""
from max_heap import del_max

def sort(arr):
    """sorts a max heap array
    Args:
        arr (list): max heap array
    Returns:
        list: sorted list 
    """
    unsort = [None] * len(arr)
    while len(arr) > 1:
        item = del_max(arr)
        unsort.append(item)
    return unsort
