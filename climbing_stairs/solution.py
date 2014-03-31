class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        t = [0] * (n + 1)
        t[1] = 1
        if n == 1:
            return t[1]
        t[2] = 2
        if n <= 2:
            return t[n]
        for i in range(3, n + 1):
            t[i] = t[i - 1] + t[i - 2]
        return t[n]
