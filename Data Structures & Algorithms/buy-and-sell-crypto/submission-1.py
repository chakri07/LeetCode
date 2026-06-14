class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0 
        right = 1

        max_p = 0 

        while right < len(prices) and left < len(prices):
            profit = prices[right] - prices[left]

            if profit > max_p: 
                max_p = profit            

            if prices[right] < prices[left]: 
                left = right 

            right = right + 1 
        
        return max_p
