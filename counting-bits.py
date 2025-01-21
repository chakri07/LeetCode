"""

Given an integer n, count the number of 1's in the binary representation of every number in the range [0, n].

Return an array output where output[i] is the number of 1's in the binary representation of i.

Example 1:

Input: n = 4

Output: [0,1,1,2,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100

Constraints:

0 <= n <= 1000

https://neetcode.io/problems/counting-bits
"""

## Dp solution

class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        dp = [0] * (n+1)

        dp[0] = 0 
        dp[1] = 1
        offset = 1
        for num in range(2,n+1):
            if offset * 2 == num:
                offset = num
            dp[num] = 1 + dp[num-offset]
        return dp