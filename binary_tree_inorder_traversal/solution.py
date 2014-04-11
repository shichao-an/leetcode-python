# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        path = []
        if root is None:
            return path
        stack = []
        while stack or root is not None:
            if root is not None:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                path.append(root.val)
                root = root.right
        return path
