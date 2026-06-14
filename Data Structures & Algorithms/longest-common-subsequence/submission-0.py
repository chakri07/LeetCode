class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if text1 == text2:
            return len(text1)

        dp = [[0] * (len(text2)) for _ in range(len(text1))]

        # first populate the 1st row

        dp[0][0] = 1 if text1[0] == text2[0] else 0
        for i in range(1,len(text2)):
            if dp[0][i-1] == 1 or text1[0] == text2[i]:
                dp[0][i] = 1

        for i in range(1,len(text1)):
            if dp[i-1][0] == 1 or text1[i] == text2[0]:
                dp[i][0] = 1

        for i in range (1,len(text1)):
            for j in range (1,len(text2)):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i-1][j-1] +1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])

        print(dp)
        return dp[-1][-1]


        

            
