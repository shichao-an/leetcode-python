class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        t = [[0 for col in row] for row in triangle]  # Initialize t
        n = len(triangle)
        row = n - 1
        while row >= 0:
            if row == n - 1:
                for col in range(row + 1):
                    t[row][col] = triangle[row][col]
            else:
                for col in range(row + 1):
                    minsum = min(t[row + 1][col], t[row + 1][col + 1])
                    t[row][col] = triangle[row][col] + minsum
            row -= 1
        return t[0][0]
