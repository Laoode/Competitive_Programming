class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        target = 0

        while right<len(prices):
            if prices[left]<prices[right]:
                current = prices[right]-prices[left]
                target = max(current, target)
            else:
                left=right
            right+=1
        return target