class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) <= 2:
            return False
        cur_min = nums[0]
        stack = []  # [cur_min, num]

        for n in nums[1:]:
            while stack and stack[-1][1] < n:
                stack.pop()
            if stack and stack[-1][1] > n > stack[-1][0]:
                return True
            cur_min = min(cur_min, n)
            stack.append([cur_min, n])

        return False
