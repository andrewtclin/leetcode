from typing import List

def maxProfit(prices: List[int]) -> int:
    if len(prices) < 2:
        return 0

    l, r, max_profit = 0, 1, 0

    while r < len(prices):
        if prices[l] < prices[r]:
            max_profit = max(prices[r] - prices[l], max_profit)
        else:
            l = r
        r += 1
    return max_profit
