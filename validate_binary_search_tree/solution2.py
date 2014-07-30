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
        maxsize = 9223372036854775806  # Assumed sys.maxsize on 64-bit platform
        INT_MIN = -maxsize - 1
        INT_MAX = maxsize
        return self.is_valid_bst_aux(root, INT_MIN, INT_MAX)

    def is_valid_bst_aux(self, root, min_val, max_val):
        """Assume that keys are distinct integers"""
        if root is None:
            return True
        if root.val < min_val or root.val > max_val:
            return False
        # If non-distinct values are allowed, + 1 and - 1 to root.val can be
        # removed
        is_left_bst = self.is_valid_bst_aux(root.left, min_val, root.val - 1)
        is_right_bst = self.is_valid_bst_aux(root.right, root.val + 1, max_val)
        return is_left_bst and is_right_bst
