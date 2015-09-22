"""
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        if numRows == 0:
            return res
        res.append([1])
        if numRows == 1:
            return res
        res.append([1, 1])
        if numRows == 2:
            return res
        # n is current row index (starting from 0)
        for n in range(2, numRows):
            cur = []
            for i in range(n + 1):
                if i == 0:
                    cur.append(1)
                elif i == n:
                    cur.append(1)
                else:
                    c = res[n - 1][i - 1] + res[n - 1][i]
                    cur.append(c)
            res.append(cur)
        return res
