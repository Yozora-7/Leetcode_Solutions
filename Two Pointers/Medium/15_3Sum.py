"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""

class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]: # if i isn't the first value in the input array and a is the same value as before
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r] # a being the first value, l the value after, and r the end of the array
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else: # if the value is at the target, append the correct values to the res array
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r: # if the two values are the same then shift the pointer again until they are different
                        l += 1

        return res
