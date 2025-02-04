"""
Given two strings s and p, return an array of all the start indices of p's 
anagrams
 in s. You may return the answer in any order.

 

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
 

Constraints:

1 <= s.length, p.length <= 3 * 104
s and p consist of lowercase English letters.

https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
"""

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        win_len = len(p)

        p_map = {}

        for char in p:
            if char in p_map:
                p_map[char] += 1
            else:
                p_map[char] = 1
        
        s_map = {}

        for char in s[0:len(p)]:
            if char in s_map:
                s_map[char] +=1 
            else:
                s_map[char] = 1

        ans = []
        if s_map == p_map:
            ans.append(0)
        
        for i in range(1,len(s)-len(p)+1):
            new_char = s[i+win_len -1]
            old_char = s[i-1]
            
            s_map[old_char] -=1
            if s_map[old_char] == 0:
                s_map.pop(old_char)
            
            if new_char in s_map:
                s_map[new_char] +=1 
            else:
                s_map[new_char] =1 
            
            if s_map == p_map:
                ans.append(i)
        
        return ans

        