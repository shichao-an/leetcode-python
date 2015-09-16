"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in
which the depth of the two subtrees of every node never differ by more than 1.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        else:
            if self.isBalanced(root.left) and self.isBalanced(root.right):
                return abs(self.depth(root.left) - self.depth(root.right)) <= 1
            else:
                return False

    def depth(self, root):
        if root is None:
            return -1
        else:
            return max(self.depth(root.left), self.depth(root.right)) + 1
