class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A:
            return 0
        j = 0
        counter = 0  # How many times repeated (1 for twice)
        n = len(A)
        for i in range(1, n):
            if A[i] == A[j] and counter <= 0:
                j += 1
                A[j] = A[i]
                counter += 1
            elif A[i] != A[j]:
                j += 1
                A[j] = A[i]
                counter = 0
        return j + 1
