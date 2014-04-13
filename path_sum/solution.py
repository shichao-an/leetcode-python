# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if root is None:
            return False
        elif root.left is None and root.right is None:
            if sum == root.val:
                return True
            else:
                return False
        else:
            sum -= root.val
            return (self.hasPathSum(root.left, sum)
                    or self.hasPathSum(root.right, sum))
