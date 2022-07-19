class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        starting = 0
        total = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < 0:
                starting = i + 1
                total = 0

        return starting
