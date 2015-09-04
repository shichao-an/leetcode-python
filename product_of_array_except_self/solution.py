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

        Memory Limit Exceeded
        """
        if not nums:
            return []
        elif len(nums) == 1:
            return [1]
        elif len(nums) == 2:
            return nums[::-1]
        else:
            m = 1
            rest = nums[1:]
            for c in rest:
                m *= c
            res = [m]
            for r in self.productExceptSelf(rest):
                res.append(r * nums[0])
            return res


a1 = [1, 2, 3]
a2 = [2, 3, 4]
a3 = [1, 2, 3, 4]
a4 = [2, 3, 4, 5]

s = Solution()
print(s.productExceptSelf(a1))
print(s.productExceptSelf(a2))
print(s.productExceptSelf(a3))
print(s.productExceptSelf(a4))
