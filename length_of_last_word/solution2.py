class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        n = len(s)
        p = n - 1
        right = -1
        while p >= 0:
            if right == - 1 and s[p] != ' ':
                right = p
            elif right >= 0 and s[p] == ' ':
                return right - p
            p -= 1
        if right >= 0:
            return right + 1
        else:
            return 0
