"""
Given an array of non-negative integers, you are initially positioned at the
first index of the array.

Each element in the array represents your maximum jump length at that
position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
"""

class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        n = len(A)
        if n == 1:
            return True
        # d[i] is the max index A[i] can reach in A
        d = [i + A[i] for i in range(n)]
        reach = n - 1
        for i in range(1, n):
            # j is from n - 1 to 0
            j = n - 1 - i
            if d[j] >= reach:
                reach = j
        return reach == 0
