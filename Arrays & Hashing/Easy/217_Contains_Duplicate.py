"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""

class Solution(object):
    def containsDuplicate(self, nums):
        hashset = set() # create a hashset to store every new number.

        for n in nums:
            if n in hashset: # if the number is already stored in the hashset, then it will return True as it is a duplicate. 
                return True
            hashset.add(n) # if this isn't true and the number is a first for the set, it will add it.
        return False # if none of these conditions have been met, it will return False.
