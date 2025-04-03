"""
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.

 

Example 1:


Input: grid = [[0,1],[1,0]]
Output: 2
Example 2:


Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4
Example 3:

Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1
https://leetcode.com/problems/shortest-path-in-binary-matrix
"""
from collections import deque
class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        queue = deque([])
        rows = len(grid)
        cols = len(grid[0])

        queue.append((0,0,0))
        neighs = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)] 
        
        ans = float('inf')

        visited = set()

        if grid[0][0] == 0:
            visited.add((0,0))
        else:
            return -1

        while queue :
            r,c,curr_dist = queue.popleft()
            curr_dist += 1 
            if (r,c) == (rows-1, cols-1):
                    print(curr_dist)
                    ans = min(ans,curr_dist)
                    continue 
            
            for dr,dc in neighs:
                nr, nc = r+dr, c+dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if not (nr,nc) in visited and grid[nr][nc] == 0:
                        visited.add((nr,nc))
                        queue.append((nr,nc,curr_dist))

        if ans == float('inf'):
            return -1 
        else: 
            return ans

                
