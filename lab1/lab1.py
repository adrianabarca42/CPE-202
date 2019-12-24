"""LAB1
CPE202
"""

#1
def get_max(int_list):
    """Computes the maximum in a list of integers
    Args:
        int_list(int): a list of int values
    Returns:
        int: the maximum value of int_list
    """
    if len(int_list) == 0:
        return None
    max1 = int_list[0]
    for i in int_list:
        if i > max1:
            max1 = i
    return max1

#2
def reverse(str1):
    """returns the reverse of the string inputted
    Args:
        str1(string): a string of characters
    Returns:
        string: the reverse of the string inputted
    """
    if len(str1) == 0:
        return ""
    return str1[len(str1)-1] + reverse(str1[0:len(str1)-1])

#3
def helper_lower(st_index, end_index, int1, int_list1):
    midpoint = len(int_list1) // 2
    if int1 == int_list1[(st_index + end_index) // 2]:
        return (st_index + end_index) // 2
    elif int1 > int_list1[(st_index + end_index) // 2]:
        return helper_lower((st_index + end_index) // 2, midpoint, int1, int_list1)
    return helper_lower(0, (st_index + end_index) // 2, int1, int_list1)

def helper_upper(st_index, end_index, int1, int_list1):
    midpoint = (st_index + end_index) // 2
    if st_index == end_index and int1 != int_list1[midpoint]:
        return None
    else:
        if int1 == int_list1[midpoint]:
            return midpoint
        elif int1 > int_list1[midpoint]:
            return helper_upper(midpoint + 1, end_index, int1, int_list1)
        return helper_upper(st_index, midpoint, int1, int_list1)


def search(int_list1, int1):
    """searches for a certain number in a list of integers and returns its index
    Args:
        int_list1(list): a list of int values
        int1(int): an int value
    Returns:
        int: the index of the number we want to search for
    """
    midpoint = len(int_list1) // 2
    if len(int_list1) == 0:
        return None
    else:
        if int1 == int_list1[midpoint]:
            return int_list1.index(int1)
        else:
            return helper_upper(0, len(int_list1) - 1, int1, int_list1)

#4
def fib(nth_num):
    """Computes the nth Fibonacci Number of the Fibonacci Numbers
    Args:
        nth_num(integer): an integer
    Returns:
        int: the nth Fibonacci Number
    """
    if nth_num == 0 or nth_num == 1:
        return nth_num
    return fib(nth_num - 1) + fib(nth_num - 2)

#5.1 factorial iterative version
def factorial_iter(nth_num):
    """Computes the factorial of nth_num
    Args:
        nth_num(int): nth_num is an integer
    Returns:
        int: the factorial of nth_num
    """
    fact = 1
    for i in range(1, nth_num):
        fact *= i+1
    return fact

#5.2 factorial recursive version
def factorial_rec(nth_num):
    """Computes the factorial of nth_num
    Args:
        nth_num(int): nth_num is an integer
    Returns:
        int: the factorial of nth_num
    """
    if nth_num == 0 or nth_num == 1:
        return 1
    return nth_num * factorial_rec(nth_num-1)
