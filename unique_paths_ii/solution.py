class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        for i in range(n):
            for j in range(m):
                if i == 0:
                    if obstacleGrid[i][j] == 0:
                        if j == 0 or (j > 0 and obstacleGrid[i][j - 1] != 0):
                            obstacleGrid[i][j] = 1
                    else:
                        obstacleGrid[i][j] = 0
                elif j == 0:
                    if obstacleGrid[i][j] == 0:
                        # i must be greater that zero here
                        if obstacleGrid[i - 1][j] != 0:
                            obstacleGrid[i][j] = 1
                    else:
                        obstacleGrid[i][j] = 0
                else:
                    if obstacleGrid[i][j] == 0:
                        obstacleGrid[i][j] = (obstacleGrid[i - 1][j]
                                              + obstacleGrid[i][j - 1])
                    else:
                        obstacleGrid[i][j] = 0
        return obstacleGrid[n - 1][m - 1]
