'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]




Link: https://leetcode.com/problems/generate-parentheses
'''

def backtrack(ans,n, S = [], left = 0, right = 0):
            if len(S) == 2 * n:
                ans.append("".join(S))
                return
            if left < n:
                S.append("(")
                backtrack(S, left+1, right,ans)
                S.pop()
            if right < left:
                S.append(")")
                backtrack(S, left, right+1,ans)
                S.pop()

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans = []
        backtrack(ans,n,[],0,0)
        return ans