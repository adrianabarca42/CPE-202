"""LAB2
CPE 202
"""

def perm_lex(a_string):
    """Returns a list of all of the permutations in a string in a lexicographic order
    Args:
        a_string(str): a string of characters
    Returns:
        list: all of the permutations of a_string in lexicographic order
    """
    if len(a_string) == 0:
        return []
    perm_list = []
    if len(a_string) == 1:
        perm_list.append(a_string)
        return perm_list
    if len(a_string) == 2:
        perm_list.append(a_string)
        perm_list.append(a_string[1] + a_string[0])
        return perm_list
    final_list = []
    small_list = []
    for char in a_string:
        small_list = perm_lex(a_string.replace(char, ""))
        for ind in small_list:
            final_list.append(char + ind)
    return final_list
