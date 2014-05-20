class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, dict):
        queue = []
        depth = 0
        queue.append((start, depth))
        n = len(dict)
        res = n
        while queue:
            start, depth = queue.pop()
            depth += 1
            if self.is_adjacent(start, end):
                if depth < res:
                    res = depth
            for word in set(dict):
                if self.is_adjacent(start, word):
                    queue.append((word, depth))
                    dict.remove(word)
        if res < n:
            return res + 1
        else:
            return 0

    def is_adjacent(self, word1, word2):
        count = 0
        n = len(word1)
        for i in range(n):
            if word1[i] != word2[i]:
                count += 1
        return count <= 1


s = Solution()
print s.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"])
