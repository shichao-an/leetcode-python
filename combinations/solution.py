class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        A = range(1, n + 1)
        return self._combine(A, k)

    def _combine(self, A, k):
        if k == 0:
            return [[]]
        if not A:
            return [[]]
        else:
            res = []
            for i, c in enumerate(A):
                if len(A[i + 1:]) >= k - 1 and k >= 0:
                    rest_comb = self._combine(A[i + 1:], k - 1)
                    for comb in rest_comb:
                        comb.insert(0, c)
                    res += rest_comb
            return res
