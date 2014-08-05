class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return a string or None
    def strStr(self, haystack, needle):
        n = len(haystack)
        m = len(needle)
        for i in range(n + 1 - m):
            matched = True
            for k in range(m):
                if haystack[i + k] != needle[k]:
                    matched = False
                    break
            if matched:
                return haystack[i:]
        return None
