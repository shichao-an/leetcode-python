"""
Given an array of integers and an integer k, find out whether there are two
distinct indices i and j in the array such that nums[i] = nums[j] and the
difference between i and j is at most k.
"""

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = {}
        for i, e in enumerate(nums):
            if e in d:
                if i - d[e] <= k:
                    return True
            d[e] = i
        return False


args1 = [[1, 0, 1, 1], 1]
s = Solution()
print(s.containsNearbyDuplicate(*args1))
