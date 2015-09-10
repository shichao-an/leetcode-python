"""
Find the kth largest element in an unsorted array. Note that it is the kth
largest element in the sorted order, not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note: You may assume k is always valid, 1 <= k <= array's length.
"""


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int

        Quickselect: O(n)
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            pivot = self.partition(nums, left, right)
            # nums[pivot] is (pivot + 1)th largest, so
            # if pivot == k - 1, it is kth largest.
            if pivot == k - 1:
                return nums[pivot]
            elif pivot < k - 1:
                left = pivot + 1
            else:
                right = pivot - 1

    def partition(self, nums, left, right):
        """Partition the array so that larger elements are to the left"""
        pivot = right
        # i is from left to right - 1
        j = left
        for i in range(left, right):
            if nums[i] > nums[pivot]:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        nums[j], nums[pivot] = nums[pivot], nums[j]
        return j


s = Solution()
a = [3, 2, 1, 5, 6, 4]

print s.findKthLargest(a, 2)
