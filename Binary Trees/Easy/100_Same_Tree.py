"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
"""

class Solution(object):
    def isSameTree(self, p, q):
        if not p and not q: return True # if p and q are both empty return True, as both trees are the same
        if not p or not q or p.val != q.val: return False # if only one is not null and the other is empty then they are not the same. If the value of p is not equal to the value of q they are not the same, return False
        
        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right)) # simply return the function and apply it to left and right of both values
