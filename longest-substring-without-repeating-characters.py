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


from collections import defaultdict
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        
        window_map = defaultdict(int)

        left = 0 

        ans = 0

        for right in range(len(s)):
            char = s[right]
            while left <= right and char in window_map and not window_map[char] == 0:
                window_map[s[left]] -=1 
                left = left + 1
            window_map[s[right]] += 1
            ans = max(ans, right-left + 1)

        return ans


# try and use a map 
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        chars = set()
        l = 0 
        res = 0 
        for r in range(len(s)):
            if s[r] not in chars:
                chars.add(s[r])
            else:
                while s[r] in chars:
                    chars.remove(s[l])
                    l= l + 1
                chars.add(s[r])
                
            res = max(res,r-l + 1)
            
        return res
                
## solution 2 using a map 

from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: 
            return 0

        chars = defaultdict(int)
        start = 0 
        end = 1 
        ans = 1
        chars[s[0]] = 1

        while end < len(s):
            curr_char = s[end]
            if curr_char in chars and chars[curr_char] > 0:
                ans = max(end-start, ans)

                chars[s[start]] -=1
                start = start + 1
            else:
                chars[s[end]] +=1 
                end = end + 1
                

        return max(ans,end-start)


            