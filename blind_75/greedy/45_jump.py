class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0
        total_jumps = 0
        while r < len(nums) - 1:
            farthest = float('-inf')
            for i in range(r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            total_jumps += 1

        return total_jumps
