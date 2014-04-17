class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        n = len(s)
        i = n - 1
        while i >= 0 and s[i].isspace():
            i -= 1
        res = 0
        while i >= 0 and not s[i].isspace():
            res += 1
            i -= 1
        return res
