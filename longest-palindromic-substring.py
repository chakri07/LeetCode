'''
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Link: https://leetcode.com/problems/longest-palindromic-substring/
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) ==0 :return ""
        start =0 
        end = 0
        for i in range(0,len(s)):
            len1 = self.helper(s,i,i)
            len2 = self.helper(s,i,i+1)
            len_ans = max(len1,len2)
            if ( len_ans > end - start):
                start = i - (len_ans - 1)//2
                end = i + len_ans//2
        return s[start:end+1]
            
    
    def helper(self,s:str,left:int,right:int)-> int:
        while(left >=0 and right<len(s) and s[left]==s[right]):
            left = left-1
            right = right+1
        return right-left-1