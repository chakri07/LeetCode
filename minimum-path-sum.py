"""

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

 

Example 1:


Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
Example 2:

Input: grid = [[1,2,3],[4,5,6]]
Output: 12


https://leetcode.com/problems/minimum-path-sum
"""


class Solution:
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 and j != n - 1:
                    dp[i][j] = grid[i][j] + dp[i][j + 1]
                elif j == n - 1 and i != m - 1:
                    dp[i][j] = grid[i][j] + dp[i + 1][j]
                elif j != n - 1 and i != m - 1:
                    dp[i][j] = grid[i][j] + min(dp[i + 1][j], dp[i][j + 1])
                else:
                    dp[i][j] = grid[i][j]
        return dp[0][0]


from typing import List
import heapq
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # sum , r, c 
        heap = [(grid[0][0],0,0)]
        dirs = [(0,1),(1,0)]

        rows = len(grid)
        cols = len(grid[0])

        matrix = [[float('inf')] * cols for _ in range(rows)]
        
        matrix[0][0] = grid[0][0]

        while heap:
            curr_sum, r, c = heapq.heappop(heap)
            
            if (r,c) == (rows-1, cols-1):
                return curr_sum

            for dr, dc in dirs:
                nr,nc = r+dr, c+dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    new_sum = curr_sum + grid[nr][nc]
                    if matrix[nr][nc] > new_sum:
                        matrix[nr][nc] = new_sum 
                        heapq.heappush(heap, (new_sum, nr,nc))

        return -1