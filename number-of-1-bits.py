"""
You are given an unsigned integer n. Return the number of 1 bits in its binary representation.

You may assume n is a non-negative integer which fits within 32-bits.

Example 1:

Input: n = 00000000000000000000000000010111

Output: 4
Example 2:

Input: n = 01111111111111111111111111111101

Output: 30

https://neetcode.io/problems/number-of-one-bits

"""

# Explanation : 
# we are AND ing the last digit with 1 , the digit is 1 then it results in one
# and we shift the number to left each time.

class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0 

        while n:
            if n & 1: 
                res +=1 
            n = n >> 1

        return res