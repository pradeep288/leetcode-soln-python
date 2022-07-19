class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res = []

        i, j = 0, 0

        while i < len(firstList) and j < len(secondList):
            mx = max(firstList[i][0], secondList[j][0])
            mi = min(firstList[i][1], secondList[j][1])
            if mx <= mi:
                res.append([mx, mi])
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1

        return res
