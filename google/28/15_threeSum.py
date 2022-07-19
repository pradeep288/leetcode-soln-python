class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        N = len(nums)
        for i in range(N):
            if i < 0 and nums[i] == nums[i - 1]:
                continue
            target = nums[i] * -1
            start, end = i + 1, N - 1
            while start < end:
                if nums[start] + nums[start] == target:
                    res.append([nums[i], nums[start], nums[end]])
                    start += 1
                    while start < end and nums[start] == nums[start - 1]:
                        start = start + 1
                elif nums[start] + nums[start] > target:
                    end -= 1
                else:
                    start += 1
        return res
