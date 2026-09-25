class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy_price = float("inf")
        maxProfit = 0

        for i in range(0,n):
            buy_price = min(buy_price, prices[i])
            profit = prices[i] - buy_price
            maxProfit = max(maxProfit, profit)
        return maxProfit