"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

 

Example 1:


Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.

https://leetcode.com/problems/rotting-oranges/description/
"""

from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        queue = deque([])
        marked = set()
        fresh = 0

        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1

        if fresh == 0 :
            return 0


        neighs = [(1,0),(0,1),(-1,0),(0,-1)]
        
        time = -1


        while queue:
            r,c = queue.popleft()
            for dr,dc in neighs:
                nr,nc = r+dr, c+dc
                if 0 <= nr < rows and \
                    0 <= nc < cols and \
                    grid[nr][nc] == 1 and \
                    (nr,nc) not in marked:
                    marked.add((nr,nc))
        
            if len(queue) == 0:
                for r,c in marked:
                    grid[r][c] = 2
                    fresh -= 1 
                queue.extend(list(marked))
                time +=1 
                marked = set()

        if fresh > 0 :
            return -1 


        return time




        