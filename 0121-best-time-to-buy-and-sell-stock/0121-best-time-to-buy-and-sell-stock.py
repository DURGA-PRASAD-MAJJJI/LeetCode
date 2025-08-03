class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = float('inf')
        maxx = 0 
        for i in range(len(prices)):
            if prices[i] < mini:
                mini = prices[i]
            else:
                res = prices[i] - mini
                maxx = max(maxx, res)
        return maxx
