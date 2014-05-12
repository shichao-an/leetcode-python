class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        n = len(A)
        if n == 1:
            return True
        t = 0  # Number of remaining steps
        for i in range(1, n):
            t = max(t, A[i - 1]) - 1
            if t < 0:
                return False
        return True
