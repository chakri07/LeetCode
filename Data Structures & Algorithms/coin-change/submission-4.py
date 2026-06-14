class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: 
            return 0
        
        coin_set = set(coins)
        
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0 

        for i in range(1, amount +1):
            if i in coins:
                dp[i] = 1
            else:
                for coin in coin_set:
                    if coin > amount:
                        continue
                    else:
                        dp[i] = min(dp[i-coin]+1,dp[i])

        if dp[-1] == float('inf'):
            return -1
        
        return dp[-1]