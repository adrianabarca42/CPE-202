"""Contains code for Node
CPE202
Node class
"""

class Node:
    """Node
    """
    def __init__(self, key, data, next=None):
        self.key = key
        self.data = data
        self.next = next

    def __repr__(self):
        """returns Node in a string representation
        """
        return "Node(%s,%s,%r)" % (self.key, self.data, self.next)

    def __eq__(self, other):
        """checks equality of two different object types Node
        """
        return isinstance(other, Node) and self.data == other.data\
               and self.next == other.next\
               and self.key == other.key
