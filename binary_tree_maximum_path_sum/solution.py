"""
Given a binary tree, find the maximum path sum.

The path may start and end at any node in the tree.

For example:
Given the below binary tree,

       1
      / \
     2   3
Return 6.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        max_res = [None]
        res = self.max_sum(root, max_res)
        return max(res, max_res[0])

    def max_sum(self, root, max_res):
        if root is None:
            return 0
        else:
            left_max = self.max_sum(root.left, max_res)
            right_max = self.max_sum(root.right, max_res)
            root_max = max(root.val,
                           root.val + left_max,
                           root.val + right_max)
            if max_res[0] is not None:
                max_res[0] = max(max_res[0],
                                 root_max,
                                 root.val + left_max + right_max)
            else:
                max_res[0] = max(root_max, root.val + left_max + right_max)
            return root_max
