# -*- coding: utf-8 -*-
"""
Write an efficient algorithm that searches for a value in an m x n matrix.
This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
For example,

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        n = len(matrix)
        m = len(matrix[0])
        if target < matrix[0][0] or target > matrix[n - 1][m - 1]:
            return False
        # Step-wise Linear Search from upper right
        y = 0
        x = m - 1
        while x >= 0 and y <= n - 1:
            if target == matrix[y][x]:
                return True
            elif target < matrix[y][x]:
                x -= 1
            else:
                y += 1
        return False


a1 = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]

s = Solution()
print(s.searchMatrix(a1, 5))
print(s.searchMatrix(a1, 20))
print(s.searchMatrix(a1, 17))
