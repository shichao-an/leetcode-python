# -*- coding: utf-8 -*-
# Time Limit Exceeded
"""
Given an array S of n integers, are there elements a, b, c, and d in S such
that a + b + c + d = target? Find all unique quadruplets in the array which
gives the sum of target.

Note:
Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b
≤ c ≤ d)
The solution set must not contain duplicate quadruplets.
    For example, given array S = {1 0 -1 0 -2 2}, and target = 0.

    A solution set is:
    (-1,  0, 0, 1)
    (-2, -1, 1, 2)
    (-2,  0, 0, 2)
"""


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n = len(nums)
        nums.sort()
        res = []
        for a in range(n - 3):
            if a > 0 and nums[a - 1] == nums[a]:
                continue
            for b in range(a + 1, n - 2):
                if b > a + 1 and nums[b - 1] == nums[b]:
                    continue
                c = b + 1
                d = n - 1
                while c < d:
                    s = nums[a] + nums[b] + nums[c] + nums[d]
                    if s == target:
                        res.append([nums[a], nums[b], nums[c], nums[d]])
                        c += 1
                        d -= 1
                        while c < d and nums[c] == nums[c - 1]:
                            c += 1
                        while c < d and nums[d] == nums[d + 1]:
                            d -= 1
                    elif s < target:
                        c += 1
                    else:
                        d -= 1
        return res
