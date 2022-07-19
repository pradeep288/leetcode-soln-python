import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hp = []

        for num in nums:
            heapq.heappush(hp, num)

        while k > 0:
            heapq.heappop(hp)
            k -= 1

        return hp[0]
