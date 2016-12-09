"""
Given two strings s and t, write a function to determine if t is an anagram of
s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.
"""


class Solution(object):

    def find_first(self, str, chr):
        for i, ch in enumerate(str):
            if ch == chr:
                return i
        return -1

    def is_anagram(self, s, t):
        if len(s) != len(t):
            return False
        s_idx = self.find_first(s, t[0])
        s_idx_start = s_idx
        if s_idx >= 0:
            t_idx = 0
            while True:
                s_idx = (s_idx + 1) % len(s)
                t_idx = (t_idx + 1) % len(s)
                if s[s_idx] == t[t_idx] and s_idx != s_idx_start:
                    continue
                elif s[s_idx] == t[t_idx] and s_idx == s_idx_start:
                    return True
                elif s[s_idx] != t[t_idx]:
                    return False
        else:
            return False

s = Solution()
print(s.is_anagram("aacc", "ccac"))
print(s.is_anagram("abcd", "bcda"))
print(s.is_anagram("aabb", "abab"))
