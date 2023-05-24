"""
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
"""

class Solution(object):
    def kthSmallest(self, root, k):
        n = 0 # tell us the number of elements visited from the tree. Once n is equal to k that's when we know we have visited every value in the tree.
        stack = [] # create a stack, as we are working iteratively
        cur = root # what node we are currently visiting

        while cur or stack: # while either are non empty we are going to continue traversing the tree
            while cur:
                stack.append(cur) # we need to add the current node to the stack before we move to the left, as this may be the final node to search before we get to the end of the stack
                cur = cur.left
            cur = stack.pop() # pop the most recently added value from our stack
            n += 1 # we have just visited another node so we must increment n by 1
            if n == k: # if n == k that means that the current node that we just processed is the value we are looking for. We are looking for the kth smallest element
                return cur.val
            cur = cur.right # the loop will go back up, ensure that every left value is traversed and subsequently added, and then move to the right
