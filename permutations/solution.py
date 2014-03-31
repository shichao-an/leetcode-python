class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        if not num:
            return [[]]
        else:
            res = []
            for i, e in enumerate(num):
                rest = num[:i] + num[i + 1:]
                rest_perms = self.permute(rest)
                for perm in rest_perms:
                    perm.append(e)
                res += rest_perms
            return res
