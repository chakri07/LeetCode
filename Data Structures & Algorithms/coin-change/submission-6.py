class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        
        coin_set = set()
        for coin in coins:
            coin_set.add(coin)

        dp[0] = 0 # no coins

        for curr in range(1,amount+1):
            if curr in coin_set:
                dp[curr] = 1
                continue
            for coin in coin_set:
                if curr - coin >= 0:
                    dp[curr] = min(dp[curr], 1 + dp[curr-coin])

        return -1 if dp[-1] == float('inf') else dp[-1]




