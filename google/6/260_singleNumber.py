class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        aXORB = nums[0]
        for i in range(1, len(nums)):
            aXORB ^= nums[i]

        right_most_set_bit = aXORB & -aXORB

        a, b = 0, 0

        for i in range(len(nums)):
            if nums[i] & right_most_set_bit:
                a ^= nums[i]
            else:
                b ^= nums[i]

        return [a, b]
