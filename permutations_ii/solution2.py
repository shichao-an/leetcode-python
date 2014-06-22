class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        return self.permute(sorted(num))

    def permute(self, num):
        if not num:
            return [[]]
        else:
            res = []
            prev = None
            for i, e in enumerate(num):
                if prev is None or prev != e:
                    rest = num[:i] + num[i + 1:]
                    rest_perms = self.permute(rest)
                    for perm in rest_perms:
                        perm.append(e)
                    res += rest_perms
                    prev = e
            return res
