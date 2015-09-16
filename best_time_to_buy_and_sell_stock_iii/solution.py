"""
Say you have an array for which the ith element is the price of a given stock
on day i.

Design an algorithm to find the maximum profit. You may complete at most two
transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must
sell the stock before you buy again).
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        n = len(prices)
        m1 = [0] * n
        m2 = [0] * n
        max_profit1 = 0
        min_price1 = prices[0]
        max_profit2 = 0
        max_price2 = prices[-1]
        for i in range(n):
            max_profit1 = max(max_profit1, prices[i] - min_price1)
            m1[i] = max_profit1
            min_price1 = min(min_price1, prices[i])
        for i in range(n):
            max_profit2 = max(max_profit2, max_price2 - prices[n - 1 - i])
            m2[n - 1 - i] = max_profit2
            max_price2 = max(max_price2, prices[n - 1 - i])
        max_profit = 0
        for i in range(n):
            max_profit = max(m1[i] + m2[i], max_profit)
        return max_profit
