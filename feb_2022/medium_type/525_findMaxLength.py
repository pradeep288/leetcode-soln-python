class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_len, sum = 0, 0
        hash_map = {}

        for i in range(len(nums)):
            if nums[i] == 0:
                sum -= 1
            else:
                sum += 1
            if sum == 0:
                max_len = i + 1
            else:
                if sum in hash_map.keys():
                    max_len = max(i-hash_map[sum]+1 , max_len)
                else:
                    hash_map[sum] = i + 1

        return max_len
