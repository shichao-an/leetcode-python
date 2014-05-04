# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        if root is None:
            return True
        else:
            left = True
            right = True
            if root.left is not None:
                left = (self.max_node(root.left).val < root.val
                        and self.isValidBST(root.left))
            if root.right is not None:
                right = (self.min_node(root.right).val > root.val
                         and self.isValidBST(root.right))
            if left and right:
                return True
            return False

    def min_node(self, root):
        while root.left is not None:
            root = root.left
        return root

    def max_node(self, root):
        while root.right is not None:
            root = root.right
        return root
