class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n + 1)
        if n == 1:
            return True

        dp[1] = True
        dp[2] = False
        for i in range(3, n + 1):
            j = 1
            while j * j <= i:
                if dp[j * j]:
                    dp[i] = True
                    break
                j += 1

        return dp[n]
