class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        res = 0
        for i in range(N):
            cur_num = nums[i]
            for j in range(i + 1, N):
                val = nums[j] ^ cur_num
                res = max(val, res)

        return res
