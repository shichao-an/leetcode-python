"""
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []
        cand = []
        self.binary_tree_paths(root, cand, res)
        return res

    def binary_tree_paths(self, root, cand, res):
        if root is None:
            return
        else:
            cand.append(root.val)
            if root.left is None and root.right is None:
                p = '->'.join(map(str, cand))
                res.append(p)
            self.binary_tree_paths(root.left, cand, res)
            self.binary_tree_paths(root.right, cand, res)
            cand.pop()
