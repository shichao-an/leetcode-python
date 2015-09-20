# -*- coding: utf-8 -*-
"""
Given an integer array of size n, find all elements that appear more than ⌊
n/3 ⌋ times. The algorithm should run in linear time and in O(1) space.
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        cand1 = None
        cand2 = None
        count1 = 0
        count2 = 0
        for c in nums:
            if cand1 == c:
                count1 += 1
            elif cand2 == c:
                count2 += 1
            elif count1 == 0:
                cand1 = c
                count1 += 1
            elif count2 == 0:
                cand2 = c
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        count1 = 0
        count2 = 0
        for c in nums:
            if cand1 == c:
                count1 += 1
            elif cand2 == c:
                count2 += 1
        m = len(nums) / 3
        res = []
        if count1 > m:
            res.append(cand1)
        if count2 > m:
            res.append(cand2)
        return res


a1 = [8, 8, 7, 7, 7]
a2 = [1, 2]
s = Solution()
print s.majorityElement(a1)
print s.majorityElement(a2)
