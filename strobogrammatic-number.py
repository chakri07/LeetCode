"""

Given a string num which represents an integer, return true if num is a strobogrammatic number.

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

 

Example 1:

Input: num = "69"
Output: true
Example 2:

Input: num = "88"
Output: true
Example 3:

Input: num = "962"
Output: false
 

Constraints:

1 <= num.length <= 50
num consists of only digits.
num does not contain any leading zeros except for zero itself.

https://leetcode.com/problems/strobogrammatic-number
"""

class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        possible = { '0':'0', '1':'1', '8':'8','6':'9','9':'6'}

        left = 0 
        right = len(num) - 1

        while left <= right:
            digit = num[left]
            if digit not in possible:
                return False
            
            if possible[digit] != num[right]:
                return False

            left += 1
            right -= 1

        return True
