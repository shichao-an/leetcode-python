# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        self.res = 0  # global variable for sum
        num = 0
        self.sn(root, num)
        return self.res

    def sn(self, root, num):
        if root is None:
            return
        elif root.left is None and root.right is None:
            num += root.val
            self.res += num
        else:
            num += root.val
            self.sn(root.left, 10 * num)
            self.sn(root.right, 10 * num)
