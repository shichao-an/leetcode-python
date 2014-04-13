class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        matrix = [[0 for i in range(n)] for j in range(n)]
        count = 1
        for i in range(n / 2):
            start = i
            end = n - i - 1
            width = end - start
            for j in range(start, end):
                offset = j - start
                # Top
                matrix[start][j] = count + offset
                # Right
                matrix[j][end] = count + width + offset
                # Bottom
                matrix[end][end - offset] = count + 2 * width + offset
                # Left
                matrix[end - offset][start] = count + 3 * width + offset
            count += 4 * width
        if n % 2 == 1:
            mid = n / 2
            matrix[mid][mid] = count
        return matrix
