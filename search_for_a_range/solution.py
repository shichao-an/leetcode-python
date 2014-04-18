class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        res = [-1, -1]
        n = len(A)
        l = 0
        r = n - 1
        while l <= r:
            mid = l + (r - l) // 2
            if target == A[mid]:
                res = [mid, mid]
                p = q = mid
                while p >= 0 and A[p] == target:
                    res[0] = p
                    p -= 1
                while q <= n - 1 and A[q] == target:
                    res[1] = q
                    q += 1
                break
            elif target < A[mid]:
                r -= 1
            else:
                l += 1
        return res
