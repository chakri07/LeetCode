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

from collections import defaultdict

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        left = 0 
        ans = 0 

        max_in_window = float('-inf')

        hash_map = defaultdict(int)

        for right in range(len(s)):
            hash_map[s[right]] += 1

            # finding the max freq variable in window
            max_in_window = max(hash_map.values())

            # number of non-freq elements are more than k
            while (right-left+1) - (max_in_window) > k:
                hash_map[s[left]] -= 1
                left += 1 
            
            ans = max(ans, right-left+1)

        
        return ans
            