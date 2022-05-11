'''
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.

https://leetcode.com/problems/longest-repeating-character-replacement/
'''

class Solution:
    def characterReplacement(self, s, k):     
        
        ans = 0
        counts = collections.defaultdict(int)
        l = 0
        max_val = float('-inf')
        
        for r in range(0,len(s)):
            counts[s[r]]+=1
            if counts[s[r]] > max_val:
                max_val = counts[s[r]]
            while r-l + 1 - (max_val) > k:
                counts[s[l]]-=1
                l = l + 1
            ans = max(ans,r-l+1)
            
        return ans
            