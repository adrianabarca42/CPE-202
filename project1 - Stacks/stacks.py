"""Contains code for StackADTs
CPE202
Project 1

Author:
    Adrian Abarca
"""
from Node import Node

class StackArray:
    """class for Stack Array
    Attributes:
        arr (list) : An array
        num_items (int) : number of items
        capacity (int) : capacity
    """
    def __init__(self):
        """The Constructor
        Args:
            arr (list) : An array
            num_items (int) : number of items
            capacity (int) : capacity
        """
        self.capacity = 2
        self.arr = [None] * self.capacity
        self.num_items = 0

    def __repr__(self):
        """representation function
        Returns:
            StackArray in a string representation
        """
        return "StackArray(%s)" % self.arr

    def __eq__(self, other):
        """checks equality of two different object types StackArray
        Args:
            other (StackArray): another StackArray
        Returns:
            Boolean: true if two StackArray objects are equal
        """
        return isinstance(other, StackArray) and self.arr == other.arr\
               and self.capacity == other.capacity\
               and self.num_items == other.num_items

    def enlarge(self):
        """enlarges the array by twice the current capacity
        """
        new_arr = [None] * (self.capacity * 2)
        for i in range(self.num_items):
            new_arr[i] = self.arr[i]
        self.arr = new_arr
        self.capacity = self.capacity * 2

    def shrink(self):
        """creates a new array half the size of the original with the same elements
        """
        new_arr = [None] * (self.capacity // 2)
        for i in range(self.num_items):
            new_arr[i] = self.arr[i]
        self.arr = new_arr
        self.capacity = self.capacity // 2

    def is_full(self):
        """determines when our stack array is full
        Returns:
            Boolean: true when array is full, false otherwise
        """
        return self.capacity == self.num_items

    def is_empty(self):
        """determines when our stack array is empty
        Returns:
            Boolean: true when array is empty, false otherwise
        """
        return self.num_items == 0

    def push(self, item):
        """adds an element to the "top" of our array
        Attributes:
            item (*): item of any type we want to append to our array
        """
        if self.is_full():
            self.enlarge()
            self.arr[self.num_items] = item
        self.arr[self.num_items] = item
        self.num_items += 1

    def pop(self):
        """removes item from the top of our stack
        Returns:
            temp (*): item of any type on the top of our stack
        """
        if self.is_empty():
            raise IndexError
        else:
            if self.capacity / self.num_items >= 4:
                self.shrink()
        self.num_items -= 1
        temp = self.arr[self.num_items]
        self.arr = self.arr[:self.num_items]
        return temp

    def peek(self):
        """Returns item from the top of our stack
        Returns:
            int or string: item on the top of our stack
        """
        if self.num_items == 0:
            return None
        return self.arr[self.num_items - 1]

    def size(self):
        """determines the size of the array
        Returns:
            int: size of our array
        """
        return self.num_items

class StackLinked:
    """Class definition for a Stack using Linked Lists
    Attributes:
        top (None or Node): the stacked linked list
        num_items (int): number of items in the linked list
    """

    def __init__(self):
        """the constructor
        Args:
            top (None or Node): the stacked linked list
            num_items (int): number of items in the linked list
        """
        self.top = None
        self.num_items = 0

    def __repr__(self):
        """the representation function
        Returns:
            string: string representation of StackLinked
        """
        return "StackLinked(%s)" % self.top

    def __eq__(self, other):
        """checks equality of two different object types StackLinked
        Args:
            other (StackLinked): another StackLinked
        Returns:
            Boolean: true if two StackLinked objects are equal
        """
        return isinstance(other, StackLinked) and self.top == other.top\
               and self.num_items == other.num_items

    def is_empty(self):
        """determines when our stack linked list is empty
        Returns:
            Boolean: true when list is empty, false otherwise
        """
        return self.num_items == 0

    def push(self, item):
        """adds an element to the "top" of our list
        Attributes:
            item (*): item of any type we want to append to our list
        """
        if self.top is None:
            self.top = Node(item, None)
        else:
            new_node = Node(item, None)
            new_node.next1 = self.top
            self.top = new_node
        self.num_items += 1

    def pop(self):
        """removes item from the top of our stack
        Returns:
            temp (*): item of any type on the top of our stack
        """
        if self.top is None:
            raise IndexError
        temp = self.top.data
        self.top = self.top.next1
        self.num_items -= 1
        return temp

    def peek(self):
        """Returns item from the top of our stack
        Returns:
            int or string: item on the top of our stack
        """
        if self.num_items == 0:
            return None
        temp = self.top.data
        return temp

    def size(self):
        """determines the size of the array
        Returns:
            int: size of our array
        """
        return self.num_items
