"""
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
"""

class Solution(object):
    def rightSideView(self, root):
        res = [] # initialise an empty result
        q = collections.deque([root]) # create a queue for values of each level to be placed in 

        while q: # while q is non empty there will be values to be taken from it
            rightSide = None
            qLen = len(q)

            for i in range(qLen):
                node = q.popleft() # popping elements from the left and adding elements to the right
                if node:
                    rightSide = node # after this loop is done, rightSide is going to have the last node that was in the current level of the queue
                    q.append(node.left)
                    q.append(node.right)
            if rightSide:
                res.append(rightSide.val) # append the values of the current rightSide value to the result
        return res
