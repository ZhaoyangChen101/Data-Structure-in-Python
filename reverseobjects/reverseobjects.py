# -*- coding: utf-8 -*-
# Nimi: Zhaoyang Chen
# Opiskelijanumero: 875497
#​‌​​​​​‌‌‌​‌​​​ Implement the reverseObjects function here below

from stack import Stack

def reverseObjects(sequence):
    """Returns the contents of sequence reversed in a list."""
    reversed_list = []
    stack = Stack()
    for element in sequence:
        stack.push(element)
    while not stack.is_empty():
        reversed_list.append(stack.pop())
    #​‌​​​​​‌‌‌​‌​​​ Do something with stack and sequence
    #​‌​​​​​‌‌‌​‌​​​ ...
    #​‌​​​​​‌‌‌​‌​​​ ...
    #​‌​​​​​‌‌‌​‌​​​ ...
    #​‌​​​​​‌‌‌​‌​​​ Return the sequence reversed

    return reversed_list

