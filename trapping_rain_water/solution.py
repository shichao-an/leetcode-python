class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        n = len(A)
        res = 0
        last = 0
        stack = []
        for i in range(1, n):
            if A[i] >= A[last]:
                # Calculate trapped water
                w = i - last - 1
                area = w * A[last]
                while stack:
                    area -= A[stack.pop()]
                res += area
                last = i
            else:
                stack.append(i)
        # Process remaining bars
        if stack:
            r = stack.pop()  # Rightmost effective bar
            while stack:
                if A[stack[-1]] >= A[r]:
                    r = stack.pop()
                else:
                    break
            while stack:
                i = stack.pop()
                if A[i] < A[r]:
                    res += A[r] - A[i]
                else:
                    r = i
        return res
