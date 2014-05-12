class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        n = len(A)
        if len(A) == 1:
            return 0
        t = [0 for i in range(n)]
        for i in range(n):
            t[i] = A[i] + i
        count = 0
        min_i = n - 1  # Mininum index able to reach `cur`
        cur = n - 1  # Current index to reach (in a loop)
        while i > 0:
            while i >= 0:
                if t[i] >= cur:
                    min_i = i
                i -= 1
            count += 1
            cur = min_i
            i = cur
        return count
