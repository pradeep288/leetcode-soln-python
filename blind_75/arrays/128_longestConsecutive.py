class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)

        longest = 0

        for num in nums:
            if (num - 1) not in nums:
                cur_len = 0
                while num + cur_len in nums:
                    cur_len += 1

                longest = max(longest, cur_len)

        return longest
