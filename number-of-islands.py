'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.


Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3


Link:https://leetcode.com/problems/number-of-islands/
'''

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        count = 0 
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == '1':
                    self.dfs(grid,x,y)
                    count = count + 1 
        return count
        
    
    def dfs(self,grid:list[list[str]],x:int,y :int):
        # 1 and 0 are there so we change to v that should do it.
        queue = []
        neighbours = [(-1,0),(1,0),(0,1),(0,-1)]
        
        queue.append((x,y))
        
        while(queue):
            x,y = queue.pop(0)
            for point_x,point_y in neighbours:
                new_x = x + point_x
                new_y = y + point_y
                
                if (new_x >=0 and new_x < len(grid) and new_y>=0 and new_y<len(grid[0])):
                    #it means its a valid point
                    if grid[new_x][new_y] == '1':
                        queue.append((new_x,new_y))
                    grid[new_x][new_y] = 'v'
                
        return