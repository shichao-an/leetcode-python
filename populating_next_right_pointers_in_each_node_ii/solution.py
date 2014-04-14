# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        head = None  # Head node of a level
        prev = None  # Last processed node of a level
        while root is not None:
            while root is not None:
                if root.left is not None:
                    if prev is None:
                        head = root.left
                    else:
                        prev.next = root.left
                    prev = root.left
                if root.right is not None:
                    if prev is None:
                        head = root.right
                    else:
                        prev.next = root.right
                    prev = root.right
                # Go to the next (right) node
                root = root.next
            # Go to the next level
            root = head
            head = None
            prev = None
