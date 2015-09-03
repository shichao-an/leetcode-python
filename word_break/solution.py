"""
Given a string s and a dictionary of words dict, determine if s can be
segmented into a space-separated sequence of one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".
"""

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        n = len(s)
        # t[i] indicates s[:i + 1] is such a string
        t = [False for i in range(n)]
        for i in range(n):
            if s[:i + 1] in wordDict:
                t[i] = True
            else:
                for j in range(i):
                    if t[j] is True and s[j + 1:i + 1] in wordDict:
                        t[i] = True
                        break
        return t[-1]
