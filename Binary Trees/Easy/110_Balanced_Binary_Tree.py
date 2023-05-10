"""
Given a binary tree, determine if it is height-balanced
Height-Balanced
A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.
"""

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root: return [True, 0] # empty tree = balanced, return True as well as a default height of 0

            left, right = dfs(root.left), dfs(root.right)
            balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1) # first index of left and right trees, as well as the absolute values of the subtrees after are no more than 1

            return [balanced, 1 + max(left[1], right[1])] # ensure that the value returned is balanced, as well as determining the height. 1 comes from the root node that we're currently at + the max of the left and right subtree

        return dfs(root)[0] # return the boolean (at index 0, or the beginning)
