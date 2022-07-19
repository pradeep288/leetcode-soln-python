class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        # find Index where the monotonic increasing sequence breaks
        last_peak_idx = -1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < nums[i - 1]:
                last_peak_idx = i
                break

        if last_peak_idx == -1:
            nums.sort()
            return

        if last_peak_idx==len(nums)-1:
            nums[last_peak_idx-1], nums[last_peak_idx]= nums[last_peak_idx], nums[last_peak_idx-1]
        else:
            next_greater = max(nums[last_peak_idx+1:])
            next_greater_idx = nums.index(next_greater)
            nums[last_peak_idx-1], nums[next_greater_idx] = nums[next_greater_idx], nums[last_peak_idx-1]

        nums[last_peak_idx:].sort()

        return 