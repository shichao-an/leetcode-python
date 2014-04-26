class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        if not num:
            return 0
        d = {}
        for e in num:
            if e not in d:
                d[e] = 1
        res = 1
        for c in num:
            current = 1
            if c not in d:
                continue
            while c - 1 in d:
                c -= 1
            del d[c]
            while c + 1 in d:
                c += 1
                current += 1
                del d[c]
            res = max(res, current)
        return res
