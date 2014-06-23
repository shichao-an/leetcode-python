# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        carry = 0
        res = None
        res_end = None
        while l1 is not None and l2 is not None:
            temp = l1.val + l2.val + carry
            digit = temp % 10
            carry = temp / 10
            if res is None:
                res = ListNode(digit)
                res_end = res
            else:
                res_end.next = ListNode(digit)
                res_end = res_end.next
            l1 = l1.next
            l2 = l2.next
        rem = None
        if l1 is not None:
            rem = l1
        else:
            rem = l2
        while rem is not None:
            temp = rem.val + carry
            digit = temp % 10
            carry = temp / 10
            if res is None:
                res = ListNode(digit)
                res_end = res
            else:
                res_end.next = ListNode(digit)
                res_end = res_end.next
            rem = rem.next
        if carry == 1:
            res_end.next = ListNode(1)
            res_end = res_end.next
        return res
