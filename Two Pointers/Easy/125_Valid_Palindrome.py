"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""

class Solution(object):
    def isPalindrome(self, s):
        newStr = ""

        for c in s:
            if c.isalnum(): # if the character is alphanumerical then include it in the new string
                newStr += c.lower()
        return newStr == newStr[::-1] # return the result of this comparison. If the newStr is equal to the reverse of it then it is a palindrome
      
# SOLUTION WITHOUT USING .isalnum()

class Solution(object):
    def isPalindrome(self, s):
        l, r = 0, len(s) - 1 # creating left and right pointers
        
        while l < r: # while the left has not crossed the right yet
            while l < r and not self.alphaNum(s[l]): # while the character at position left is not alphanumeric
                l += 1
            while r > l and not self.alphaNum(s[r]): # to call another function inside of an object use self
                r -= 1

            if s[l].lower() != s[r].lower():
                return False # if the two positions are not equal then immediately return false, as it shows that the string isn't a palindrome
            l, r = l + 1, r - 1 # next increment
        
        return True


    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
         ord('a') <= ord(c) <= ord('z') or
         ord('0') <= ord(c) <= ord ('9')) # returns true if c is an uppercase, lowercase, or numerical value. If it's not alphanumeric then this will return false
