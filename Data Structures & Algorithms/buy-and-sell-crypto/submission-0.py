class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        win = 0
        p = prices[0]
        for i in range(1, len(prices)):
            win = max(win , prices[i] - p)
            p = min(p,prices[i])
        return win 
