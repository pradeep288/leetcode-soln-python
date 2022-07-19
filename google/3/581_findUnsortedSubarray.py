class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        left_boundary, right_boundary = -1, -1
        for i in range(len(sorted_nums)):
            if nums[i] != sorted_nums[i]:
                left_boundary = i
                break
        if left_boundary == -1:
            return 0

        for i in range(len(sorted_nums) - 1, -1, -1):
            if nums[i] != sorted_nums[i]:
                right_boundary = i
                break

        return right_boundary - left_boundary + 1
