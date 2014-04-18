class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        S.sort()
        return self._subsets(S, len(S))

    def _subsets(self, S, k):
        if k == 0:
            return [[]]
        else:
            res = [[]]
            for i in range(len(S)):
                if i > 0 and S[i] == S[i - 1]:
                    pass
                else:
                    rest_subsets = self._subsets(S[i + 1:], k - 1)
                    for subset in rest_subsets:
                        subset.insert(0, S[i])
                    res += rest_subsets
            return res
