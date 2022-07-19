import heapq


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        hp = []  # (cost, costa, costb)
        for cost in costs:
            heapq.heappush(hp, (cost[0] - cost[1], cost[0], cost[1]))
        total = 0
        for i in range(len(costs)):
            cost = heapq.heappop(hp)
            if i < (len(costs) / 2):
                total += cost[1]
            else:
                total += cost[2]

        return total

