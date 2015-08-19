# Using bit manipulation
class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        S.sort()
        k = len(S)
        n = 2 ** k
        res = []
        for i in range(n):
            s = self.filter(S, k, i)
            res.append(s)
        return res

    def filter(self, S, k, i):
        res = []
        for j in range(k):
            mask = 1 << j
            if i & mask > 0:
                res.append(S[j])
        return res

s = Solution()
print(s.subsets([1, 2, 3]))
