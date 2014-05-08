class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        n = len(s)
        cur_len = 1
        max_len = 1
        d = {}
        d[s[0]] = 0
        for i in range(1, n):
            if s[i] in d:
                cur_len = min(i - d[s[i]], cur_len + 1)
            else:
                cur_len += 1
            max_len = max(cur_len, max_len)
            d[s[i]] = i
        return max_len
