"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
"""
class Solution(object):
    def isValidBST(self, root):
        
        def valid(node, left, right):
            if not node:
                return True
            
            if not (node.val < right and node.val > left): # finds a node that breaks the binary search tree
                return False

            return (valid(node.left, left, node.val) and # update the right boundary to the node's value because we know that every value in the left subtree has to be less than the parent, and so the parent is going to be set to the right boundary. 
            valid(node.right, node.val, right)) # the left boundary is going to be updated because we know every value in the right subtree has to be greater than the parent node (left boundary)

        return valid(root, float("-inf"), float("inf")) # set the left boundary to -infinity, and the right boundary to infinity. The values can be anything inbetween
