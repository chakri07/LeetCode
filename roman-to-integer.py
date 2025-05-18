'''



https://leetcode.com/problems/roman-to-integer/
'''

class Solution:
    def romanToInt(self, s: str) -> int:
        curr_num = 0 
        s = list(s)
        val_map = {'I':1, 'V':5, 'X':10, 
                'L':50, 'C':100, 'D':500, 'M':1000}
        sub_map = {'I' :['V','X'], 'X': ['L','C'], 'C':['D','M']}
        i = 0 
        while i < len(s):
            curr_num
            char = s[i]
            if char in sub_map and i+1 < len(s) and (s[i+1] in sub_map[char]):
                    curr_num -= val_map[char]
            else:
                curr_num += val_map[char]    
            i += 1
        return curr_num



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