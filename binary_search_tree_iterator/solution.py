# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        self._arr = []
        self._inorder(root)
        self._cur = -1

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        if self._arr[self._cur + 1:]:
            return True
        return False

    # @return an integer, the next smallest number
    def next(self):
        if self.hasNext():
            self._cur += 1
            return self._arr[self._cur]

    def _inorder(self, root):
        if root is not None:
            if root.left is not None:
                self._inorder(root.left)
            self._arr.append(root.val)
            if root.right is not None:
                self._inorder(root.right)

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
