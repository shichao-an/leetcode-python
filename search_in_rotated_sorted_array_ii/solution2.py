"""
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Follow up for "Search in Rotated Sorted Array":

What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Write a function to determine if a given target is in the array.
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            mid = left + (right - left) / 2
            if target == nums[mid]:
                return True
            # Left part is sorted
            elif nums[mid] > nums[right]:
                if nums[left] <= target < nums[mid]:
                    right = mid
                else:
                    left = mid
            # Right part is sorted
            elif nums[mid] < nums[right]:
                if nums[mid] < target <= nums[right]:
                    left = mid
                else:
                    right = mid
            else:
                right -= 1
        if nums[left] == target or nums[right] == target:
            return True
        return False
