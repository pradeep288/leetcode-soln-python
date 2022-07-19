class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        N = len(nums)
        expected = N * (N + 1) // 2
        actual = sum(nums)
        return expected - actual
