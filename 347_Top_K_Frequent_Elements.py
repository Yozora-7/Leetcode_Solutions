"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
"""

class Solution(object):
    def topKFrequent(self, nums, k):
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items(): # going to return every key value pair that gets added to the dictionary
            freq[c].append(n) # for every number and count were going to append n, as it appears every c value of times

        res = []
        for i in range(len(freq) - 1, 0, -1): # going from right to left (descending order)
            for n in freq[i]: # getting the n value that occurs most frequently
                res.append(n)
                if len(res) == k: # if the k value (which determines the most frequent elements) is the same as the length
                    return res   # of the result, then return the result as we know that the k most common values are there
