"""
Reverse Bits
Solved 
Given a 32-bit unsigned integer n, reverse the bits of the binary representation of n and return the result.

Example 1:

Input: n = 00000000000000000000000000010101

Output:    2818572288 (10101000000000000000000000000000)
Explanation: Reversing 00000000000000000000000000010101, which represents the unsigned integer 21, gives us 10101000000000000000000000000000 which represents the unsigned integer 2818572288.

https://neetcode.io/problems/reverse-bits
"""

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0 

        for i in range(32):
            digit = n & 1
            res = res + (digit << (31 - i))

            n = n >> 1

        return res
        