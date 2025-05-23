'''
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.

Link:https://leetcode.com/problems/longest-common-subsequence 
'''



# cleanest solution
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Dimensions of dp table: (len(text2) + 1) x (len(text1) + 1)
        dp = [[0] * (len(text1) + 1) for _ in range(len(text2) + 1)]

        # Populate the dp table
        for i in range(1, len(text2) + 1):
            for j in range(1, len(text1) + 1):
                if text2[i - 1] == text1[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1]


class Solution:
    def longestCommonSubsequence2(self, text1: str, text2: str) -> int:
        dp = []
        
        for i in range(0,len(text1)):
            temp = []
            for j in range(0,len(text2)):
                temp.append(0)
            dp.append(temp)
        def helper(i,j):
            if i < 0 or j < 0:
                return 0
            if dp[i][j] != 0:
                return dp[i][j]
            if text1[i] == text2[j]:
                dp[i][j] = helper(i-1,j-1) + 1
            else:
                left = helper(i-1,j)
                top = helper(i,j-1)
                
                dp[i][j] = max(left,top)
            
            return dp[i][j]
        
        
        ans=  helper(len(text1)-1,len(text2)-1)
        return ans

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1)
        n2 = len(text2)
        rows, cols = (n1, n2)
        dp = [[0 for i in range(cols)] for j in range(rows)]
        self.helper(text1,text2,dp,n1-1,n2-1)
        return dp[n1-1][n2-1]
    
    def helper(self,text1: str, text2: str,dp :list[list[int]],index1:int,index2:int) ->int:
        if index1 < 0 or index2 < 0:
            return 0
        if dp[index1][index2] != 0:
            return dp[index1][index2]

        if text1[index1] == text2[index2]:
            diag = self.helper(text1,text2,dp,index1-1,index2-1)
            dp[index1][index2] = diag+1
        else:
            left = self.helper(text1,text2,dp,index1-1,index2)
            top = self.helper(text1,text2,dp,index1,index2-1)
            dp[index1][index2] = max(left,top)
        return dp[index1][index2]
    