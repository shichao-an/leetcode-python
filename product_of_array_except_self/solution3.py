"""
Given an array of n integers where n > 1, nums, return an array output such
that output[i] is equal to the product of all the elements of nums except
nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity? (Note: The output array
does not count as extra space for the purpose of space complexity analysis.)
"""

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        Space: O(n)
        """
        n = len(nums)
        # left[i] is the product to the left of i (nums[0..i - 1])
        left = [1 for i in range(n)]
        # right[i] is the product to the right of i (nums[i + 1..-1])
        right = [1 for i in range(n)]
        for i in range(1, n):
            # i ranges from 1 to n - 1
            # j ranges from n - 2 to 0
            j = n - 1 - i
            left[i] = left[i - 1] * nums[i - 1]
            right[j] = right[j + 1] * nums[j + 1]
        res = [1 for i in range(n)]
        for i in range(n):
            res[i] = left[i] * right[i]
        return res


a0 = [0, 0]
a1 = [1, 2, 3]
a2 = [2, 3, 4]
a3 = [1, 2, 3, 4]
a4 = [2, 3, 4, 5]

s = Solution()
print(s.productExceptSelf(a0))
print(s.productExceptSelf(a1))
print(s.productExceptSelf(a2))
print(s.productExceptSelf(a3))
print(s.productExceptSelf(a4))
