import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[-1]

        hp = []
        for i in range(len(stones)):
            heapq.heappush(hp, stones[i] * -1)

        while len(hp) >= 2:
            stone_a, stone_b = (heapq.heappop(hp)) * -1, (heapq.heappop(hp)) * -1
            if stone_a - stone_b > 0:
                heapq.heappush(hp, (stone_a - stone_b) * -1)

        print(hp)
        if len(hp) == 0:
            return 0

        return hp[-1] * -1
