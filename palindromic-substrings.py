"""
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 

Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters.

https://leetcode.com/problems/palindromic-substrings
"""

class Solution:
    def countSubstrings(self, s: str) -> int:

        def helper(s,left,right):
            ans = 0 
            while left >= 0 and right < len(s):
                if not s[left] == s[right]:
                    break
                left -= 1
                right += 1
                ans += 1
            return ans
            
        ans = 0 

        for i in range(0,len(s)):
            ans += helper(s,i,i)
            ans += helper(s,i,i+1)

        return ans

    