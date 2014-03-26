# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head is None:
            return None
        if head.next is None:
            return head
        last = head
        current = head.next
        while current is not None:
            next_node = current.next
            if current.val == last.val:
                last.next = next_node
                # free(current) in C
            else:
                last = last.next
            current = next_node
        return head
