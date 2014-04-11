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
