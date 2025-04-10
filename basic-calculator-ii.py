"""

Given a string s which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

Example 1:

Input: s = "3+2*2"
Output: 7
Example 2:

Input: s = " 3/2 "
Output: 1
Example 3:

Input: s = " 3+5 / 2 "
Output: 5
 

Constraints:

1 <= s.length <= 3 * 105
s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
s represents a valid expression.
All the integers in the expression are non-negative integers in the range [0, 231 - 1].
The answer is guaranteed to fit in a 32-bit integer.

https://leetcode.com/problems/basic-calculator-ii
"""

class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ','')
        
        if not s:
            return 0
        
        stack = []
        operand = '+'
        curr_num = ''

        for i in range(len(s)):
            if s[i].isdigit():
                curr_num += s[i]
            
            if not s[i].isdigit() or i == len(s) -1:
                curr_num = int(curr_num)
                if operand == '+':
                    stack.append(int(curr_num))
                if operand == '-':
                    stack.append(-1 * int(curr_num))
                if operand == '*':
                    num1 = stack.pop()
                    stack.append((curr_num) * num1)
                if operand == '/':
                    num1 = stack.pop()
                    stack.append(int(float(num1)/curr_num))
                
                operand = s[i]
                curr_num = ''

        return sum(stack)
