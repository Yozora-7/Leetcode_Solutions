"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.
"""

class Solution(object):
    def minEatingSpeed(self, piles, h):
        l, r = 1, max(piles) # initialising left and right pointers
        res = r # max that the solution could possibly be

        while l <= r:
            k = (l + r) // 2 # finding the middle
            hours = 0
            for p in piles:
                hours += math.ceil((float(p)) / k) # finding the number of hours it takes to eat a certain pile and then rounding it up to the next hour

            if hours <= h: # check if the hours is less than or equal to the given input
                res = min(res, k) # update the result to the new minimum
                r = k - 1 # search the left portion for any smaller values
            else:
                l = k + 1 # this would be carried out if the rate was too small, so we have to find a bigger rate that would allow us to eat the bananas in the given time interval
        
        return res
