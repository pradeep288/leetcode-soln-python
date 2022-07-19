class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        dp = [nums[0], max(nums[0], nums[1])]

        for i in range(2, len(nums)):
            if dp[i - 2] + nums[i] > dp[i - 1]:
                dp.append(dp[i - 2] + nums[i])
            else:
                dp.append(dp[i - 1])

        return dp[-1]
