"""
Given a singly linked list where elements are sorted in ascending order,
convert it to a height balanced BST.
"""
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        if head is None:
            return None
        else:
            # Get the middle node
            slow = head
            fast = head
            prev = None  # Previous node to slow (mid)
            while fast.next is not None and fast.next.next is not None:
                prev = slow
                fast = fast.next.next
                slow = slow.next
            if head is slow:
                head = None
            if prev is not None:
                prev.next = None
            root = TreeNode(slow.val)
            left = self.sortedListToBST(head)
            right = self.sortedListToBST(slow.next)
            root.left = left
            root.right = right
            return root
