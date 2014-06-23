class Solution:
    # @return an integer
    def reverse(self, x):
        pos = True
        if x < 0:
            pos = False
            x = -x
        t = 0
        while x != 0:
            t = t * 10 + x % 10
            x /= 10
        if not pos:
            return -t
        return t
