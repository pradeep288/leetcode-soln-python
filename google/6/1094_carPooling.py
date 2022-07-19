import heapq


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda t: t[1])

        min_heap = []  # (end, cur_pass)
        total_pass = 0
        for trip in trips:
            new_pass, cur_start, cur_end = trip
            while len(min_heap) and min_heap[0][0] <= cur_start:
                total_pass -= min_heap[0][1]
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, (cur_end, new_pass))
            total_pass += new_pass
            if total_pass > capacity:
                return False

        return True
