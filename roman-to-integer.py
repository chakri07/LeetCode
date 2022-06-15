'''



https://leetcode.com/problems/roman-to-integer/
'''

class Solution:
    def romanToInt(self, s: str) -> int:
        values = {"I":1,"V":5, "X":10, "L":50,"C":100, "D":500,"M":1000}
        ans = 0
        i = 0
        while(i < len(s)):
            if i+1 < len(s) and values[s[i]] < values[s[i+1]]:
                    ans = ans - values[s[i]]
            else:
                ans = ans + values[s[i]]
            i = i + 1
                    
        return ans