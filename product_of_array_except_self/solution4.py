
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
        """
        n = len(nums)
        res = [1 for i in range(n)]
        # Scan from left to right
        for i in range(1, n):
            # i is from 1 to n - 1
            # res[i] is the product accumulated to the left
            res[i] = res[i - 1] * nums[i - 1]

        # right_product is the product accumulated to the right
        right_product = 1
        for i in range(1, n):
            # j ranges from i - 2 to 0
            j = n - 1 - i
            right_product *= nums[j + 1]
            res[j] *= right_product
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
