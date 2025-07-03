"""
There is a ball in a maze with empty spaces (represented as 0) and walls (represented as 1). The ball can go through the empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the m x n maze, the ball's start position and the destination, where start = [startrow, startcol] and destination = [destinationrow, destinationcol], return the shortest distance for the ball to stop at the destination. If the ball cannot stop at destination, return -1.

The distance is the number of empty spaces traveled by the ball from the start position (excluded) to the destination (included).

You may assume that the borders of the maze are all walls (see examples).

 

Example 1:


Input: maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [4,4]
Output: 12
Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.
The length of the path is 1 + 1 + 3 + 1 + 2 + 2 + 2 = 12.
Example 2:


Input: maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [3,2]
Output: -1
Explanation: There is no way for the ball to stop at the destination. Notice that you can pass through the destination but you cannot stop there.
Example 3:

Input: maze = [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]], start = [4,3], destination = [0,1]
Output: -1

https://leetcode.com/problems/the-maze-ii
"""

import heapq
from typing import List

class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        
        # distance r,c 
        heap = [(0,start[0],start[1])]

        dirs = [(0,1),(1,0),(-1,0),(0,-1)]

        rows = len(maze)
        cols = len(maze[0])


        dist_grid = [[float('inf')] * cols for _ in range(rows)]

        dist_grid[start[0]][start[1]] = 0 

        while heap:
            curr_dist, r,c = heapq.heappop(heap)

            if r == destination[0] and c == destination[1]:
                return curr_dist

            # from here it can go all 4 dirs
            for dr, dc in dirs:
                nr ,nc = r,c 
                temp_dist = curr_dist
                while 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == 0:
                    nr += dr
                    nc += dc
                    temp_dist += 1
                
                nr -= dr
                nc -= dc
                temp_dist -= 1
                if dist_grid[nr][nc] > temp_dist:
                    dist_grid[nr][nc] = temp_dist
                    heapq.heappush(heap, (temp_dist, nr, nc))

        return -1
