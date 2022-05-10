'''
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

 

Example 1:


Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
Example 2:


Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3



Link : https://leetcode.com/problems/number-of-provinces/
'''
# basically dfs

class Solution:
    def findCircleNum(self, grid: list[list[int]]) -> int:
        ans = 0 
        for x,row in enumerate(grid):
            for y,val in enumerate(row):
                if val == 1:
                    grid[x][y] = 'v'
                    self.dfs(grid,x)
                    ans = ans + 1
        return ans
    
    def dfs( self, grid : list[list[int]],start:int):
        conn =[]
        conn.append(start)
        while conn:
            x = conn.pop()
            row = grid[x]
            for y,val in enumerate(row):
                if val == 1 and x != y:
                    conn.append(y)
                grid[x][y] = 'v'
            
            
            
                
        
                    
        