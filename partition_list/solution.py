# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        l = ListNode(0)
        g = ListNode(0)
        p = l
        q = g
        while head is not None:
            if head.val < x:
                p.next = head
                p = p.next
            else:
                q.next = head
                q = q.next
            head = head.next
        q.next = None
        p.next = None
        g = g.next
        p.next = g
        return l.next
