# https://www.youtube.com/watch?v=d-B_gk_gJtQ
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        res = 0
        diffs = []
        for c1, c2 in costs:
            diffs.append([c2 - c1, c1, c2])

        diffs.sort()
        for i in range(len(diffs)):
            if i < len(costs) // 2:
                res += diffs[i][2]
            else:
                res += diffs[i][1]

        return res
