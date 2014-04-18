class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        n = len(A)
        if n == 1:
            return True
        t = [0 for i in range(n)]
        for i in range(n - 1):
            t[i] = A[i] + i
        i = n - 1
        reach = n - 1
        while i >= 0:
            if t[i] >= reach:
                reach = i
            i -= 1
        return reach == 0
