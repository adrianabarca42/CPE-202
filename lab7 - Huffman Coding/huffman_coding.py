"""Huffman Coding
CPE202

Author:
    Put your name here
"""
from huffman import HuffmanNode
from min_pq import MinPQ

def cnt_freq(filename):
    """returns a Python list of 256 integers the frequencies of characters in file
    Args:
        filename (str): name of the file
    Returns:
        list: array of 256 integers of the frequencies of characters in file

    """
    freq_dict = {}
    list_of_freqs = [0]*256
    file = open(filename, "r")
    file_open = file.readlines()
    for line in file_open:
        for char in line:
            if char in freq_dict:
                freq_dict[char] += 1
            else:
                freq_dict[char] = 1
    for item in freq_dict:
        list_of_freqs[ord(item)] = freq_dict[item]
    return list_of_freqs

def create_huff_tree(list_of_freqs):
    """returns the root node of a Huffman Tree
    """
    huff_tree = []
    for idx in range(len(list_of_freqs)):
        if list_of_freqs[idx] != 0:
            huff_tree.append(HuffmanNode(list_of_freqs[idx], chr(idx)))
    huff_arr = MinPQ()
    huff_arr.heapify(huff_tree)
    while huff_arr.num_items > 1:
        node1 = huff_arr.del_min()
        node2 = huff_arr.del_min()
        freq = node1.freq + node2.freq
        char = min(node1.char, node2.char)
        new_huff_node = HuffmanNode(freq, char)
        new_huff_node.left = node1
        new_huff_node.right = node2
        huff_arr.insert(new_huff_node)
    return huff_arr.min()

def create_code(root_node):
    """returns a Python list of 256 strings representing the code
    Return an array of size 256 whose idex corresponds to ascii code of a letter.
    """
    code = ''
    code_list = [None] * 256
    create_code_helper(root_node, code, code_list)
    return code_list

def create_code_helper(root_node, code, code_list):
    """create_code_helper function
    """
    if root_node is None:
        return
    if root_node.left is None and root_node.right is None:
        code_list[ord(root_node.char)] = code
    create_code_helper(root_node.left, code + '0', code_list)
    create_code_helper(root_node.right, code + '1', code_list)
    return

def huffman_encode(in_file, out_file):
    """encodes in_file and writes the it to out_file
    This function calls cnt_freq, create_huff_tree, and create_code functions.
    """
    freq_list = cnt_freq(in_file)
    huff_tree = create_huff_tree(freq_list)
    file_list = create_code(huff_tree)
    huff_str = ''
    file = open(in_file, "r")
    file_open = file.readlines()
    for line in file_open:
        for char in line:
            huff_str = huff_str + file_list[ord(char)]
    print(huff_str)
    file1 = open(out_file, 'w')
    if len(huff_str) > 90:
        huff_str2 = huff_str[91:]
        file1.write(huff_str[:91])
        file1.write("\n")
        file1.write(huff_str2)
    else:
        file1.write(huff_str)
