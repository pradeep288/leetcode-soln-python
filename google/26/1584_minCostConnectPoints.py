import heapq


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Create adjacency graph in format A= [(costB, B)]

        adj = {i: [] for i in range(len(points))}

        for i in range(len(points)):
            x1, y1 = points[i][0], points[i][1]
            for j in range(i, len(points)):
                x2, y2 = points[j][0], points[j][1]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append((dist, j))
                adj[j].append((dist, i))

        res = 0
        min_heap = []
        visit = set()
        heapq.heappush(min_heap, (0, 0))
        while min_heap:
            dist, node = heapq.heappop(min_heap)
            if node in visit:
                continue
            visit.add(node)
            res += dist

            for d, n in adj[node]:
                if n in visit:
                    continue
                heapq.heappush(min_heap, (d, n))

        return res
