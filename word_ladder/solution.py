"""
Given two words (beginWord and endWord), and a dictionary, find the length of
shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the dictionary
For example,

Given:
start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
"""

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordDict):
        """
        :type beginWord: str
        :type endWord: str
        :type wordDict: Set[str]
        :rtype: int
        """
        queue = []
        queue.append((beginWord, 0))
        self.letters = map(chr, range(ord('a'), ord('z') + 1))
        self.word_dict = wordDict
        # Remove words that are same as beginWord
        for word in set(wordDict):
            if beginWord == word:
                wordDict.remove(beginWord)
        wordDict.add(endWord)
        while queue:
            cur = queue.pop(0)
            if cur[0] == endWord:
                return cur[1] + 1
            for word in self.get_adjacent(cur[0]):
                wordDict.remove(word)  # Mark as visited
                queue.append((word, cur[1] + 1))
        return 0

    def get_adjacent(self, word1):
        res = []
        for i, e in enumerate(word1):
            for letter in self.letters:
                word = word1[:i] + letter + word1[i + 1:]
                if word in self.word_dict:
                    res.append(word)
        return res


s = Solution()
print s.ladderLength("hit", "dow", set(["hot", "dot", "dog", "lot", "log"]))
print s.ladderLength("hit", "cog", set(["hot", "dot", "dog", "lot", "log"]))
print s.ladderLength("hit", "cog", set(["aos", "dis", "dog", "lot", "log"]))
