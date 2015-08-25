"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find
the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity. Could you implement it
using only constant extra space complexity?
"""

# Alternative solution using a method similar to First Missing Positive

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        i = 0
        while i < n:
            j = nums[i]
            if nums[i] != i and j < n:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        for i, e in enumerate(nums):
            if i != e:
                return i
        else:
            return n


a0 = [0]
a1 = [0, 1, 3]
a2 = [3, 0, 1]
a3 = [3, 5, 1, 2, 0]
s = Solution()
print(s.missingNumber(a0))
print(s.missingNumber(a1))
print(s.missingNumber(a2))
print(s.missingNumber(a3))
