"""
You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

Return the size of the largest island in grid after applying this operation.

An island is a 4-directionally connected group of 1s.

 

Example 1:

Input: grid = [[1,0],[0,1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
Example 2:

Input: grid = [[1,1],[1,0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.
Example 3:

Input: grid = [[1,1],[1,1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 4.
 

Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 500
grid[i][j] is either 0 or 1.

https://leetcode.com/problems/making-a-large-island/
"""

"""
instead of flipping 0 to 1 and calulcating the areas what we do is 

we caluclate the area of the island in the exisiting grid and mark each cell in the grid 
with a label and we store area corressponding to that label in a map 

Then we start flipping bits and combine the areas of the islands with neighbouring cell labels
and get the max.
"""


from collections import defaultdict
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        # find the area of each island, mark the each cell with(area,label)
        # then change each 0 to 1 and see what the max area we can get
        area_map = defaultdict(int)
        rows = len(grid)
        cols = len(grid[0])

        neighs = [(1,0),(0,1),(-1,0),(0,-1)]

        label = 2 # starts from 2 to n 

        def dfs(r,c,label):
            
            for dr,dc in neighs:
                nr, nc = r+dr, c+dc 
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == 1:
                        grid[nr][nc] = label
                        area_map[label] += 1
                        dfs(nr,nc,label)
        # caluclate the areas
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    grid[r][c]= label
                    area_map[label] += 1
                    dfs(r,c,label)
                    label += 1
        
        if area_map.values():
            ans = max(list(area_map.values()))
        else:
            ans = 0
        # update the zero to one and combine the areas
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    label_set = set()
                    for dr,dc in neighs:
                        nr,nc = r+dr,c +dc
                        if 0 <= nr < rows and 0 <= nc <cols:
                            label_set.add(grid[nr][nc])

                    combined_area = 1
                    for label in label_set:
                        combined_area += area_map[label]

                    ans = max(combined_area,ans)

        return ans
