# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        stack = []
        if root is None:
            return stack
        queue = []
        level = []
        queue.append(root)
        queue.append(None)
        while queue:
            root = queue.pop(0)
            if root is None:
                stack.append(level[:])
                level = []
                if queue:
                    queue.append(None)
            else:
                level.append(root.val)
                if root.left is not None:
                    queue.append(root.left)
                if root.right is not None:
                    queue.append(root.right)
        res = []
        while stack:
            res.append(stack.pop())
        return res
