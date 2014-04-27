# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        if root is None:
            return
        self.flatten(root.left)
        self.flatten(root.right)
        left = root.left
        right = root.right
        if left is not None:
            root.right = left
            root.left = None
            current = left
            while current.right is not None:
                current = current.right
            current.right = right
