class Solution:
    def maxEnvelopes(self, envelopes):
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        dp = [1] * len(envelopes)

        for i in range(len(envelopes)):
            j = 0
            while j <= i:
                if envelopes[j][1] < envelopes[i][1] and envelopes[j][0] != envelopes[i][0]:
                    dp[i] = max(dp[i], 1 + dp[j])
                j += 1

        return max(dp)