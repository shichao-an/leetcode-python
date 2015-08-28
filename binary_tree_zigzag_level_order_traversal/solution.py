"""
Given a binary tree, return the zigzag level order traversal of its nodes'
values. (ie, from left to right, then right to left for the next level and
alternate between).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
        if root is None:
            return []
        res = []
        queue = []
        rev = False  # Reverse direction
        level = []
        queue.append(root)
        queue.append(None)
        while queue:
            root = queue.pop(0)
            if root is None:
                if queue:
                    queue.append(None)
                res.append(level)
                level = []
                rev = not rev  # Toggle direction
            else:
                if rev:
                    level.insert(0, root.val)
                else:
                    level.append(root.val)
                if root.left is not None:
                    queue.append(root.left)
                if root.right is not None:
                    queue.append(root.right)
        return res
