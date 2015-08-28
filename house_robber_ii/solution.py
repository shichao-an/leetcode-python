"""
Note: This is an extension of House Robber.

After robbing those houses on that street, the thief has found himself a new
place for his thievery so that he will not get too much attention. This time,
all houses at this place are arranged in a circle. That means the first house
is the neighbor of the last one. Meanwhile, the security system for these
houses remain the same as for those in the previous street.

Given a list of non-negative integers representing the amount of money of each
house, determine the maximum amount of money you can rob tonight without
alerting the police.
"""

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]
        return max(self.rob_aux(nums, 0), self.rob_aux(nums, 1))

    def rob_aux(self, nums, left):
        n = len(nums) - 1
        t = [0 for i in range(n + 1)]
        if n == 0:
            return t[n]
        t[1] = nums[left]
        if n <= 1:
            return t[n]
        t[2] = max(nums[left: left + 2])
        for i in range(3, n + 1):
            t[i] = max(t[i - 2] + nums[left + i - 1], t[i - 1])
        return t[n]

a1 = [1]
a2 = [4, 1, 6, 10, 5, 13, 2, 7]
s = Solution()
print(s.rob(a1))
print(s.rob(a2))
