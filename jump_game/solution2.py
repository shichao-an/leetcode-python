class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        n = len(A)
        if n == 1:
            return True
        d = [i + A[i] for i in range(n)]
        reach = n - 1
        for i in range(1, n):
            j = n - 1 - i
            if d[j] >= reach:
                reach = j
        return reach == 0
