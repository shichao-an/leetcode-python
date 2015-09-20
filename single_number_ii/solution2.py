"""
Given an array of integers, every element appears three times except for one.
Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it
without using extra memory?
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Not correct on LeetCode
        """
        # An 32-bit integer has at most 20 bits as base-3
        m = 20
        pow3 = [1 for _ in range(m)]
        for i in range(1, m):
            pow3[i] = pow3[i - 1] * 3
        print pow3

        bits = [0 for _ in range(m)]
        # For each bit of every integer, do XOR on three elements
        for i in range(m):
            for c in nums:
                bits[i] = (bits[i] + c / pow3[i]) % 3
        res = 0
        for i in range(m):
            res += pow3[i] * bits[i]
        return res


a1 = [2, 2, 3, 2]
s = Solution()
print s.singleNumber(a1)
