"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's
key.
The right subtree of a node contains only nodes with keys greater than the
node's key.
Both the left and right subtrees must also be binary search trees.
"""

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
        self.prev = None
        return self.is_valid_bst_aux(root)

    def is_valid_bst_aux(self, root):
        if root is None:
            return True
        else:
            if not self.is_valid_bst_aux(root.left):
                return False
            if self.prev is not None:
                if self.prev.val >= root.val:
                    return False
            self.prev = root
            if not self.is_valid_bst_aux(root.right):
                return False
            return True
