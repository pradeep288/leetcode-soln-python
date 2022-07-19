class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i:(i[0], i[1]))

        res = [intervals[0]]
        for i in range(1, len(intervals)):
            prevL, prevR = res[-1]
            if prevL <= intervals[i][0] and prevR >= intervals[i][1]:
                continue
            res.append(intervals[i])
        print(res)

        return len(res)
