class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, dict):
        queue = []
        distance = []
        queue.append(start)
        distance.append(1)
        # Remove words that are same as start
        for word in set(dict):
            if start == word:
                dict.remove(start)
        dict.add(end)
        while queue:
            cur = queue.pop(0)
            d = distance.pop(0)
            for word in set(dict):  # Iterate over the copy of dict
                if self.is_adjacent(cur, word):
                    dict.remove(word)  # Mark as visited
                    queue.append(word)
                    if word == end:
                        return d + 1
                    distance.append(d + 1)
        return 0

    def is_adjacent(self, word1, word2):
        count = 0
        n = len(word1)
        for i in range(n):
            if word1[i] != word2[i]:
                count += 1
        return count == 1


s = Solution()
print s.ladderLength("hit", "dow", set(["hot", "dot", "dog", "lot", "log"]))
print s.ladderLength("hit", "cog", set(["hot", "dot", "dog", "lot", "log"]))
