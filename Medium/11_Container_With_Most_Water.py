"""

"""

# BRUTE FORCE METHOD

class Solution(object):
    def maxArea(self, height):
        res = 0

        for l in range(len(height)):
            for r in range(l + 1, len(height)):
                area = (r - l) * min(height[l], height[r])# width * minimum height
                res = max(res, area) # everytime we calculate the area, if it's higher than the current res than we update it.

            return res
          
# OPTIMAL METHOD 

class Solution(object):
    def maxArea(self, height):
        res = 0
        l, r = 0, len(height) - 1

        while l < r:
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
                
        return res
