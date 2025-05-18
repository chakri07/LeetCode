"""

You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

 

Example 1:


Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0


https://leetcode.com/problems/max-area-of-island
"""

from collections import defaultdict
from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        max_area = [float('-inf')]

        neighs = [(1,0),(0,1),(0,-1),(-1,0)]

        rows = len(grid)
        cols = len(grid[0])

        area_map = defaultdict(int)

        def dfs(r,c,label):
            for dr,dc in neighs:
                nr,nc = r+dr, c+dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 0
                        area_map[label] += 1
                        dfs(nr,nc,label)

        label = 2
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    grid[r][c] = 0
                    area_map[label] += 1
                    dfs(r,c,label)
                    label += 1

        if not list(area_map.values()):
            return 0 
        else:
            return max(list(area_map.values()))
