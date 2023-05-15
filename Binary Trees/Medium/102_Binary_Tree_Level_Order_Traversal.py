"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
"""
class Solution:
    def levelOrder(self, root):
        res = []

        q = collections.deque() # this will give us a queue
        q.append(root) # add the root node to the queue

        while q:
            qLen = len(q) # ensuring that we're iterating one level at a time
            level = []
            for i in range(qLen):
                node = q.popleft() # pop nodes from the left of the queue (first in, first out)
                if node: # if not null
                    level.append(node.val) # take the node value and append it to the list level
                    q.append(node.left) # ensure to add the children of the specific node, so when the next loop comes around it will move to the children
                    q.append(node.right)
            if level: # if there are values still left to the level list
                res.append(level) # add every level to our result. Keep running the loop until there are no nodes left in our queue

        return res

"""
Initialize a queue with the root node of the tree.
Loop through the queue while there are still nodes in it:
a. Get the current node by popping the front of the queue.
b. Add the current node's value to the current level.
c. If the current node has left and/or right children, add them to the back of the queue.
d. If the current level has finished (i.e. there are no more nodes in the queue at the current level), add it to the result list and start a new level.
Return the result list.
"""
