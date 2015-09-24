"""
Given n, how many structurally unique BST's (binary search trees) that store
values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        t = [-1 for _ in range(n + 1)]
        return self.num_trees_aux(n, t)

    def num_trees_aux(self, n, t):
        if n == 0 or n == 1:
            return 1
        elif t[n] != -1:
            return t[n]
        else:
            res = 0
            for i in range(n):
                res += self.num_trees_aux(i, t) * \
                    self.num_trees_aux(n - 1 - i, t)
            t[n] = res
            return res
