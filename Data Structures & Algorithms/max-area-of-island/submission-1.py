class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # I have to do dfs .? visited grid or change to zero.?

        rows = len(grid)
        cols = len(grid[0])

        max_area = 0 

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = self.dfs(r,c,grid)
                    max_area = max(area, max_area)

        return max_area



    def dfs(self,r,c,grid) -> int:
        rows = len(grid)
        cols = len(grid[0])
        if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1:
            grid[r][c] = 0
            area = 1 
            
            dirs = [(0,1),(0,-1),(1,0),(-1,0)]
            
            for dr, dc in dirs:
                area += self.dfs(r + dr, c + dc, grid) 
                    
            return area
        else:
            return 0
                


        