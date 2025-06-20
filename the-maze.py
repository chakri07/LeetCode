"""

There is a ball in a maze with empty spaces (represented as 0) and walls (represented as 1). The ball can go through the empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the m x n maze, the ball's start position and the destination, where start = [startrow, startcol] and destination = [destinationrow, destinationcol], return true if the ball can stop at the destination, otherwise return false.

You may assume that the borders of the maze are all walls (see examples).

 

Example 1:


Input: maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [4,4]
Output: true
Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.
Example 2:


Input: maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [3,2]
Output: false
Explanation: There is no way for the ball to stop at the destination. Notice that you can pass through the destination but you cannot stop there.
Example 3:

Input: maze = [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]], start = [4,3], destination = [0,1]

https://leetcode.com/problems/the-maze
"""
from typing import List

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        dirs = [(0,1),(1,0),(-1,0),(0,-1)]

        rows = len(maze)
        cols = len(maze[0])

        def dfs(x,y, visited):
            if visited[x][y]:
                return False

            if x == destination[0] and y == destination[1]:
                return True
            
            visited[x][y] = True

            dirs = [(0,1),(1,0),(-1,0),(0,-1)]

            for dr,dc in dirs:
                nr, nc = x+dr, y+dc
                while 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == 0:
                    nr += dr
                    nc += dc

                if dfs(nr-dr,nc-dc,visited):
                    return True

            return False

        visited = [[False] * cols for _ in range(rows)]

        return dfs(start[0], start[1], visited)