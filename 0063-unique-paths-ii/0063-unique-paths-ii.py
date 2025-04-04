class Solution:
    def findPaths(self, row, col, grid, maxRow, maxCol, memo):
        if row == maxRow and col == maxCol:
            return 1
        if row > maxRow or col > maxCol or grid[row][col] == 1:
            return 0
        if memo[row][col] != -1:
            return memo[row][col]
        memo[row][col] = self.findPaths(row, col + 1, grid, maxRow, maxCol, memo) + self.findPaths(row + 1, col, grid, maxRow, maxCol, memo)
        return memo[row][col]

    def uniquePathsWithObstacles(self, grid):
        rows, cols = len(grid), len(grid[0])
        if grid[rows - 1][cols - 1] == 1:
            return 0
        memo = [[-1] * cols for _ in range(rows)]
        return self.findPaths(0, 0, grid, rows - 1, cols - 1, memo)
