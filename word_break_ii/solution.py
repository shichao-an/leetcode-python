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
        :rtype: List[str]

        Time Limit Exceeded
        """
        cand = []
        res = []
        self.word_break_aux(s, wordDict, cand, res)
        return res

    def word_break_aux(self, s, wordDict, cand, res):
        """
        Determine if s[:i + 1] can be segmented by dict wordDict
        """
        if not s:
            res.append(' '.join(cand))
        else:
            for i, c in enumerate(s):
                word = s[:i + 1]
                rest = s[i + 1:]
                if word in wordDict:
                    cand.append(word)
                    self.word_break_aux(rest, wordDict, cand, res)
                    cand.pop()


s1 = "catsanddog"
d1 = ["cat", "cats", "and", "sand", "dog"]
s = Solution()
print(s.wordBreak(s1, d1))
