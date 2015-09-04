"""
Given an array of non-negative integers, you are initially positioned at the
first index of the array.

Each element in the array represents your maximum jump length at that
position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from
index 0 to 1, then 3 steps to the last index.)
"""

class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return 0
        start = 1
        end = nums[0]  # `end` is nums[start - 1]
        res = 1  # At least one step if len(nums) > 1
        reached = False
        while end < n - 1:
            res += 1
            max_end = end  # `end` for the next loop
            for i in range(start, end + 1):
                if i + nums[i] > max_end:
                    max_end = i + nums[i]
                    reached = True
            if not reached:
                return -1
            reached = False
            start = end + 1
            end = max_end
        return res


s = Solution()
a1 = [2, 3, 1, 1, 4]
a2 = [3, 2, 1, 0, 4]
print s.jump(a1)
print s.jump(a2)
