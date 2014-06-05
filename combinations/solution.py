class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        a = range(1, n + 1)
        return self.combine_aux(a, k)

    def combine_aux(self, a, k):
        if k == 0:
            return [[]]
        else:
            res = []
            for i, e in enumerate(a):
                rest_comb = self.combine_aux(a[i + 1:], k - 1)
                for comb in rest_comb:
                    comb.insert(0, e)
                res += rest_comb
            return res
