"""

Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

 

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
 

Constraints:

-100.0 < x < 100.0
-231 <= n <= 231-1
n is an integer.
Either x is not zero or n > 0.
-104 <= xn <= 104
https://leetcode.com/problems/powx-n/description/
"""
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def helper(x,n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            if n == 1:
                return x
            
            if n %2 == 0:
                # even power 
                res = helper(x,n//2)
                return res * res
            else:
                res = helper(x,n//2)
                return x * res * res 
        
        if n >=0 :
            return helper(x,n)
        else:
            return 1/helper(x,abs(n))

