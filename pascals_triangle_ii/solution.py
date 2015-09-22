"""
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].


[1,1,1,1,1],
[1,1,1,1,1],
[1,2,1,1,1],
[1,3,3,1,1],
[1,4,6,4,1],

Note:
Could you optimize your algorithm to use only O(k) extra space?
"""

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [1 for i in range(rowIndex + 1)]
        for row in range(rowIndex + 1):
            for col in range(1, row):
                col = row - col
                res[col] += res[col - 1]
        return res

s = Solution()
print s.getRow(3)
