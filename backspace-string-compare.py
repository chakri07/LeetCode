'''Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

 

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a##c", t = "#a#c"
Output: true
Explanation: Both s and t become "c".
Example 4:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".

Link: https://leetcode.com/problems/backspace-string-compare/
'''


# method -1 using deque
from collections import deque 

def backspaceCompare(self, s: str, t: str) -> bool:
    stack1 = deque()
    stack2 = deque()
    
    for char in s:
        if char == '#':
            if stack1:
                stack1.pop()
                continue
        else:
            stack1.append(char)
    
    # print(stack1)
    
    for char in t:
        if char == '#':
            if stack2:
                stack2.pop()
                continue
        else:
            stack2.append(char)
    
    return (stack1== stack2)

# method 2 using a using strings
def backspaceCompare2(self, s: str, t: str) -> bool:
    ans1 = ''
    ans2 = ''
    
    for char in s: 
        if char == '#':
            if ans1:
                ans1 = ans1[:-1]
                continue
        else:
            ans1  = ans1 + char
    # print(ans1)
    
    for char in t: 
        if char == '#':
            if ans2:
                ans2 = ans2[:-1]
                continue
        else:
            ans2  = ans2 + char
    # print(ans2)
    return (ans2 == ans1)


