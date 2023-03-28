"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
"""

class Solution(object):
    def generateParenthesis(self, n):
        # only add an open bracket if open < n
        # only add a closing bracket if closed < open
        # valid IF open == closed == n

        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack)) # take every character in the stack and join them together into an empty string.
                return

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop() # pop the character just added to the stack every time the backtrack function is called to add an open bracket

            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop() # same as above for closed brackets

        backtrack(0, 0)
        return res
