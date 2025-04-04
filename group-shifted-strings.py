"""
Perform the following shift operations on a string:

Right shift: Replace every letter with the successive letter of the English alphabet, where 'z' is replaced by 'a'. For example, "abc" can be right-shifted to "bcd" or "xyz" can be right-shifted to "yza".
Left shift: Replace every letter with the preceding letter of the English alphabet, where 'a' is replaced by 'z'. For example, "bcd" can be left-shifted to "abc" or "yza" can be left-shifted to "xyz".
We can keep shifting the string in both directions to form an endless shifting sequence.

For example, shift "abc" to form the sequence: ... <-> "abc" <-> "bcd" <-> ... <-> "xyz" <-> "yza" <-> .... <-> "zab" <-> "abc" <-> ...
You are given an array of strings strings, group together all strings[i] that belong to the same shifting sequence. You may return the answer in any order.

 

Example 1:

Input: strings = ["abc","bcd","acef","xyz","az","ba","a","z"]

Output: [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]

Example 2:

Input: strings = ["a"]

Output: [["a"]]

 

Constraints:

1 <= strings.length <= 200
1 <= strings[i].length <= 50
strings[i] consists of lowercase English letters.

https://leetcode.com/problems/group-shifted-strings
"""

from collections import defaultdict
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        # group by lengths
        diff_groups = defaultdict(list)

        def get_diff_pattern(s):
            # get difference pattern for each string
            # if difference between letters is same 
            # then the it belongs to same group.
            if not s:
                return tuple()
            
            pattern = []

            for i in range(len(s)-1):
                diff = ord(s[i+1]) - ord(s[i])

                normalized_diff = (diff+26) % 26 
                pattern.append(normalized_diff)

            return tuple(pattern)

        for s in strings:
            s_pattern = get_diff_pattern(s)
            diff_groups[s_pattern].append(s)

        return list(diff_groups.values())