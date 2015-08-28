"""
Find the contiguous subarray within an array (containing at least one number)
which has the largest sum.

For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
the contiguous subarray [4,−1,2,1] has the largest sum = 6.
"""

class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        if not A:
            return 0
        res = A[0]
        cur_sum = A[0]
        n = len(A)
        for i in range(1, n):
            cur_sum = max(cur_sum + A[i], A[i])
            res = max(res, cur_sum)
        # If negative sum is not allowed, add the following line:
        # if res < 0: return 0
        return res
