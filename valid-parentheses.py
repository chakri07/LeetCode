'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

https://leetcode.com/problems/valid-parentheses/
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == '(' or char == '{' or char == '[': 
                stack.append(char)
            else:
                if len(stack) ==0:
                    return False
                else:
                    recent = stack.pop()
                    if char == ')' and recent != '(':
                        return False
                    elif char == '}' and recent != '{':
                        return False
                    elif char == ']' and recent != '[':
                        return False
                
                
        return len(stack) == 0