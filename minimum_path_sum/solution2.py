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
        t = [[-1 for i in range(m)] for j in range(n)]
        return self.min_path_sum_aux(grid, m - 1, n - 1, t)

    def min_path_sum_aux(self, grid, x, y, t):
        if x == 0 and y == 0:
            return grid[y][x]
        elif t[y][x] != -1:
            return t[y][x]
        elif x == 0 and y > 0:
            t[y][x] = grid[y][x] + self.min_path_sum_aux(grid, x, y - 1, t)
            return t[y][x]
        elif x > 0 and y == 0:
            t[y][x] = grid[y][x] + self.min_path_sum_aux(grid, x - 1, y, t)
            return t[y][x]
        else:
            a = self.min_path_sum_aux(grid, x - 1, y, t)
            b = self.min_path_sum_aux(grid, x, y - 1, t)
            t[y][x] = grid[y][x] + min(a, b)
            return t[y][x]
