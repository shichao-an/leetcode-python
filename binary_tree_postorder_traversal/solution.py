# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        path = []
        if root is None:
            return path
        stack1 = []
        stack2 = []
        stack1.append(root)
        while stack1:
            root = stack1.pop()
            stack2.append(root.val)
            if root.left is not None:
                stack1.append(root.left)
            if root.right is not None:
                stack1.append(root.right)
        while stack2:
            path.append(stack2.pop())
        return path
