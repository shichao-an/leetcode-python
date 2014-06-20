class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        n = len(A)
        if len(A) == 1:
            return 0
        t = [0 for i in range(n - 1)]
        for i in range(n - 1):
            t[i] = A[i] + i
        count = 0
        min_i = n - 1  # Mininum index able to reach `cur`
        cur = n - 1  # Current index to reach (in a loop)
        i = cur - 1
        reached = False  # Whether `cur` can be reached by previous elements
        # Worst case: O(n^2)
        while i >= 0:
            while i >= 0:
                if t[i] >= cur:
                    min_i = i
                    reached = True
                i -= 1
            if not reached:
                return -1
            reached = False
            count += 1
            cur = min_i
            i = cur - 1
        return count


a1 = [2, 3, 1, 1, 4]
a2 = [3, 2, 1, 0, 4]
a3 = [1, 1, 1, 1, 1, 1]
a4 = [1, 0, 1, 1, 1, 1]
s = Solution()
print s.jump(a1)
print s.jump(a2)
print s.jump(a3)
print s.jump(a4)
