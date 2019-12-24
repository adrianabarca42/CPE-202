"""HuffmanNode
CPE202

Author:
    Adrian Abarca
"""
class HuffmanNode:
    """Node class for HuffmanNode
    Attributes:
        freq (int): frequency of char
        char (str): a character
        left (HuffmanNode): left subnode
        right (HuffmanNode): rifht subnode
    """
    def __init__(self, frequency, char, left=None, right=None):
        """The Constructor
        Args:
            freq (int): frequency of char
            char (str): a character
            left (HuffmanNode): left subnode
            right (HuffmanNode): rifht subnode
        """
        self.freq = frequency
        self.char = char
        self.left = left
        self.right = right

    def __eq__(self, other):
        """checks equality of two different object types HuffmanNode
        Args:
            other (HuffmanNode): another HuffmanNode
        Returns:
            Boolean: true if two HuffmanNodes are equal, false otherwise
        """
        return isinstance(other, HuffmanNode) and self.freq == other.freq\
               and self.char == other.char and self.left == other.left\
               and self.right == other.right

    def __repr__(self):
        """representation function
        Args:
            None
        Returns:
            HuffmanNode in a string representation
        """
        return "HuffmanNode(freq:%d, char:%s, left:%s, right:%s)" %\
               (self.freq, self.char, self.left, self.right)

    def __lt__(self, other):
        """Implementing this function let you compare two HuffmanNode objects
         with < in your program
        Args:
            other (HuffmanNode): other HUffmanNode object to be compared with self
        Returns:
            True if self <= other, else return False
        """
        if self.freq == other.freq:
            return ord(self.char) < ord(other.char)
        else:
            return self.freq < other.freq
