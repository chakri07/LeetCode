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

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1)
        n2 = len(text2)
        rows, cols = (n1, n2)
        dp = [[-1 for i in range(cols)] for j in range(rows)]
        self.helper(text1,text2,dp,n1-1,n2-1)
        return dp[n1-1][n2-1]
    
    def helper(self,text1: str, text2: str,dp :list[list[int]],index1:int,index2:int) ->int:
        if index1 < 0 or index2 < 0:
            return 0
        if dp[index1][index2] != -1:
            return dp[index1][index2]
        
        
        if text1[index1] == text2[index2]:
            diag = self.helper(text1,text2,dp,index1-1,index2-1)
            dp[index1][index2] = diag+1
        else:
            left = self.helper(text1,text2,dp,index1-1,index2)
            top = self.helper(text1,text2,dp,index1,index2-1)
            dp[index1][index2] = max(left,top)
        return dp[index1][index2]