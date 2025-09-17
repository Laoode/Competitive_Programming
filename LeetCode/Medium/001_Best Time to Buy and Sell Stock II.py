class Solution:
    def maxProfit(self, prices: List[int]):
        profit = 0
        for i in range(len(prices)-1):
            current = prices[i+1]-prices[i]
            if current>0:
                profit+=current
        return profit