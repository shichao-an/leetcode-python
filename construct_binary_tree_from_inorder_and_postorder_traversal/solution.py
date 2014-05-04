# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
        if not inorder or not postorder:
            return None
        else:
            d = postorder[-1]
            root = TreeNode(d)
            i = inorder.index(d)
            left = self.buildTree(inorder[:i], postorder[:i])
            right = self.buildTree(inorder[i + 1:], postorder[i:-1])
            root.left = left
            root.right = right
            return root
