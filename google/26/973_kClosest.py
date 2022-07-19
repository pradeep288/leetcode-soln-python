import heapq
import math


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Build Min Heap
        min_heap = []
        x0, y0 = 0, 0
        for i in range(len(points)):
            x1, y1 = points[i]
            dist = math.sqrt(pow((x1 - x0), 2) + pow((y1 - y0), 2))
            heapq.heappush(min_heap, [dist, x1, y1])

        res = []
        for i in range(k):
            _, x1, y1 = heapq.heappop(min_heap)
            res.append([x1, y1])

        return res
