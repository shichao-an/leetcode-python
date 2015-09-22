"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you
climb to the top?
"""

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        t = [0 for i in range(n + 1)]
        return self.climb(n, t)

    def climb(self, n, t):
        if n == 0:
            return 1
        elif n < 0:
            return 0
        elif t[n] != 0:
            return t[n]
        else:
            t[n] = self.climb(n - 1, t) + self.climb(n - 2, t)
            return t[n]


s = Solution()
print(s.climbStairs(0))
print(s.climbStairs(1))
print(s.climbStairs(2))
print(s.climbStairs(3))
print(s.climbStairs(4))
