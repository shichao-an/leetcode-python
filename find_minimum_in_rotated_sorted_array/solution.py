"""
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.
"""

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        left = 0
        right = n - 1
        if n == 1 or nums[left] < nums[right]:
            return nums[0]
        while left <= right:
            mid = left + (right - left) / 2
            if mid > 0 and nums[mid - 1] > nums[mid]:
                return nums[mid]
            # The minimum element is in the right side
            elif nums[mid] > nums[right]:
                left = mid + 1
            # The minimum element is in the left side
            else:
                right = mid - 1


a1 = [4, 5, 6, 7, 0, 1, 2]
s = Solution()
print(s.findMin(a1))
