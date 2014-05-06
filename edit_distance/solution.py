class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
        n = len(word1)
        m = len(word2)
        d = [[0 for j in range(m + 1)] for i in range(n + 1)]
        for i in range(n + 1):
            d[i][0] = i
        for j in range(m + 1):
            d[0][j] = j
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:
                    d[i][j] = d[i - 1][j - 1]
                else:
                    op = min(d[i - 1][j - 1],  # Substitute
                             d[i - 1][j],  # Insert
                             d[i][j - 1])  # Delete
                    d[i][j] = op + 1
        return d[n][m]
