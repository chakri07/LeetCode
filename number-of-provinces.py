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
        conn = []
        conn.append(start)
        while conn:
            x = conn.pop()
            row = grid[x]
            for y,val in enumerate(row):
                if val == 1 and x != y:
                    conn.append(y)
                grid[x][y] = 'v'
            
            
            
from typing import List
from collections import defaultdict
## Another solution
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()

        # r = source city 
        # c = dest city  
        graph = defaultdict(set)
        n = len(isConnected)
        def make_graph():
            for i in range(n):
                for j in range(n):
                    if isConnected[i][j] == 1:
                        graph[i].add(j)
                        graph[j].add(i)

        def dfs(city):
            neigh = graph[city]
            for neigh_city in neigh:
                if neigh_city not in visited:
                    visited.add(neigh_city)
                    dfs(neigh_city)

        ans = 0 
        make_graph()
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1 and i not in visited:
                    visited.add(i)
                    dfs(i)
                    # print(visited)
                    ans += 1
        
        return ans
