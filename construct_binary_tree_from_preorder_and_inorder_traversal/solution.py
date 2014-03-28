# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        if len(inorder) == 0:
            return None
        else:
            root_val = preorder.pop(0)
            root_index = inorder.index(root_val)
            left_tree = self.buildTree(preorder, inorder[:root_index])
            right_tree = self.buildTree(preorder, inorder[root_index + 1:])
            root = TreeNode(root_val)
            root.left = left_tree
            root.right = right_tree
            return root
