"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""

class Solution(object):
    def maxProfit(self, prices):
        l, r = 0, 1 # initialising pointers, left = buy, right = sell
        maxP = 0 # (max profit)

        while r < len(prices):
            if prices[l] < prices[r]: # if there is profit
                profit = prices[r] - prices[l] # calculate the profit
                maxP = max(maxP, profit) # update the max profit if it is higher than the current max
            else:
                l = r # move our left pointer to be at the minimum
            r += 1

        return maxP
