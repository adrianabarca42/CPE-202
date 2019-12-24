"""Your module doc string here
"""
class Node:
    """class for our Node which contains the previous and next items
    """
    def __init__(self, data, prev=None, next1=None):
        """The Constructor
        Attributes:
            data (int): value of node
            next (int): next value in list
            prev (int): prev value in list
        """
        self.data = data
        self.prev = prev
        self.next1 = next1

    def __eq__(self, other):
        return isinstance(other, Node)\
               and self.data == other.data\
               and self.prev == other.prev\
               and self.next1 == other.next1

    def __repr__(self):
        return "Node(%s, %s)" % (self.data, self.next1)

class OrderedList:
    """class for the Ordered List
    """
    def __init__(self):
        """The Constructor
        Attributes:
            head (None or Node): smallest value of the list
            tail (None or Node): largest value of the list
            num_items (int): number of items in the list
        """
        self.head = None
        self.tail = None
        self.num_items = 0

    def __eq__(self, other):
        return isinstance(other, OrderedList) and self.head == other.head\
               and self.tail == other.head\
               and self.num_items == other.num_items

    def __repr__(self):
        return "OrderedList(%s, %s)" % (self.head, self.tail)

    def add(self, item):
        """adds an item to the ordered list
        Args:
            item (int): item that will be added to the list
        Returns:
            Nothing
        """
        new_node = Node(item)
        place_holder = self.head
        prev_place = None
        iterator = False
        if self.is_empty() is True:
            self.head = new_node
            self.tail = new_node
            self.num_items += 1
        while place_holder is not None and iterator is False:
            if place_holder.data <= item:
                prev_place = place_holder
                place_holder = place_holder.next1
            else:
                iterator = True
        if prev_place is not None:
            new_node.next1 = place_holder
            new_node.prev = prev_place
            prev_place.next1 = new_node
            if new_node.next1 is None:
                self.tail = new_node
            self.num_items += 1
        else:
            new_node.next1 = place_holder
            self.head = new_node
            self.num_items += 1

    def remove(self, item):
        """removes an item from the ordered list
        Args:
            item (int): item that is removed from the list
        Returns:
            int: position of the item removed or -1 if item is not in the list
        """
        if self.num_items == 1 and self.head.data == item:
            self.head = None
            self.tail = None
            self.num_items -= 1
            return 0

    def search_forward(self, item):
        """searches for an item using the head of the list
        Args:
            item (int): item being searched for
        Returns:
            booelan: True if item is in the list and False otherwise
        """
        if self.head.data == item:
            return True
        elif self.head.data < item:
            self.head = self.head.next1
            if self.head is None:
                return False
            else:
                return self.search_forward(item)

    def search_backward(self, item):
        """searches for an item using the tail of the list
        Args:
            item (int): item being searched for
        Returns:
            booelan: True if item is in the list and False otherwise
        """
        if self.tail.data == item:
            return True
        elif self.tail.data > item:
            self.tail = self.tail.next1
            if self.tail is None:
                return False
            else:
                return self.search_backward(item)

    def is_empty(self):
        """checks if the list is empty
        Args:
            None
        Returns:
            Boolean: True if list is empty, False otherwise
        """
        return self.num_items == 0

    def size(self):
        """returns the size of the list
        Args:
            None
        Returns:
            int: number of items in the list
        """
        return self.num_items

    def index(self, item):
        """finds the index of a given number
        Args:
            item (int): item we want the index of
        Returns:
            idx (int0): index of the item
        """
        idx = 0
        while self.head.data < item:
            if self.head.data == item:
                return idx
            else:
                idx += 1
                self.head = self.head.next
        idx = -1
        return idx

    def pop(self, pos=None):
        """returns the item of the list at the given position
        Args:
            pos (int): position of the number to be removed
        Returns:
            int: item if its in the list, -1 otherwise
        """
        if pos is None:
            return self.tail.data
        if pos > self.size:
            return -1
