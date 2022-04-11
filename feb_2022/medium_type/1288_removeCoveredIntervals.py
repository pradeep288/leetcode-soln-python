class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        uncovered_internals = len(intervals)

        for i in range(len(intervals)):
            for j in range(len(intervals)):
                if i == j:
                    continue
                if intervals[i][0] >= intervals[j][0] and intervals[i][
                    1] <= intervals[j][1]:
                    uncovered_internals -= 1
                    break

        return uncovered_internals
