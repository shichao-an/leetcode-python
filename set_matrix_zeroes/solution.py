class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        self.m = m
        self.n = n
        first_row_zero = False
        first_column_zero = False
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    if i == 0:
                        first_row_zero = True
                    if j == 0:
                        first_column_zero = True
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, n):
            if matrix[i][0] == 0:
                self.set_row_zero(matrix, i)
        for j in range(1, m):
            if matrix[0][j] == 0:
                self.set_column_zero(matrix, j)
        if first_row_zero:
            self.set_row_zero(matrix, 0)
        if first_column_zero:
            self.set_column_zero(matrix, 0)

    def set_column_zero(self, matrix, x):
        for i in range(self.n):
            matrix[i][x] = 0

    def set_row_zero(self, matrix, y):
        for j in range(self.m):
            matrix[y][j] = 0
