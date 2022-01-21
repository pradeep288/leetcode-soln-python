class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        start_point, total = 0, 0

        for i in range(len(cost)):
            total += gas[i] - cost[i]

            if total < 0:
                total = 0
                start_point = i

        return start_point
