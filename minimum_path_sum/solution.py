"""
Given a m x n grid filled with non-negative numbers, find a path from top left
to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
"""

class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        n = len(grid)
        m = len(grid[0])
        t = [[0 for i in range(m)] for j in range(n)]
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    t[i][j] = grid[i][j]
                elif i == 0:
                    t[i][j] = grid[i][j] + t[i][j - 1]
                elif j == 0:
                    t[i][j] = grid[i][j] + t[i - 1][j]
                else:
                    t[i][j] = grid[i][j] + min(t[i - 1][j], t[i][j - 1])
        return t[n - 1][m - 1]
