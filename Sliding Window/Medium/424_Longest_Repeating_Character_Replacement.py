"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.
"""

class Solution(object):
    def characterReplacement(self, s, k):
        count = {} # create a hashmap to count the occurances of each character
        res = 0

        l = 0
        for r in range(len(s)): # the right position will go through every position in the string s
            count[s[r]] = 1 + count.get(s[r], 0) # 1 + whatever the count currently was. If the character doesn't exist in the hashmap it will default to 0

            while (r - l + 1) - max(count.values()) > k: # while the length of the window - the count of the most frequent character. This will determine the number of replacements we have to make in comparison to the number of replacements that are allowed to be made (k)

                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1) # update the max with the highest value of either the result itself or the size of the window (the calculation at the end)
        
        return res
      
# similar solution that implements a max frequency instead of manually finding the number of replacements due to be made

class Solution(object):
    def characterReplacement(self, s, k):
        count = {} # create a hashmap to count the occurances of each character
        res = 0

        l = 0
        maxf = 0
        for r in range(len(s)): # the right position will go through every position in the string s
            count[s[r]] = 1 + count.get(s[r], 0) # 1 + whatever the count currently was. If the character doesn't exist in the hashmap it will default to 0
            maxf = max(maxf, count[s[r]])
            
            while (r - l + 1) - maxf > k: # while the length of the window - the maximum frequency possible

                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1) # update the max with the highest value of either the result itself or the size of the window (the calculation at the end)
        
        return res
