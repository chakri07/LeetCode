"""

A substring is a contiguous (non-empty) sequence of characters within a string.

A vowel substring is a substring that only consists of vowels ('a', 'e', 'i', 'o', and 'u') and has all five vowels present in it.

Given a string word, return the number of vowel substrings in word.

 

Example 1:

Input: word = "aeiouu"
Output: 2
Explanation: The vowel substrings of word are as follows (underlined):
- "aeiouu"
- "aeiouu"
Example 2:

Input: word = "unicornarihan"
Output: 0
Explanation: Not all 5 vowels are present, so there are no vowel substrings.
Example 3:

Input: word = "cuaieuouac"
Output: 7
Explanation: The vowel substrings of word are as follows (underlined):
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
 

https://leetcode.com/problems/count-vowel-substrings-of-a-string
"""

class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        n = len(word)
        ans = 0

        vowel_set = set(['a','e','i','o','u'])

        for i in range(n):
            if not word[i] in vowel_set:
                continue
            seen = set()
            for j in range(i,n):
                if not word[j] in vowel_set:
                    break
                
                seen.add(word[j])

                if len(seen) == 5:
                    ans += 1

        return ans
