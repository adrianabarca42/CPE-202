"""Contains code for infix and postfix expressions
CPE202
Project 2

Author:
    Adrian Abarca
"""
from stacks import StackLinked
oper = dict([("+", 2), ("-", 2), ("*", 3), ("/", 3), ("~", 5), ("^", 5), ("(", 1) ])

def infix_to_postfix(infix_expr):
    """converts an infix expression to a postfix expression
    Args:
        infix_expr (str): the infix expression
    Returns:
        str: the postfix expression
    """
    postfix_list = []
    oper_stack = StackLinked()
    split_list = infix_expr.split()
    for item in split_list:
        if item in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or item.isdigit():
            postfix_list.append(item)
        elif item == '(':
            oper_stack.push(item)
        elif item == ')':
            top = oper_stack.pop()
            while top != '(':
                postfix_list.append(top)
                top = oper_stack.pop()
        elif item == "^" and oper_stack.peek() == "~":
            oper_stack.push(item)
        elif item == "~" and oper_stack.peek() == "~":
            oper_stack.push(item)
        else:
            while (not oper_stack.is_empty()) and \
                   (oper[oper_stack.peek()] >= oper[item]):
                postfix_list.append(oper_stack.pop())
            oper_stack.push(item)
    while not oper_stack.is_empty():
        postfix_list.append(oper_stack.pop())
    return " ".join(postfix_list)

def postfix_eval(postfix_expr):
    """evaluates the postfix expression
    Args:
        postfix_expr (str): the postfix expression to be evaluated
    Returns:
        int: the value of the evaluated expression
    Raises:
        SyntaxError: if the postfix expression is invalid
        ZeroDivisionError: if postfix expression has a divisor of 0
    """
    if postfix_valid(postfix_expr) is True:
        eval_stack = StackLinked()
        oper_list = postfix_expr.split()
        for item in oper_list:
            if item.isdigit():
                eval_stack.push(int(item))
            else:
                if item is "~":
                    oper1 = eval_stack.pop()
                    answer = -oper1
                    eval_stack.push(answer)
                else:
                    oper1 = eval_stack.pop()
                    oper2 = eval_stack.pop()
                    answer = evaluate(item, oper1, oper2)
                    eval_stack.push(answer)
        return eval_stack.pop()
    else:
        raise SyntaxError

def evaluate(oper, oper1, oper2):
    """performs math of 2 operands and an operator
    Args:
        oper (+, -, ^, *, /): math operators
        oper1 (int): an integer
        oper2 (int): an integer
    Returns:
        int: evaluation of the operands and operator
    Raises:
        ZeroDivisionError: if an operand is being divided by 0
    """
    if oper == "+":
        return oper1 + oper2
    elif oper == "-":
        return oper2 - oper1
    elif oper == "^":
        return oper2 ** oper1
    elif oper == "*":
        return oper1 * oper2
    elif oper == "/":
        if oper2 == 0:
            raise ZeroDivisionError 
        return oper2/oper1

def postfix_valid(postfix_expr):
    """checks if a postfix expression is valid or not
    Args:
        postfix_expr (str):postfix expr that the function checks for validity
    Returns:
        Booelan: true if postfix expr is valid, false otherwise
    """
    counter = 0
    postfix_list = postfix_expr.split()
    for item in postfix_list:
        if item.isdigit():
            counter += 1
        elif item in ("+", "-", "^", "*", "/"):
            counter -= 1
            counter -= 1
            if counter < 0:
                return False
            else:
                counter += 1
        else:
            counter -= 1
            if counter < 0:
                return False
            else:
                counter += 1
    if counter == 1:
        return True
    else:
        return False



    
