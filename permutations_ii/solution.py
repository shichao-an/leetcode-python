class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        d = {}
        return self.permute(num, d)

    def permute(self, num, d):
        if not num:
            return [[]]
        else:
            res = []
            for i, c in enumerate(num):
                if c in d:
                    continue
                else:
                    d[c] = True
                rest_perms = self.permuteUnique(num[:i] + num[i + 1:])
                for perm in rest_perms:
                    perm.insert(0, c)
                res += rest_perms
            return res
