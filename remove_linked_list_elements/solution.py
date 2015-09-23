"""
Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
            return None
        current = head
        last = None
        while current is not None:
            if current.val == val:
                if last is not None:
                    # Remove `current` node and `last` node is not changed
                    last.next = current.next
                else:
                    # `current` is the head node
                    # Remove the head node and `last` node is still None
                    head = current.next
                    last = None
            else:
                last = current
            current = current.next
        return head
