class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        res = False

        def helper(idx, running_sum):
            nonlocal res
            if running_sum == target:
                res = True
                return

            if idx >= len(nums) or running_sum > target:
                return

            for i in range(idx, len(nums)):
                helper(i, running_sum + nums[i])

        helper(0, 0)

        return res