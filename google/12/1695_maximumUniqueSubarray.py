class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        mx, i, j = 0, 0, 0
        unique = set()
        cur_sum = 0
        for j in range(len(nums)):
            while nums[j] in unique:
                cur_sum -= nums[i]
                unique.remove(nums[i])
                i += 1
            unique.add(nums[j])
            cur_sum += nums[j]
            mx = max(mx, cur_sum)

        return mx
