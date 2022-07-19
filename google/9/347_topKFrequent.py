from heapq import heappop, heappush
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hp = []
        freq = Counter(nums)

        for key, val in freq.items():
            heappush(hp, (val * -1, key))

        res = []
        for i in range(k):
            key, val = heappop(hp)
            res.append(val)

        return res
