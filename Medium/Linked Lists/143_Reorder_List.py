"""
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.
"""

class Solution(object):
    def reorderList(self, head):
        slow, fast = head, head.next # finding the middle of the list
        while fast and fast.next: # while fast is non null and fast has not reached the end of the list
            slow = slow.next
            fast = fast.next.next

        second = slow.next # second half of the list
        prev = slow.next = None # splitting the list

        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp # reversing the second portion of the list

        # merge two halves of the list
        first, second = head, prev # prev is the last node
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1 # inserting the second node in between first and first.next, which is what tmp1 is
            first, second = tmp1, tmp2
