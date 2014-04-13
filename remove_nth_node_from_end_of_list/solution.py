# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        if head is None:
            return None
        elif n == 0:
            return head
        else:
            q = p = pp = head  # `pp` is the node preceding `p`
            while q is not None:
                if n <= 0:
                    pp = p
                    p = p.next
                q = q.next
                n -= 1
            # Remove the head node
            if pp is p:
                head = pp.next
            else:
                pp.next = p.next
                # Free p
            return head
