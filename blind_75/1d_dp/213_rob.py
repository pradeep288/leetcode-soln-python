class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(arr):
            dp = [0] * len(arr)
            dp[0], dp[1] = arr[0], max(arr[0], arr[1])
            for i in range(2, len(arr)):
                dp[i] = max(dp[i - 1], dp[i - 2] + arr[i])

            return max(dp)

        if len(nums) == 1:
            return nums[-1]

        if len(nums) == 2:
            return max(nums[0], nums[1])

        return max(helper(nums[:len(nums) - 1]), helper(nums[1:]))
