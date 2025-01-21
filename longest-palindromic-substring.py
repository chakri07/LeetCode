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
## Two pointers approach - Expand around center thinking center is a letter or two letters
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expandAroundCenter(left,right):
            while left >=0 and right < len(s) and s[left] == s[right]:
                left-=1 
                right+=1 

            return left+1,right

        start,end =0,0

        for i in range(len(s)):
            left1,right1 = expandAroundCenter(i,i)
            left2,right2 = expandAroundCenter(i,i+1)

            if right1 - left1 > end - start:
                end = right1
                start = left1
            if right2 - left2 > end-start:
                end = right2
                start = left2

        return s[start:end]
        