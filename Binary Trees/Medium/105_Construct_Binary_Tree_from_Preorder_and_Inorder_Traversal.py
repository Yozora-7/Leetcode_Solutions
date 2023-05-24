"""
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.
"""

class Solution(object):
    def buildTree(self, preorder, inorder):
        
        # Preorder start from top traverse from left to right 
        # Inorder start from root take care of the entire left subtree first, then take care of root node and right subtree

        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0]) # always start with the root
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid]) # calling the function we are inside of and passing through the first index (the first on the left) and ending it at the middle point. The inorder is then called to start from the first index but just before the middle. They just follow the principles of both (preorder start from root, inorder start from first index on the left)
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :]) # the same but for the right, where the preorder is taking indexes starting from the middle index to the end, with the inorder doing the same.
        return root
