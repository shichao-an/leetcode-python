"""
Given an array nums, write a function to move all 0's to the end of it while
maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums
should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i, c in enumerate(nums):
            if c != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1


a1 = [0, 1, 0, 3, 12]
s = Solution()
s.moveZeroes(a1)
print a1
