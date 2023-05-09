"""
Given the root of a binary tree, invert the tree, and return its root.
"""

class Solution(object):
    def invertTree(self, root):
        if not root:
            return None # check the base case (what's expected to happen), if the root is null then we don't have to continue

        # swap the children
        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invertTree(root.left) # making a recurisve call to the function we're inside
        self.invertTree(root.right)
        return root # once we have inverted the subtrees, return the root
