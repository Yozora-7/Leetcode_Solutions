"""
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.
"""

class Solution(object):
    def dailyTemperatures(self, temperatures):
        res = [0] * len(temperatures) # sets default value to 0 if nothing is received
        stack = [] # [temperature, index]

        for i, t in enumerate(temperatures): # enumerate means to get the value and index at the same time
            while stack and t > stack[-1][0]: # while the current temperature is greater than the top of the stack
                stackT, stackInd = stack.pop() # retrieve the temperature and the index
                res[stackInd] = (i - stackInd) # gives us the number of days it took to find a greater temperature
            stack.append([t, i])
        return res
