class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = len(prices)
        if l <= 1:
            return 0

        if l == 2 and prices[1] > prices[0]:
            return prices[1] - prices[0]
        elif l == 2:
            return 0

        dp = [[0] * 2 for _ in range(l)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]

        dp[1][0] = max(dp[0][0], dp[0][1]+prices[1])
        dp[1][1] = max(dp[0][1], -prices[1])

        for i in range(2, l):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-2][0]-prices[i])
        return dp[l-1][0]
