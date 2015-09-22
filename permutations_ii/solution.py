"""
Given a collection of numbers that might contain duplicates, return all
possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[1,1,2], [1,2,1], and [2,1,1].
"""

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        d = {}
        return self.permute(nums, d)

    def permute(self, nums, d):
        if not nums:
            return [[]]
        else:
            res = []
            for i, c in enumerate(nums):
                if c in d:
                    continue
                else:
                    d[c] = True
                rest_perms = self.permuteUnique(nums[:i] + nums[i + 1:])
                for perm in rest_perms:
                    perm.insert(0, c)
                res += rest_perms
            return res
