# -*- coding: utf-8 -*-
# Nimi: Zhaoyang Chen
# Opiskelijanumero: 875497


from stack import Stack

def checkParentheses(input_string):
    """Check if input_string has correctly formatted parentheses.
    If parentheses are correct, return True, else return False."""

    #​‌​​​​​‌‌‌​‌​​​ Example behaviour:
    #​‌​​​​​‌‌‌​‌​​​ ================= ==============================
    #​‌​​​​​‌‌‌​‌​​​ input_string      checkParentheses(input_string)
    #​‌​​​​​‌‌‌​‌​​​ ================= ==============================
    #​‌​​​​​‌‌‌​‌​​​ ()                True
    #​‌​​​​​‌‌‌​‌​​​ (()({}))          True
    #​‌​​​​​‌‌‌​‌​​​ {aaa(vv)f[gg]df}  True
    #​‌​​​​​‌‌‌​‌​​​ a                 True
    #​‌​​​​​‌‌‌​‌​​​ (                 False
    #​‌​​​​​‌‌‌​‌​​​ (]                False
    #​‌​​​​​‌‌‌​‌​​​ aa(b]b)ee         False
    #​‌​​​​​‌‌‌​‌​​​ ({)}              False
    #​‌​​​​​‌‌‌​‌​​​ ================= ==============================
    allPa = ["(", ")", "{", "}", "[", "]"]
    leftPa = ["{", "(", "["]
    rightPa = ["}", ")", "]"]

    #nonPa = []
    stack = Stack()

    for element in input_string:
        # if element not in allPa:
        #     nonPa.append(element)
        # else:
        if element in allPa:
            if element in leftPa:
                stack.push(element)
            elif element in rightPa:
                if not stack.is_empty():
                    rightIndex = rightPa.index(element)
                    leftIndex = leftPa.index(stack.top())
                    if rightIndex == leftIndex:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
    if stack.is_empty():
        return True
    else:
        return False

    #​‌​​​​​‌‌‌​‌​​​ YOUR CODE HERE

    
    #raise NotImplementedError("checkParentheses not yet implemented")

    #return False

