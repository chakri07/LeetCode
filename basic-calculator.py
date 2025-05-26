"""

Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

Example 1:

Input: s = "1 + 1"
Output: 2
Example 2:

Input: s = " 2-1 + 2 "
Output: 3
Example 3:

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
 

Constraints:

1 <= s.length <= 3 * 105
s consists of digits, '+', '-', '(', ')', and ' '.
s represents a valid expression.
'+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
'-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
There will be no two consecutive operators in the input.
Every number and running calculation will fit in a signed 32-bit integer.

https://leetcode.com/problems/basic-calculator
"""

from collections import deque

class Solution:
  def calculate(self, s: str) -> int:
    """
    Evaluates a basic arithmetic expression string.

    The method iterates through the string, managing the current number (`operand`),
    the accumulated result for the current scope (`result`), and the `sign`
    for the current `operand`. A stack is used to handle parentheses:
    - On '(': current `result` and `sign` are pushed to the stack. `result` is reset
      to 0 and `sign` to 1 for the new parenthesized sub-expression.
    - On ')': the sub-expression's `result` is finalized by adding the last `operand`
      within it. Then, this sub-expression's `result` is combined with the
      `result` and `sign` popped from the stack (which were from the scope
      before this parenthesis started).
    - Operators '+' or '-': update `result` by adding the `sign * operand` that
      preceded the operator, then set `sign` for the next operand.
    - Digits are used to build the multi-digit `operand`.
    - Spaces are ignored.
    After iterating through the entire string, any final `operand` is added to the `result`.
    """
    stack = deque()
    operand = 0
    result = 0  # Current accumulated result for the active scope (global or inside parentheses)
    sign = 1    # Sign of the current 'operand': 1 for positive, -1 for negative

    for char_idx, char in enumerate(s):
      if char.isdigit():
        operand = operand * 10 + int(char)
      elif char == '+':
        result += sign * operand # Process the number (and its sign) before the '+'
        operand = 0              # Reset operand for the next number
        sign = 1                 # The next number will be positive (unless changed by a unary minus)
      elif char == '-':
        result += sign * operand # Process the number (and its sign) before the '-'
        operand = 0              # Reset operand for the next number
        sign = -1                # The next number will be negative
      elif char == '(':
        # Push the current result and sign onto the stack.
        # 'result' holds the accumulated value from the scope *before* this '('.
        # 'sign' holds the sign that should be applied to the *entire result* of this '(...)' block.
        stack.append(result)
        stack.append(sign)
        
        # Reset for the new sub-expression within the parentheses.
        result = 0
        sign = 1 # Default sign for the first number/term inside the parentheses.
      elif char == ')':
        result += sign * operand # Process the last number (and its sign) inside this parenthesis.
        operand = 0              # Reset operand.
        
        # The value of the expression within the parentheses is now stored in 'result'.
        # Pop the sign that was active *before* this parenthesis block started.
        # This sign applies to the entire result of the just-calculated parenthesized expression.
        sign_of_parenthesized_block = stack.pop() 
        # Pop the result from the outer scope (accumulated before this parenthesis started).
        result_from_outer_scope = stack.pop()
        
        # Combine: result_outer_scope + (sign_for_block * result_inside_parentheses)
        result = result_from_outer_scope + (sign_of_parenthesized_block * result)
        # 'sign' is not explicitly changed here by popping. It retains its last value from
        # within the parenthesis. If an operator follows this ')', that operator will set the 'sign'.
        # If the string ends, the final 'operand' (which is 0 after ')' processing) is added using this 'sign'.
      
      # Spaces are implicitly skipped as they do not match any of the conditions
      # and do not alter 'operand', 'result', or 'sign'.

    # After the loop, add the last pending operand (if any) to the result.
    # This handles cases like "123" or "1+2".
    result += sign * operand
    
    return result
