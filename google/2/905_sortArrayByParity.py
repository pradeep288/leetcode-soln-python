class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even, odd = 0, len(nums) - 1
        while even < odd:
            if nums[even] % 2 == 1:
                while odd > even and nums[odd] % 2 != 0:
                    odd = odd - 1
                nums[even], nums[odd] = nums[odd], nums[even]
                even += 1
                odd -= 1
            elif nums[even] % 2 == 0 and nums[odd] % 2 == 1:
                even += 1
                odd -= 1
            elif nums[even] % 2 == 0 and nums[odd] % 2 != 1:
                even += 1

        return nums
