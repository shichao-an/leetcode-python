class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        row_left = 0
        row_right = len(matrix) - 1
        while row_left <= row_right:
            row_mid = row_left + (row_right - row_left) / 2
            row = matrix[row_mid]
            if target >= row[0] and target <= row[-1]:
                left = 0
                right = len(row) - 1
                while left <= right:
                    mid = left + (right - left) / 2
                    if target == row[mid]:
                        return True
                    elif target < row[mid]:
                        right -= 1
                    else:
                        left += 1
                return False
            elif target < row[0]:
                row_right -= 1
            elif target > row[-1]:
                row_left += 1
        return False
