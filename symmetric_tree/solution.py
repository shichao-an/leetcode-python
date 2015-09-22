"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric
around its center).

For example, this binary tree is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following is not:
    1
   / \
  2   2
   \   \
   3    3
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        if root.left is None and root.right is None:
            return True
        if root.left is not None and root.right is not None:
            return self._isSymmetric(root.left, root.right)
        return False

    def _isSymmetric(self, left, right):
        if left is None and right is None:
            return True
        if left is not None and right is not None:
            return (left.val == right.val and
                    self._isSymmetric(left.left, right.right) and
                    self._isSymmetric(left.right, right.left))
        return False
