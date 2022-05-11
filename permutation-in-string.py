'''

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false


https://leetcode.com/problems/permutation-in-string/
'''

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        wl = len(s1)
        l = 0 
        r = l + wl - 1
        
        s1 = sorted(s1)
        while r < len(s2):
            temp = s2[l:r+1]
            temp = sorted(temp)
            if temp == s1:
                return True
            else:
                l = l + 1
                r = r + 1
        return False