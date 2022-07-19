import collections
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hp = []
        freq = collections.Counter(nums)
        for key, val in enumerate(freq):
            heapq.heappush(hp, (val, key))
        res = []
        for i in range(k):
            key, val = heapq.heappop(hp)
            res.append(val)

        return res
