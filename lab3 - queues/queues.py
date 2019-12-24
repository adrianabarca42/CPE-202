"""CPE202
    LAB 3 Queues for both Array and Linked List
"""
class QueueArray:
    """Queue using a Circular Array
        Attributes:
            capacity (int) : capacity
            front (int) : front of the array
            rear (int) : rear of the array
            items (array) : array whose size is the capacity
            num_items (int) : number of items in the array
    """
    def __init__(self, capacity):
        self.capacity = capacity + 1
        self.front = 0
        self.rear = 0
        self.items = [None] * self.capacity
        self.num_items = 0

    def __repr__(self):
        """represents QueueArray as an array
        """
        return "QueueArray(%s)" % (self.items)

    def __eq__(self, other):
        """checks equality of two different object types QueueArray
        Attributes:
            other (QueueArray): a different QueueArray
        """
        return isinstance(other, QueueArray) and self.capacity == other.capacity\
               and self.front == other.front\
               and self.rear == other.rear\
               and self.items == other.items\
               and self.num_items == other.num_items

    def is_empty(self):
        """checks if the array is empty
        Returns:
            Boolean: True is QueueArray is empty, False otherwise
        """
        return self.num_items == 0

    def is_full(self):
        """checks if the array is full
        Returns:
            Boolean: True if QueueArray is full, False otherwise
        """
        return self.front == ((self.rear + 1) % (len(self.items)))

    def enqueue(self, item):
        """Enqueues an item to the end of QueueArray
        Attributes:
            item (any data type) : gets added to QueueArray at the end of the Array
        Returns:
            NoneType: IndexError if Array is full
        """
        if self.is_full():
            raise IndexError
        if self.rear + 1 == len(self.items):
            self.rear %= len(self.items)
        self.num_items = self.num_items + 1
        self.items[self.rear] = item
        self.rear = self.rear + 1

    def dequeue(self):
        """Dequeues an item to the end of QueueArray
        Returns:
            item (any data type) : returns the item that was dequeued
            NoneType: IndexError if Array is empty
        """
        if self.is_empty():
            raise IndexError
        if self.front + 1 == len(self.items):
            self.front %= len(self.items)
        item = self.items[self.front]
        self.front += 1
        self.num_items -= 1
        return item

    #returns the number of items in the queue
    def size(self):
        """gives the size of QueueArray
        Returns:
            num_items (int) : size of the Array
        """
        return self.num_items

#You must have the same functionalities for the Linked List Implementation
class Node:
    """A Linked List is one of
        -None, or
        -Node(data, next1): A Linked List
    Attributes:
        data (Any Type) : any data type
        next1 (Node) : object of Node class (a linked list)
    """
    def __init__(self, data, next):
        self.data = data
        self.next = next

class QueueLinked:
    """QueueLinked is a Queue implementation using linked lists
    Attributes:
        capacity (int): capacity of the linked list
        front (
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.front = None #pointer to the front of queue
        self.rear = None #pointer to the rear of queue
        self.num_items = 0 #number of items in array

    def __repr__(self):
        """returns a string representation of QueueLinked
        """
        
        return "QueueLinked(%s)" % (self.num_items)
    
    def __eq__(self):
        """returns whether two different classes of QueueLinked are equal or not
        """
        return isinstance(other, QueueLinked) and self.capacity == other.capacity\
               and self.front == other.front\
               and self.rear == other.rear\
               and self.num_items == other.num_items
        

    def is_empty(self):
        """returns true if linked list is empty, false otherwise
        Returns:
            Boolean: true if linked list is empty
        """
        return self.num_items == 0

    def is_full(self):
        """returns true if linked list is full, false otherwise
        Returns:
            Boolean: true if linked list is full
        """
        return self.num_items == self.capacity

    def enqueue(self, item):
        """enqueue's an item to the linked list
        Attributes:
            item (any type): any type of data
        Returns:
            NoneType: IndexError if linked list is full
        """
        if self.is_full():
            raise IndexError
        temp = Node(item, None)
        if self.rear is None:
            self.rear = self.front = temp
        else:
            self.rear.next = temp
        self.num_items += 1

    def dequeue(self):
        """dequeue's an item from the linked list
        Returns:
            item (any type): any type of data
            NoneType: IndexError if linked list is empty
        """
        if self.is_empty():
            raise IndexError
        temp = self.front
        self.front = temp.next
        self.num_items -= 1
        return temp.data

    def size(self):
        """gives the size of the linked list
        Returns:
            num_items (int): the number of items in the linked list
        """
        return self.num_items
