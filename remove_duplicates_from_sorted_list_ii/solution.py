# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        d = {}
        h = head
        while head is not None:
            if head.val not in d:
                d[head.val] = 1
            else:
                d[head.val] += 1
            head = head.next
        res = ListNode(0)  # Dummy head of result list
        end = res  # End of result list
        while h is not None:
            if d[h.val] == 1:
                end.next = h
                end = end.next
            h = h.next
        end.next = None
        return res.next
