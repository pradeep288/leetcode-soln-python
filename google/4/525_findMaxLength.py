from collections import defaultdict


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dp = []
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = -1

        freq = defaultdict(int)
        prefix = 0
        max_len = float('-inf')
        for i in range(len(nums)):
            prefix += nums[i]
            if prefix in freq.keys():
                max_len = max(max_len, i - freq[prefix])
            else:
                freq[prefix] = i
        
        return max_len
