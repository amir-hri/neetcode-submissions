class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        islands=0

        def dfs(grid, i, j):
            row = len(grid)
            col = len(grid[0])
            if (i<0 or i>=row or j<0 or j>=col or grid[i][j]=='0'):
                return
            grid[i][j]='0'
            dfs(grid, i, j-1)
            dfs(grid, i, j+1)
            dfs(grid, i-1, j)
            dfs(grid, i+1, j)

        for r in range(n):
            for c in range(m):
                if grid[r][c]=='1':
                    islands+=1
                    dfs(grid, r, c)
        return islands