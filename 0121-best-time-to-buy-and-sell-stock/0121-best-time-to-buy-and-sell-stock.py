class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=float('inf')
        maxx=0
        for i in prices:
            mini=min(mini,i)
            maxx=max(maxx,i-mini)
        return maxx