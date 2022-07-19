import collections
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = collections.defaultdict(list)

        for x, y, w in times:
            adj_list[x].append((y, w))

        visited = set()
        hp = [(k, 0)]
        total = 0
        while hp:
            cur_node, val = heapq.heappop(hp)
            visited.add(cur_node)
            if len(visited) == n:
                return val

            for node, weight in adj_list[cur_node]:
                if node in visited:
                    continue
                heapq.heappush(hp, (node, weight+val))
        return -1
