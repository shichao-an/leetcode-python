# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        if root is None:
            return []
        one = []
        res = []
        self.ps(root, sum, one, res)
        return res

    def ps(self, root, sum, one, res):
        if root is None:
            return
        elif root.left is None and root.right is None:
            if root.val == sum:
                one.append(root.val)
                res.append(one[:])
                one.pop()
        else:
            one.append(root.val)
            self.ps(root.left, sum - root.val, one, res)
            self.ps(root.right, sum - root.val, one, res)
            one.pop()
