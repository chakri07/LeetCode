'''
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

 

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].

https://leetcode.com/problems/plus-one/
'''
from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        carry = 1

        for i in range(len(digits)-1, -1, -1 ):
            val = carry + digits[i]

            digits[i] = val % 10 
            carry = val // 10 

            if carry == 0 :
                break

        if carry == 0:
            return digits
        else:
            return [carry] + digits


class Solution:
    def plusOne(self, digit: list[int]) -> list[int]:
        
        carry = (digit[-1] + 1) // 10 
        digit[-1] = (digit[-1] + 1) % 10 
        for i in range(len(digit)-2,-1,-1):
            temp_digit = (digit[i] + carry) % 10 
            carry  = (digit[i] + carry) // 10
            digit[i] = temp_digit
            print(carry)
         
        if carry != 0:
            return [carry] + digit
        return digit
        