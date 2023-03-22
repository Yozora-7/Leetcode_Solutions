"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""

class Solution(object):
    def groupAnagrams(self, strs):
        res = defaultdict(list) # mapping the character count of each string to list of anagrams

        for s in strs:
            count = [0] * 26 # a ... z

            for c in s:
                count[ord(c) - ord("a")] += 1

                # a = 80 -> 0, 80 - 80
                # b = 81 -> 1, 81 - 80

            res[tuple(count)].append(s) # lists cannot be keys

        return res.values()
