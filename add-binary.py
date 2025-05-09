"""
Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.


https://leetcode.com/problems/add-binary
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0 

        a = list(a)
        b = list(b)

        i = len(a) - 1
        j = len(b) - 1 

        ans = []

        while i >= 0 or j >= 0:
            if i >=0 :
                a1 = int(a[i])
            else: 
                a1 = 0 
            
            if j >= 0:
                b1 = int(b[j])
            else:
                b1 = 0

            val = a1 + b1 + carry 

            ans.append(val % 2)
            carry = val // 2
            i -= 1
            j -= 1

        if carry > 0:
            ans.append(carry)
        
        # print(ans)
        final = ''
        for i in range(len(ans)-1,-1,-1):
            final += str(ans[i])

        return final
