"""

Given a string n representing an integer, return the closest integer (not including itself), which is a palindrome. If there is a tie, return the smaller one.

The closest is defined as the absolute difference minimized between two integers.

 

Example 1:

Input: n = "123"
Output: "121"
Example 2:

Input: n = "1"
Output: "0"
Explanation: 0 and 2 are the closest palindromes but we return the smallest which is 0.
 

Constraints:

1 <= n.length <= 18
n consists of only digits.
n does not have leading zeros.
n is representing an integer in the range [1, 1018 - 1].


https://leetcode.com/problems/find-the-closest-palindrome
"""

class Solution:
    def nearestPalindromic(self, n: str) -> str:
        def half_palindrome(left, even):
            res = left
            if not even:
                left = left //10
            while left >0:
                res = res * 10 + left % 10
                left = left // 10

            return res


        len_n = len(n)

        first_half_len = len_n //2 -1 if len_n %2 == 0 else len_n//2     

        first_half = int(n[:first_half_len+1])   

        possibilities = []
        possibilities.append(half_palindrome(first_half, len_n%2 == 0))
        possibilities.append(half_palindrome(first_half+1, len_n%2 == 0))
        possibilities.append(half_palindrome(first_half-1, len_n%2 == 0))
        possibilities.append(10 ** (len_n -1)-1)
        possibilities.append(10 ** len_n+1)

        diff = float('inf')
        res = 0 
        nl = int(n)
        for can in possibilities:
            if can == nl:
                continue
            if abs(can-nl) < diff:
                diff = abs(can-nl)
                res = can
            elif abs(can-nl) == diff:
                res = min(res, can)
        
        return str(res)
