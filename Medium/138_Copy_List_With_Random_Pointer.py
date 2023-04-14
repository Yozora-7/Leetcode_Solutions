"""
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.
"""

# Linear Time Algorithm

class Solution(object):
    def copyRandomList(self, head):
        oldToCopy = { None : None } # create a hashmap that maps every old node to the copy of that node that we create. The values inside ensure that if the next value of copy is null, then the value added to the hashmap will match what it currently is

        cur = head
        while cur: # iterate over the list
            copy = Node(cur.val) # create a clone of the node
            oldToCopy[cur] = copy
            cur = cur.next

        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next] # set the next and random pointers
            copy.random = oldToCopy[cur.random]
            cur = cur.next
        
        return oldToCopy[head]
