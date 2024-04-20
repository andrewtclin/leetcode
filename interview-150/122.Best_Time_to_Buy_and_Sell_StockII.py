from typing import List

def maxProfit(prices: List[int]) -> int:
    l, r = 0, 1
    total_profits = 0

    if len(prices) < 2:
        return 0

    while r < len(prices):
        if prices[r] > prices[l]:
            total_profits += prices[r] - prices[l]
        l = r
        r += 1
        
    return total_profits