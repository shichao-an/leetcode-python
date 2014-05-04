# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        i = 1
        res = head  # Start of the beginning part
        res_end = head  # End of the beginning part
        rev = None  # Start of reversed part
        rev_end = None  # End of reversed part
        while head is not None:
            next_node = head.next
            if i < m:
                res_end = head
            elif i >= m and i <= n:
                head.next = rev
                rev = head
                if i == m:
                    rev_end = head
            else:  # i > n
                break
            head = next_node
            i += 1
        # No beginning part
        if m == 1:
            res = rev
            res_end = rev_end
        else:
            res_end.next = rev
        rev_end.next = head
        return res
