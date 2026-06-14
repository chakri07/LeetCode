class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0 

        min_until = prices[0]

        for sell_price in prices:
            profit = sell_price - min_until
            max_p = max(max_p, profit)
            min_until = min(min_until,sell_price)

        return max_p
