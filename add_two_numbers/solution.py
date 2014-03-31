# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        carry = 0
        p = l1
        q = l2
        h = r = ListNode(0)
        while q is not None and p is not None:
            if p.val + q.val + carry > 9:
                r.next = ListNode(p.val + q.val + carry - 10)
                carry = 1
            else:
                r.next = ListNode(p.val + q.val + carry)
                carry = 0
            p = p.next
            q = q.next
            r = r.next
        while q is not None:
            if q.val + carry > 9:
                r.next = ListNode(0)#
                carry = 1
            else:
                r.next = ListNode(q.val + carry)
                carry = 0
            q = q.next
            r = r.next
        while p is not None:
            if p.val + carry > 9:
                r.next = ListNode(0)#
                carry = 1
            else:
                r.next = ListNode(p.val + carry)
                carry = 0
            p = p.next
            r = r.next
        if carry == 1:
            r.next = ListNode(1)
        return h.next
    

