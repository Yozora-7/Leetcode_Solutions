"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.
"""

class Solution(object):
    def findMin(self, nums):
        res = nums[0] # choose leftmost value
        l, r = 0, len(nums) - 1 

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l]) # setting the minimum value out of itself and the current value of the left iteration of nums
                break

            # if the array is not sorted then carry out the binary search function
            m = (l + r) // 2 # finding the middle value
            res = min(res, nums[m])
            if nums[m] >= nums[l]: # determine if the middle value is a part of the left portion
                l = m + 1
            else: # else we are in the right sided portion
                r = m - 1
        return res

