"""Minimum Priority Queue
For:
    CPE202
    Sections 7 & 9
    Fall 2019
Author:
    Adrian Abarca
"""
class MinPQ:
    """Minimum Priority Queue
    Attributes:
        capacity (int): the capacity of the queue. The default capacity is 2,
            but will be increased automatically.
        num_items (int): the number of items in the queue.
        arr (list): an array which contains the items in the queue.
    """
    def __init__(self, capacity=2):
        """the constructor
        """
        self.capacity = capacity
        self.num_items = 0
        self.arr = [None] * self.capacity

    def __eq__(self, other):
        """checks equality of two nodes
        """
        return isinstance(other, MinPQ) and self.capacity == other.capacity\
               and self.num_items == other.num_items\
               and self.arr == other.arr

    def __repr__(self):
        """repr constructor
        """
        return "MinPQ(cap:%d, items:%d, %s)" % (self.capacity, self.num_items, self.arr)

    def heapify(self, arr):
        """initialize the queue with a given array and conver the array into a min heap
        Args:
            arr (list): an array
        Returns:
            None : it returns nothing
        """
        self.arr = arr
        self.capacity = len(arr)
        self.num_items = self.capacity
        i = (self.num_items - 2)//2
        while i >= 0:
            self.shift_down(i, self.num_items - 1)
            i = i - 1
        return

    def insert(self, item):
        """inserts an item to the queue
        If the capacity == the num_items before inserting an item, enlarge the array.

        Args:
            item (*): an item to be inserted to the queue. It is of any data type.
        Returns:
            None : it returns nothing
        """
        end = self.num_items - 1
        if end is None:
            raise IndexError()
        if self.capacity == self.num_items:
            self.enlarge()
            self.arr[self.num_items] = item
            self.shift_up(end+1)
            self.num_items += 1
        else:
            self.arr[self.num_items] = item
            self.shift_up(end+1)
            self.num_items += 1
        return

    def enlarge(self):
        """enlarges our min heap
        """
        new_arr = [None] * (self.capacity*2)
        for i in range(self.num_items):
            new_arr[i] = self.arr[i]
        self.arr = new_arr
        self.capacity = self.capacity * 2

    def shrink(self):
        """shrinks our min heap
        """
        new_arr = [None] * (self.capacity // 2)
        for i in range(self.num_items):
            new_arr[i] = self.arr[i]
        self.arr = new_arr
        self.capacity = self.capacity // 2

    def del_min(self):
        """deletes the minimum item in the queue
        If the capacity > 2 and num_items > 0 and <= capacity // 4, shrink the array
        Returns:
             * : it returns the minimum item, which has just been deleted
        Raises:
            IndexError : Raises IndexError when the queue is empty
        """
        if self.is_empty():
            raise IndexError
        end = self.num_items - 1
        min_item = self.arr[0]
        self.arr[0] = self.arr[end]
        self.shift_down(0, end-1)
        self.num_items -= 1
        if self.capacity > 2 and (self.num_items > 0 and self.num_items <= (self.capacity // 4)):
            self.shrink()
        return min_item

    def min(self):
        """returns the minimum item in the queue without deleting the item
        Returns:
        * : it returns the minimum item
        Raises:
            IndexError : Raises IndexError when the queue is empty
        """
        if self.is_empty():
            raise IndexError
        return self.arr[0]

    def is_empty(self):
        """checks if the queue is empty
        Returns:
            bool : True if empty, False otherwise.
        """
        return self.num_items == 0

    def size(self):
        """returns the number of items in the queue
        Returns:
            int : it returns the number of items in the queue
        """
        return self.num_items

    def shift_up(self, i):
        """shifts up an item correspondning to an index i
        """
        iparent = self.index_parent(i)
        if iparent < 0 or self.arr[iparent] < self.arr[i]:
            return
        if self.arr[iparent] == self.arr[i]:
            return
        temp = self.arr[i]
        self.arr[i] = self.arr[iparent]
        self.arr[iparent] = temp
        return self.shift_up(iparent)

    def shift_down(self, i, end):
        """shifts down an item corresponding to an index i
        """
        imin = self.min_child(i, end)
        if imin is None or imin < 0:
            return None
        if self.arr[imin] < self.arr[i]:
            temp = self.arr[i]
            self.arr[i] = self.arr[imin]
            self.arr[imin] = temp
        return self.shift_down(imin, end)

    def index_parent(self, idx):
        """returns the index of the parent of given index
        """
        return (idx - 1) // 2

    def min_child(self, i, end):
        """computes the index of the min child of a parent
        """
        left = 2*i + 1
        right = 2*i + 2
        if left > end and right > end:
            return None
        elif left <= end and right <= end:
            if self.arr[left] < self.arr[right]:
                return left
            else:
                return right
        elif left <= end:
            return left
        else:
            return right
