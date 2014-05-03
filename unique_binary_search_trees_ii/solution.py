# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @return a list of tree node
    def generateTrees(self, n):
        a = range(1, n + 1)
        return self.generate_bst(a)

    def generate_bst(self, a):
        if not a:
            return [None]
        else:
            res = []
            for i, c in enumerate(a):
                left = self.generate_bst(a[:i])
                right = self.generate_bst(a[i + 1:])
                for l in left:
                    for r in right:
                        root = TreeNode(c)
                        root.left = l
                        root.right = r
                        res.append(root)
            return res
