class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0

        buy_price = prices[0]

        for i in prices[1:]:
            if buy_price > i:
                buy_price = i 
            else:
                ans = max(ans, i - buy_price)

        return ans