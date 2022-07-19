# https://www.youtube.com/watch?v=f7JOBJIC-NA
import heapq


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Create adjacency graph
        n = len(points)
        adj = {i: [] for i in range(n)}
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                diff = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([diff, j])
                adj[j].append([diff, i])

        # Prims Algorithm
        hp = [[0, 0]]
        res = 0
        visited = set()
        while len(visited) < n:
            cost, cur_node = heapq.heappop(hp)
            if cur_node in visited:
                continue
            res += cost
            visited.add(cur_node)

            for neigh_cost, neigh in adj[cur_node]:
                if neigh in visited:
                    continue
                heapq.heappush(hp, [neigh_cost, neigh])

        return res
