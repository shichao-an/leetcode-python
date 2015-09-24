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
        n = len(nums)
        left = 0
        right = n - 1
        while left + 1 < right:
            mid = left + (right - left) / 2
            if mid > 0 and nums[mid - 1] < target < nums[mid]:
                return mid
            elif target <= nums[mid]:
                right = mid
            else:
                left = mid
        if nums[left] < target < nums[right]:
            return left + 1
        elif nums[left] == target:
            return left
        elif nums[right] == target:
            return right
        elif nums[left] > target:
            return min(0, left)
        elif nums[right] < target:
            return max(n, right)


a1 = [1, 3]
s = Solution()
print s.searchInsert(a1, 2)
