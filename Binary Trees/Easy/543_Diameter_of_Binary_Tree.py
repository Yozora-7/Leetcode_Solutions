"""
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.
"""

class Solution(object):
    def diameterOfBinaryTree(self, root):
        res = [0] # global variable

        def dfs(root):
            if not root:
                return -1 # lets the maths work out, return the height of a null tree
            left = dfs(root.left)
            right = dfs(root.right)

            res[0] = max(res[0], 2 + left + right) # potentially updating it to find the diameter

            return 1 + max(left, right) # return the height running through the root node

        dfs(root) # call the function with the root parameter
        return res[0]
