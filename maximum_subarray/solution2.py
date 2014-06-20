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
