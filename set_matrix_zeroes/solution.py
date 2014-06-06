class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        column_zero = False
        row_zero = False
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    # Check whether the first row and column contain
                    # zeroes before recording
                    if i == 0:
                        row_zero = True
                    if j == 0:
                        column_zero = True
                    # Record zeroes using the first row and column
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        # Set zeroes except for the first row and column
        for i in range(n):
            for j in range(m):
                if i > 0 and j > 0:
                    if matrix[0][j] == 0 or matrix[i][0] == 0:
                        matrix[i][j] = 0
        # Set the first row and column
        if row_zero:
            for j in range(m):
                matrix[0][j] = 0
        if column_zero:
            for i in range(n):
                matrix[i][0] = 0
