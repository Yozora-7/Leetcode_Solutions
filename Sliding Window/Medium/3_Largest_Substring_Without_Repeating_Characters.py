"""
Given a string s, find the length of the longest 
substring without repeating characters.
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        charSet = set() # create a hashset that will store every character and ensure that only one of each specific character can be stored

        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet: # while the value of the right pointer is already in the charSet (is a duplicate)
                charSet.remove(s[l]) # remove the left pointer value to update the window
                l += 1 # update the left pointer, and keep doing this until there aren't any more duplicate characters in the character set
            charSet.add(s[r]) # add the rightmost character to the set
            res = max(res, r - l + 1) # update the result variable if the current window size is greater than it is right now
        return res
