"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
"""

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
         cur = root # start at the root node

         while cur:
            if p.val > cur.val and q.val > cur.val: # if both the p value and the q value are greater than the root value that is currently being visited, go down the right subtree 
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val: # if the values are less than the current value, go down the left subtree
                cur = cur.left
            else:
                return cur # if the result itself has been found then return the current value
