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
        while l1 is not None or l2 is not None or carry == 1:
            temp = 0
            if l1 is not None:
                temp += l1.val
                l1 = l1.next
            if l2 is not None:
                temp += l2.val
                l2 = l2.next
            temp += carry
            digit = temp % 10
            carry = temp / 10
            if res is None:
                res = ListNode(digit)
                res_end = res
            else:
                res_end.next = ListNode(digit)
                res_end = res_end.next
        return res
