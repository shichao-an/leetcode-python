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
            return 1 if grid[y][x] == 0 else 0
        elif t[y][x] != -1:
            return t[y][x]
        elif x > 0 and y == 0:
            if grid[y][x] == 1:
                t[y][x] = 0
            else:
                t[y][x] = self.unique_paths(grid, x - 1, y, t)
            return t[y][x]
        elif y > 0 and x == 0:
            if grid[y][x] == 1:
                t[y][x] = 0
            else:
                t[y][x] = self.unique_paths(grid, x, y - 1, t)
            return t[y][x]
        else:
            if grid[y][x] == 1:
                t[y][x] = 0
            else:
                a = self.unique_paths(grid, x - 1, y, t)
                b = self.unique_paths(grid, x, y - 1, t)
                t[y][x] = a + b
            return t[y][x]
