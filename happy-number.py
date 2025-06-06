"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

 

Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
Example 2:

Input: n = 2
Output: false


https://leetcode.com/problems/happy-number
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        
        def helper(n,visited):
            s = 0
            while n > 0:
                
                digit = n % 10 
                n = n // 10
                s += (digit * digit)

            if s in visited:
                return False
            
            visited.add(s)
            if s == 1:
                return True

            return helper(s,visited)

        return helper(n,set())



class Solution:
    def isHappy(self, n: int) -> bool:

        def get_next(n):
            s = 0 
            while n > 0:
                digit = n % 10 
                n = n // 10 

                s += (digit * digit)

            return s

        seen = set()

        while n != 1 and (n not in seen):
            seen.add(n)
            n = get_next(n)

        return n == 1