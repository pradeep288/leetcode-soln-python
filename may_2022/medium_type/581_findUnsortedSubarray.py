class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        temp = sorted(nums)
        left_bound, right_bound = 0, 0
        unsorted_subarry_exists = False

        # Identify the leftmost index where the sort poperty breaks
        for i in range(len(nums)):
            if nums[i] != temp[i]:
                unsorted_subarry_exists = True
                left_bound = i

        # Identify the rightmost index where the sort poperty breaks
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] != temp[i]:
                unsorted_subarry_exists = True
                right_bound = i

        # Handle Edge Cases
        if left_bound == right_bound:
            if unsorted_subarry_exists:
                return len(nums) + 1 - left_bound
            else:
                return 0

        return right_bound - left_bound + 1
