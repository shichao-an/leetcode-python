# -*- coding: utf-8 -*-
"""
Given a sorted array and a target value, return the index if the target is
found. If not, return the index where it would be if it were inserted in
order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0

"""

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        if not nums:
            return 0
        else:
            left = 0
            right = n - 1
            while left <= right:
                mid = (left + right) / 2
                if nums[mid] == target:
                    return mid
                elif (mid < n - 1 and nums[mid] < target
                        and nums[mid + 1] > target):
                    return mid + 1
                elif target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            if left > n - 1:
                return n
            elif right < 0:
                return 0


a = [1, 3, 5, 6]
s = Solution()
print(s.searchInsert(a, 5))
print(s.searchInsert(a, 2))
print(s.searchInsert(a, 7))
print(s.searchInsert(a, 0))
