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
        count = 0
        cand = None
        for c in nums:
            if count == 0:
                cand = c
                count += 1
            elif cand == c:
                count += 1
            else:
                count -= 1
        return cand
