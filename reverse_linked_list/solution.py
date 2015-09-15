"""
Reverse a singly linked list.

click to show more hints.

Hint:
A linked list can be reversed either iteratively or recursively. Could you
implement both?
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        res = None
        while head is not None:
            next_node = head.next
            if res is None:
                res = head
                res.next = None
            else:
                # Insert to the head of `res`
                head.next = res
                res = head
            head = next_node
        return res


n1 = ListNode(1)
n2 = ListNode(2)
n1.next = n2
s = Solution()
r1 = s.reverseList(n1)
print r1.val
print r1.next.val
print r1.next.next.val
