from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # lets do bfs
        rows = len(grid)
        cols = len(grid[0])
        max_area = 0 


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = self.bfs(r,c,grid)
                    max_area = max(area, max_area)

        return max_area

    def bfs(self,r,c,grid):
        area = 1
        grid[r][c] = 0 
        queue = deque()
        queue.append((r,c))

        rows = len(grid)
        cols = len(grid[0])

        dirs = [(0,1),(0,-1),(-1,0),(1,0)]

        while queue:
            r,c = queue.popleft()
            for dr,dc in dirs:
                nr, nc = r+dr, c+dc 
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 0 
                        area += 1
                        queue.append((nr,nc))

        return area












