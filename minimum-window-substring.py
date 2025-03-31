'''
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in 
t (including duplicates) is included in the window. 
If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.

https://leetcode.com/problems/minimum-window-substring/
'''

import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        t_map = collections.defaultdict(int)
        for char in t:
            t_map[char]+=1
        
        n = len(t_map)
        
        formed = 0
        
        l,r = 0,0
        
        ans = float('inf'),None,None
        
        window_map = collections.defaultdict(int)
        
        while r < len(s):
            curr_char = s[r]
            window_map[curr_char] += 1
            
            if curr_char in t_map and window_map[curr_char] == t_map[curr_char]:
                formed += 1
            
            while formed == n and l <= r:
                l_char = s[l]
                if r-l+1 < ans[0]:
                    ans = (r-l+1,l,r)
                    
                window_map[l_char] -= 1
                if l_char in t_map and window_map[l_char] < t_map[l_char]:
                    formed -= 1
                    
                l += 1 
                
            r += 1
            
        if ans[0] == float('inf'):
            print(ans)
            return ""
        
        return s[ans[1]:ans[2]+1]
                    