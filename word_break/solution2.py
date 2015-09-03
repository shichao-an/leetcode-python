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
        t = [None for i in range(n)]
        return self.word_break_aux(s, wordDict, n - 1, t)

    def word_break_aux(self, s, wordDict, i, t):
        """
        Determine if s[:i + 1] can be segmented by dict wordDict
        """
        if s[:i + 1] in wordDict:
            return True
        elif t[i] is not None:
            return t[i]
        else:
            for j in range(i):
                if (self.word_break_aux(s, wordDict, j, t) is True
                        and s[j + 1:i + 1] in wordDict):
                    t[i] = True
                    return True
            else:
                t[i] = False
                return False


s = Solution()
print(s.wordBreak('leetcode', ['leet', 'code']))
print(s.wordBreak('leetcode', ['lee', 'code']))
