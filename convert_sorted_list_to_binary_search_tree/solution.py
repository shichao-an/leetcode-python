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
        pp = p = q = head
        while q is not None and q.next is not None:
            pp = p  # pp is the previous node to p
            p = p.next
            q = q.next.next
        root = TreeNode(p.val)
        pp.next = None  # Split the linked list
        if pp == p:
            left = None
        else:
            left = self.sortedListToBST(head)
        right = self.sortedListToBST(p.next)
        root.left = left
        root.right = right
        return root
