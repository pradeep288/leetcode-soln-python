class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            end = res[-1][1]

            if intervals[i][0] <= end:
                res[-1][1] = max(end, intervals[i][1])
            else:
                res.append([intervals[i][0], intervals[i][1]])

        return res
