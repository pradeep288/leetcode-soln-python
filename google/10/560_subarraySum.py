class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = {0: 1}
        cur_sum = 0
        res = 0

        for num in nums:
            cur_sum += num
            if cur_sum in prefix_sum.keys():
                prefix_sum[cur_sum] += 1
            else:
                prefix_sum = 1

            if cur_sum - k in prefix_sum.keys():
                res += prefix_sum[cur_sum - k]

        return res
