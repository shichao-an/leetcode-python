class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsetsWithDup(self, nums):
        nums.sort()
        return self.subsets_aux(nums)

    def subsets_aux(self, nums):
        if not nums:
            return [[]]
        else:
            res = [[]]
            for i, e in enumerate(nums):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                rest_subsets = self.subsets_aux(nums[i + 1:])
                for subset in rest_subsets:
                    subset.insert(0, e)
                res += rest_subsets
            return res

s = Solution()
print s.subsetsWithDup([1, 2, 2])
