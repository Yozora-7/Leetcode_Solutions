"""
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.
"""

class Solution(object):
    def isSubtree(self, root, subRoot):
        if not subRoot: # base cases
            return True
        if not root:
            return False

        if self.sameTree(root, subRoot):
            return True # if both of the trees are the same then return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot) # check if the subtree is the same as the left subtree of root, or the right subtree of root. If it is, then return True

    def sameTree(self, root, subRoot):
        if not root and not subRoot:
            return True # if they're both empty they're technically the same
            
        if root and subRoot and root.val == subRoot.val:
            return self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right) # if both are True, meaning the left subtree and the right subtree are the same, it will return True
        return False # if none of the conditions are met then return False. Will usually occur when one subtree is empty and the other isn't
