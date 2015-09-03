"""
Given a triangle, find the minimum path sum from top to bottom. Each step you
may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, where n is
the total number of rows in the triangle.
"""

class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        t = [[0 for col in row] for row in triangle]  # Initialize t
        n = len(triangle)
        row = n - 1
        while row >= 0:
            if row == n - 1:
                for col in range(row + 1):
                    t[row][col] = triangle[row][col]
            else:
                for col in range(row + 1):
                    minsum = min(t[row + 1][col], t[row + 1][col + 1])
                    t[row][col] = triangle[row][col] + minsum
            row -= 1
        return t[0][0]
