class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        win_start, win_end = 0, 1
        res = []
        while win_start < len(nums):
            prev_num = nums[win_start]
            while win_end < len(nums):
                if not nums[win_end] == prev_num + 1:
                    break
                prev_num = nums[win_end]
                win_end += 1
            if prev_num == nums[win_start]:
                res.append(str(prev_num))
                win_start = win_start+ 1
            else:
                res.append(str(nums[win_start]) + "->" + str(prev_num))
                win_start = win_end
            win_end=win_start+ 1
        return res
