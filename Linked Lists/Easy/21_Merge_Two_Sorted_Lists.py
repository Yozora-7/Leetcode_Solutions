"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode() # create a dummy node
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1: # if only one of the lists is non-null
            tail.next = list1 # taking the remaining portion of list1 and appending it to the end of the list
        elif list2:
            tail.next = list2

        return dummy.next
