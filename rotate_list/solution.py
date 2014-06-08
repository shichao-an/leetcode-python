# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if head is None:
            return None
        n = 0
        h = head
        while head is not None:
            n += 1
            head = head.next
        k = k % n
        if k == 0:
            return h
        res = h  # Head of result
        prev = h  # Previous node of result
        i = 0
        while res is not None:
            if i == n - k:
                break
            prev = res
            res = res.next
            i += 1
        end = res
        while end.next is not None:
            end = end.next
        end.next = h
        prev.next = None
        return res
