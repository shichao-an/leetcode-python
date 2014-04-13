class Solution:
    # @return an integer
    def reverse(self, x):
        t = 0
        if x > 0:
            positive = True
        else:
            positive = False
            x = -x
        while x != 0:
            t = 10 * t + x % 10
            x /= 10
        return t if positive else -t
