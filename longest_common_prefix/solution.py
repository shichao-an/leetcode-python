class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        res = strs[0]
        for s in strs[1:]:
            n = len(s)
            for i, c in enumerate(res):
                if i >= n or res[i] != s[i]:
                    res = res[:i]
                    break
        return res
