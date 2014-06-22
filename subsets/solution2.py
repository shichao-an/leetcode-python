class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        S.sort()
        return self.subsets_aux(S)

    def subsets_aux(self, S):
        if not S:
            return [[]]
        else:
            res = [[]]
            for i, e in enumerate(S):
                rest_subsets = self.subsets_aux(S[i + 1:])
                for subset in rest_subsets:
                    subset.insert(0, e)
                res += rest_subsets
            return res
