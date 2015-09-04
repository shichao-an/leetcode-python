"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while
preserving the order of characters. No two characters may map to the same
character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

Note:
You may assume both s and t have the same length.
"""

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d = {}
        for i, c in enumerate(s):
            if c not in d:
                d[c] = t[i]
            else:
                if d[c] != t[i]:
                    return False
        d = {}
        for i, c in enumerate(t):
            if c not in d:
                d[c] = s[i]
            else:
                if d[c] != s[i]:
                    return False
        return True


s = Solution()
f = s.isIsomorphic
print(f('ab', 'aa'))
print(f('egg', 'add'))
print(f('foo', 'bar'))
print(f('paper', 'title'))
