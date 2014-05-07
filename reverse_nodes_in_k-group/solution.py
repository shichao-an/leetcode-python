# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        if k <= 0:
            return head
        # Calculate length
        n = 0
        h = head
        while head is not None:
            n += 1
            head = head.next
        g = n / k  # Number of groups
        m = g * k  # Largest index (1-base) that can form a group
        if m == 0:
            return h
        i = 1
        p = h
        res = None  # Head of result list
        end = res  # End node of result list
        t = None  # Head of temporary list
        t_end = t  # End node of temporary list
        while p is not None:
            next_node = p.next
            if i <= m:
                if t is None:
                    t_end = p
                p.next = t
                t = p
                if i % k == 0:
                    # Append temporary list to result list
                    if end is None:
                        res = t
                        end = t_end
                    else:
                        end.next = t
                        end = t_end
                    # Reset temporary list
                    t = None
            else:
                end.next = p
                break
            i += 1
            p = next_node
        return res
