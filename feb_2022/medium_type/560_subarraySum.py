# Incomplete solution
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum, count, freq_map = 0, 0, {0: 1}

        for num in nums:
            prefix_sum += num
            count += freq_map.get(prefix_sum - k, 0)
            freq_map[prefix_sum] += 1 + freq_map.get(prefix_sum, 0)

        return count
