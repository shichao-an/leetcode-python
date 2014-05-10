class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        n = len(A)
        i = 0
        while i < n:
            j = A[i] - 1
            if A[i] != i + 1 and A[i] >= 1 and A[i] <= n and A[i] != A[j]:
                A[i], A[j] = A[j], A[i]
            else:
                i += 1
        for i, e in enumerate(A):
            if e != i + 1:
                return i + 1
        return n + 1
