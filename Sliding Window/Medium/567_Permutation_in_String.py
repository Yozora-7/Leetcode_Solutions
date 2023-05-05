"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.
"""

class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2): return False # ensure that it is actually possible to search for a permutation

        s1Count, s2Count = [0] * 26, [0] * 26 # implement a hashmap through an array, 26 numbers, each being 0

        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1 # getting the ASCII value of this character. This will map to one of the 26 indexes
            s2Count[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0) # if characters match

        l = 0
        for r in range(len(s1), len(s2)): # this will start us at the next character that we left off at
            if matches == 26: return True

            index = ord(s2[r]) - ord('a') # map the specific character to an index of our count arrays
            s2Count[index] += 1 # we know that the index character was the character just added to the window in our s2Count string so it should be moved to the next value. 
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]: # if this is the case, then the two counts were equal, but were incremented one too many times due to the s2Count increment
                matches -= 1

            index = ord(s2[l]) - ord('a') # do the opposite to the above. Index r we added a character, but index l we removed a character. 
            s2Count[index] -= 1 # decrement the count as this is the character that we just removed from the left side of our window
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26 # return the matches if they equal 26
