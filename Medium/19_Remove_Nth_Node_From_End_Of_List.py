"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.
"""

class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head) # inserting the node at the beginning of the head
        left = dummy
        right = head # initialising pointers, 

        while n > 0 and right:
            right = right.next
            n -= 1 # once n = 0 then it means we have shifted by the amount that we wanted to

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next # deleting the node
        return dummy.next
