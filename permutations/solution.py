"""
Given a collection of numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].

"""


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        else:
            res = []
            for i, e in enumerate(nums):
                rest = nums[:i] + nums[i + 1:]
                rest_perms = self.permute(rest)
                for perm in rest_perms:
                    perm.append(e)
                res += rest_perms
            return res
