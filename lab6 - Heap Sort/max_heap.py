"""Contains code for Max Heap
CPE 202
Lab 6
Author: Adrian Abarca
"""

def insert(arr, item, end):
    """inserts an item to the heap
    Args:
        arr (list): heap array
        item (int): item you want to add
        end (int): end of the max heap
    Returns:
        list: heap after item was inserted
    Raises:
        IndexError: if end is none or the end of the list
    """
    if end is None or end == (len(arr)-1):
        raise IndexError
    arr[end+1] = item
    shift_up(arr, end)
    return arr

def del_max(arr, end=None):
    """deletes the max item in the heap
    Args:
        arr (list): heap array
        end (int): end of the heap
    Returns:
        list: arr after deleting max
        int: max value that was deleted
        int: end of the list
    """
    end = len(arr) - 1
    max_val = arr[0]
    arr[0] = arr[end]
    shift_down(arr, 0, end-1)
    return arr, max_val, end-1

def shift_up(arr, index):
    """shifts up item at index
    Args:
        arr (list): heap array
        index (int): index of item you want to shift up
    """
    idxparent = index_parent(index)
    if arr[idxparent] is None:
        return
    if idxparent < 0 or arr[idxparent] >= arr[index]:
        return
    temp = arr[index+1]
    arr[index+1] = arr[idxparent]
    arr[idxparent] = temp
    return shift_up(arr, idxparent)

def shift_down(arr, index, end):
    """shifts down item at index
    Args:
        arr (list): heap array
        index (int): index of item you want to shift down
        end (int): end of the heap array
    """
    max_idx = index_maxchild(arr, index, end)
    if max_idx < 0:
        return None
    if arr[max_idx] is None:
        return None
    temp = arr[index]
    arr[index] = arr[max_idx]
    arr[max_idx] = temp
    return shift_down(arr, max_idx, end)
    
def heapify(arr):
    """heapifies an arr
    Args:
        arr (list): heap array
    Returns:
        list: array that has been heapified
    """
    length = len(arr)
    idx = index_parent(length - 1)
    while idx >= 0:
        shift_down(arr, idx)
        idx = idx - 1
    return arr

def index_parent(idx):
    """computes parent of an index
    Args:
        idx (int): index of item you want to find parent of
    Returns:
        int: index of the parent
    """
    return (idx - 1) // 2

def index_left(idx):
    """computes left child of an index
    Args:
        idx (int): index of item you want to find left child
    Returns:
        int: left child of the index node
    """
    return 2 * (idx) + 1

def index_right(idx):
    """computes right child of an index
    Args:
        idx (int): index of item you want to find right child
    Returns:
        int: right child of the index node
    """
    return 2 * (idx) + 2

def index_maxchild(arr, idx, end):
    """computes max child of an index
    Args:
        arr (list): heap array
        idx (int): index interested in of finding max child
        end (end): end index of heap array
    Returns:
        int: max child of the index
    """
    left = arr[index_left(idx)]
    right = arr[index_right(idx)]
    if left <= end and right <= end:
        if left > right:
            return left
        else:
            return right
