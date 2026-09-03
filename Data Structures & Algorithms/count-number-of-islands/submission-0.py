class Solution:
    def dfs(self, grid, r, c):
        rows = len(grid)
        cols = len(grid[0])
        if (r<0 or r>rows-1) or (c<0 or c>cols-1):
            return
        if grid[r][c]=="0":
            return
        grid[r][c]="0"
        self.dfs(grid, r-1, c)
        self.dfs(grid, r+1, c)
        self.dfs(grid, r, c-1)
        self.dfs(grid, r, c+1)



    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        islands=0
        for i in range(n):
            for j in range(m):
                curr = grid[i][j]
                if curr=="1":
                    islands+=1
                    self.dfs(grid, i-1, j)
                    self.dfs(grid, i+1, j)
                    self.dfs(grid, i, j-1)
                    self.dfs(grid, i, j+1)
        return islands
                    
