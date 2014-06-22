class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        candidates.sort()
        res = []
        cand = []
        self.combination_sum_aux(candidates, target, cand, res)
        return res

    def combination_sum_aux(self, candidates, target, cand, res):
        if target == 0:
            res.append(cand[:])
        else:
            prev = None
            for i, c in enumerate(candidates):
                if prev is None or prev != c:
                    if target - c >= 0:
                        cand.append(c)
                        self.combination_sum_aux(candidates[i + 1:],
                                                 target - c, cand, res)
                        cand.pop()
                prev = c
