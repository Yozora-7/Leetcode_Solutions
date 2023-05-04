"""
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.
"""

class Solution(object):
    def largestRectangleArea(self, heights):
        maxArea = 0
        stack = [] # pair (index, height)

        for i, h in enumerate(heights): # iterate over both the index and the height
            start = i # because we dont know if we can extend it backwards
            while stack and stack[-1][1] > h: # if the top value of the stack's height is greater than the height we just reached then we pop the stack
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index)) # checking to see if this height that were popping could've been the max area rectangle by multiplying the height by the width (current iteration - beginning index value)
                start = index
            stack.append((start, h))

        for i, h in stack: # there still might be some entries in our stack left at the end of the histogram
            maxArea = max(maxArea, h * (len(heights) - i)) # compute the height by taking the max value of the maxArea variable as well as calculating the width by finding the length of the histogram and subtract it from the stack index value of i
        return maxArea
