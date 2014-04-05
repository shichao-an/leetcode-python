class Solution:
    # @return a list of integers
    def grayCode(self, n):
        if n == 0:
            return [0]
        else:
            res = []
            res.append(0)
            for c in self.grayCode(n - 1):
                nc = 2 ** (n - 1) + c
                res.append(nc)
            r = self.grayCode(n - 1)
            r.reverse()
            for c in r[:-1]:
                res.append(c)
            return res


s = Solution()
print map(lambda x: bin(x)[2:].zfill(2), s.grayCode(2))
print map(lambda x: bin(x)[2:].zfill(3), s.grayCode(3))
print map(lambda x: bin(x)[2:].zfill(4), s.grayCode(4))
