class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hash_map = {}
        for k, v in enumerate(numbers):
            if target - v in hash_map.keys():
                return [hash_map[target - v] + 1, k]
            else:
                hash_map[v] = k
