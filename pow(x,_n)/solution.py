class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        if n % 2 == 0:
            return pow(x * x, n / 2)
        else:
            return pow(x * x, (n - 1) / 2) * x
