class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for i in range(len(nums)):
            if nums[i] in freq_map.keys():
                freq_map[nums[i]] += 1
            else:
                freq_map[nums[i]] = 1

        freq_map = dict(sorted(freq_map.items(), key=lambda item: item[1],
                               reverse=True))

        i, res = 0, []

        for key in freq_map.keys():
            if i >= k:
                break
            res.append(key)
            i += 1

        return res
