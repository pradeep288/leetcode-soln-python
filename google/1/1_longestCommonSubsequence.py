class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text2) + 1)] * len(text1) + 1
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        for i in range(1, len(text1)):
            for j in range(1, len(text2)):
                print(dp[i][j])
            print("\\n")
        return dp[len(text1) - 1][len(text2) - 1]
