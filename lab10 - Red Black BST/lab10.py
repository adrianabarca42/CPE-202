"""this contains code for lab10 and tree map
"""
import bstree_rb
from classmate import Classmate, classmate_factory


class TreeMap:
    """TreeMap class for a tree
    Attributes:
        tree (BST): a binary search tree
        num_items (int): number of items in the tree
    """
    def __init__(self):
        """The Constructor
        Args:
           tree (BST): a binary search tree
            num_items (int): number of items in the tree
        """
        self.tree = None
        self.num_items = 0

    def __repr__(self):
        return "TreeMap(tree:%s, num_items:%d)" % (self.tree, self.num_items)

    def __eq__(self, other):
        return isinstance(other, TreeMap) and self.tree == other.key\
               and self.num_items == other.num_items

    def __getitem__(self, key):
        """implementing this method enables getting an item with [] notation
        This function calls your get method.

        Args:
            key (*) : a key which is compareable by <,>,==
        Returns:
            * : the value associated with the key
        Raises:
            KeyError : it raises KeyError because the get function in bst.py raises the error.
        """
        return self.get(key)

    def __setitem__(self, key, val):
        """implementing this method enables setting a key value pair with [] notation
        This function calls your put method.

        Args:
            key (*) : a key which is compareable by <,>,==
            val (*): the value associated with the key
        """
        self.put(key, val)

    def __contains__(self, key):
        """implementing this method enables checking if a key exists with in notaion

        Args:
            key (*) : a key which is compareable by <,>,==
        Returns:
            bool : True is the key exists, otherwise False
        """
        return self.contains(key)

    def put(self, key, val):
        """put a key value pair into the map
        Calls insert function in bst.py

        Args:
            key (*) : a key which is compareable by <,>,==
            val (*): the value associated with the key
        """
        self.tree = bstree_rb.insert(self.tree, key, val)
        self.num_items += 1

    def get(self, key):
        """put a key value pair into the map
        Calls insert function in bst.py

        Args:
            key (*) : a key which is compareable by <,>,==
        Returns:
            * : the value associated with th key
        """
        return bstree_rb.get(self.tree, key)

    def contains(self, key):
        """Write the docstring
        Args:
            key (*) : a key which is compareable by <,>,==
        Returns:
            bool : True is the key exists, otherwise False
        """
        return bstree_rb.contains(self.tree, key)

    def delete(self, key):
        """Write the docstring
        Args:
            key (*) : a key which is compareable by <,>,==
        """
        self.tree = bstree_rb.delete(self.tree, key)
        self.num_items -= 1

    def size(self):
        """returns the number of items in the map
        Returns:
            int : the number of items in the map
        """
        return self.num_items

    def find_min(self):
        """Write the docstring
        """
        return bstree_rb.find_min(self.tree)

    def find_max(self):
        """Write the docstring
        """
        return bstree_rb.find_max(self.tree)

    def inorder_list(self):
        """Write the docstring
        """
        return bstree_rb.inorder_list(self.tree)

    def preorder_list(self):
        """Write the docstring
        """
        return bstree_rb.preorder_list(self.tree)

    def tree_height(self):
        """Write the docstring
        """
        return bstree_rb.tree_height(self.tree)

    def range_search(self, lower, higher):
        """Write the docstring
        """
        return bstree_rb.range_search(self.tree, lower, higher)

def import_classmates(filename):
    """Imports classmates from a tsv file

    Design Recipe step 4 (Templating) is doen for you.
    Complete this function by following the template.

    Args:
        filename (str) : the file name of a tsv file containing classmates

    Returns:
        TreeMap : return an object of TreeMap containing classmates.
    """
    #create an object of TreeMap
    tree_map = TreeMap()
    #create an empty list for classmates
    classmates = []
    #---- to do ----
    # complete this function by following the comments below
    #
    #open the file filename with python builtin open() function
    #read all lines in the file and assign it to variable lines
    #for each line in lines
        #split the line at tabs (\t) and assign it to a variable tokens
        #classmate = classmate_factory(tokens)
        #append the classmate to a list classmates
    #---------- ----
    file = open(filename)
    lines = file.readlines()
    for line in lines:
        tokens = line.split("\t")
        classmate = classmate_factory(tokens)
        classmates.append(classmate)
    #---- to do ----
    # complete this function by following the comments below
    #
    #for each classmate in classmates
        #put the classmate into the tree_map using its last name as the key
    #---------- ----
    for classmate in classmates:
        TreeMap.put(classmate.sid, classmate.major)
    return tree_map

def search_classmate(tmap, last):
    """Searches a classmate in a TreeMap using the last name as a key

    Args:
        tmap (TreeMap) : an object of TreeMap
        last (str) : the last name of a classmate
    Returns:
        Classmate : a Classmate object
    Raises:
        KeyError : if a classmate with the last name does not exist
    """
    if last in tmap:
        return tmap[last]
    raise KeyError("A classmate with the lastname does not exist!")
