"""
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

 

Example 1:


Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4
Example 2:


Input: matrix = [["0","1"],["1","0"]]
Output: 1
Example 3:

Input: matrix = [["0"]]
Output: 0
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 300
matrix[i][j] is '0' or '1'.


https://leetcode.com/problems/maximal-square/description/

"""

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        rows = len(matrix)
        cols = len(matrix[0])

        dp = [[ 0 for _ in range(cols)] for _ in range(rows)]
        # what to store in dp .? 
        # we are storing what is the maximum number of square at that place 
        # we find the minimum of neighbours
        # if all are 1 only then we add it as big square 
        # Similarly if all 2's then the biggest sqaure is 3 etc

        

        ans = 0
        for i in range(rows):
            if matrix[i][0] == "1":
                dp[i][0] = 1
                ans = 1
            else:
                dp[i][0] = 0
        
        for i in range(cols):
            if matrix[0][i] == "1":
                dp[0][i] = 1
                ans = 1
            else:
                dp[0][i] = 0
        

        for r in range(1,rows):
            for c in range(1,cols):
                if matrix[r][c] == "1":
                    dp[r][c] = min(dp[r-1][c-1],\
                                    dp[r][c-1],\
                                    dp[r-1][c]) + 1
                    
                    ans = max(dp[r][c],ans)

        return ans * ans
