'''

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"

https://leetcode.com/problems/decode-string/submissions/
'''

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(0,len(s)):
            if s[i] == ']':
                decode = ""
                while stack[-1] != '[':
                    decode = decode + stack.pop()
                
                stack.pop()
                base = 1
                k = 0
                while len(stack) != 0 and stack[-1].isdigit():
                    k = k + int(stack.pop())*base
                    base = base * 10 
                    
                while k!= 0:
                    for j in range(len(decode)-1,-1,-1):
                        stack.append(decode[j])
                    k = k - 1
                    
            else:
                stack.append(s[i])
                
        return "".join(stack)