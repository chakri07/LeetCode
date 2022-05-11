'''
Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

https://leetcode.com/problems/longest-substring-without-repeating-characters
'''

# try and use a map 
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        l = 0 
        r = 1
        
        ans = 1
        while r < len(s):
            curr = s[r]
            if curr in s[l:r]:
                while curr in s[l:r] and l <r:
                    l = l + 1
            
            ans  = max(r-l+1,ans)
            r = r + 1
            
        return ans
            