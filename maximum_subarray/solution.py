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
