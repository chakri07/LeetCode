'''
Given two integers a and b, return any string s such that:

s has length a + b and contains exactly a 'a' letters, and exactly b 'b' letters,
The substring 'aaa' does not occur in s, and
The substring 'bbb' does not occur in s.
 

Example 1:

Input: a = 1, b = 2
Output: "abb"
Explanation: "abb", "bab" and "bba" are all correct answers.
Example 2:

Input: a = 4, b = 1
Output: "aabaa"

Link: https://leetcode.com/problems/string-without-aaa-or-bbb/
'''

class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        ans = []
        while a > 0 or b >0:
            if len(ans) >=2 and ans[-1] == ans[-2]:
                writeA = ans[-1] == 'b'
            else:
                writeA = a >= b
                
            if writeA:
                a = a-1
                ans.append('a')
            else:   
                b = b-1
                ans.append('b')
        return "".join(ans)