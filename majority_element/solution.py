"""
Given an array of size n, find the majority element. The majority element is
the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always
exist in the array.
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = len(nums) / 2
        d = {}
        for k in nums:
            if k not in d:
                d[k] = 1
            else:
                d[k] += 1
        for k in d:
            if d[k] > m:
                return k
