"""
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths
would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.

Note: m and n will be at most 100.
"""

class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        t = [[-1 for i in range(m)] for j in range(n)]
        return self.unique_paths(obstacleGrid, m - 1, n - 1, t)

    def unique_paths(self, grid, x, y, t):
        if x == 0 and y == 0:
            t[y][x] = 1 if grid[y][x] == 0 else 0
            return t[y][x]
        elif grid[y][x] == 1:
            t[y][x] = 0
            return t[y][x]
        elif t[y][x] != -1:
            return t[y][x]
        elif x > 0 and y == 0:
            t[y][x] = self.unique_paths(grid, x - 1, y, t)
            return t[y][x]
        elif y > 0 and x == 0:
            t[y][x] = self.unique_paths(grid, x, y - 1, t)
            return t[y][x]
        else:
            a = self.unique_paths(grid, x - 1, y, t)
            b = self.unique_paths(grid, x, y - 1, t)
            t[y][x] = a + b
            return t[y][x]
