"""
Given two integers n and k, return all possible combinations of k numbers out
of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        a = range(1, n + 1)
        return self.combine_aux(a, k)

    def combine_aux(self, a, k):
        if k == 0:
            return [[]]
        else:
            res = []
            for i, e in enumerate(a):
                rest_comb = self.combine_aux(a[i + 1:], k - 1)
                for comb in rest_comb:
                    comb.insert(0, e)
                res += rest_comb
            return res
