class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        res = []
        if numRows == 0:
            return res
        res.append([1])
        if numRows == 1:
            return res
        res.append([1, 1])
        if numRows == 2:
            return res
        # n is current row index (starting from 0)
        for n in range(2, numRows):
            cur = []
            for i in range(n + 1):
                if i == 0:
                    cur.append(1)
                elif i == n:
                    cur.append(1)
                else:
                    c = res[n - 1][i - 1] + res[n - 1][i]
                    cur.append(c)
            res.append(cur)
        return res
