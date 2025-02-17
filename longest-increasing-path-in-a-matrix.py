"""

Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

 

Example 1:


Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:


Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
Example 3:

Input: matrix = [[1]]
Output: 1
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
0 <= matrix[i][j] <= 231 - 1

https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/

"""

class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        rows = len(matrix)
        cols = len(matrix[0])

        ans = [1]

        dp = [[0 for _ in range(cols)] for _ in range(rows)]

        def dfs(r,c):
            
            neighs = [(0,1),(1,0),(-1,0),(0,-1)]

            if not dp[r][c] == 0:
                return dp[r][c]

            dp[r][c] = 1


            for dr,dc in neighs:
                nr,nc = r+dr, c+dc
                
                if 0 <= nr < rows and 0 <= nc < cols:
                    if matrix[r][c] < matrix[nr][nc]:
                        dp[r][c] = max(dp[r][c],1 + dfs(nr,nc))
                        ans[0] = max(ans[0],dp[r][c])

            return dp[r][c]

        for r in range(rows):
            for c in range(cols):
                dfs(r,c)
        print(dp)
        return ans[0]
