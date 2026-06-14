class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}

        def helper(s,dp):
            if s in dp:
                return dp[s]
            
            if len(s) ==0:
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