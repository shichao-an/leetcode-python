"""
Given a string s and a dictionary of words dict, add spaces in s to construct
a sentence where each word is a valid dictionary word.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].
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
        res = self.word_break_aux(s, wordDict, n - 1, t)
        return res

    def word_break_aux(self, s, wordDict, i, t):
        """
        Determine if s[:i + 1] can be segmented by dict wordDict
        """
        if s[:i + 1] in wordDict:
            t[i] = [s[:i + 1]]
            return t[i]
        elif t[i] is not None:
            return t[i]
        else:
            res = []
            for j in range(i):
                rest = self.word_break_aux(s, wordDict, j, t)
                word = s[j + 1:i + 1]
                if rest and word in wordDict:
                    for r in rest:
                        res.append(r + ' ' + word)
            t[i] = res
            return t[i]


s1 = "catsanddog"
d1 = ["cat", "cats", "and", "sand", "dog"]
s = Solution()
print(s.wordBreak(s1, d1))
print(s.wordBreak('leetcode', ['leet', 'code']))
