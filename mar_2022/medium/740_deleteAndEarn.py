from collections import Counter


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = Counter(nums)
        nums = sorted(list(set(nums)))
        if len(nums) == 1:
            return nums[0] * count[nums[0]]

        # Case 1: When the index of the element is 0
        dp = [nums[0] * count[nums[0]]]

        # Case 1: When the index of the element is 1
        if nums[1] == nums[0] + 1:
            dp.append(max(dp[0], nums[1] * count[nums[1]]))
        else:
            dp.append(dp[0] + nums[1] * count[nums[1]])

        # Case 2 When the index of the element is >1
        for i in range(2, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                dp.append(max(dp[i - 1], dp[i - 2] + nums[i] * count[nums[i]]))
            else:
                dp.append(dp[i - 1] + nums[i] * count[nums[i]])

        return dp[-1]
