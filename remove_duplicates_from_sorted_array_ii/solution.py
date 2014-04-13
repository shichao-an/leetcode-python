class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A:
            return 0
        if len(A) == 1:
            return 1
        j = 0  # Position of last processed non-duplicate
        n = len(A)
        twice = False  # Whether last processed non-duplicate appreared twice
        for i in range(1, n):
            # Duplicate is found
            if A[i] == A[j] and not twice:
                twice = True
                j += 1
                A[j] = A[i]
            elif A[i] != A[j]:
                j += 1
                A[j] = A[i]
                twice = False
        return j + 1
