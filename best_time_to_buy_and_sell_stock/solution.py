class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if not prices:
            return 0
        max_profit = 0
        min_price = prices[0]
        for i, p in enumerate(prices, start=0):
            max_profit = max(max_profit, (p - min_price))
            min_price = min(min_price, p)
        return max_profit
