class Solution:
    # @param {character[][]} grid
    # @return {integer}
    def numIslands(self, grid):
        self.islands = set()  # coordinates of 1s (set of tuples)
        res = 0
        n = len(grid)
        if n == 0:
            return 0
        m = len(grid[0])
        if m == 0:
            return 0
        for y in range(n):
            for x in range(m):
                if grid[y][x] == '1' and (x, y) not in self.islands:
                    self.probe(grid, x, y, m, n)
                    res += 1
        return res

    def probe(self, grid, x, y, m, n):
        """
        Probe right and down
        """
        if x >= m or y >= n:
            return
        elif grid[y][x] == '0':
            return
        else:
            self.islands.add((x, y))
            self.probe(grid, x + 1, y, m, n)
            self.probe(grid, x, y + 1, m, n)


g1 = [
    list('11000'),
    list('11000'),
    list('00100'),
    list('00011')
]
for r in g1:
    print(r)
s = Solution()
print(s.numIslands(g1))
print(s.islands)
