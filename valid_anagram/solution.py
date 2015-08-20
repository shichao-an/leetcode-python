class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        d = {}
        for c in s:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
        for c in t:
            if c not in d:
                return False
            else:
                d[c] -= 1
            if d[c] < 0:
                return False
        return True

s = Solution()
print(s.isAnagram("aacc", "ccac"))
print(s.isAnagram("abcd", "bcda"))
