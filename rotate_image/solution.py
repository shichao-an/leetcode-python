class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        n = len(matrix)
        # Layers
        for i in range(n / 2):
            # Each layer's index range
            start = i
            end = n - 1 - i
            for j in range(start, end):
                offset = j - start
                top = matrix[start][j]
                # Left to Top
                matrix[start][j] = matrix[end - offset][start]
                # Bottom to Left
                matrix[end - offset][start] = matrix[end][end - offset]
                # Right to Bottom
                matrix[end][end - offset] = matrix[j][end]
                # Top to Right
                matrix[j][end] = top
        return matrix
