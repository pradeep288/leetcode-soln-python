from collections import Counter


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = Counter(nums)

        nums = sorted(list(set(nums)))

        dp = [0] * len(nums)
        dp[0] = nums[0] * count[nums[0]]

        for i in range(1, len(nums)):
            cur_earn = nums[i] * count[nums[i]]

            if nums[i] == nums[i - 1]:
                old = 0
                if i > 1:
                    old = nums[i - 1]
                dp[i] = cur_earn + old
            else:
                dp[i] = cur_earn + dp[i - 1]

        return dp[-1]
