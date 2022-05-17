'''

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
'''

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        coin_set = set(coins)

        for i in range(1,amount+1):   
            if i in coin_set:
                dp[i] = 1
                continue
            else:
                for coin in coin_set:
                    if coin > i:
                        continue
                    if dp[i-coin] != float('inf'):
                        dp[i] = min(dp[i-coin]+1, dp[i])

        if dp[-1] == float('inf'):
            return -1
        return dp[-1]