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

        Recursive (Time Limit Exceeded)
        """
        if head is None:
            return None
        else:
            rev_rest = self.reverseList(head.next)
            current = rev_rest
            if current is None:
                return head
            while current and current.next is not None:
                current = current.next
            current.next = head
            head.next = None
            return rev_rest


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n1.next = n2
n2.next = n3
s = Solution()
r1 = s.reverseList(n1)
print r1.val
print r1.next.val
print r1.next.next.val
