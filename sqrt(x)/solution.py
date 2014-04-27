class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        left = 0
        right = x
        while left <= right:
            mid = left + (right - left) / 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                if (mid + 1) * (mid + 1) > x:
                    return mid
                left = mid + 1
            else:
                if (mid - 1) * (mid - 1) < x:
                    return mid - 1
                right = mid - 1
