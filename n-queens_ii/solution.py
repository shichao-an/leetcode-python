class Solution:
    # @return an integer
    def totalNQueens(self, n):
        self.res = 0
        self.n = n
        columns = [-1 for i in range(n)]
        self.solve(columns, 0)
        return self.res

    def is_valid(self, columns, row, col):
        for r in range(row):
            c = columns[r]
            if c == col:
                return False
            if abs(c - col) == row - r:
                return False
        return True

    def solve(self, columns, row):
        if row == self.n:
            self.res += 1
        else:
            for col in range(self.n):
                if self.is_valid(columns, row, col):
                    columns[row] = col
                    self.solve(columns, row + 1)
