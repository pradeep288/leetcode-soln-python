from collections import Counter


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        freq = Counter(nums)
        count = 0
        for c in [0, 1, 2]:
            v = freq[c]
            for x in range(count, v):
                nums[x] = c
            count += v

        return nums
        """
        l, m, h = 0, 0, len(nums) - 1
        while m <= h:
            if nums[m] == 0:
                nums[l], nums[m] = nums[m], nums[l]
                m += 1
                l += 1
            elif nums[m] == 1:
                m += 1
            else:
                nums[m], nums[h] = nums[h], nums[m]
                h -= 1
