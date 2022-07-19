import heapq


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        hp = []
        for i in range(len(mat)):
            heapq.heappush(hp, [sum(mat[i], i)])

        res = []
        for i in range(k):
            _, idx=heapq.heappop(hp)
            res.append(idx)

        return res
