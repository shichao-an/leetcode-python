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
