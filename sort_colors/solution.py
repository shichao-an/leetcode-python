class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        n = len(A)
        r = 0  # Last index of red
        b = n - 1  # First index of white
        i = 0
        while i <= b:
            if A[i] == 0:
                A[i], A[r] = A[r], A[i]
                r += 1
                # Increment i because swapped item must be 1 or 0
                i += 1
            elif A[i] == 2:
                A[i], A[b] = A[b], A[i]
                b -= 1
                # Do not increment i, since swapped item may be 0, 1, or 2
                continue
            # A[i] == 1
            else:
                i += 1
