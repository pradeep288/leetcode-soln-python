class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        prefix_sum = [0] * len(nums)
        res = 0
        cur_sum = 0
        hash_map = {0:1}

        for num in nums:
            if num < k:
                res += 1
            cur_sum += num

            if cur_sum < k:
                res += 1

            return 0