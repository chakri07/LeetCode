class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [[1,0],[0,1],[-1,0],[0,-1]]

        rows, cols = len(grid), len(grid[0])

        # Corrected initialization of visited array
        visited = [[False for _ in range(cols)] for _ in range(rows)] 

        ans = 0

        def dfs(r,c):
            if r >= 0 and r < rows \
                and c >= 0 and c < cols:
                if grid[r][c] == "1" and not visited[r][c]:
                    visited[r][c] = True
                    for dr,dc in dirs:
                        dfs(r+dr,c+dc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and not visited[r][c]:
                    dfs(r,c)
                    ans = ans + 1
        
        return ans