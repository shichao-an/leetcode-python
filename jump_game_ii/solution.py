class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        n = len(A)
        if len(A) == 1:
            return 0
        start = 1
        end = A[0]  # `end` is A[start - 1]
        res = 1  # At least one step if len(A) > 1
        while end < n - 1:
            res += 1
            max_end = 0  # `end` for the next loop
            for i in range(start, end + 1):
                if i + A[i] > max_end:
                    max_end = i + A[i]
            start = end + 1
            end = max_end
        return res
