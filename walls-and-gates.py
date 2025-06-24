"""

You are given an m x n grid rooms initialized with these three possible values.

-1 A wall or an obstacle.
0 A gate.
INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

 

Example 1:


Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
Example 2:

Input: rooms = [[-1]]
Output: [[-1]]
 

Constraints:

m == rooms.length
n == rooms[i].length
1 <= m, n <= 250
rooms[i][j] is -1, 0, or 231 - 1.

https://leetcode.com/problems/walls-and-gates
"""


from collections import deque
from typing import List

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not rooms[0]:
            return

        rows = len(rooms)
        cols = len(rooms[0])
        
        # Directions for neighbors (right, down, left, up)
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        queue = deque()

        # Initialize the queue with all gates
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:  # If it's a gate
                    queue.append((r, c))
        
        # Perform multi-source BFS
        while queue:
            r, c = queue.popleft()

            # Explore neighbors
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                # Check if neighbor is within bounds, is an empty room, and hasn't been visited with a shorter path
                # An empty room is rooms[nr][nc] == float('inf') (or 2147483647)
                # Since BFS guarantees shortest path, if rooms[nr][nc] is still INF, it means we found a shorter path
                if 0 <= nr < rows and 0 <= nc < cols and rooms[nr][nc] == 2147483647: # Assuming INF is 2147483647
                    rooms[nr][nc] = rooms[r][c] + 1
                    queue.append((nr, nc))

        # The rooms grid is modified in-place, so no return value is needed.