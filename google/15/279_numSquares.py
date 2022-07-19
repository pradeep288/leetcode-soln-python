import math


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0, 1, 2, 3]

        for i in range(4, n + 1):
            min_val = float('inf')
            for j in range(1, i):
                if j * j > i:
                    break
                target = i - (j * j)
                min_val = min(dp[target] + 1, min_val)
            dp.append(min_val)

        return dp[-1]