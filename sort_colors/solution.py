class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        red = 0  # 0
        white = 0  # 1
        blue = 0  # 2
        n = len(A)
        for i in range(n):
            j = i
            if A[i] == 0:
                while j - 1 >= red:
                    A[j], A[j - 1] = A[j - 1], A[j]
                    j -= 1
                red += 1
            elif A[i] == 1:
                while j - 1 >= white + red:
                    A[j], A[j - 1] = A[j - 1], A[j]
                    j -= 1
                white += 1
            elif A[i] == 2:
                while j - 1 >= blue + white + red:
                    A[j], A[j - 1] = A[j - 1], A[j]
                    j -= 1
                blue += 1
