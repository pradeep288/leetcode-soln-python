class Solution:
    def countOrders(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 6

        dp = [0, 1, 6]

        mod = pow(10, 9) + 7

        for i in range(3, n + 1):
            odd_number = 2 * i - 1
            permutation = odd_number * (odd_number + 1) // 2
            dp.append((dp[i - 1] * permutation) % mod)

        return dp[-1]
