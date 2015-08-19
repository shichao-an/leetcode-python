class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        S.sort()
        cand = []
        res = []
        self.subsets_aux(S, cand, res)
        return res

    def subsets_aux(self, S, cand, res):
        res.append(cand[:])
        for i, e in enumerate(S):
            cand.append(S[i])
            self.subsets_aux(S[i + 1:], cand, res)
            cand.pop()

s = Solution()
print(s.subsets([1, 2, 3]))
