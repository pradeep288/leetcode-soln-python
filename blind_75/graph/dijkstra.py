from heapq import heappush, heappop


class Solution:

    # Function to find the shortest distance of all the vertices
    # from the source vertex S.
    def dijkstra(self, V, adj, S):
        # list representing distance of all nodes from the  S
        distance = [float('inf')] * V
        visited = set()

        hp = []  # Heap element representing distance from S and node
        heappush(hp, (0, S))

        # Run BFS
        while hp:
            cur_distance, cur_node = heappop(hp)
            if cur_node in visited:
                continue
            visited.add(cur_node)
            distance[cur_node] = min(distance[cur_node], cur_distance)
            for n, d in adj[cur_node]:
                heappush(hp, (d + cur_distance, n))
        return distance
