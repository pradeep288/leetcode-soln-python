from heapq import heappop, heappush


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        hp = []
        # Create a MaxHeap
        for stone in stones:
            heappush(hp, -1 * stone)

        while not 0 <= len(hp) <= 1:
            stone1 = (heappop(hp)) * -1
            stone2 = (heappop(hp)) * -1
            # Add remaining stone if the diff is greater than zero
            if stone1 - stone2 > 0:
                heappush(hp, -1*(stone1 - stone2))

        if len(hp) == 1:
            return -1*hp[0]

        return 0
