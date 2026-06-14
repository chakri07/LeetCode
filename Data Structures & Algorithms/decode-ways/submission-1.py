class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s)+1)

        dp[0] = 1

        if s[0] == "0":
            dp[1] = 0 
        else:
            dp[1] = 1
        
        for i in range(2, len(s)+1):
            one = int(s[i-1:i])
            two = int(s[i-2:i])

            if 0 < one < 10:
                dp[i] = dp[i] + dp[i-1]
            if 10 <= two < 27:
                dp[i] = dp[i] + dp[i-2]

        return dp[-1]
