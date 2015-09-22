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
        if n == 0:
            return 1
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


s = Solution()
print(s.climbStairs(0))
print(s.climbStairs(1))
print(s.climbStairs(2))
print(s.climbStairs(3))
print(s.climbStairs(4))
