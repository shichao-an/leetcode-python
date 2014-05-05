# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        h = head  # h is the temporary head node
        # First node of h
        if head is not None:
            head = head.next
            h.next = None
        while head is not None:
            next_node = head.next
            # Insertion sort
            current = h
            prev = h
            while current is not None and head.val > current.val:
                prev = current
                current = current.next
            # head is smaller than the head node of h
            # Insert head to the beginning of h
            if prev == current:
                head.next = h
                h = head
            # Insert head to the middle or end of h
            else:
                prev.next = head
                head.next = current
            head = next_node
        return h
