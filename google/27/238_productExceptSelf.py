class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        prefix_list, suffix_list = [1] * N, [1] * N
        mul = 1
        for i in range(N):
            prefix_list[i] = mul
            mul *= nums[i]
        mul = 1
        for i in range(N - 1, -1, -1):
            suffix_list[i] = mul
            mul *= nums[i]

        res = []
        for i in range(N):
            res.append(prefix_list[i] * suffix_list[i])

        return res
