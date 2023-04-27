"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""

class Solution(object):
    def reverseList(self, head):
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
      
# ANOTHER EXAMPLE

class Solution(object):
    def reverseList(self, head):
        
        if not head:
            return None # if head is null return null

        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head # reversing the link between the next node and head
        head.next = None

        return newHead
