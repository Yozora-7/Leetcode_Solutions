"""
Given two binary strings a and b, return their sum as a binary string.
"""

class Solution(object):
    def addBinary(self, a, b):
        res = "" # returning the result in string form.
        carry = 0

        a, b = a[::-1], b[::-1] # because binary works right to left.

    # whichever of the two has the longest loop will be iterated over.
        for i in range(max(len(a), len(b))):
            digitA = ord(a[i]) - ord("0") if i < len(a) else 0 # if it's in bounds.
            digitB = ord(b[i]) - ord("0") if i < len(b) else 0 

            total = digitA + digitB + carry
            char = str(total % 2) # base 2
            res = char + res
            carry = total // 2

        if carry: # if carry is non-zero
            res = "1" + res
        return res
