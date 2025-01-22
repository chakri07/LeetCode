'''
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
 

Constraints:

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.


https://leetcode.com/problems/word-break/

'''

## solution using word dict: better and easier solution

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}
        def helper(s,dp):
            if s in dp:
                return dp[s]

            if len(s) == 0:
                return True

            for word in wordDict:
                n = len(word)
                if s[0:n] == word:
                    if helper(s[n:],dp):
                        dp[s] = True
                        return True
                        
            dp[s] = False
            return False

        helper(s,dp)
        return dp[s]

        



from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s)+1)
        
        dp[0] = True
        
        for i in range(0,len(s)):
            for j in range(i,len(s)):
                if dp[i] and s[i:j+1] in wordDict:
                    dp[j+1] = True
                    
                    
        return dp[-1]
    
