"""contains code for BSTNode
"""
class BSTNode:
    """Node class for Bst
    Attributes:
        key (int): a ky
        val (*): a value of any type
        left (BSTNode): left subtree
        right (BSTNode): right subtree
    """
    def __init__(self, key, val, color, left=None, right=None):
        """The Constructor
        Args:
            key (int): a ky
            val (*): a value of any type
            color (str): color of the node
            left (BSTNode): left subtree
            right (BSTNode): right subtree
        """
        self.key = key
        self.val = val
        self.color = color
        self.left = left
        self.right = right

    def __eq__(self, other):
        return isinstance(other, BSTNode) and self.color == other.color\
               and self.val == other.val and self.left == other.left\
               and self.right == other.right and self.key == other.key

    def __repr__(self):
        return "BSTNode(key:%d, val:%s, color:%s, left:%s, right:%s)" %\
               (self.key, self.val, self.color, self.left, self.right)

def get(bst, value):
    """returns a certain value of a BST
    Args:
        bst (BSTNode): a BSTNode
        value (int): value you want to return
    Returns:
        int: value you want to get from BSTNode
    """
    if bst.key == value:
        return bst.val
    if value >= bst.key:
        return get(bst.right, value)
    return get(bst.left, value)

def contains(bst, key):
    """checks if a key is in a BST
    Args:
        bst (BSTNode): a BSTNode
        key (int): value you want to see is in the BST
    Returns:
        boolean: True if key is in the BST, False otherwise
    """
    if bst is None:
        return False
    if bst.key == key:
        return True
    if bst.key > key:
        return contains(bst.left, key)
    return contains(bst.right, key)

def insert_help(bst, key, val):
    """inserts a key with its val into a BST
    Args:
        bst (BSTNode): a BSTNode
        key (int): the key you want to insert
        val (*): any type you want connected to key
    """
    if bst is None:
        return BSTNode(key, val, 'red')
    if key < bst.key:
        return rebalance(BSTNode(bst.key, bst.val, bst.color,\
            insert_help(bst.left, key, val), bst.right))
    return rebalance(BSTNode(bst.key, bst.val, bst.color, bst.left,\
        insert_help(bst.right, key, val)))

def insert(bst, key, val):
    """inserts a key val pair
    """
    bst = insert_help(bst, key, val)
    return BSTNode(bst.key, bst.val, "black", bst.left, bst.right)

def rebalance(bst):
    """rebalance function
    """
    if bst.color == "black" and bst.left and bst.left.color == "red"\
        and bst.left.left and bst.left.left.color == "red":
        return BSTNode(bst.left.key, bst.left.val, "red",\
            BSTNode(bst.left.left.key, bst.left.left.val, "black",\
            bst.left.left.left, bst.left.left.right), BSTNode(bst.key, bst.val,\
            "black", bst.left.right, bst.right))
    elif bst.color == "black" and bst.left and bst.left.color == "red"\
        and bst.left.right and bst.left.right.color == "red":
        return BSTNode(bst.left.right.key, bst.left.right.val, "red", BSTNode(\
            bst.left.key, bst.left.val, "black", bst.left.left, bst.left.right.left),\
            BSTNode(bst.key, bst.val, "black", bst.left.right.right, bst.right))
    elif bst.color == "black" and bst.right and bst.right.color == "red"\
        and bst.right.left and bst.right.left.color == "red":
        return BSTNode(bst.right.left.key, bst.right.left.val, "red", BSTNode(\
            bst.key, bst.val, "black", bst.left, bst.right.left.left),\
            BSTNode(bst.right.key, bst.right.val, "black", bst.right.left.right, bst.right.right))
    elif bst.color == "black" and bst.right and bst.right.color == "red"\
        and bst.right.right and bst.right.right.color == "red":
        return BSTNode(bst.right.key, bst.right.val, "red",\
            BSTNode(bst.key, bst.val, "black", bst.left, bst.right.left),\
            BSTNode(bst.right.right.key, bst.right.right.val, "black", bst.right.right.left,\
            bst.right.right.right))
    return bst

def delete(bst, key):
    """deletes a key in a BST
    Args:
        bst (BSTNode): a BSTNode
        key (int): int you want to delete
    """
    if bst is None:
        raise KeyError("key does not exist")
    if bst.key == key:
        if bst.left:
            return bst.left
        if bst.right:
            bst = bst.right
            return bst
        elif bst.left and bst.right:
            node = get_node(bst.right)
            bst = delete(bst, node.key)
            bst.key, bst.val = node.key, node.val
            return bst
        else:
            return bst.right
    if bst.key > key:
        return delete(bst.left, key)
    else:
        return delete(bst.right, key)
    return bst

def get_node(bst):
    """get a node in BST
    Args:
        bst (BSTNode): a BSTNode
    Returns:
        BSTNode: node you want
    """
    if bst is None:
        raise ValueError("empty tree")
    if bst.left is None:
        return bst
    return get_node(bst.left)

def find_min(bst):
    """find the min in a BST
    Args:
        bst (BSTNode): a BSTNode
    Returns:
        int: min of the BST
    """
    if bst.left is None:
        return bst.key
    return find_min(bst.left)

def find_max(bst):
    """find the max in a BST
    Args:
        bst (BSTNode): a BSTNode
    Returns:
        int: max of the BST
    """
    if bst.right is None:
        return bst.key
    return find_max(bst.right)

def inorder_list(bst):
    """returns a list of the BST inorder
    Args:
        bst (BSTNode): a BSTNode
    Returns:
        list: list of nodes inorder
    """
    bst_list = []
    if bst:
        bst_list = inorder_list(bst.left)
        bst_list.append(bst.key)
        bst_list = bst_list + inorder_list(bst.right)
    return bst_list

def preorder_list(bst):
    """returns a list of the BST preorder
    Args:
        bst (BSTNode): a BSTNode
    Returns:
        list: list of nodes preorder
    """
    bst_list = []
    if bst:
        bst_list.append(bst.key)
        bst_list = bst_list + preorder_list(bst.left)
        bst_list = bst_list + preorder_list(bst.right)
    return bst_list

def tree_height(bst):
    """finds the height of the BST
    Args:
        bst (BSTNode): a BSTNode
    Returns:
        int: height of the tree
    """
    if bst is None:
        return -1
    elif bst.left is None and bst.right is None:
        return 0
    else:
        leftheight = tree_height(bst.left)
        rightheight = tree_height(bst.right)
        if leftheight > rightheight:
            return 1 + leftheight
        else:
            return 1 + rightheight

def range_search(bst, lo, hi):
    """returns a list of nodes in a certain range
    Args:
        bst (BSTNode): a BSTNode
        lo (int): lowest number in search
        hi (int): highest number in search
    Returns:
        list: list of nodes in the range
    """
    return range_help(bst, lo, hi, [])

def range_help(bst, lo, hi, list1):
    """helper function for range_search
    Args:
        bst (BSTNode): a BSTNode
        lo (int): lowest number in search
        hi (int): highest number in search
        list1 (list): empty list
    Returns:
        list: list of nodes in the range
    """
    if bst is None:
        return list1
    if bst.key >= hi:
        return range_help(bst.left, lo, hi, list1)
    if bst.key < lo:
        return range_help(bst.right, lo, hi, list1)
    list1 = range_help(bst.left, lo, hi, list1)
    list1.append(bst.val)
    list1 = range_help(bst.right, lo, hi, list1)
    return list1
