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
            msg = 'The input array must contain at least one number.'
            raise Exception(msg)
        max_sum = A[0]
        max_current = max_sum
        for i in range(1, len(A)):
            max_current = max(A[i], max_current + A[i])
            max_sum = max(max_sum, max_current)
        return max_sum
