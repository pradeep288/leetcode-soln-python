class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        N = len(nums)

        median = nums[N // 2]

        temp = []
        for i in range(N):
            temp.append(abs(median - nums[i]))

        return sum(temp)
