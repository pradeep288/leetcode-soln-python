class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        i = 1
        while i < len(nums) - 2:
            if nums[i - 1] < nums[i] and nums[i + 1] < nums[i]:
                return True
            i += 1
        return False
