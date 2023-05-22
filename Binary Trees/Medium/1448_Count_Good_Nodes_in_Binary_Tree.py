"""
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.
"""

class Solution(object):
    def goodNodes(self, root):
        def dfs(node, maxVal):
            if not node: # if node is empty there are therefore 0 good nodes
                return 0
            
            res = 1 if node.val >= maxVal else 0 # if node is a good node res = 1. Otherwise the res will be 0 if the node is not good
            maxVal = max(maxVal, node.val) # this must be passed along to our recursive dfs call
            res += dfs(node.left, maxVal) # this function itself is just counting the no. of good nodes, so they must be added to the result
            res += dfs(node.right, maxVal)
            return res

        return dfs(root, root.val) # root node always counts as a good node
