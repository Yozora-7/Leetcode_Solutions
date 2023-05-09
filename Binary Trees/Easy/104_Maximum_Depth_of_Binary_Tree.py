"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""

# Recursive DFS (Depth For Search) 

class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) # comparing the two depth values of both trees and returning the max one
      
# Breadth For Search 

class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0

        level = 0
        q = deque([root]) # create a double ended queue at the root
        while q: # keep going until q is empty

            for i in range(len(q)): # traverse the entire level and add the next level
                node = q.popleft() # pop the leftmost value of q (tree)
                if node.left: # if the left value is non-null (theres a value), add it
                    q.append(node.left)
                if node.right:
                    q.append(node.right) # same with the right value

            level += 1 # once we are done adding the level then we add another one for the next iteration
        
        return level
      
# Iterative DFS (Depth For Search)

class Solution(object):
    def maxDepth(self, root):

        stack = [[root], 1]
        res = 0

        while stack:
            node, depth = stack.pop()

            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1]) # adding the children of the specific stack value to the stack, along with their depths
                stack.append([node.right, depth + 1])
            return res
      
      
