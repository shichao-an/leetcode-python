class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        if not B:
            return
        for i in range(m):
            if A[i] > B[0]:
                A[i], B[0] = B[0], A[i]
            # Bubble the first element to the correct position
                j = 0
                while j < n - 1 and B[j] > B[j + 1]:
                    B[j], B[j + 1] = B[j + 1], B[j]
                    j += 1
        for j in range(m, m + n):
            A[j] = B[j - m]
