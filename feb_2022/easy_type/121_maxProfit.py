class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_val = float('+inf')

        for price in prices:
            if price < min_val:
                min_val = price
            elif price - min_val > profit:
                profit = price - min_val

        return profit
