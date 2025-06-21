"""

You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.

You may change 0's to 1's to connect the two islands to form one island.

Return the smallest number of 0's you must flip to connect the two islands.

 

Example 1:

Input: grid = [[0,1],[1,0]]
Output: 1
Example 2:

Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2
Example 3:

Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1
 

Constraints:

n == grid.length == grid[i].length
2 <= n <= 100
grid[i][j] is either 0 or 1.
There are exactly two islands in grid.

https://leetcode.com/problems/shortest-bridge
"""

# class UnionFind:
#     def __init__(self):
#         self.parent = []
#         self.rank = 
#         self.num_sets

from typing import List
from collections import deque

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        """
        I feel like this is again disjoint set union find.
        """
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        rows = len(grid)
        cols = len(grid[0])

        queue= deque([])

        def dfs(r,c):
            
            grid[r][c] = 2
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc 
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == 1:
                        queue.append((nr,nc,0))
                        dfs(nr,nc)
                        

        is_marked = False
        for r in range(rows):
            if is_marked:
                break
            for c in range(cols):
                if grid[r][c] == 1:
                    queue.append((r,c,0))
                    grid[r][c] = 2
                    dfs(r,c)
                    is_marked = True
                    break
        
        
        while queue:
            r,c, dist = queue.popleft()
            for dr, dc in dirs:
                nr,nc = r+dr, c +dc 
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == 1:
                        return dist
                    elif grid[nr][nc] == 0:
                        grid[nr][nc] = 2
                        queue.append((nr,nc, dist + 1))

        return -1
