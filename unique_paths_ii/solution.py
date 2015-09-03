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
        grid = obstacleGrid
        n = len(grid)
        m = len(grid[0])
        t = [[-1 for i in range(m)] for j in range(n)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    t[i][j] = 0
                else:
                    if i == 0 and j == 0:
                        t[i][j] = 1
                    elif i == 0:
                        t[i][j] = t[i][j - 1]
                    elif j == 0:
                        t[i][j] = t[i - 1][j]
                    else:
                        t[i][j] = t[i - 1][j] + t[i][j - 1]
        return t[n - 1][m - 1]
