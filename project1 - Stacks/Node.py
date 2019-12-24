"""Contains code for Node
CPE202
Node class
"""

class Node:
    """Node
    """
    def __init__(self, data, next1):
        self.data = data
        self.next1 = next1

    def __repr__(self):
        """returns Node in a string representation
        """
        return "Node(%s, %r)" % (self.data, self.next1)

    def __eq__(self, other):
        """checks equality of two different object types Node
        """
        return isinstance(other, Node) and self.data == other.data\
               and self.next1 == other.next1
    
