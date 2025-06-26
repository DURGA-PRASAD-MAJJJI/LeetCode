class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows,cols =len(grid),len(grid[0])
        maxx=0
        def dfs(r,c):
            if r<0 or c<0 or r>=rows or c>=cols or grid[r][c]==0:
                return 0
            grid[r][c] = 0
            l=1
            l+=dfs(r + 1, c)
            l+=dfs(r - 1, c)
            l+=dfs(r, c + 1)
            l+=dfs(r, c - 1)
            return l
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]== 1:
                    maxx=max(maxx,dfs(i, j))
        return maxx
        