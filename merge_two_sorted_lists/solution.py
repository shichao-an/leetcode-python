"""
Merge two sorted linked lists and return it as a new list. The new list should
be made by splicing together the nodes of the first two lists.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode

        No dummy node
        """
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
