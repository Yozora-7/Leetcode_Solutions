"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""

# SOLUTION 1

class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0) # if this key does not exist in the hashmap then the default value being returned will be 0.
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False

        return True 
    
# SOLUTION 2

class Solution(object):
    def isAnagram(self, s, t):
        return Counter(s) == Counter(t) # Counter is a function that stores hashable values 
    
# SOLUTION 3

class Solution(object):
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)
