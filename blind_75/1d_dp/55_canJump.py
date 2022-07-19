class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReachableIndex = 0
        n = len(nums)
        for i in range(n):
            if maxReachableIndex < i:
                return False
            maxReachableIndex = max(maxReachableIndex, i + nums[i])
        return True
