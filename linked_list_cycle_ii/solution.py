# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        if head is None or head.next is None:
            return None
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break
        # No cycle
        if fast is None or fast.next is None:
            return None
        # Has a cycle, put `slow` back to head
        slow = head
        while True:
            if fast == slow:
                break
            slow = slow.next
            fast = fast.next
        return slow
