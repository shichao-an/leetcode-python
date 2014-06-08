# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        res = None
        res_end = None
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                if res is None:
                    res = l1
                    res_end = res
                else:
                    res_end.next = l1
                    res_end = res_end.next
                l1 = l1.next
            else:
                if res is None:
                    res = l2
                    res_end = res
                else:
                    res_end.next = l2
                    res_end = res_end.next
                l2 = l2.next
        if l1 is not None:
            if res is not None:
                res_end.next = l1
            else:
                res = l1
        if l2 is not None:
            if res is not None:
                res_end.next = l2
            else:
                res = l2
        return res
