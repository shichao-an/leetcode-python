class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def maximalRectangle(self, matrix):
        # Make a list of heights
        if not matrix:
            return 0
        n = len(matrix)
        if not matrix[0]:
            return 0
        m = len(matrix[0])
        hist = [[0 for j in range(m)] for i in range(n)]
        for i in range(n):
            for j in range(m):
                if i == 0:
                    hist[i][j] = int(matrix[i][j])
                else:
                    if matrix[i][j] == '1':
                        hist[i][j] = 1 + hist[i - 1][j]
        res = 0
        for row in hist:
            res = max(res, self.max_hist_rect(row))
        return res

    def max_hist_rect(self, heights):
        if not heights:
            return 0
        n = len(heights)
        max_area = heights[0]
        stack = []
        for i in range(n + 1):
            while stack and (i == n or heights[stack[-1]] > heights[i]):
                h = heights[stack.pop()]
                if stack:
                    w = i - stack[-1] - 1
                else:
                    w = i
                max_area = max(max_area, h * w)
            stack.append(i)
        return max_area
