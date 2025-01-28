#  This is a good question

"""
542. 01 Matrix
Solved
Medium
Topics
Companies
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two cells sharing a common edge is 1.

 

Example 1:


Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]
Example 2:


Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
mat[i][j] is either 0 or 1.
There is at least one 0 in mat.

https://leetcode.com/problems/01-matrix/description/

"""

# the key logic is that we mark the all the zeros as zero first
# then start bfs with all the zeros and keep updating the values.





from collections import deque
class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(mat)
        cols = len(mat[0])

        dp = [[float('inf') for _ in range(cols)] for _ in range(rows)]
        queue = deque()
        
        for c in range(cols):
            for r in range(rows):
                if mat[r][c] == 0:
                    dp[r][c] = 0 
                    queue.append((r,c))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            r,c = queue.popleft()
            for dr,dc in directions:
                nr,nc = r+dr, c+dc 
                if 0 <= nr < rows and 0 <= nc < cols:
                    if dp[nr][nc] > dp[r][c] + 1:
                        dp[nr][nc] = dp[r][c] + 1
                        queue.append((nr,nc))

        return dp