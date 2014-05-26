class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        res = [1 for i in range(rowIndex + 1)]
        for row in range(rowIndex + 1):
            for col in range(row + 1):
                col = row - col
                if col < row and col > 0:
                    res[col] += res[col - 1]
        return res
