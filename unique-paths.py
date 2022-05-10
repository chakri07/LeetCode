'''
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

 

Example 1:


Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down


Link:https://leetcode.com/problems/unique-paths/
'''

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = []
        for i in  range(0,m):
            temp = []
            for j in range(0,n):
                temp.append(0)
            dp.append(temp)
            
        dp[0][0] = 1
        for x in range(0,m):
            for y in range(0,n):
                if x-1 >=0 and y-1 >=0:
                    dp[x][y] = dp[x-1][y]+ dp[x][y-1]
                elif y-1 >=0:
                    dp[x][y] = dp[x][y-1]
                elif x-1 >=0:
                    dp[x][y] = dp[x-1][y]
        
        return dp[m-1][n-1]