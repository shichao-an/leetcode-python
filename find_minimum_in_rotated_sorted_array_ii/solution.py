"""
Follow up for "Find Minimum in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array may contain duplicates.
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
        if n == 1:
            return nums[0]
        while left <= right:
            mid = left + (right - left) / 2
            if mid > 0 and nums[mid - 1] > nums[mid]:
                return nums[mid]
            # The minimum element is in the right side
            elif nums[mid] > nums[right]:
                left = mid + 1
            # The minimum element is in the left side
            elif nums[mid] < nums[right]:
                right = mid - 1
            # The mid element equals the right element
            else:
                right -= 1
        # All elements are equal
        return nums[0]

a1 = [4, 5, 6, 7, 0, 1, 2]
a2 = [4, 5, 6, 7, 0, 1, 1, 1]
a3 = [4, 5, 6, 7, 0, 1, 2, 4]
a5 = [1, 1]
a4 = [1, 1, 1]
s = Solution()
print(s.findMin(a1))
print(s.findMin(a2))
print(s.findMin(a3))
print(s.findMin(a4))
print(s.findMin(a5))
