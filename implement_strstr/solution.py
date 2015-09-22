"""
Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if
needle is not part of haystack.
"""

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n = len(haystack)
        m = len(needle)
        for i in range(n + 1 - m):
            matched = True
            for k in range(m):
                if haystack[i + k] != needle[k]:
                    matched = False
                    break
            if matched:
                return i
        return -1
