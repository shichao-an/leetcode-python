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

          needle: |       n       |
        haystack: |   n - m   | m |
        """
        n = len(haystack)
        m = len(needle)
        for i in range(n + 1 - m):
            for k in range(m):
                if haystack[i + k] != needle[k]:
                    break
            else:
                return i
        return -1
