class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix_sum = 0
        min_val = 101
        for num in nums:
            prefix_sum += num
            min_val = min(prefix_sum, min_val)

        if min_val < 0:
            return abs(min_val) + 1

        return 1
