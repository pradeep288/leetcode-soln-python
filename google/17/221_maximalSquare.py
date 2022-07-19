class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        max_val = 0
        for i in range(len(matrix[0])):
            if int(matrix[0][i]):
                max_val = 1
            dp[0][i] = int(matrix[0][i])

        for j in range(len(matrix)):
            if int(matrix[j][0]):
                max_val = 1
            dp[j][0] = int(matrix[j][0])

        for r in range(1, len(matrix)):
            for c in range(1, len(matrix[0])):
                if matrix[r][c] == "1":
                    dp[r][c] = 1 + min(dp[r - 1][c], dp[r][c - 1], dp[r - 1][c - 1])
                    max_val = max(max_val, dp[r][c])

        return max_val * max_val
