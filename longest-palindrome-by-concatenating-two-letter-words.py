"""

You are given an array of strings words. Each element of words consists of two lowercase English letters.

Create the longest possible palindrome by selecting some elements from words and concatenating them in any order. Each element can be selected at most once.

Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0.

A palindrome is a string that reads the same forward and backward.

 

Example 1:

Input: words = ["lc","cl","gg"]
Output: 6
Explanation: One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of length 6.
Note that "clgglc" is another longest palindrome that can be created.
Example 2:

Input: words = ["ab","ty","yt","lc","cl","ab"]
Output: 8
Explanation: One longest palindrome is "ty" + "lc" + "cl" + "yt" = "tylcclyt", of length 8.
Note that "lcyttycl" is another longest palindrome that can be created.
Example 3:

Input: words = ["cc","ll","xx"]
Output: 2
Explanation: One longest palindrome is "cc", of length 2.
Note that "ll" is another longest palindrome that can be created, and so is "xx".
 

Constraints:

1 <= words.length <= 105
words[i].length == 2
words[i] consists of lowercase English letters.

https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words

"""


from collections import defaultdict
from typing import List

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        freq_map = defaultdict(int)

        for word in words:
            freq_map[word] += 1
        
        ans = 0 

        central = False

        for word in freq_map.keys():
            freq = freq_map[word]
            if word[0] == word[1]:
                if freq %2 == 0:
                    ans += freq
                else:
                    ans += freq -1
                    central = True
            
            elif word[0] < word[1]:
                reverse = word[1] + word[0]
                if reverse in freq_map:
                    ans += 2 * min(freq, freq_map[reverse])
        
        if central: 
            ans += 1
        
        return 2 * ans
