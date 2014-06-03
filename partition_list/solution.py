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
        if head is None:
            return head
        large = None
        large_end = None
        res = None
        res_end = None
        while head is not None:
            next_node = head.next
            if head.val >= x:
                if large is None:
                    large = head
                    large_end = large
                else:
                    large_end.next = head
                    large_end = large_end.next
            else:
                if res is None:
                    res = head
                    res_end = res
                else:
                    res_end.next = head
                    res_end = res_end.next
            head = next_node
        if large_end is not None:
            large_end.next = None
        if res is not None:
            res_end.next = large
        else:
            res = large
        return res
