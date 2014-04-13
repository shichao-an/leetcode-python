class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        m = [0] * (rowIndex + 1)
        m[0] = 1
        for j in range(2, rowIndex + 1):
            for i in range(j / 2, 0, -1):
                if j % 2 == 0:
                    if i == j / 2:
                        m[i] = m[i - 1] * 2
                    else:
                        m[i] = m[i - 1] + m[i]
                else:
                    m[i] = m[i - 1] + m[i]

        # Mirror right part
        for i in range(rowIndex / 2 + 1, rowIndex + 1):
                m[i] = m[rowIndex - i]

        return m
