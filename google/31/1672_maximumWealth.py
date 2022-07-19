import heapq


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        hp = []
        for i in range(len(accounts)):
            total = sum(accounts[i]) * -1
            heapq.heappush(hp, total)

        return heapq.heappop(hp) * -1
