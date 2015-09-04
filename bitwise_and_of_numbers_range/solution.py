"""
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND
of all numbers in this range, inclusive.

For example, given the range [5, 7], you should return 4.
"""

class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        shift = 0
        while n > m:
            shift += 1
            m = m >> 1
            n = n >> 1
        return m << shift


s = Solution()
print(s.rangeBitwiseAnd(5, 6))
print(s.rangeBitwiseAnd(0, 2147483647))
