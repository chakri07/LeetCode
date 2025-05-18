'''
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

https://leetcode.com/problems/regular-expression-matching
'''

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_len = len(s)
        p_len = len(p)

        dp = [ [ False for _ in range(p_len + 1)] for _ in range(s_len + 1)]

        dp[0][0] = True 

        # base case where s = ''

        for j in range(1,p_len + 1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]

        # now the actual iteration 

        for s_ptr in range(1,s_len+1):
            for p_ptr in range(1,p_len + 1):
                if p[p_ptr - 1] != '*':
                    if p[p_ptr -1] == s[s_ptr -1] or p[p_ptr -1] == '.':
                        dp[s_ptr][p_ptr] = dp[s_ptr-1][p_ptr-1]
                else:
                    # p[p_ptr-1] == '*'
                    # case 1 : zero occurences of the current 
                    zero_occur = dp[s_ptr][p_ptr-2]

                    # case 2 : one or more occurence 
                    one_occur = False
                    if s[s_ptr-1] == p[p_ptr-2] or p[p_ptr-2] == '.':
                        one_occur = dp[s_ptr-1][p_ptr]

                    dp[s_ptr][p_ptr] = zero_occur or one_occur
        

        return dp[-1][-1]
