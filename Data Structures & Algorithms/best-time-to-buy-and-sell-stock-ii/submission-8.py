class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        res = 0

        for l in range(len(prices) - 1):
            if prices[l] < prices[l + 1]:
                res += prices[l + 1] - prices[l]
        return res
