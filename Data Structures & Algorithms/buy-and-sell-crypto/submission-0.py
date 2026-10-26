class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        n = len(prices)
        if n == 1:
            return res
        
        l = 0
        for r in range(1, n):
            profit = prices[r] - prices[l]
            res = max(res, profit)
            if prices[r] < prices[l]:
                l = r
            
        
        return res