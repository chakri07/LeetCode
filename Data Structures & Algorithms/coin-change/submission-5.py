class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        coin_set = set(coins) 

        for i in range(1,amount+1):
            if i in coin_set:
                dp[i] =1
            else:
                for coin in coin_set:
                    if i < coin:
                        continue
                    else:
                        dp[i] = min(dp[i], dp[i-coin] +1)

        return dp[-1] if dp[-1] != float('inf') else -1