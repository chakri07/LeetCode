"""
Minimum Window Substring
Solved 
Given two strings s and t, return the shortest substring of s such that every character in t, including duplicates, is present in the substring. If such a substring does not exist, return an empty string "".

You may assume that the correct output is always unique.

Example 1:

Input: s = "OUZODYXAZV", t = "XYZ"

Output: "YXAZ"
Explanation: "YXAZ" is the shortest substring that includes "X", "Y", and "Z" from string t.

Example 2:

Input: s = "xyz", t = "xyz"

Output: "xyz"
Example 3:

Input: s = "x", t = "xy"

Output: ""
Constraints:

1 <= s.length <= 1000
1 <= t.length <= 1000
s and t consist of uppercase and lowercase English letters.

https://neetcode.io/problems/minimum-window-with-characters
"""

## Inefficient 

from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        def compare(big_hash,small_hash):
            for char in small_hash.keys():
                if big_hash[char] < small_hash[char]:
                    return False
            return True


        ans_start,ans_end = 0,float('inf')
        start,end = 0,0
        
        if len(s) < len(t):
            return ""
        
        t_hash = defaultdict(int)
        for char in t:
            t_hash[char]+= 1

        s_hash = defaultdict(int)
        while end < len(s):
            s_hash[s[end]] +=1
            while compare(s_hash,t_hash):
                if end - start < ans_end - ans_start:
                    ans_start,ans_end = start,end
                s_hash[s[start]] -= 1
                start += 1
            
            end += 1
        
        if ans_end == float('inf'):
            return ""
        return s[ans_start:ans_end+1]


