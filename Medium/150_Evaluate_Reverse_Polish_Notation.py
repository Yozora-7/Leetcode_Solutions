"""
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.
"""

class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop()) # we know that there will be 2 previous numbers, so the two numbers will be popped out of the stack for addition and then replaced by the result of the addition.
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a)) # int and float will round it toward 0
            else:
                stack.append(int(c))
        return stack[0]
