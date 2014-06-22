class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        n = len(A)
        num_max_left = [0 for i in range(n)]
        num_max_right = [0 for i in range(n)]
        max_left = 0
        max_right = 0
        res = 0
        for i in range(n):
            num_max_left[i] = max_left
            max_left = max(A[i], max_left)
        for i in range(n):
            j = n - 1 - i
            num_max_right[j] = max_right
            max_right = max(A[j], max_right)
        for i in range(1, n - 1):
            min_num = min(num_max_left[i], num_max_right[i])
            if min_num > A[i]:
                res += min_num - A[i]
        return res
