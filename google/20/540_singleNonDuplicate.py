class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if nums[0] != nums[1]:
            return nums[0]

        if nums[-1] != nums[-2]:
            return nums[-2]

        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2

            if nums[m] != nums[m - 1] and nums[m] != nums[m + 1]:
                return nums[m]

            if (m % 2 == 0 and nums[m] == nums[m + 1]) or (m % 2 == 1 and nums[m] == nums[m - 1]):
                l = m + 1
            else:
                r = m - 1

        return -1
