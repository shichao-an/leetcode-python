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
        t = set()
        return self.word_break_aux(s, wordDict, t)

    def word_break_aux(self, s, wordDict, t):
        if not s:
            return True
        if s in t:
            return True
        else:
            for i, c in enumerate(s):
                word = s[:i + 1]
                rest = s[i + 1:]
                if word in wordDict and self.wordBreak(rest, wordDict):
                    t.add(s)
                    print(t)
                    return True
            return False
