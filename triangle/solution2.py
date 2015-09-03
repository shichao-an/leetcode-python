"""
Given a triangle, find the minimum path sum from top to bottom. Each step you
may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, where n is
the total number of rows in the triangle.
"""

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        m = 0
        res = None
        for i, row in enumerate(triangle):
            m = len(row)
            if i > 0:
                for j, col in enumerate(row):
                    if 0 < j < m - 1:
                        triangle[i][j] += min(triangle[i - 1][j - 1],
                                              triangle[i - 1][j])
                    elif j == 0:
                        triangle[i][j] += triangle[i - 1][j]
                    # j == m - 1
                    else:
                        triangle[i][j] += triangle[i - 1][j - 1]
            if i == n - 1:
                for col in row:
                    if res is None:
                        res = col
                    else:
                        res = min(col, res)
        return res


a1 = [
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]

s = Solution()
print(s.minimumTotal(a1))
