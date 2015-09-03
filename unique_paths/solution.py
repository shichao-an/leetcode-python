"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in
the diagram below).

The robot can only move either down or right at any point in time. The robot
is trying to reach the bottom-right corner of the grid (marked 'Finish' in the
diagram below).

How many possible unique paths are there?
"""

class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        t = [[1] * m] * n
        i = j = 0
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    t[i][j] = 1
                elif j == 0:
                    t[i][j] = 1
                else:
                    t[i][j] = t[i - 1][j] + t[i][j - 1]
        return t[n - 1][m - 1]
