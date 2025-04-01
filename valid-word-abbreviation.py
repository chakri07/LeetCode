"""

A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths. The lengths should not have leading zeros.

For example, a string such as "substitution" could be abbreviated as (but not limited to):

"s10n" ("s ubstitutio n")
"sub4u4" ("sub stit u tion")
"12" ("substitution")
"su3i1u2on" ("su bst i t u ti on")
"substitution" (no substrings replaced)
The following are not valid abbreviations:

"s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
"s010n" (has leading zeros)
"s0ubstitution" (replaces an empty substring)
Given a string word and an abbreviation abbr, return whether the string matches the given abbreviation.

A substring is a contiguous non-empty sequence of characters within a string.

 

Example 1:

Input: word = "internationalization", abbr = "i12iz4n"
Output: true
Explanation: The word "internationalization" can be abbreviated as "i12iz4n" ("i nternational iz atio n").
Example 2:

Input: word = "apple", abbr = "a2e"
Output: false
Explanation: The word "apple" cannot be abbreviated as "a2e".


https://leetcode.com/problems/valid-word-abbreviation/
"""


class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        word_idx = 0
        abbr_idx = 0 

        while word_idx < len(word) and abbr_idx < len(abbr):
            if abbr[abbr_idx].isalpha():
                if not word[word_idx] == abbr[abbr_idx]:
                    return False

                abbr_idx += 1
                word_idx += 1

            elif abbr[abbr_idx].isdigit():
                if abbr[abbr_idx] == '0':
                    return False

                num = ''
                while abbr_idx < len(abbr) and abbr[abbr_idx].isdigit():
                    num += abbr[abbr_idx]
                    abbr_idx += 1 
                    
                if num[0] == 0 and len(num) > 1:
                    return False

                num = int(num)
                word_idx += num
        
        return word_idx == len(word) and abbr_idx == len(abbr)
