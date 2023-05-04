"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
"""

class Solution(object):
    def longestConsecutive(self, nums):
        numSet = set(nums) # create a hashset for nums to be stored as
        longest = 0

        for n in nums: # check if it's the start of a sequence
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet: # checks the current num
                    length += 1
                longest = max(length, longest)
        return longest
